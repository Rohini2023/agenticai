# import streamlit as st
# from audio.record_audio import record_audio
# from audio.preprocess_audio import preprocess_audio
# from audio.speech_text import speech_to_text
# from audio.text_speech import speak
# from agent.agent_executor import run_agent
# from database.chat_history import save_chat, get_chat_history

# # Page config
# st.set_page_config(page_title="AI Voice Assistant", layout="wide")

# # Session state
# if "listening" not in st.session_state:
#     st.session_state.listening = False

# # 🎨 CSS Styling
# st.markdown("""
# <style>

# /* Background */
# .main {
#     background-color: #f1f5f9;
# }

# /* Sidebar */
# [data-testid="stSidebar"] {
#     background-color: #111827;
#     color: white;
# }

# /* Chat styles */
# .chat-user {
#     color: #60a5fa;
#     font-weight: bold;
# }
# .chat-bot {
#     color: #34d399;
#     margin-bottom: 10px;
# }

# /* Title */
# .title {
#     text-align: center;
#     font-size: 34px;
#     font-weight: bold;
#     color: #1e293b;
#     margin-bottom: 20px;
# }

# /* Status */
# .status {
#     margin-top: 25px;
#     font-size: 20px;
#     color: #475569;
#     text-align: center;
# }

# </style>
# """, unsafe_allow_html=True)

# # 🧭 Sidebar - Chat History
# st.sidebar.title("🗂 Chat History")

# history = get_chat_history()

# if history:
#     for user, bot in history[::-1][:10]:
#         st.sidebar.markdown(f'<div class="chat-user">👤 {user}</div>', unsafe_allow_html=True)
#         st.sidebar.markdown(f'<div class="chat-bot">🤖 {bot}</div>', unsafe_allow_html=True)
#         st.sidebar.markdown("---")
# else:
#     st.sidebar.write("No chat history yet")

# # 🎯 Center Layout
# left, center, right = st.columns([1, 2, 1])

# with center:

#     st.markdown('<div class="title">🎤 AI Voice Assistant</div>', unsafe_allow_html=True)

#     st.write("")
#     st.write("")

#     # 🎤 Clickable Mic Image
#     mic_html = """
#     <div style="text-align:center;">
#         <img src="https://cdn-icons-gif.flaticon.com/19015/19015816.gif"
#              width="130"
#              style="cursor:pointer; transition: 0.2s;"
#              onclick="window.location.href='?mic=true'">
#     </div>
#     """
#     st.markdown(mic_html, unsafe_allow_html=True)

#     # Detect click
#     query_params = st.query_params
#     if "mic" in query_params:
#         st.session_state.listening = True

#     # 🎧 Listening Flow
#     if st.session_state.listening:

#         st.markdown('<div class="status">🎧 Listening...</div>', unsafe_allow_html=True)

#         raw = record_audio()

#         if not raw:
#             st.markdown('<div class="status">❌ Could not hear you</div>', unsafe_allow_html=True)

#         else:
#             st.markdown('<div class="status">🧠 Processing...</div>', unsafe_allow_html=True)

#             clean = preprocess_audio(raw)
#             text = speech_to_text(clean)

#             if not text:
#                 st.markdown('<div class="status">❌ Could not understand</div>', unsafe_allow_html=True)

#             else:
#                 st.markdown(f'<div class="status">👤 {text}</div>', unsafe_allow_html=True)

#                 # 🤖 Agent Response
#                 response = run_agent(text)

#                 st.markdown('<div class="status">🔊 Speaking...</div>', unsafe_allow_html=True)

#                 speak(response)

#                 # Save chat
#                 save_chat(text, response)

#         # Reset state
#         st.session_state.listening = False


import streamlit as st
import time

from audio.record_audio import record_audio
from audio.preprocess_audio import preprocess_audio
from audio.speech_text import speech_to_text
from audio.text_speech import speak
from agent.agent_executor import run_agent
from database.chat_history import save_chat, get_chat_history
from database.reminder import get_pending_reminders

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="AI Voice Assistant", layout="wide")

