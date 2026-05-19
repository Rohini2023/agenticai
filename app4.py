# import streamlit as st
# import time

# from audio.record_audio import record_audio
# from audio.preprocess_audio import preprocess_audio
# from audio.speech_text import speech_to_text
# from audio.text_speech import speak
# from agent.agent_executor import run_agent
# from database.chat_history import save_chat, get_chat_history
# from database.reminder import get_pending_reminders

# # ------------------ PAGE CONFIG ------------------
# st.set_page_config(page_title="AI Voice Assistant", layout="wide")

# # ------------------ SESSION ------------------
# if "listening" not in st.session_state:
#     st.session_state.listening = False

# # ------------------ CSS ------------------
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

# /* Title */
# .title {
#     # text-align: center;
#     font-size: 36px;
#     font-weight: bold;
#     color: #1e293b;
#     margin-bottom: 10px;
# }

# /* Button styling */
# div.stButton > button {
#     background: linear-gradient(135deg, #2563eb, #1d4ed8);
#     color: white;
#     border-radius: 12px;
#     padding: 10px 25px;
#     font-size: 18px;
#     border: none;
#     margin-top: 15px;
#     # margin-left: 180%;

# /* Hover */
# div.stButton > button:hover {
#     transform: scale(1.05);
# }

# /* Status */
# .status {
#     margin-top: 25px;
#     font-size: 20px;
#     color: #475569;
#     text-align: center;
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

# </style>
# """, unsafe_allow_html=True)

# # ------------------ 🔔 REMINDER MARQUEE ------------------
# reminders = get_pending_reminders()

# if reminders:
#     try:
#         reminder_text = " 🔔 ".join([str(r[0]) for r in reminders])
#     except:
#         reminder_text = " 🔔 ".join([str(r) for r in reminders])

#     st.markdown(f"""
#     <marquee behavior="scroll" direction="left" style="
#         background-color:#111827;
#         color:white;
#         padding:10px;
#         font-size:16px;
#         border-radius:8px;
#         margin-bottom:10px;">
#         🔔 Pending Reminders: {reminder_text}
#     </marquee>
#     """, unsafe_allow_html=True)

# # ------------------ SIDEBAR ------------------
# st.sidebar.title("🗂 Chat History")

# history = get_chat_history()

# if history:
#     for user, bot in history[::-1][:10]:
#         st.sidebar.markdown(f'<div class="chat-user">👤 {user}</div>', unsafe_allow_html=True)
#         st.sidebar.markdown(f'<div class="chat-bot">🤖 {bot}</div>', unsafe_allow_html=True)
#         st.sidebar.markdown("---")
# else:
#     st.sidebar.write("No chat history yet")

# # ------------------ CENTER UI ------------------
# left, center, right = st.columns([1, 2, 1])

# with center:

#     st.markdown('<div class="title"> Elderly Voice Assistant</div>', unsafe_allow_html=True)

#     # ✅ FORCE PERFECT CENTER
#     st.markdown("""
#         <div style="display:flex; flex-direction:column; align-items:center;">
#     """, unsafe_allow_html=True)

#     # 🎤 MIC IMAGE (NOW PERFECT CENTER)
#     st.markdown("""
#         <img src="https://cdn-icons-gif.flaticon.com/19015/19015816.gif" width="110">
#     """, unsafe_allow_html=True)

#     # 🎤 BUTTON (ALSO CENTERED)
#     mic_clicked = st.button("🎤 Tap to Speak")

#     st.markdown("</div>", unsafe_allow_html=True)

#     if mic_clicked:
#         st.session_state.listening = True

#     # ------------------ STATUS ------------------
#     status_placeholder = st.empty()

#     # ------------------ LISTENING FLOW ------------------
#     if st.session_state.listening:

#         status_placeholder.markdown(
#             '<div class="status">🎧 Listening...</div>',
#             unsafe_allow_html=True
#         )

#         time.sleep(0.5)

#         raw = record_audio()

#         if not raw:
#             status_placeholder.markdown(
#                 '<div class="status">❌ Could not hear you</div>',
#                 unsafe_allow_html=True
#             )

#         else:
#             status_placeholder.markdown(
#                 '<div class="status">🧠 Processing...</div>',
#                 unsafe_allow_html=True
#             )

#             clean = preprocess_audio(raw)
#             text = speech_to_text(clean)

