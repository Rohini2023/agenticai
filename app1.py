# import streamlit as st
# from streamlit_image_coordinates import streamlit_image_coordinates
# from audio.record_audio import record_audio
# from audio.preprocess_audio import preprocess_audio
# from audio.speech_text import speech_to_text
# from audio.text_speech import speak
# from agent.agent_executor import run_agent
# from database.chat_history import save_chat, get_chat_history
# from database.reminder import get_pending_reminders
# from datetime import datetime
# import time

# st.set_page_config(page_title="AI Voice Assistant", layout="wide")

# # 🎨 CSS
# st.markdown("""
# <style>
# .main {background: linear-gradient(to right, #0f172a, #1e293b);}
# .title {
#     text-align:center;
#     font-size:48px;
#     font-weight:bold;
#     background: linear-gradient(90deg,#3b82f6,#22c55e);
#     -webkit-background-clip:text;
#     -webkit-text-fill-color:transparent;
# }
# .marquee {color:#facc15; font-weight:bold;}
# .status {text-align:center; color:white; font-size:20px;}
# </style>
# """, unsafe_allow_html=True)

# # 📜 CHAT HISTORY
# st.sidebar.title("Chat History")
# for user, bot in get_chat_history()[::-1][:10]:
#     st.sidebar.write(f"👤 {user}")
#     st.sidebar.write(f"🤖 {bot}")
#     st.sidebar.write("---")

# # ⏰ REMINDERS
# reminders = get_pending_reminders()
# valid = []
# for r in reminders:
#     _, task, t = r
#     try:
#         dt = datetime.fromisoformat(str(t))
#         if dt > datetime.now():
#             valid.append(f"{task} at {dt.strftime('%I:%M %p')}")
#     except:
#         pass

# if valid:
#     st.markdown(f'<div class="marquee"><marquee>{" | ".join(valid)}</marquee></div>', unsafe_allow_html=True)

# # 🎯 CENTER
# col1, col2, col3 = st.columns([1,2,1])

# with col2:
#     st.markdown('<div class="title">🎤 AI Voice Assistant</div>', unsafe_allow_html=True)

#     # 🔥 PLACEHOLDERS (IMPORTANT)
#     status_box = st.empty()
#     user_box = st.empty()
#     bot_box = st.empty()

#     # 🎙 CLICKABLE MIC
#     click = streamlit_image_coordinates(
#         "https://cdn-icons-gif.flaticon.com/19015/19015816.gif"
#     )

#     if click:

#         # 🎧 Listening
#         status_box.markdown('<div class="status">🎧 Listening...</div>', unsafe_allow_html=True)
#         time.sleep(0.5)

#         raw = record_audio()

#         if raw:

#             # 🧠 Processing
#             status_box.markdown('<div class="status">🧠 Processing...</div>', unsafe_allow_html=True)

#             clean = preprocess_audio(raw)
#             text = speech_to_text(clean)

#             if text:

#                 # 👤 Show user text
#                 user_box.markdown(f'<div class="status">👤 {text}</div>', unsafe_allow_html=True)

#                 # 🤖 Generate response
#                 response = run_agent(text)

#                 # 🔊 Speaking
#                 status_box.markdown('<div class="status">🔊 Speaking...</div>', unsafe_allow_html=True)

#                 speak(response)

#                 # 🤖 Show bot response
#                 bot_box.markdown(f'<div class="status">🤖 {response}</div>', unsafe_allow_html=True)

#                 save_chat(text, response)

#             else:
#                 status_box.markdown('<div class="status">❌ Could not understand</div>', unsafe_allow_html=True)
#         else:
#             status_box.markdown('<div class="status">❌ No audio</div>', unsafe_allow_html=True)


import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
from audio.record_audio import record_audio
from audio.preprocess_audio import preprocess_audio
from audio.speech_text import speech_to_text
from audio.text_speech import speak
from agent.agent_executor import run_agent
from database.chat_history import save_chat, get_chat_history
from database.reminder import get_pending_reminders
from datetime import datetime
import time

st.set_page_config(page_title="AI Voice Assistant", layout="wide")

