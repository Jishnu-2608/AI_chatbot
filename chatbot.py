import streamlit as st
from groq import Groq

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Jishnu AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# GROQ API
# ==========================================================

GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

/* REMOVE DEFAULT STREAMLIT SPACE */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
    height: 0px !important;
}

[data-testid="stToolbar"] {
    visibility: hidden;
    height: 0px;
}

.block-container {
    padding-top: 0.5rem !important;
    padding-bottom: 1rem !important;
    max-width: 1500px !important;
}


/* MAIN BACKGROUND */

.stApp {

    background:
        radial-gradient(
            circle at 15% 15%,
            rgba(79, 70, 229, 0.22),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 80%,
            rgba(147, 51, 234, 0.20),
            transparent 32%
        ),
        linear-gradient(
            135deg,
            #070b18 0%,
            #0d1225 45%,
            #100b20 100%
        );

    min-height: 100vh;
}


/* ANIMATED BACKGROUND */

.stApp::before {

    content: "";

    position: fixed;

    width: 320px;
    height: 320px;

    left: 20%;
    top: 15%;

    border-radius: 50%;

    background: rgba(99, 102, 241, 0.12);

    filter: blur(90px);

    animation: orbOne 9s ease-in-out infinite;

    pointer-events: none;

    z-index: 0;
}


.stApp::after {

    content: "";

    position: fixed;

    width: 300px;
    height: 300px;

    right: 10%;
    bottom: 10%;

    border-radius: 50%;

    background: rgba(168, 85, 247, 0.13);

    filter: blur(90px);

    animation: orbTwo 11s ease-in-out infinite;

    pointer-events: none;

    z-index: 0;
}


@keyframes orbOne {

    0% {
        transform: translate(0, 0);
    }

    50% {
        transform: translate(80px, 50px);
    }

    100% {
        transform: translate(0, 0);
    }
}


@keyframes orbTwo {

    0% {
        transform: translate(0, 0);
    }

    50% {
        transform: translate(-70px, -40px);
    }

    100% {
        transform: translate(0, 0);
    }
}


/* ==========================================================
   FORCE NORMAL APP TEXT TO BE FULLY VISIBLE
========================================================== */

.stMarkdown,
.stMarkdown p,
.stMarkdown span {

    opacity: 1 !important;

}


/* SIDEBAR */

section[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            #090d1c,
            #0d1326
        ) !important;

    border-right:
        1px solid rgba(129, 140, 248, 0.20);

}


section[data-testid="stSidebar"] * {

    color: #e5e7eb !important;

}


/* SIDEBAR BRAND */

.sidebar-brand {

    text-align: center;

    padding: 18px 10px 22px 10px;

}


.sidebar-logo {

    width: 65px;
    height: 65px;

    margin: auto;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 20px;

    font-size: 32px;

    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #9333ea
        );

    box-shadow:
        0 0 30px rgba(99, 102, 241, 0.45);

    animation: logoPulse 3s ease-in-out infinite;

}


@keyframes logoPulse {

    0% {
        box-shadow:
        0 0 15px rgba(99,102,241,0.30);
    }

    50% {
        box-shadow:
        0 0 35px rgba(168,85,247,0.55);
    }

    100% {
        box-shadow:
        0 0 15px rgba(99,102,241,0.30);
    }
}


.sidebar-name {

    font-size: 22px;

    font-weight: 800;

    margin-top: 12px;

    background:
        linear-gradient(
            90deg,
            #818cf8,
            #c084fc
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

}


.sidebar-subtitle {

    color: #94a3b8 !important;

    font-size: 13px;

}


/* SIDEBAR BOX */

.sidebar-section {

    margin-top: 22px;

    padding: 15px;

    border-radius: 16px;

    background:
        rgba(30, 41, 59, 0.45);

    border:
        1px solid rgba(148, 163, 184, 0.10);

}


/* MODEL SELECT */

div[data-baseweb="select"] > div {

    background: #111827 !important;

    border:
        1px solid rgba(129, 140, 248, 0.35) !important;

    border-radius: 12px !important;

}


/* BUTTON */

.stButton > button {

    width: 100%;

    border-radius: 12px;

    border:
        1px solid rgba(129, 140, 248, 0.35);

    background:
        linear-gradient(
            135deg,
            #4338ca,
            #7e22ce
        );

    color: white !important;

    font-weight: 700;

    transition: all 0.25s ease;

}


.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 8px 25px rgba(124, 58, 237, 0.35);

}


/* ==========================================================
   HEADER
========================================================== */

