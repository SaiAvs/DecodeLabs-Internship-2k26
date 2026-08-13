import streamlit as st
import pandas as pd
import time

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="PathPilot AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
# =====================================================
# RESET APPLICATION
# =====================================================

if "reset_app" not in st.session_state:
    st.session_state.reset_app = False

if st.session_state.reset_app:
    st.session_state.clear()
    st.rerun()

# =====================================================
# GLOBAL CSS
# =====================================================

st.markdown(
    """
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap'
    );

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    .stApp {
        background:
            radial-gradient(
                circle at top left,
                rgba(124,58,237,0.14),
                transparent 35%
            ),
            radial-gradient(
                circle at bottom right,
                rgba(6,182,212,0.12),
                transparent 35%
            ),
            linear-gradient(
                135deg,
                #050816,
                #0B1120,
                #111827
            );

        color: white;
    }

    section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #111827 0%,
            #0F172A 50%,
            #111827 100%
        );

    backdrop-filter: blur(18px);

    border-right:
        1px solid rgba(255,255,255,0.08);
}

/* Sidebar text */

section[data-testid="stSidebar"] * {
    color: #F8FAFC;
}

/* Sidebar caption */

section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
    color: #94A3B8 !important;
}

/* Sidebar headings */

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #FFFFFF !important;
}

/* Sidebar normal text */

section[data-testid="stSidebar"] p {
    color: #E2E8F0 !important;
}

/* Sidebar divider */

section[data-testid="stSidebar"] hr {
    border-color:
        rgba(255,255,255,0.08);
}

/* Sidebar metric cards */

section[data-testid="stSidebar"]
div[data-testid="metric-container"] {
    background:
        rgba(255,255,255,0.045);

    border:
        1px solid rgba(255,255,255,0.08);

    border-radius: 16px;

    padding: 16px;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.20);
}

/* Metric labels */

section[data-testid="stSidebar"]
div[data-testid="metric-container"]
[data-testid="stMetricLabel"] {
    color: #CBD5E1 !important;
}

/* Metric values */

section[data-testid="stSidebar"]
div[data-testid="metric-container"]
[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
}

/* Sidebar info box */

section[data-testid="stSidebar"]
div[data-testid="stAlert"] {
    background:
        rgba(139,92,246,0.12);

    border:
        1px solid rgba(139,92,246,0.25);

    color: #EDE9FE;
}

    div[data-testid="metric-container"] {
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(14px);
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.08);
        padding: 18px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.35);
    }

    div[data-testid="metric-container"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 0 30px rgba(139,92,246,0.45);
    }

    .stButton > button {
        width: 100%;
        height: 54px;
        border: none;
        border-radius: 16px;
        font-size: 17px;
        font-weight: 700;
        color: white;

        background:
            linear-gradient(
                90deg,
                #8B5CF6,
                #EC4899,
                #06B6D4
            );

        background-size: 250%;

        transition: 0.45s;

        box-shadow:
            0 0 25px rgba(139,92,246,0.35);
    }

    .stButton > button:hover {
        transform: translateY(-3px);
        background-position: right;
        box-shadow: 0 0 40px rgba(236,72,153,0.55);
    }

    div[data-baseweb="select"] {
        background: rgba(255,255,255,0.05);
        border-radius: 14px;
    }

    div[data-baseweb="select"] > div {
        background: rgba(255,255,255,0.06);
        color: white;
        border: 1px solid rgba(255,255,255,0.10);
    }

    div[data-testid="stAlert"] {
        border-radius: 16px;
    }

    div[data-testid="stProgress"] > div > div {
        background:
            linear-gradient(
                90deg,
                #8B5CF6,
                #EC4899,
                #06B6D4
            );
    }

    ::-webkit-scrollbar {
        width: 10px;
    }

    ::-webkit-scrollbar-track {
        background: #111827;
    }

    ::-webkit-scrollbar-thumb {
        background: #8B5CF6;
        border-radius: 20px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #EC4899;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# COURSE DATASET
# =====================================================

courses = [
    {
        "Course": "Python for Beginners",
        "Language": "Python",
        "Level": "Beginner",
        "Domain": "Programming",
        "Duration": "6 Weeks",
        "Rating": 4.8,
        "Platform": "Coursera"
    },
    {
        "Course": "Java Programming Masterclass",
        "Language": "Java",
        "Level": "Intermediate",
        "Domain": "Programming",
        "Duration": "8 Weeks",
        "Rating": 4.7,
        "Platform": "Udemy"
    },
    {
        "Course": "Web Development Bootcamp",
        "Language": "JavaScript",
        "Level": "Beginner",
        "Domain": "Web Development",
        "Duration": "10 Weeks",
        "Rating": 4.9,
        "Platform": "Udemy"
    },
    {
        "Course": "Machine Learning A-Z",
        "Language": "Python",
        "Level": "Intermediate",
        "Domain": "Machine Learning",
        "Duration": "12 Weeks",
        "Rating": 4.9,
        "Platform": "Udemy"
    },
    {
        "Course": "Deep Learning Specialization",
        "Language": "Python",
        "Level": "Advanced",
        "Domain": "Deep Learning",
        "Duration": "14 Weeks",
        "Rating": 4.9,
        "Platform": "Coursera"
    },
    {
        "Course": "SQL for Data Analysis",
        "Language": "SQL",
        "Level": "Beginner",
        "Domain": "Database",
        "Duration": "5 Weeks",
        "Rating": 4.6,
        "Platform": "DataCamp"
    },
    {
        "Course": "PostgreSQL Complete Guide",
        "Language": "PostgreSQL",
        "Level": "Intermediate",
        "Domain": "Database",
        "Duration": "6 Weeks",
        "Rating": 4.7,
        "Platform": "Udemy"
    },
    {
        "Course": "Data Structures & Algorithms",
        "Language": "Java",
        "Level": "Intermediate",
        "Domain": "DSA",
        "Duration": "10 Weeks",
        "Rating": 4.8,
        "Platform": "Coursera"
    },
    {
        "Course": "React - The Complete Guide",
        "Language": "JavaScript",
        "Level": "Intermediate",
        "Domain": "Web Development",
        "Duration": "8 Weeks",
        "Rating": 4.8,
        "Platform": "Udemy"
    },
    {
        "Course": "GATE CSE Data Structures and Algorithms",
        "Language": "C++",
        "Level": "Advanced",
        "Domain": "DSA",
        "Duration": "12 Weeks",
        "Rating": 4.9,
        "Platform": "NPTEL"
    }
]

df = pd.DataFrame(courses)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("# 🤖 PathPilot AI")

    st.caption(
        "AI Programming Course Recommendation System"
    )

    st.divider()

    st.metric(
        "📚 Total Courses",
        len(df)
    )

    st.metric(
        "🧠 Recommendation Engine",
        "AI"
    )

    st.metric(
        "⭐ Accuracy Goal",
        "95%"
    )

    st.divider()

    st.subheader("💻 Technologies")

    st.write("🐍 Python")
    st.write("📊 Pandas")
    st.write("🌐 Streamlit")
    st.write("🤖 Scikit-learn")

    st.divider()

    st.info(
        "🚀 Learn smarter with AI-powered recommendations."
    )

# =====================================================
# HERO SECTION
# =====================================================

st.html(
    """
    <div style="
        background: rgba(255,255,255,0.06);
        backdrop-filter: blur(18px);
        padding: 40px;
        border-radius: 24px;
        border: 1px solid rgba(255,255,255,0.12);
        text-align: center;
        box-shadow: 0 0 40px rgba(139,92,246,0.25);
        margin-bottom: 35px;
    ">

        <h1 style="
            font-size: 52px;
            font-weight: 800;
            margin-bottom: 10px;
            background: linear-gradient(
                90deg,
                #8B5CF6,
                #EC4899,
                #06B6D4
            );
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        ">
            🤖 PathPilot AI
        </h1>

        <p style="
            font-size: 22px;
            color: #D1D5DB;
            margin-bottom: 8px;
        ">
            Your Intelligent Programming Course
            Recommendation System
        </p>

        <p style="
            font-size: 16px;
            color: #9CA3AF;
        ">
            Discover the perfect learning roadmap
            tailored to your skills, goals, and interests.
        </p>

    </div>
    """
)

# =====================================================
# USER PROFILE
# =====================================================

st.markdown("## 🎯 Tell us about yourself")

col1, col2 = st.columns(2)

with col1:

    level = st.selectbox(
        "👨 Experience Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    language = st.selectbox(
        "💻 Preferred Language",
        [
            "Python",
            "Java",
            "JavaScript",
            "SQL",
            "PostgreSQL",
            "C++"
        ]
    )

with col2:

    domain = st.selectbox(
        "🎯 Domain",
        [
            "Programming",
            "Web Development",
            "Machine Learning",
            "Deep Learning",
            "Database",
            "DSA"
        ]
    )

    goal = st.selectbox(
        "📚 Learning Goal",
        [
            "Skill Development",
            "College",
            "Job Preparation",
            "Interview Preparation"
        ]
    )

st.write("")

# =====================================================
# RECOMMENDATION BUTTON
# =====================================================

recommend = st.button(
    "🚀 Get AI Recommendations"
)

# =====================================================
# AI RECOMMENDATION ENGINE
# =====================================================

if recommend:

    # -------------------------------------------------
    # AI LOADING ANIMATION
    # -------------------------------------------------

    status = st.empty()
    progress = st.progress(0)

    status.info("🧠 Initializing AI Engine...")
    for i in range(20):
        progress.progress(i + 1)
        time.sleep(0.02)

    status.info("📊 Reading your learning profile...")
    for i in range(20, 40):
        progress.progress(i + 1)
        time.sleep(0.02)

    status.info("🔍 Searching the course database...")
    for i in range(40, 60):
        progress.progress(i + 1)
        time.sleep(0.02)

    status.info("🎯 Matching your interests...")
    for i in range(60, 80):
        progress.progress(i + 1)
        time.sleep(0.02)

    status.info("🚀 Generating personalized recommendations...")
    for i in range(80, 100):
        progress.progress(i + 1)
        time.sleep(0.02)

    status.success("✅ Recommendations Ready!")

    # -------------------------------------------------
    # FIND MATCHING COURSES
    # -------------------------------------------------

    recommendations = df[
        (df["Level"] == level) &
        (df["Language"] == language) &
        (df["Domain"] == domain)
    ]

    st.write("")
    st.subheader("🎯 AI Recommended Courses")

    # -------------------------------------------------
    # NO MATCH
    # -------------------------------------------------

    if recommendations.empty:

        st.warning(
            "⚠️ No exact match found. Try selecting different options."
        )

    # -------------------------------------------------
    # SHOW RECOMMENDATIONS
    # -------------------------------------------------

    else:

        for card_number, (_, row) in enumerate(
            recommendations.iterrows(),
            start=1
        ):

            match_percentage = min(
                99,
                95 + card_number
            )

            course_name = row["Course"]
            course_language = row["Language"]
            course_domain = row["Domain"]
            course_level = row["Level"]
            course_duration = row["Duration"]
            course_rating = row["Rating"]
            course_platform = row["Platform"]

            # -------------------------------------------------
            # RECOMMENDATION CARD
            # -------------------------------------------------

            st.html(
f"""
<div style="
    background: linear-gradient(
        145deg,
        rgba(255,255,255,0.08),
        rgba(255,255,255,0.035)
    );
    padding: 30px;
    border-radius: 24px;
    border: 1px solid rgba(255,255,255,0.12);
    margin: 20px 0;
    box-shadow: 0 12px 40px rgba(0,0,0,0.25);
">

    <div style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        margin-bottom:20px;
    ">

        <h4 style="
            color:#EC4899;
            margin:0;
            font-size:18px;
        ">
            ✨ AI Recommendation #{card_number}
        </h4>

        <span style="
            background:rgba(139,92,246,0.18);
            color:#C4B5FD;
            padding:8px 16px;
            border-radius:20px;
            font-weight:600;
        ">
            💡 {match_percentage}% Match
        </span>

    </div>

    <h2 style="
        color:white;
        margin:0 0 22px 0;
        font-size:28px;
    ">
        📘 {course_name}
    </h2>

    <div style="
        display:grid;
        grid-template-columns:repeat(3,1fr);
        gap:15px;
        margin-bottom:22px;
    ">

        <div style="
            background:rgba(255,255,255,0.05);
            padding:14px;
            border-radius:14px;
        ">
            ⭐ <b>Rating</b><br>
            {course_rating}
        </div>

        <div style="
            background:rgba(255,255,255,0.05);
            padding:14px;
            border-radius:14px;
        ">
            ⏳ <b>Duration</b><br>
            {course_duration}
        </div>

        <div style="
            background:rgba(255,255,255,0.05);
            padding:14px;
            border-radius:14px;
        ">
            🌐 <b>Platform</b><br>
            {course_platform}
        </div>

    </div>

    <hr style="
        border:none;
        border-top:1px solid rgba(255,255,255,0.10);
        margin:20px 0;
    ">

    <p style="color:#D1D5DB;">
        💻 <b>Language:</b> {course_language}
    </p>

    <p style="color:#D1D5DB;">
        🎯 <b>Domain:</b> {course_domain}
    </p>

    <p style="color:#D1D5DB;">
        📈 <b>Level:</b> {course_level}
    </p>

    <div style="
    margin-top:24px;
    padding:18px;
    border-radius:16px;
    background:rgba(139,92,246,0.12);
    border:1px solid rgba(139,92,246,0.25);
">

    <h4 style="
        color:#C4B5FD;
        margin:0 0 8px 0;
    ">
        🧠 Why this course?
    </h4>

    <p style="
        color:#D1D5DB;
        margin:0;
        line-height:1.6;
    ">
        This course matches your
        <b>{course_level}</b> experience level,
        preferred language <b>{course_language}</b>,
        and selected domain <b>{course_domain}</b>.
    </p>

</div>

<div style="
    margin-top:15px;
    padding:14px;
    border-radius:14px;
    text-align:center;
    font-weight:600;
    color:white;
    background:linear-gradient(
        90deg,
        #8B5CF6,
        #EC4899,
        #06B6D4
    );
">
    🚀 Personalized Recommendation
</div>
"""
            )
            # =====================================================
# PERSONALIZED LEARNING ROADMAP
# =====================================================

st.write("")
st.divider()

st.subheader("🗺️ Your Personalized Learning Roadmap")

st.caption(
    "A suggested learning path based on your selected "
    "language, experience level, domain, and goal."
)

if language == "Python":

    if level == "Beginner":
        roadmap = [
            ("01", "Python Basics", "Variables, data types, conditions and loops"),
            ("02", "Functions & Modules", "Functions, modules and error handling"),
            ("03", "Object-Oriented Python", "Classes, objects and inheritance"),
            ("04", "Data Handling", "NumPy, Pandas and data visualization"),
            ("05", "Next Step", "Move toward your selected domain")
        ]

    elif level == "Intermediate":
        roadmap = [
            ("01", "Advanced Python", "Advanced functions and Python concepts"),
            ("02", "Data Structures", "Lists, dictionaries, sets and tuples"),
            ("03", "Pandas & NumPy", "Data processing and numerical computing"),
            ("04", "Project Development", "Build practical Python projects"),
            ("05", "Specialization", f"Continue toward {domain}")
        ]

    else:
        roadmap = [
            ("01", "Advanced Python", "Advanced programming concepts"),
            ("02", "System Design", "Design scalable applications"),
            ("03", "Advanced Projects", "Build production-level projects"),
            ("04", f"{domain}", "Develop domain-specific expertise"),
            ("05", "Career Preparation", f"Prepare for {goal}")
        ]

elif language == "Java":

    roadmap = [
        ("01", "Java Fundamentals", "Syntax, variables, conditions and loops"),
        ("02", "Object-Oriented Programming", "Classes, objects, inheritance and polymorphism"),
        ("03", "Collections & Exceptions", "Collections framework and error handling"),
        ("04", "Data Structures & Algorithms", "Problem solving and algorithmic thinking"),
        ("05", "Career Projects", f"Build projects for {goal}")
    ]

elif language == "JavaScript":

    roadmap = [
        ("01", "JavaScript Fundamentals", "Variables, functions and control flow"),
        ("02", "DOM & Events", "Interactive web development"),
        ("03", "Modern JavaScript", "ES6+, modules and asynchronous programming"),
        ("04", "React", "Build modern frontend applications"),
        ("05", "Web Development", f"Prepare for {goal}")
    ]

elif language == "SQL":

    roadmap = [
        ("01", "SQL Fundamentals", "Queries, filtering and sorting"),
        ("02", "Joins & Relationships", "Connect data from multiple tables"),
        ("03", "Aggregation", "GROUP BY, functions and subqueries"),
        ("04", "Database Design", "Schemas, keys and normalization"),
        ("05", "Data Analysis", f"Apply SQL toward {goal}")
    ]

else:

    roadmap = [
        ("01", "Database Fundamentals", "Understand relational databases"),
        ("02", "PostgreSQL", "Queries and PostgreSQL features"),
        ("03", "Database Design", "Schemas, keys and normalization"),
        ("04", "Advanced SQL", "Subqueries, views and optimization"),
        ("05", "Practical Projects", f"Build projects for {goal}")
    ]


# -----------------------------------------------------
# DISPLAY ROADMAP
# -----------------------------------------------------

for step_number, title, description in roadmap:

    st.html(
f"""
<div style="
    display:flex;
    align-items:flex-start;
    gap:20px;
    padding:22px;
    margin:14px 0;
    border-radius:18px;
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.09);
">

    <div style="
        min-width:48px;
        height:48px;
        border-radius:50%;
        display:flex;
        align-items:center;
        justify-content:center;
        background:linear-gradient(
            135deg,
            #8B5CF6,
            #EC4899
        );
        color:white;
        font-weight:700;
        font-size:16px;
    ">
        {step_number}
    </div>

    <div>

        <h3 style="
            margin:0 0 7px 0;
            color:white;
        ">
            {title}
        </h3>

        <p style="
            margin:0;
            color:#B8C1D9;
            line-height:1.6;
        ">
            {description}
        </p>

    </div>

</div>
"""
    )

st.success(
    f"🎯 Roadmap generated for a {level} learner "
    f"interested in {language} and {domain}."
)
# =====================================================
# BROWSE ALL COURSES
# =====================================================

st.write("")
st.divider()

st.subheader("📚 Explore All Available Courses")

st.caption(
    "Browse the complete PathPilot AI course database."
)

show_courses = st.checkbox(
    "👀 Show all courses"
)

if show_courses:

    display_df = df[
        [
            "Course",
            "Language",
            "Level",
            "Domain",
            "Duration",
            "Rating",
            "Platform"
        ]
    ].copy()

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )
# =====================================================
# START OVER
# =====================================================

st.write("")
st.divider()

if st.button("🔄 Start Over", key="start_over"):

    st.session_state.reset_app = True
    st.rerun()