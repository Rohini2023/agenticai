# import streamlit as st
# from audio.record_audio import record_audio
# from audio.preprocess_audio import preprocess_audio
# from audio.speech_text import speech_to_text
# from audio.text_speech import speak
# from agent.agent_executor import run_agent
# from database.chat_history import save_chat
# st.set_page_config(page_title="Voice Assistant", layout="centered")

# # 🎨 CLEAN CSS
# st.markdown("""
# <style>
# body {
#     background-color: #f8fafc;
#     color: #111827;
# }

# /* Center layout */
# .container {
#     display: flex;
#     flex-direction: column;
#     align-items: center;
#     justify-content: center;
#     margin-top: 120px;
# }

# /* Mic button */
# .mic button {
#     background-color: #2563eb;
#     color: white;
#     border-radius: 50%;
#     height: 100px;
#     width: 100px;
#     font-size: 30px;
#     border: none;
# }

# /* Status text */
# .status {
#     margin-top: 25px;
#     font-size: 18px;
#     color: #374151;
#     text-align: center;
# }
# </style>
# """, unsafe_allow_html=True)

# # 🎯 Layout
# st.markdown('<div class="container">', unsafe_allow_html=True)

# st.markdown("<h2>🎤 Voice Assistant</h2>", unsafe_allow_html=True)

# # 🎤 Mic button
# if st.button("🎤 Tap to Speak"):

#     # Listening
#     st.markdown('<div class="status">Listening...</div>', unsafe_allow_html=True)

#     raw = record_audio()

#     if not raw:
#         st.markdown('<div class="status">Could not hear you</div>', unsafe_allow_html=True)
#     else:
#         # Processing
#         st.markdown('<div class="status">Processing...</div>', unsafe_allow_html=True)

#         clean = preprocess_audio(raw)
#         text = speech_to_text(clean)

#         if not text:
#             st.markdown('<div class="status">Could not understand</div>', unsafe_allow_html=True)
#         else:
#             st.markdown(f'<div class="status">You said: {text}</div>', unsafe_allow_html=True)

#             # Agent
#             response = run_agent(text)

#             # Speaking
#             st.markdown('<div class="status">Speaking...</div>', unsafe_allow_html=True)

#             speak(response)
#             save_chat(text, response) 
# st.markdown('</div>', unsafe_allow_html=True)


# import streamlit as st
# from audio.record_audio import record_audio
# from audio.preprocess_audio import preprocess_audio
# from audio.speech_text import speech_to_text
# from audio.text_speech import speak
# from agent.agent_executor import run_agent
# from database.chat_history import save_chat, get_chat_history

# st.set_page_config(page_title="AI Voice Assistant", layout="wide")

# # 🎨 PROFESSIONAL CSS
# st.markdown("""
# <style>

# /* App background */
# .main {
#     background-color: #f1f5f9;
# }

# /* Sidebar */
# [data-testid="stSidebar"] {
#     background-color: #111827;
#     color: white;
# }

# /* Chat history text */
# .chat-user {
#     color: #60a5fa;
#     font-weight: bold;
# }
# .chat-bot {
#     color: #34d399;
#     margin-bottom: 10px;
# }

# /* Center container */
# .center-box {
#     display: flex;
#     flex-direction: column;
#     align-items: center;
#     justify-content: center;
#     margin-top: 120px;
# }

# /* Mic button */
# div.stButton > button {
#     background: linear-gradient(135deg, #2563eb, #1d4ed8);
#     color: white;
#     border-radius: 50%;
#     height: 120px;
#     width: 120px;
#     font-size: 32px;
#     border: none;
#     box-shadow: 0 4px 20px rgba(0,0,0,0.2);
# }

# /* Status text */
# .status {
#     margin-top: 25px;
#     font-size: 20px;
#     color: #374151;
#     text-align: center;
# }

# .title {
#     text-align: center;
#     font-size: 32px;
#     font-weight: bold;
#     color: #1e293b;
# }

# </style>
# """, unsafe_allow_html=True)

# # 🧭 SIDEBAR → CHAT HISTORY
# st.sidebar.title("🗂 Chat History")

# history = get_chat_history()

