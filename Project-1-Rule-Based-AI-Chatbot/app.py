import streamlit as st
from datetime import datetime
import random
import math

# ======================================================
# PAGE CONFIGURATION
# ======================================================

st.set_page_config(
    page_title="DecodeBot AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================
# CUSTOM CSS
# ======================================================

st.markdown("""
<style>

/* -----------------------------
   Hide Streamlit Default Elements
------------------------------ */

#MainMenu{
    visibility:hidden;
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* -----------------------------
   Main Background
------------------------------ */

.stApp{
    background:#050505;
    color:white;
}

/* -----------------------------
   Sidebar
------------------------------ */

section[data-testid="stSidebar"]{
    background:#0B0F19;
    border-right:1px solid #1F2937;
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* -----------------------------
   Cards / Metrics
------------------------------ */

div[data-testid="metric-container"]{
    background:#111827;
    border:1px solid #2563EB;
    border-radius:18px;
    padding:15px;
    box-shadow:0 0 20px rgba(37,99,235,.25);
}

/* -----------------------------
   Buttons
------------------------------ */

.stButton>button{

    width:100%;
    height:48px;

    background:linear-gradient(90deg,#2563EB,#3B82F6);

    color:white;

    border:none;

    border-radius:12px;

    font-size:16px;

    font-weight:600;

    transition:.3s;

}

.stButton>button:hover{

    background:linear-gradient(90deg,#3B82F6,#60A5FA);

    transform:scale(1.02);

    box-shadow:0 0 20px rgba(59,130,246,.45);

}

/* -----------------------------
   Inputs
------------------------------ */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"]{

    background:#111827 !important;

    color:white !important;

    border:1px solid #374151 !important;

    border-radius:12px !important;

}

/* -----------------------------
   Chat Input
------------------------------ */
div[data-testid="stChatInput"]{
    background:#050505 !important;
}

div[data-testid="stChatInput"] textarea{
    background:#111827 !important;
    color:#FFFFFF !important;
    caret-color:#FFFFFF !important;
    border:1px solid #2563EB !important;
    border-radius:12px !important;
}

div[data-testid="stChatInput"] textarea::placeholder{
    color:#9CA3AF !important;
    opacity:1 !important;
}

div[data-testid="stChatInput"] button{
    background:#2563EB !important;
    color:white !important;
}

/* -----------------------------
   Chat Messages
------------------------------ */

div[data-testid="stChatMessage"]{

    background:#111827;

    border-radius:18px;

    padding:12px;

    margin-bottom:10px;

    border:1px solid #1F2937;

}

/* -----------------------------
   Expander
------------------------------ */

.streamlit-expanderHeader{

    color:white !important;

    font-weight:bold;

}

/* -----------------------------
   Code Block
------------------------------ */

pre{

    border-radius:12px !important;

}

/* -----------------------------
   Scrollbar
------------------------------ */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-track{

    background:#050505;

}

::-webkit-scrollbar-thumb{

    background:#2563EB;

    border-radius:20px;

}

::-webkit-scrollbar-thumb:hover{

    background:#3B82F6;

}

</style>
""", unsafe_allow_html=True)

# ======================================================
# SESSION STATE
# ======================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "commands" not in st.session_state:
    st.session_state.commands = 0

if "calculator" not in st.session_state:
    st.session_state.calculator = 0

if "games" not in st.session_state:
    st.session_state.games = 0

if "number" not in st.session_state:
    st.session_state.number = random.randint(1,10)

# ======================================================
# SIDEBAR
# ======================================================

with st.sidebar:

    st.markdown("# 🤖 DecodeBot")

    st.caption("DecodeLabs AI Internship")

    st.divider()

    st.metric("💬 Commands", st.session_state.commands)

    st.metric("🧮 Calculator", st.session_state.calculator)

    st.metric("🎮 Games", st.session_state.games)

    st.divider()

    st.subheader("📅 Today")

    st.success(datetime.now().strftime("%d %B %Y"))

    st.subheader("⏰ Time")

    st.info(datetime.now().strftime("%I:%M:%S %p"))

    st.divider()

    st.subheader("Available Commands")

    st.code("""
hello
date
time
day
joke
quote
fact
calculator
game
help
exit
""")

    st.divider()

if st.button("🗑️ Clear Chat", key="sidebar_clear"):
    st.session_state.messages = []
    st.rerun()

# ======================================================
# HERO SECTION
# ======================================================

st.markdown("""
<div style="
padding:30px;
border-radius:20px;
background:linear-gradient(135deg,#111827,#1E3A8A);
box-shadow:0px 0px 35px rgba(59,130,246,.30);
margin-bottom:25px;
text-align:center;
">

<h1 style="font-size:48px;color:white;">

🤖 DecodeBot AI

</h1>

<p style="font-size:20px;color:#d1d5db;">

Your Smart Rule-Based AI Assistant

</p>

</div>
""",unsafe_allow_html=True)

# ======================================================
# WELCOME CARD
# ======================================================

st.markdown("""
<div style="
background:#111827;
padding:25px;
border-radius:18px;
border:1px solid #374151;
margin-bottom:25px;
">

<h2>👋 Welcome</h2>

DecodeBot can help you with:

✔ Date & Time

✔ Day

✔ Funny Jokes

✔ Motivational Quotes

✔ Interesting Facts

✔ Smart Calculator

✔ Guess The Number Game

Type **help** in the chat to see all commands.

</div>
""",unsafe_allow_html=True)

# ======================================================
# CHAT HISTORY
# ======================================================

for role, msg in st.session_state.messages:

    with st.chat_message(role):

        if role == "assistant":
            st.markdown(
                f"<h4 style='color:#60A5FA;'>🤖 DecodeBot</h4>"
                f"<p style='color:white;font-size:17px;'>{msg}</p>",
                unsafe_allow_html=True
            )

        else:
            st.markdown(
                f"<h4 style='color:#22C55E;'>🧑 You</h4>"
                f"<p style='color:white;font-size:17px;'>{msg}</p>",
                unsafe_allow_html=True
            )

prompt=st.chat_input("Ask DecodeBot anything...")

if prompt:

    st.session_state.commands+=1

    st.session_state.messages.append(("user",prompt))

    text=prompt.lower().strip()

    jokes=[
        "Why don't programmers like nature? Because it has too many bugs! 😂",
        "Python developers wear glasses because they can't C.",
        "Debugging is being the detective and the culprit."
    ]

    quotes=[
        "Dream big. Start small. Act now.",
        "Consistency beats perfection.",
        "Every expert was once a beginner."
    ]

    facts=[
        "Python was created in 1991.",
        "Artificial Intelligence is transforming every industry.",
        "The first computer bug was actually a moth."
    ]

    if text in ["hi","hello","hey"]:

        reply="Hello! 👋 Nice to meet you."

    elif text=="date":

        reply=datetime.now().strftime("%d %B %Y")

    elif text=="time":

        reply=datetime.now().strftime("%I:%M:%S %p")

    elif text=="day":

        reply=datetime.now().strftime("%A")

    elif text=="joke":

        reply=random.choice(jokes)

    elif text=="quote":

        reply=random.choice(quotes)

    elif text=="fact":

        reply=random.choice(facts)

    elif text=="calculator":

        reply="🧮 Scroll down to use the Smart Calculator."

    elif text=="game":

        reply="🎮 Scroll down to play Guess The Number."

    elif text=="help":

        reply="""
Available Commands

• hello
• date
• time
• day
• joke
• quote
• fact
• calculator
• game
• help
• exit
"""

    elif text=="exit":

        reply="👋 Goodbye! Have a wonderful day."

    else:

        reply="Sorry, I don't understand that. Type **help**."

    st.session_state.messages.append(("assistant",reply))

    st.rerun()
# ======================================================
# SMART CALCULATOR
# ======================================================

st.divider()

st.subheader("🧮 Smart Calculator")

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("First Number", value=0.0)

with col2:
    num2 = st.number_input("Second Number", value=0.0)

operation = st.selectbox(
    "Choose Operation",
    [
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Power",
        "Square Root"
    ]
)

if st.button("Calculate"):

    st.session_state.calculator += 1

    if operation == "Addition":
        result = num1 + num2

    elif operation == "Subtraction":
        result = num1 - num2

    elif operation == "Multiplication":
        result = num1 * num2

    elif operation == "Division":
        if num2 == 0:
            result = "❌ Cannot divide by zero"
        else:
            result = num1 / num2

    elif operation == "Power":
        result = num1 ** num2

    elif operation == "Square Root":

        if num1 < 0:
            result = "❌ Invalid Number"
        else:
            result = math.sqrt(num1)

    st.success(f"✅ Result : {result}")

    st.balloons()

# ======================================================
# GUESS THE NUMBER GAME
# ======================================================

st.divider()

st.subheader("🎮 Guess The Number")

st.write("I'm thinking of a number between **1 and 10**.")

guess = st.number_input(
    "Enter your Guess",
    min_value=1,
    max_value=10,
    step=1
)

col1, col2 = st.columns(2)

with col1:

    if st.button("🎯 Guess"):

        st.session_state.games += 1

        if guess == st.session_state.number:

            st.success("🎉 Congratulations! Correct Guess!")

            st.balloons()

            st.session_state.number = random.randint(1,10)

        elif guess < st.session_state.number:

            st.warning("📉 Too Low")

        else:

            st.warning("📈 Too High")

with col2:

    if st.button("🔄 New Number"):

        st.session_state.number = random.randint(1,10)

        st.info("New Number Generated!")

# ======================================================
# ABOUT SECTION
# ======================================================

st.divider()

with st.expander("ℹ️ About DecodeBot"):

    st.markdown("""

### 🤖 DecodeBot AI

DecodeBot is a **Rule-Based AI Chatbot**
developed using **Python** and **Streamlit**
for the **DecodeLabs AI Internship**.

### 🚀 Features

- 💬 AI Chat
- 📅 Date & Time
- 😂 Random Jokes
- 💡 Quotes
- 📚 AI Facts
- 🧮 Smart Calculator
- 🎮 Guess The Number
- 📊 Session Statistics

### 👨‍💻 Developer

**Sai**

""")

# ======================================================
# SESSION SUMMARY
# ======================================================

st.divider()

st.subheader("📊 Session Summary")

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Commands",
        st.session_state.commands
    )

with c2:

    st.metric(
        "Calculator Used",
        st.session_state.calculator
    )

with c3:

    st.metric(
        "Games Played",
        st.session_state.games
    )

# ======================================================
# FOOTER
# ======================================================

st.divider()

st.markdown("""
<div style="
text-align:center;
padding:25px;
background:#111827;
border-radius:15px;
margin-top:20px;
">

<h3 style="color:#60A5FA;">
🤖 DecodeBot AI
</h3>

<p style="color:#D1D5DB;">

Built with ❤️ using Python & Streamlit

</p>

<p style="color:#9CA3AF;">

DecodeLabs AI 2026

</p>

<p style="color:#9CA3AF;">

Developed by <b>Saianshi</b>

</p>

</div>
""", unsafe_allow_html=True)    