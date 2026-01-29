# AI-Based Resume Screening and Job Recommendation System

An AI-powered backend system that automatically analyzes resumes and matches them with job descriptions using **Natural Language Processing (NLP)** and **Machine Learning similarity techniques**.  
Built using **Python, Django, and Django REST Framework**, this project demonstrates how AI can be integrated into real-world recruitment workflows.

---

## 🚀 Project Overview

Manual resume screening is time-consuming and often inconsistent.  
This project aims to **automate resume analysis and candidate-job matching** by computing a similarity score between resume content and job descriptions.

The system is designed as an **API-first backend**, making it scalable and suitable for integration with any frontend application.

---

## 🧠 Core Features

- RESTful APIs for resume and job submission  
- NLP-based text preprocessing  
- TF-IDF vectorization for feature extraction  
- Cosine similarity to calculate match percentage  
- Explainable and interpretable AI results  
- Clean Django project architecture  

---

## 🛠 Tech Stack

**Backend**
- Python 3.x
- Django
- Django REST Framework

**AI / NLP**
- TF-IDF Vectorizer
- Cosine Similarity
- Scikit-learn

**Database**
- SQLite (development)

**Tools**
- Thunder Client / Postman
- Python Virtual Environment (venv)

---

## 📂 Project Structure
AI_Resume_Screening_Django_Project/
│
├── core/ # Django project settings
├── resume/ # Resume & Job app (models, views, NLP logic)
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ ├── nlp.py
│ └── urls.py
│
├── manage.py
├── requirements.txt
└── README.md
---



---

## ⚙️ How the System Works

1. Resume and job description data are submitted via REST APIs  
2. Text data is cleaned and vectorized using **TF-IDF**  
3. **Cosine similarity** is computed between resume and job vectors  
4. The system returns a **match percentage** indicating suitability  

---

## ▶️ Re-Execution Steps (After Initial Setup)

```bash
# Activate virtual environment
venv\Scripts\activate

# Start Django server
python manage.py runserver

```
http://127.0.0.1:8000/


