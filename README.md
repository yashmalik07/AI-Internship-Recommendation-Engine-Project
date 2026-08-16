# 🎯 AI Internship Recommendation Engine

An AI-powered internship recommendation system that recommends suitable internships to students based on their **skills, interests, domain, and previous preferences**.

This project uses **Collaborative Filtering**, **Content-Based Filtering**, and a **Hybrid Recommendation approach** to generate personalized internship recommendations.

---

## 📌 Project Information

| Details                   | Information                             |
| ------------------------- | --------------------------------------- |
| Project Name              | AI Internship Recommendation Engine     |
| Task ID                   | AI-SS-002                               |
| Domain                    | Student Support & Internship Management |
| Technology                | Python                                  |
| Machine Learning          | Scikit-learn                            |
| Data Processing           | Pandas                                  |
| Numerical Computing       | NumPy                                   |
| Recommendation Techniques | Collaborative + Content-Based + Hybrid  |

---

## 🚀 Project Objective

The main objective of this project is to build an intelligent recommendation system that helps students find internships that match their skills and career interests.

The system analyzes:

* Student skills
* Student domain
* Experience level
* Internship requirements
* Previous internship ratings

and generates suitable internship recommendations.

---

## 🧠 Recommendation Techniques

### 1. Collaborative Filtering

Collaborative Filtering recommends internships based on the preferences and ratings of students with similar interests.

The system creates a **student-internship rating matrix** and uses **Cosine Similarity** to find similar students.

---

### 2. Content-Based Filtering

Content-Based Filtering compares the student's skills and domain with the skills and domain required by internships.

The project uses:

* TF-IDF Vectorization
* Cosine Similarity

to calculate the similarity between a student profile and internship requirements.

---

### 3. Hybrid Recommendation

The Hybrid Recommendation system combines both approaches to provide better recommendations.

The project uses:

* **60% weight → Collaborative Filtering**
* **40% weight → Content-Based Filtering**

The final internships are ranked according to their combined score.

---

## 📂 Project Structure

```text
AI-Internship-Recommendation-Engine/
│
├── data/
│   ├── students.csv
│   ├── internships.csv
│   └── ratings.csv
│
├── recommendation_engine.py
├── app.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

### students.csv

Contains student information such as:

* Student ID
* Name
* Skills
* Domain
* Experience Level

### internships.csv

Contains internship information such as:

* Internship ID
* Internship Title
* Required Skills
* Domain
* Duration

### ratings.csv

Contains student internship ratings used for Collaborative Filtering.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* TF-IDF
* Cosine Similarity
* Streamlit

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/AI-Internship-Recommendation-Engine.git
```

Move into the project directory:

```bash
cd AI-Internship-Recommendation-Engine
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🎯 How the System Works

```text
Student Profile
      ↓
Skills + Domain + Experience
      ↓
┌─────────────────────────┐
│ Collaborative Filtering │
└─────────────────────────┘
      +
┌─────────────────────────┐
│ Content-Based Filtering │
└─────────────────────────┘
      ↓
Hybrid Recommendation
      ↓
Ranked Internship List
```

---

## ✨ Features

* 👨‍🎓 Student profile selection
* 📚 Internship database
* 🔍 Skill-based internship matching
* 🤝 Collaborative Filtering
* 🎯 Content-Based Filtering
* 🔀 Hybrid Recommendation
* 📊 Similarity scoring
* 🌐 Streamlit interface
* 📁 CSV-based dataset
* 🚫 No database required

---

## 📈 Example Output

The system generates recommendations such as:

```text
Recommended Internships

1. Machine Learning Intern
   Domain: AI
   Duration: 6 months
   Match Score: 0.82

2. Data Scientist Intern
   Domain: Data Science
   Duration: 6 months
   Match Score: 0.76

3. AI Intern
   Domain: AI
   Duration: 3 months
   Match Score: 0.71
```

*The actual recommendations and scores depend on the selected student and dataset.*

---

## 🎓 Learning Outcomes

Through this project, the following concepts are demonstrated:

* Recommendation Systems
* Data Preprocessing
* Collaborative Filtering
* Content-Based Filtering
* TF-IDF
* Cosine Similarity
* Hybrid Recommendation
* Machine Learning using Scikit-learn
* Data Processing using Pandas

---

## 🔮 Future Improvements

The system can be extended with:

* Real-time recommendation updates
* User feedback
* Larger internship datasets
* Advanced recommendation algorithms
* Deep Learning-based recommendations
* Recommendation dashboard
* Web API using Flask or Django

---

## 📸 Project Screenshots

Add screenshots of:

1. Student Profile
2. Internship Recommendations
3. Hybrid Recommendation Results
4. Available Internship Dataset
5. Streamlit Dashboard

---

## 🎥 Project Demonstration

**YouTube Demo:**
`Add your YouTube video link here`

The demonstration should show the recommendation generation and explain the Collaborative Filtering, Content-Based Filtering, and Hybrid Recommendation processes.

---

## 🔗 Task Information

**Task ID:** AI-SS-002
**Task Name:** AI Internship Recommendation Engine
**Domain:** Student Support & Internship Management

---

## 👨‍💻 Author

**Name:** Your Name

**GitHub:**
`https://github.com/YOUR-USERNAME`

---

## 📜 License

This project is created for educational and internship purposes.