# if history:
#     for user, bot in history[::-1][:10]:
#         st.sidebar.markdown(f'<div class="chat-user">👤 {user}</div>', unsafe_allow_html=True)
#         st.sidebar.markdown(f'<div class="chat-bot">🤖 {bot}</div>', unsafe_allow_html=True)
#         st.sidebar.markdown("---")
# else:
#     st.sidebar.write("No chat history yet")

# # 🎯 MAIN CENTER UI
# st.markdown('<div class="center-box">', unsafe_allow_html=True)

# st.markdown('<div class="title">🎤 AI Voice Assistant</div>', unsafe_allow_html=True)

# # 🎤 MIC BUTTON
# if st.button("🎤"):

#     # Listening
#     st.markdown('<div class="status">🎧 Listening...</div>', unsafe_allow_html=True)

#     raw = record_audio()

#     if not raw:
#         st.markdown('<div class="status">❌ Could not hear you</div>', unsafe_allow_html=True)
#     else:
#         # Processing
#         st.markdown('<div class="status">🧠 Processing...</div>', unsafe_allow_html=True)

#         clean = preprocess_audio(raw)
#         text = speech_to_text(clean)

#         if not text:
#             st.markdown('<div class="status">❌ Could not understand</div>', unsafe_allow_html=True)
#         else:
#             st.markdown(f'<div class="status">👤 {text}</div>', unsafe_allow_html=True)

#             # 🤖 Agent response
#             response = run_agent(text)

#             # Speaking
#             st.markdown('<div class="status">🔊 Speaking...</div>', unsafe_allow_html=True)

#             speak(response)

#             # 💾 Save chat
#             save_chat(text, response)

# st.markdown('</div>', unsafe_allow_html=True)




import streamlit as st
from audio.record_audio import record_audio
from audio.preprocess_audio import preprocess_audio
from audio.speech_text import speech_to_text
from audio.text_speech import speak
from agent.agent_executor import run_agent
from database.chat_history import save_chat, get_chat_history

st.set_page_config(page_title="AI Voice Assistant", layout="wide")

# 🎨 PROFESSIONAL CSS
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

/* Chat styles */
.chat-user {
    color: #60a5fa;
    font-weight: bold;
}
.chat-bot {
    color: #34d399;
    margin-bottom: 10px;
}

/* Title */
.title {
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    color: #1e293b;
    margin-bottom: 20px;
}

/* Mic button */
div.stButton > button {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white;
    border-radius: 50%;
    height: 130px;
    width: 130px;
    font-size: 36px;
    border: none;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    transition: all 0.2s ease;
}

/* Hover */
div.stButton > button:hover {
    transform: scale(1.08);
}

/* Status */
.status {
    margin-top: 30px;
    font-size: 20px;
    color: #475569;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# 🧭 SIDEBAR → CHAT HISTORY
st.sidebar.title("🗂 Chat History")

history = get_chat_history()

if history:
    for user, bot in history[::-1][:10]:
        st.sidebar.markdown(f'<div class="chat-user">👤 {user}</div>', unsafe_allow_html=True)
        st.sidebar.markdown(f'<div class="chat-bot">🤖 {bot}</div>', unsafe_allow_html=True)
        st.sidebar.markdown("---")
else:
    st.sidebar.write("No chat history yet")

# 🎯 CENTER LAYOUT USING COLUMNS (BEST METHOD)
left, center, right = st.columns([1, 2, 1])

with center:

    st.markdown('<div class="title">🎤 AI Voice Assistant</div>', unsafe_allow_html=True)

    # Add vertical spacing
    st.write("")
    st.write("")

    # 🎤 MIC BUTTON (CENTERED)
    if st.button("🎤"):

        st.markdown('<div class="status">🎧 Listening...</div>', unsafe_allow_html=True)

        raw = record_audio()

        if not raw:
            st.markdown('<div class="status">❌ Could not hear you</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status">🧠 Processing...</div>', unsafe_allow_html=True)

            clean = preprocess_audio(raw)
            text = speech_to_text(clean)

            if not text:
                st.markdown('<div class="status">❌ Could not understand</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="status">👤 {text}</div>', unsafe_allow_html=True)

                response = run_agent(text)

                st.markdown('<div class="status">🔊 Speaking...</div>', unsafe_allow_html=True)

                speak(response)

                save_chat(text, response)