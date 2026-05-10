import streamlit as st
from rag_pipeline import TravelAdvisorRAG

st.set_page_config(
    page_title="Travel Advisor Chatbot",
    layout="centered"
)


st.markdown("""
<style>
body {
    background-color: #0e1117;
}

.main {
    max-width: 760px;
    margin: auto;
}

.chat-container {
    display: flex;
    flex-direction: column;
    gap: 14px;
    margin-bottom: 120px;
}

/* USER MESSAGE (LEFT - PINK) */
.user-bubble {
    align-self: flex-start;
    background: linear-gradient(135deg, #ff5fa2, #ff7eb3);
    color: black;
    padding: 14px 18px;
    border-radius: 18px;
    max-width: 75%;
    font-weight: 500;
}

/* ASSISTANT MESSAGE (RIGHT - DARK) */
.assistant-bubble {
    align-self: flex-end;
    background: #1c1f2b;
    color: white;
    padding: 14px 18px;
    border-radius: 18px;
    max-width: 75%;
}

/* SOURCES */
.sources {
    font-size: 0.85rem;
    opacity: 0.8;
    margin-top: 8px;
}

/* INPUT BAR */
.input-bar {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 720px;
    background: #0e1117;
    padding: 12px;
    border-top: 1px solid #222;
}

/* REMOVE STREAMLIT FOOTER */
footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

st.markdown("##  Travel Advisor Chatbot")


if "messages" not in st.session_state:
    st.session_state.messages = []


@st.cache_resource
def load_rag():
    return TravelAdvisorRAG()

rag = load_rag()


st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f'<div class="user-bubble">{msg["content"]}</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="assistant-bubble">{msg["content"]}',
            unsafe_allow_html=True
        )

        if msg.get("sources"):
            st.markdown("<div class='sources'><b>Sources:</b><ul>", unsafe_allow_html=True)
            for s in msg["sources"]:
                st.markdown(f"<li>{s}</li>", unsafe_allow_html=True)
            st.markdown("</ul></div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


with st.form("chat_form", clear_on_submit=True):
    st.markdown('<div class="input-bar">', unsafe_allow_html=True)

    user_input = st.text_input(
        "",
        placeholder="Ask a travel question...",
        label_visibility="collapsed"
    )
    send = st.form_submit_button("Send")

    st.markdown("</div>", unsafe_allow_html=True)


if send and user_input.strip():
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    with st.spinner("Thinking..."):
        result = rag.answer(user_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": result["answer"],
        "sources": result["sources"]
    })

    st.rerun()
