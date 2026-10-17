
import streamlit as st

st.set_page_config(
    page_title="Dusshera Vacation",
    page_icon="🔌",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff7e6, #ffe0b2);
}

.main .block-container {
    max-width: 700px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, p {
    text-align: center;
    color: #542b12;
}

.intro {
    font-size: 18px;
    margin-bottom: 25px;
}

.socket-area {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 230px;
    margin: 15px auto;
}

.adapter {
    width: 180px;
    height: 150px;
    background: linear-gradient(145deg, #ffffff, #d9d9d9);
    border: 4px solid #a6a6a6;
    border-radius: 25px;
    box-shadow: 0 10px 20px #00000025;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: relative;
}

.socket {
    display: flex;
    gap: 28px;
    margin-bottom: 12px;
}

.hole {
    width: 13px;
    height: 35px;
    background: #292929;
    border-radius: 8px;
}

.adapter-label {
    color: #666;
    font-size: 12px;
    font-weight: bold;
}

.plug {
    font-size: 55px;
    margin-right: -15px;
    z-index: 2;
    transition: transform 0.5s ease;
}

.inserted .plug {
    transform: translateX(35px);
}

.inserted .adapter {
    box-shadow: 0 0 25px #ffb300;
    border-color: #ff9800;
}

.vacation-message {
    background: linear-gradient(135deg, #ff9800, #ff5722);
    color: white;
    padding: 22px 12px;
    border-radius: 18px;
    font-size: 27px;
    font-weight: bold;
    text-align: center;
    margin: 25px 0;
    box-shadow: 0 8px 20px #00000020;
    animation: appear 0.8s ease;
}

@keyframes appear {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}

.profile {
    display: flex;
    justify-content: center;
    margin-top: 35px;
}

.profile img {
    width: 220px;
    height: 220px;
    border-radius: 50%;
    object-fit: cover;
    border: 6px solid white;
    box-shadow: 0 8px 25px #00000030;
}

.footer {
    text-align: center;
    font-size: 13px;
    color: #80552c;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1>🔌 A Little Holiday Surprise!</h1>",
    unsafe_allow_html=True
)

st.markdown(
    '<p class="intro">Insert the plug into the adapter to reveal your surprise!</p>',
    unsafe_allow_html=True
)

if "plugged_in" not in st.session_state:
    st.session_state.plugged_in = False

if st.session_state.plugged_in:
    st.markdown("""
    <div class="socket-area inserted">
        <div class="plug">🔌</div>
        <div class="adapter">
            <div class="socket">
                <div class="hole"></div>
                <div class="hole"></div>
            </div>
            <div class="adapter-label">POWER ON</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="vacation-message">
        🎉 Enjoy Dusshera Vacation 🎉
    </div>
    """, unsafe_allow_html=True)

    st.balloons()

    if st.button("🔄 Unplug and Reset", use_container_width=True):
        st.session_state.plugged_in = False
        st.rerun()

else:
    st.markdown("""
    <div class="socket-area">
        <div class="plug">🔌</div>
        <div class="adapter">
            <div class="socket">
                <div class="hole"></div>
                <div class="hole"></div>
            </div>
            <div class="adapter-label">ADAPTER</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("⚡ Insert Plug", use_container_width=True):
        st.session_state.plugged_in = True
        st.rerun()

st.markdown("---")

st.markdown(
    '<h2>✨ Have a Wonderful Holiday! ✨</h2>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="profile">
    <img src="https://premswaroop.pythonanywhere.com/static/images/pp.jpg"
         alt="Profile photo">
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="footer">Made with ❤️ using Streamlit</div>',
    unsafe_allow_html=True
)
