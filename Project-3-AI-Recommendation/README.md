# 🤖 PathPilot AI

### AI Programming Course Recommendation System

PathPilot AI is an interactive programming course recommendation system built with Python and Streamlit.

It analyzes a user's experience level, preferred programming language, domain, and learning goal to recommend suitable courses and generate a personalized learning roadmap.

---

## ✨ Features

- 🎯 Personalized course recommendations
- 🧠 Weighted course matching system
- 📊 Course match percentage
- 💡 Explanation of why a course was recommended
- 🗺️ Personalized learning roadmap
- 📚 Browse complete course database
- ⭐ Course rating and duration information
- 🔄 Start Over functionality
- ✨ Interactive Streamlit UI
- 🎨 Custom animated and modern interface

---

## 🧠 How It Works

The user provides:

- Experience Level
- Preferred Programming Language
- Domain
- Learning Goal

PathPilot AI then analyzes the available courses and calculates a compatibility score.

### Match Score

| Factor | Weight |
|---|---:|
| Programming Language | 40 points |
| Experience Level | 30 points |
| Domain | 20 points |
| Course Rating | 10 points |
| **Total** | **100 points** |

Courses are ranked according to their calculated score, and the highest-ranked courses are displayed as recommendations.

---

## 🗺️ Personalized Roadmap

Based on the selected programming language and experience level, PathPilot AI generates a suggested learning path.

For example:

```text
Fundamentals
     ↓
Core Concepts
     ↓
Data Structures / Tools
     ↓
Projects
     ↓
Career Preparation