.chat-header {

    position: relative;

    z-index: 2;

    margin-top: 5px;

    padding: 22px 28px;

    border-radius: 22px;

    background:
        linear-gradient(
            135deg,
            rgba(30, 41, 88, 0.72),
            rgba(59, 30, 91, 0.65)
        );

    border:
        1px solid rgba(129, 140, 248, 0.25);

    box-shadow:
        0 15px 45px rgba(0,0,0,0.25);

    backdrop-filter: blur(15px);

}


.header-content {

    display: flex;

    align-items: center;

    gap: 18px;

}


.ai-icon {

    width: 64px;
    height: 64px;

    min-width: 64px;

    border-radius: 18px;

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 32px;

    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #9333ea
        );

    box-shadow:
        0 0 30px rgba(99,102,241,0.35);

}


.header-title {

    font-size: 31px;

    font-weight: 800;

    color: #ffffff;

}


.header-description {

    margin-top: 3px;

    color: #a5b4fc;

    font-size: 14px;

}


.online-status {

    margin-left: auto;

    padding: 7px 14px;

    border-radius: 30px;

    background:
        rgba(34,197,94,0.12);

    border:
        1px solid rgba(34,197,94,0.25);

    color: #86efac;

    font-size: 13px;

}


/* ==========================================================
   WELCOME
========================================================== */

.welcome-card {

    margin-top: 22px;

    padding: 35px;

    text-align: center;

    border-radius: 22px;

    background:
        linear-gradient(
            135deg,
            rgba(30,41,59,0.60),
            rgba(49,46,129,0.30)
        );

    border:
        1px solid rgba(129,140,248,0.18);

    box-shadow:
        0 15px 40px rgba(0,0,0,0.20);

}


.welcome-icon {

    font-size: 48px;

    margin-bottom: 8px;

}


.welcome-title {

    font-size: 25px;

    font-weight: 750;

    color: #ffffff;

}


.welcome-text {

    color: #94a3b8;

    margin-top: 7px;

    font-size: 15px;

}


/* FEATURES */

.feature-row {

    display: flex;

    gap: 12px;

    justify-content: center;

    margin-top: 22px;

}


.feature {

    padding: 10px 15px;

    border-radius: 12px;

    background:
        rgba(15,23,42,0.55);

    border:
        1px solid rgba(148,163,184,0.12);

    color: #cbd5e1;

    font-size: 13px;

}


/* ==========================================================
   CHAT MESSAGES
   BRIGHT WHITE TEXT
========================================================== */

[data-testid="stChatMessage"] {

    margin-top: 12px;

    padding: 13px;

    border-radius: 18px;

    background:
        rgba(15, 23, 42, 0.68);

    border:
        1px solid rgba(129, 140, 248, 0.14);

    box-shadow:
        0 8px 25px rgba(0,0,0,0.15);

    animation: messageIn 0.35s ease;

}


/* FORCE CHAT TEXT TO PURE WHITE */

[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] span,
[data-testid="stChatMessage"] div,
[data-testid="stChatMessage"] li,
[data-testid="stChatMessage"] ul,
[data-testid="stChatMessage"] ol {

    color: #ffffff !important;

    opacity: 1 !important;

}


/* CHAT HEADINGS */

[data-testid="stChatMessage"] h1,
[data-testid="stChatMessage"] h2,
[data-testid="stChatMessage"] h3,
[data-testid="stChatMessage"] h4,
[data-testid="stChatMessage"] h5,
[data-testid="stChatMessage"] h6 {

    color: #ffffff !important;

    opacity: 1 !important;

}


/* CHAT CODE */

[data-testid="stChatMessage"] code {

    color: #ffffff !important;

    opacity: 1 !important;

}


/* CHAT CODE BLOCK */

[data-testid="stChatMessage"] pre {

    background: #111827 !important;

    color: #ffffff !important;

    border-radius: 10px;

    border:
        1px solid rgba(129,140,248,0.25);

}


[data-testid="stChatMessage"] pre code {

    color: #ffffff !important;

    opacity: 1 !important;

}


/* CHAT LINKS */

[data-testid="stChatMessage"] a {

    color: #a5b4fc !important;

}


/* CHAT TABLE */

[data-testid="stChatMessage"] table {

    color: #ffffff !important;

}


[data-testid="stChatMessage"] th,
[data-testid="stChatMessage"] td {

    color: #ffffff !important;

}


/* CHAT BLOCKQUOTE */

[data-testid="stChatMessage"] blockquote {

    color: #ffffff !important;

    border-left:
        3px solid #818cf8;

}


/* MESSAGE ANIMATION */

@keyframes messageIn {

    from {

        opacity: 0;

        transform: translateY(12px);

    }

    to {

        opacity: 1;

        transform: translateY(0);

    }

}