# 🎨 SIRI STYLE CSS
st.markdown("""
<style>

/* Background */
.main {
    background: radial-gradient(circle at center, #020617, #0f172a);
}

/* Title */
.title {
    text-align:center;
    font-size:50px;
    font-weight:bold;
    background: linear-gradient(90deg,#60a5fa,#22c55e);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

/* Wave animation */
.wave {
    display:flex;
    justify-content:center;
    gap:5px;
    margin-top:20px;
}

.wave span {
    width:6px;
    height:20px;
    background:#3b82f6;
    animation:wave 1s infinite ease-in-out;
}

.wave span:nth-child(2){animation-delay:0.1s;}
.wave span:nth-child(3){animation-delay:0.2s;}
.wave span:nth-child(4){animation-delay:0.3s;}
.wave span:nth-child(5){animation-delay:0.4s;}

@keyframes wave {
    0%,100% {height:20px;}
    50% {height:50px;}
}

/* Mic pulse */
.mic {
    display:flex;
    justify-content:center;
    margin-top:30px;
}

.mic img {
    width:30px;
    border-radius:50%;
    animation:pulse 2s infinite;
    cursor:pointer;
}

@keyframes pulse {
    0% {box-shadow:0 0 0 0 rgba(59,130,246,0.7);}
    70% {box-shadow:0 0 0 25px rgba(59,130,246,0);}
    100% {box-shadow:0 0 0 0 rgba(59,130,246,0);}
}

/* Status */
.status {
    text-align:center;
    color:white;
    font-size:22px;
    margin-top:20px;
}

/* Marquee */
.marquee {
    color:#facc15;
    font-weight:bold;
    text-align:center;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# 📜 CHAT HISTORY
st.sidebar.title("🗂 Chat History")
for user, bot in get_chat_history()[::-1][:10]:
    st.sidebar.write(f"👤 {user}")
    st.sidebar.write(f"🤖 {bot}")
    st.sidebar.write("---")

# ⏰ REMINDER MARQUEE
reminders = get_pending_reminders()
valid = []
for r in reminders:
    _, task, t = r
    try:
        dt = datetime.fromisoformat(str(t))
        if dt > datetime.now():
            valid.append(f"{task} at {dt.strftime('%I:%M %p')}")
    except:
        pass

if valid:
    st.markdown(f'<div class="marquee"><marquee>{" | ".join(valid)}</marquee></div>', unsafe_allow_html=True)

# 🎯 CENTER
col1, col2, col3 = st.columns([1,2,1])

with col2:

    st.markdown('<div class="title">Elderly Voice Assistant</div>', unsafe_allow_html=True)

    status_box = st.empty()
    wave_box = st.empty()
    user_box = st.empty()
    bot_box = st.empty()

    # 🎙 MIC CLICK
    click = streamlit_image_coordinates(
        "https://cdn-icons-gif.flaticon.com/19015/19015816.gif"
    )

    if click:

        # 🎧 Listening
        status_box.markdown('<div class="status">🎧 Listening...</div>', unsafe_allow_html=True)

        # 🎵 Wave animation
        wave_box.markdown("""
        <div class="wave">
            <span></span><span></span><span></span><span></span><span></span>
        </div>
        """, unsafe_allow_html=True)

        raw = record_audio()

        if raw:

            # 🧠 Processing
            status_box.markdown('<div class="status">🧠 Understanding...</div>', unsafe_allow_html=True)
            wave_box.empty()

            clean = preprocess_audio(raw)
            text = speech_to_text(clean)

            if text:

                user_box.markdown(f'<div class="status">👤 {text}</div>', unsafe_allow_html=True)

                # 🤖 Thinking
                status_box.markdown('<div class="status">🤖 Thinking...</div>', unsafe_allow_html=True)

                response = run_agent(text)

                # 🔊 Speaking
                status_box.markdown('<div class="status">🔊 Speaking...</div>', unsafe_allow_html=True)

                speak(response)

                bot_box.markdown(f'<div class="status">🤖 {response}</div>', unsafe_allow_html=True)

                save_chat(text, response)

            else:
                status_box.markdown('<div class="status">❌ Could not understand</div>', unsafe_allow_html=True)

        else:
            status_box.markdown('<div class="status">❌ No audio detected</div>', unsafe_allow_html=True)