#             if not text:
#                 status_placeholder.markdown(
#                     '<div class="status">❌ Could not understand</div>',
#                     unsafe_allow_html=True
#                 )

#             else:
#                 status_placeholder.markdown(
#                     f'<div class="status">👤 {text}</div>',
#                     unsafe_allow_html=True
#                 )

#                 # 🤖 Agent
#                 response = run_agent(text)

#                 status_placeholder.markdown(
#                     '<div class="status">🔊 Speaking...</div>',
#                     unsafe_allow_html=True
#                 )

#                 speak(response)

#                 # Save chat
#                 save_chat(text, response)

#         # Reset state
#         st.session_state.listening = False


import streamlit as st
import time
from datetime import datetime

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
.main { background-color: #f1f5f9; }

[data-testid="stSidebar"] {
    background-color: #111827;
    color: white;
}

.title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: #1e293b;
}

div.stButton > button {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white;
    border-radius: 12px;
    padding: 10px 25px;
    font-size: 18px;
    border: none;
    margin-top: 15px;
}

.status {
    margin-top: 25px;
    font-size: 20px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ------------------ 🔔 FILTERED REMINDERS ------------------
def get_valid_reminders():
    now = datetime.now()
    valid = []

    for r in get_pending_reminders():
        try:
            text = r[0]
            remind_time = r[1]

            # Only future reminders
            if remind_time > now:
                valid.append(r)
        except:
            continue

    return valid

# ------------------ 🔔 AUTO TRIGGER ------------------
def check_reminders():
    now = datetime.now()

    for r in get_pending_reminders():
        try:
            text, remind_time = r

            # Trigger within 30 sec window
            if abs((remind_time - now).total_seconds()) < 30:
                try:
                    speak(f"Reminder: {text}")
                except Exception as e:
                    st.error(f"TTS Error: {e}")

                st.warning(f"🔔 Reminder: {text}")
                return
        except:
            continue

check_reminders()

# ------------------ 🔔 MARQUEE ------------------
reminders = get_valid_reminders()

if reminders:
    reminder_text = " 🔔 ".join([str(r[0]) for r in reminders])

    st.markdown(f"""
    <marquee style="background:#111827;color:white;padding:10px;">
    🔔 Pending Reminders: {reminder_text}
    </marquee>
    """, unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
st.sidebar.title("🗂 Chat History")

history = get_chat_history()
for user, bot in history[::-1][:10]:
    st.sidebar.markdown(f"👤 {user}")
    st.sidebar.markdown(f"🤖 {bot}")
    st.sidebar.markdown("---")

# ------------------ CENTER UI ------------------
left, center, right = st.columns([1,2,1])

with center:

    st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)

    st.markdown('<div class="title">🎤 Elderly Voice Assistant</div>', unsafe_allow_html=True)

    st.markdown("""
    <img src="https://cdn-icons-gif.flaticon.com/19015/19015816.gif" width="110">
    """, unsafe_allow_html=True)

    mic_clicked = st.button("🎤 Tap to Speak")

    st.markdown('</div>', unsafe_allow_html=True)

    if mic_clicked:
        st.session_state.listening = True

    status = st.empty()

    # ------------------ LISTENING ------------------
    if st.session_state.listening:

        status.markdown('<div class="status">🎧 Listening...</div>', unsafe_allow_html=True)
        time.sleep(0.5)

        raw = record_audio()

        if not raw:
            status.markdown('<div class="status">❌ Could not hear you</div>', unsafe_allow_html=True)

        else:
            status.markdown('<div class="status">🧠 Processing...</div>', unsafe_allow_html=True)

            clean = preprocess_audio(raw)
            text = speech_to_text(clean)

            if not text:
                status.markdown('<div class="status">❌ Could not understand</div>', unsafe_allow_html=True)

            else:
                status.markdown(f'<div class="status">👤 {text}</div>', unsafe_allow_html=True)

                response = run_agent(text)

                status.markdown('<div class="status">🔊 Speaking...</div>', unsafe_allow_html=True)

                # ✅ SAFE SPEAK
                try:

                    result = run_agent(text)

                    response = result["response"]

                    
                    speak(response)
                except Exception as e:
                    st.error(f"Voice Error: {e}")

                save_chat(text, response)

        st.session_state.listening = False