# ------------------ SESSION ------------------
if "listening" not in st.session_state:
    st.session_state.listening = False

# ------------------ CSS ------------------
st.markdown("""
<style>

/* Background */
.main {
    background-color: #f1f5f9;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #111827;
    color: white;
}

/* Title */
.title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: #1e293b;
    margin-bottom: 10px;
}

/* Mic image center */
.mic-container {
    text-align: center;
    margin-top: 10px;
    margin-left: 180%;
            
}

/* Button styling */
div.stButton > button {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white;
    border-radius: 12px;
    padding: 10px 25px;
    font-size: 18px;
    border: none;
    margin-top: 15px;
    margin-left: 180%;
}

/* Hover */
div.stButton > button:hover {
    transform: scale(1.05);
}

/* Status */
.status {
    margin-top: 25px;
    font-size: 20px;
    color: #475569;
    text-align: center;
}

/* Chat styles */
.chat-user {
    color: #60a5fa;
    font-weight: bold;
}
.chat-bot {
    color: #34d399;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# ------------------ 🔔 REMINDER MARQUEE ------------------
reminders = get_pending_reminders()

if reminders:
    try:
        reminder_text = " 🔔 ".join([str(r[0]) for r in reminders])
    except:
        reminder_text = " 🔔 ".join([str(r) for r in reminders])

    st.markdown(f"""
    <marquee behavior="scroll" direction="left" style="
        background-color:#111827;
        color:white;
        padding:10px;
        font-size:16px;
        border-radius:8px;
        margin-bottom:10px;">
        🔔 Pending Reminders: {reminder_text}
    </marquee>
    """, unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
st.sidebar.title("🗂 Chat History")

history = get_chat_history()

if history:
    for user, bot in history[::-1][:10]:
        st.sidebar.markdown(f'<div class="chat-user">👤 {user}</div>', unsafe_allow_html=True)
        st.sidebar.markdown(f'<div class="chat-bot">🤖 {bot}</div>', unsafe_allow_html=True)
        st.sidebar.markdown("---")
else:
    st.sidebar.write("No chat history yet")

# ------------------ CENTER UI ------------------
left, center, right = st.columns([1, 2, 1])

with center:

    # 🎤 TITLE
    st.markdown('<div class="title">🎤 AI Voice Assistant</div>', unsafe_allow_html=True)

    # 🎤 MIC IMAGE (JUST BELOW TITLE)
    st.markdown('<div class="mic-container">', unsafe_allow_html=True)
    st.image("https://cdn-icons-gif.flaticon.com/19015/19015816.gif", width=110)
    st.markdown('</div>', unsafe_allow_html=True)

    # 🎤 BUTTON (VISIBLE + STYLED)
    mic_clicked = st.button("🎤 Tap to Speak")

    if mic_clicked:
        st.session_state.listening = True

    # ------------------ STATUS ------------------
    status_placeholder = st.empty()

    # ------------------ LISTENING FLOW ------------------
    if st.session_state.listening:

        status_placeholder.markdown(
            '<div class="status">🎧 Listening...</div>',
            unsafe_allow_html=True
        )

        time.sleep(0.5)

        raw = record_audio()

        if not raw:
            status_placeholder.markdown(
                '<div class="status">❌ Could not hear you</div>',
                unsafe_allow_html=True
            )

        else:
            status_placeholder.markdown(
                '<div class="status">🧠 Processing...</div>',
                unsafe_allow_html=True
            )

            clean = preprocess_audio(raw)
            text = speech_to_text(clean)

            if not text:
                status_placeholder.markdown(
                    '<div class="status">❌ Could not understand</div>',
                    unsafe_allow_html=True
                )

            else:
                status_placeholder.markdown(
                    f'<div class="status">👤 {text}</div>',
                    unsafe_allow_html=True
                )

                response = run_agent(text)

                status_placeholder.markdown(
                    '<div class="status">🔊 Speaking...</div>',
                    unsafe_allow_html=True
                )

                speak(response)
                save_chat(text, response)

        st.session_state.listening = False