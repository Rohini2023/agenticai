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

st.set_page_config(page_title="AI Voice Assistant", layout="wide")

# 🎨 CSS
st.markdown("""
<style>

/* Background */
.main {
    background: radial-gradient(circle at center, #020617, #0f172a);
}

/* Title */
.title {
    text-align:center;
    font-size:42px;
    font-weight:bold;
    background: linear-gradient(90deg,#60a5fa,#22c55e);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

/* Status */
.status {
    text-align:center;
    color:white;
    font-size:18px;
    margin-top:10px;
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

history = get_chat_history()
if history:
    for user, bot in history[::-1][:10]:
        st.sidebar.write(f"👤 {user}")
        st.sidebar.write(f"🤖 {bot}")
        st.sidebar.write("---")
else:
    st.sidebar.write("No chat history")

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

# 🎯 CENTER UI
col1, col2, col3 = st.columns([1,2,1])

with col2:

    st.markdown('<div class="title">🎤 Voice Assistant</div>', unsafe_allow_html=True)

    # 🔥 Placeholders (ORDER FIXED)
    mic_box = st.empty()
    status_box = st.empty()
    user_box = st.empty()
    bot_box = st.empty()

    # 🎙 MIC (REAL SIZE CONTROL ✅)
    click = streamlit_image_coordinates(
        "https://cdn-icons-gif.flaticon.com/19015/19015816.gif",
        width=120   # 🔥 THIS CONTROLS SIZE (not CSS)
    )

    # 👇 STATUS ALWAYS BELOW MIC
    if click:
        status_box.markdown('<div class="status">🎧 Listening...</div>', unsafe_allow_html=True)

        raw = record_audio()

        if raw:
            status_box.markdown('<div class="status">🧠 Processing...</div>', unsafe_allow_html=True)

            clean = preprocess_audio(raw)
            text = speech_to_text(clean)

            if text:
                user_box.markdown(f'<div class="status">👤 {text}</div>', unsafe_allow_html=True)

                status_box.markdown('<div class="status">🤖 Thinking...</div>', unsafe_allow_html=True)

                response = run_agent(text)

                status_box.markdown('<div class="status">🔊 Speaking...</div>', unsafe_allow_html=True)

                speak(response)

                bot_box.markdown(f'<div class="status">🤖 {response}</div>', unsafe_allow_html=True)

                save_chat(text, response)

            else:
                status_box.markdown('<div class="status">❌ Could not understand</div>', unsafe_allow_html=True)

        else:
            status_box.markdown('<div class="status">❌ No audio detected</div>', unsafe_allow_html=True)