/* ==========================================================
   CHAT INPUT
========================================================== */

[data-testid="stChatInput"] {

    position: relative;

    z-index: 5;

}


[data-testid="stChatInput"] > div {

    background:
        rgba(15,23,42,0.92) !important;

    border:
        1px solid rgba(129,140,248,0.35) !important;

    border-radius: 18px !important;

    box-shadow:
        0 0 25px rgba(79,70,229,0.15);

}


[data-testid="stChatInput"] textarea {

    color: #ffffff !important;

    background: transparent !important;

}


[data-testid="stChatInput"] textarea::placeholder {

    color: #94a3b8 !important;

}


/* ==========================================================
   FOOTER
========================================================== */

.chat-footer {

    text-align: center;

    margin-top: 18px;

    color: #64748b;

    font-size: 12px;

}

</style>
""", unsafe_allow_html=True)


# ==========================================================
# SESSION STATE
# ==========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.html("""
    <div class="sidebar-brand">

        <div class="sidebar-logo">
            🤖
        </div>

        <div class="sidebar-name">
            Jishnu AI
        </div>

        <div class="sidebar-subtitle">
            Powered by Groq
        </div>

    </div>
    """)

    st.markdown(
        '<div class="sidebar-section">',
        unsafe_allow_html=True
    )

    st.markdown("### ⚙️ AI Model")

    model = st.selectbox(
        "Choose a model",
        [
            "openai/gpt-oss-120b",
            "openai/gpt-oss-20b"
        ],
        label_visibility="collapsed"
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        '<div class="sidebar-section">',
        unsafe_allow_html=True
    )

    st.markdown("### 💬 Conversation")

    st.markdown(
        f"**Messages:** `{len(st.session_state.messages)}`"
    )

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        '<div class="sidebar-section">',
        unsafe_allow_html=True
    )

    st.markdown("### ✨ Features")

    st.markdown(
        """
        🧠 **AI Conversations**

        💾 **Session History**

        ⚡ **Fast Groq Responses**

        🎯 **Multiple AI Models**

        🎨 **Modern Interface**
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ==========================================================
# MAIN HEADER
# ==========================================================

st.html("""
<div class="chat-header">

    <div class="header-content">

        <div class="ai-icon">
            🤖
        </div>

        <div>

            <div class="header-title">
                Jishnu's AI Assistant
            </div>

            <div class="header-description">
                Your intelligent AI companion powered by Groq
            </div>

        </div>

        <div class="online-status">
            ● Online
        </div>

    </div>

</div>
""")


# ==========================================================
# WELCOME SCREEN
# ==========================================================

if len(st.session_state.messages) == 0:

    st.html("""
    <div class="welcome-card">

        <div class="welcome-icon">
            ✨
        </div>

        <div class="welcome-title">
            Welcome to Jishnu's AI Assistant
        </div>

        <div class="welcome-text">
            Ask me anything. I can help you learn,
            code, explain concepts and solve problems.
        </div>

        <div class="feature-row">

            <div class="feature">
                💻 Coding
            </div>

            <div class="feature">
                📚 Learning
            </div>

            <div class="feature">
                🧠 Problem Solving
            </div>

            <div class="feature">
                ✨ Ideas
            </div>

        </div>

    </div>
    """)


# ==========================================================
# DISPLAY CHAT HISTORY
# ==========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ==========================================================
# CHAT INPUT
# ==========================================================

user_message = st.chat_input(
    "Message Jishnu's AI Assistant..."
)


# ==========================================================
# GROQ RESPONSE
# ==========================================================

if user_message:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    with st.chat_message("user"):

        st.markdown(user_message)

    with st.chat_message("assistant"):

        with st.spinner("✨ Jishnu AI is thinking..."):

            try:

                response = client.chat.completions.create(

                    model=model,

                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are Jishnu's AI Assistant. "
                                "You are helpful, friendly, "
                                "accurate and knowledgeable. "
                                "Give clear and beginner-friendly "
                                "answers whenever possible."
                            )
                        }
                    ] + st.session_state.messages,

                    temperature=0.7,

                    max_tokens=2048
                )

                assistant_message = (
                    response.choices[0].message.content
                )

                st.markdown(assistant_message)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": assistant_message
                    }
                )

            except Exception as e:

                st.error(
                    "❌ Unable to connect to Groq."
                )

                st.write(
                    "Error details:",
                    str(e)
                )


# ==========================================================
# FOOTER
# ==========================================================

st.html("""
<div class="chat-footer">

    ⚡ Powered by Groq
    &nbsp; • &nbsp;
    🤖 Jishnu AI
    &nbsp; • &nbsp;
    ✨ Built by Jishnu

</div>
""")
