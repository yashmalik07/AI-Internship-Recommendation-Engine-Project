import pandas as pd
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


class InternshipRecommender:

    def __init__(self):

        self.students_df = pd.read_csv("data/students.csv")
        self.internships_df = pd.read_csv("data/internships.csv")
        self.ratings_df = pd.read_csv("data/ratings.csv")

        # Convert skills from string to list
        self.students_df["skills"] = self.students_df["skills"].apply(
            lambda x: x.lower().split("|")
        )

        self.internships_df["required_skills"] = self.internships_df[
            "required_skills"
        ].apply(lambda x: x.lower().split("|"))

        # Create rating matrix
        self.user_item_matrix = self.create_user_item_matrix()

    def create_user_item_matrix(self):

        matrix = self.ratings_df.pivot(
            index="student_id",
            columns="internship_id",
            values="rating"
        ).fillna(0)

        return matrix

    # -----------------------------
    # Collaborative Filtering
    # -----------------------------

    def collaborative_filtering(self, student_id, top_n=5):

        if student_id not in self.user_item_matrix.index:
            return []

        student_ratings = self.user_item_matrix.loc[student_id]

        similarities = cosine_similarity(
            [student_ratings],
            self.user_item_matrix.values
        )[0]

        # Get similar students
        similar_indices = np.argsort(similarities)[::-1]

        recommendations = {}

        for idx in similar_indices:

            similar_student_id = self.user_item_matrix.index[idx]

            # Don't compare student with himself
            if similar_student_id == student_id:
                continue

            similar_ratings = self.user_item_matrix.loc[
                similar_student_id
            ]

            for internship_id, rating in similar_ratings.items():

                # Recommend only internships not already rated
                if student_ratings[internship_id] == 0 and rating > 0:

                    if internship_id not in recommendations:
                        recommendations[internship_id] = []

                    recommendations[internship_id].append(rating)

        # Average rating
        scores = []

        for internship_id, ratings in recommendations.items():

            score = np.mean(ratings)

            scores.append(
                (internship_id, score)
            )

        scores.sort(
            key=lambda x: x[1],
            reverse=True
        )

        results = []

        for internship_id, score in scores[:top_n]:

            row = self.internships_df[
                self.internships_df["internship_id"] == internship_id
            ].iloc[0]

            results.append({
                "internship_id": internship_id,
                "title": row["title"],
                "domain": row["domain"],
                "duration": row["duration"],
                "score": round(score, 2)
            })

        return results

    # -----------------------------
    # Content-Based Filtering
    # -----------------------------

    def content_based_filtering(self, student_id, top_n=5):

        student_rows = self.students_df[
            self.students_df["student_id"] == student_id
        ]

        if student_rows.empty:
            return []

        student = student_rows.iloc[0]

        internship_text = []

        for _, row in self.internships_df.iterrows():

            text = (
                " ".join(row["required_skills"])
                + " "
                + row["domain"].lower()
            )

            internship_text.append(text)

        vectorizer = TfidfVectorizer()

        internship_vectors = vectorizer.fit_transform(
            internship_text
        )

        student_text = (
            " ".join(student["skills"])
            + " "
            + student["domain"].lower()
        )

        student_vector = vectorizer.transform(
            [student_text]
        )

        similarities = cosine_similarity(
            student_vector,
            internship_vectors
        )[0]

        top_indices = np.argsort(
            similarities
        )[::-1][:top_n]

        results = []

        for index in top_indices:

            row = self.internships_df.iloc[index]

            results.append({
                "internship_id": row["internship_id"],
                "title": row["title"],
                "domain": row["domain"],
                "duration": row["duration"],
                "score": round(
                    float(similarities[index]),
                    3
                )
            })

        return results

    # -----------------------------
    # Hybrid Recommendation
    # -----------------------------

    def hybrid_recommendation(
        self,
        student_id,
        top_n=5
    ):

        collaborative = self.collaborative_filtering(
            student_id,
            top_n=10
        )

        content = self.content_based_filtering(
            student_id,
            top_n=10
        )

        combined = {}

        # Collaborative weight = 60%
        for rec in collaborative:

            combined[
                rec["internship_id"]
            ] = {
                "title": rec["title"],
                "domain": rec["domain"],
                "duration": rec["duration"],
                "score":
                    rec["score"] * 0.6
            }

        # Content weight = 40%
        for rec in content:

            internship_id = rec["internship_id"]

            if internship_id in combined:

                combined[internship_id]["score"] += (
                    rec["score"] * 0.4
                )

            else:

                combined[internship_id] = {
                    "title": rec["title"],
                    "domain": rec["domain"],
                    "duration": rec["duration"],
                    "score":
                        rec["score"] * 0.4
                }

        sorted_results = sorted(
            combined.items(),
            key=lambda x: x[1]["score"],
            reverse=True
        )

        results = []

        for internship_id, data in sorted_results[:top_n]:

            results.append({
                "internship_id": internship_id,
                "title": data["title"],
                "domain": data["domain"],
                "duration": data["duration"],
                "hybrid_score":
                    round(data["score"], 3)
            })

        return results
