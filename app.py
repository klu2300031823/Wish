
import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

st.set_page_config(
    page_title="Enjoy Holidays",
    page_icon="🔌",
    layout="centered"
)

# Load your original photo from the repository
image_path = Path(__file__).parent / "profile.png"

if not image_path.exists():
    st.error("Please add your original photo as profile.png beside app.py.")
    st.stop()

image_data = base64.b64encode(image_path.read_bytes()).decode("utf-8")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff4df, #ffe0b2);
}
.block-container {
    max-width: 500px;
    padding-top: 1rem;
}
h1 {
    text-align: center;
    color: #8b3500;
}
</style>
""", unsafe_allow_html=True)

st.title("🔌 A Holiday Surprise!")
st.caption("Drag the plug upward and connect it to the adapter.")

html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: transparent;
}

.scene {
    position: relative;
    width: 100%;
    max-width: 360px;
    margin: auto;
    overflow: hidden;
    border-radius: 12px;
    background: #111;
    user-select: none;
    touch-action: pan-y;
}

.photo {
    display: block;
    width: 100%;
    height: auto;
    pointer-events: none;
}

/* Adapter at the bottom of the shirt */
.adapter {
    position: absolute;
    top: 56%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 58px;
    height: 48px;
    border: 3px solid #ff9800;
    border-radius: 12px;
    background: #f6f6f6;
    box-shadow: 0 0 18px #ff9800;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 13px;
    z-index: 3;
    transition: box-shadow .3s;
}

.hole {
    width: 6px;
    height: 19px;
    background: #252525;
    border-radius: 5px;
}

/* Plug starts lower down, on the trousers */
.plug {
    position: absolute;
    top: 66%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 65px;
    cursor: grab;
    touch-action: none;
    user-select: none;
    z-index: 5;
    line-height: 1;
    filter: drop-shadow(0 3px 3px #0007);
}

.plug:active {
    cursor: grabbing;
}

.arrow {
    position: absolute;
    top: 61%;
    left: 50%;
    transform: translateX(-50%);
    color: white;
    font-size: 27px;
    font-weight: bold;
    pointer-events: none;
    z-index: 2;
    text-shadow: 0 0 5px #000;
}

.message {
    display: none;
    position: absolute;
    top: 72%;
    left: 4%;
    width: 92%;
    padding: 14px 5px;
    text-align: center;
    color: white;
    background: linear-gradient(135deg, #ffb300, #ff3d00);
    border: 3px solid #ffe66d;
    border-radius: 17px;
    box-shadow: 0 0 22px #ff9800;
    font-size: clamp(17px, 5vw, 24px);
    font-weight: bold;
    text-shadow: 2px 2px 3px #9e1900;
    z-index: 6;
}

.message.show {
    display: block;
    animation: appear .6s ease;
}

@keyframes appear {
    from {
        opacity: 0;
        transform: scale(.7);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

.scene.connected .adapter {
    box-shadow: 0 0 35px #ffb300;
}

.hint {
    max-width: 360px;
    margin: 10px auto;
    padding: 10px;
    border-radius: 8px;
    text-align: center;
    background: #fff8ed;
    color: #773500;
    font-size: 14px;
}

.reset {
    display: none;
    margin: 10px auto;
    padding: 10px 20px;
    border: 0;
    border-radius: 9px;
    background: #d9570b;
    color: white;
    font-weight: bold;
    cursor: pointer;
}
</style>
</head>

<body>
<div class="scene" id="scene">

    <img class="photo"
         src="data:image/png;base64,IMAGE_BASE64"
         alt="My full-body photo">

    <div class="adapter" id="adapter">
        <span class="hole"></span>
        <span class="hole"></span>
    </div>

    <div class="arrow" id="arrow">⬆</div>

    <div class="plug" id="plug" role="button"
         aria-label="Drag plug into adapter">🔌</div>

    <div class="message" id="message">
        🎉 Enjoy Your Holidays 🎉
    </div>
</div>

<div class="hint" id="hint">
    👆 Drag the plug upward into the adapter
</div>

<button class="reset" id="reset">Try Again 🔄</button>

<script>
const scene = document.getElementById("scene");
const plug = document.getElementById("plug");
const adapter = document.getElementById("adapter");
const message = document.getElementById("message");
const arrow = document.getElementById("arrow");
const hint = document.getElementById("hint");
const reset = document.getElementById("reset");

let dragging = false;
let connected = false;
let startX = 0;
let startY = 0;
let initialX = 0;
let initialY = 0;

function resetPlug() {
    plug.style.left = "50%";
    plug.style.top = "66%";
    plug.style.transform = "translate(-50%, -50%)";
}

plug.addEventListener("pointerdown", function(e) {
    if (connected) return;

    dragging = true;

    const plugRect = plug.getBoundingClientRect();

    startX = e.clientX;
    startY = e.clientY;
    initialX = plugRect.left + plugRect.width / 2;
    initialY = plugRect.top + plugRect.height / 2;

    plug.setPointerCapture(e.pointerId);
    e.preventDefault();
});

plug.addEventListener("pointermove", function(e) {
    if (!dragging || connected) return;

    const sceneRect = scene.getBoundingClientRect();

    const x = initialX + e.clientX - startX;
    const y = initialY + e.clientY - startY;

    plug.style.left = (x - sceneRect.left) + "px";
    plug.style.top = (y - sceneRect.top) + "px";
    plug.style.transform = "translate(-50%, -50%)";

    const p = plug.getBoundingClientRect();
    const a = adapter.getBoundingClientRect();

    const dx = (p.left + p.width / 2) -
               (a.left + a.width / 2);
    const dy = (p.top + p.height / 2) -
               (a.top + a.height / 2);

    if (Math.abs(dx) < 35 && Math.abs(dy) < 35) {
        connectPlug();
    }
});

plug.addEventListener("pointerup", function() {
    dragging = false;
    if (!connected) resetPlug();
});

plug.addEventListener("pointercancel", function() {
    dragging = false;
    if (!connected) resetPlug();
});

function connectPlug() {
    if (connected) return;

    connected = true;
    dragging = false;

    const a = adapter.getBoundingClientRect();
    const s = scene.getBoundingClientRect();

    plug.style.left = (a.left + a.width / 2 - s.left) + "px";
    plug.style.top = (a.top + a.height / 2 - s.top) + "px";
    plug.style.fontSize = "34px";
    plug.style.transform = "translate(-50%, -50%)";

    scene.classList.add("connected");
    message.classList.add("show");
    arrow.style.display = "none";
    hint.textContent = "⚡ Connected! Happy holidays!";
    reset.style.display = "block";
}

reset.addEventListener("click", function() {
    connected = false;
    message.classList.remove("show");
    scene.classList.remove("connected");

    plug.style.fontSize = "43px";
    arrow.style.display = "block";
    hint.textContent = "👆 Drag the plug upward into the adapter";
    reset.style.display = "none";

    resetPlug();
});
</script>
</body>
</html>
"""

html_code = html_code.replace("IMAGE_BASE64", image_data)

components.html(html_code, height=1850, scrolling=True)
