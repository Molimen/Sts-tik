import streamlit as st
import time
import random
import base64
from streamlit_extras.stylable_container import stylable_container
import extra
import time
import math
import about_us
# TO-DO
# add a few round!
# BEFORE RELEASE, PLEASE FIX THE LANG!

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def games_reset():
    if st.session_state.round == ROUND and st.session_state.round != 0:
        st.session_state.score += st.session_state.correct / ROUND

    st.session_state.menu_select = 0
    st.session_state.diff = ""
    st.session_state.round = 1
    st.session_state.time = 0
    st.session_state.answer = []
    st.session_state.correct = 0

ROUND = 3

def games():
    TIME_LIMIT = 10 if st.session_state.diff == "Easy bos" else 8 if st.session_state.diff == "okayy" else 7 if st.session_state.diff == "hard" else 15 if st.session_state.diff == "DESPAIR" else 0.11037

    st.markdown(f"<h4>Round: {'{:02d}'.format(st.session_state.round)}/{ROUND}</h4>", unsafe_allow_html=True)

    timer_placeholder = st.empty()
    progress_placeholder = st.empty()

    st.audio(f"https://dict.youdao.com/dictvoice?audio={st.session_state.word}&type=2")
    st.write(st.session_state.word)

    user_input = st.text_input("Type the word here:")

    while 1:
        elapsed = -(st.session_state.time - math.floor(time.time()))

        if user_input:
            st.session_state.answer.append([user_input,1 if user_input.strip().lower() == st.session_state.word.lower() else 3, st.session_state.word])
            if user_input.strip().lower() == st.session_state.word.lower():
                st.session_state.correct += 1 if st.session_state.diff == "Easy bos" else 2 if st.session_state.diff == "okayy" else 4 if st.session_state.diff == "hard" else 8 if st.session_state.diff == "DESPAIR" else 0
            break

        if elapsed > TIME_LIMIT:
            st.session_state.answer.append([user_input,2, st.session_state.word])
            break

        timer_placeholder.markdown(f"⏳ *Time: {elapsed} seconds*")
        progress_placeholder.progress(elapsed / TIME_LIMIT)
        time.sleep(.5)

    st.session_state.menu_select = 4
    st.rerun()

params = st.query_params
placeholder = st.empty()

if "menu_select" not in st.session_state:
    st.session_state.menu_select = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "diff" not in st.session_state:
    st.session_state.diff = ""
if "round" not in st.session_state:
    st.session_state.round = 1
if "time" not in st.session_state:
    st.session_state.time = 0
if "answer" not in st.session_state:
    st.session_state.answer = []
if "word" not in st.session_state:
    st.session_state.word = ""
if "correct" not in st.session_state:
    st.session_state.correct = 0

st.set_page_config(page_title="Spelling Bee", page_icon="assets/icon.png")

spelling_bee_words = {
    # 🍎 EASY — kata dasar, sehari-hari (±90 kata)
    "easy": [
        "apple", "banana", "orange", "grape", "table", "chair", "window", "garden", "river", "school",
        "music", "happy", "friend", "family", "ocean", "mountain", "forest", "animal", "summer", "winter",
        "teacher", "computer", "flower", "planet", "light", "shadow", "rain", "cloud", "dream", "story",
        "book", "pencil", "dog", "cat", "bird", "cake", "bread", "milk", "smile", "water",
        "door", "city", "tree", "baby", "movie", "dance", "house", "shirt", "fruit", "game",
        "train", "bus", "car", "road", "park", "street", "sun", "moon", "star", "sky",
        "grass", "sand", "beach", "lake", "toy", "bag", "pen", "clock", "bed", "mirror",
        "cup", "plate", "shoe", "hat", "phone", "fish", "map", "ship", "salt", "sugar",
        "juice", "music", "bread", "watch", "lamp", "ring", "key", "box", "door", "photo"
    ],

    # 🌟 MEDIUM — kata umum tapi lebih kompleks & panjang (±75 kata)
    "medium": [
        "bicycle", "elephant", "library", "umbrella", "chocolate", "whisper", "journey", "mystery",
        "adventure", "fantasy", "puzzle", "courage", "energy", "festival", "galaxy", "gravity",
        "language", "memory", "moment", "parallel", "rhythm", "silence", "trophy", "village",
        "voyage", "wonderful", "balance", "discovery", "horizon", "imagination", "architecture",
        "biology", "creative", "melody", "justice", "pattern", "fragrant", "captain", "culture",
        "direction", "fortune", "harvest", "machine", "picture", "science", "season", "station",
        "treasure", "victory", "triangle", "rainbow", "volcano", "musician", "electric", "adoption",
        "airplane", "backpack", "building", "courageous", "democracy", "elevator", "furniture",
        "geography", "hospital", "industry", "language", "marathon", "newspaper", "occasion",
        "painting", "reliable", "strength", "theater", "training", "valuable", "whistle"
    ],

    # 🔥 HARD — kata akademik, abstrak, atau jarang dipakai (±65 kata)
    "hard": [
        "phenomenon", "ambiguous", "onomatopoeia", "entrepreneur", "acquaintance", "benevolent",
        "miscellaneous", "superfluous", "conscientious", "magnificent", "nostalgia", "quarantine",
        "silhouette", "symphony", "vocabulary", "catastrophe", "hypothesis", "perception",
        "persuasion", "renaissance", "subconscious", "synchronous", "transcend", "vulnerability",
        "xenophobia", "aesthetic", "charisma", "dilemma", "eloquent", "serendipity", "idyllic",
        "labyrinth", "meticulous", "notorious", "symbolism", "tranquility", "benevolence",
        "rhetoric", "hierarchy", "juxtapose", "analogy", "epiphany", "criterion",
        "contemplation", "repertoire", "empathy", "dissonance", "catalyst", "equilibrium",
        "articulate", "contradiction", "hypocrisy", "philosophy", "morality", "inheritance",
        "correlation", "manifestation", "aberration", "substitute", "compassion", "credibility",
        "innovation", "intellect", "legitimate", "manipulate", "profound"
    ],

    # 👑 EXTREME — kata super panjang, akademik, atau tricky banget dieja (±55 kata)
    "extreme": [
        "pneumonoultramicroscopicsilicovolcanoconiosis", "floccinaucinihilipilification",
        "antidisestablishmentarianism", "sesquipedalian", "xylophonist", "schadenfreude",
        "hippopotomonstrosesquipedaliophobia", "juxtaposition", "synecdoche", "ubiquitous",
        "pulchritudinous", "lugubrious", "perspicacious", "idiosyncrasy", "circumlocution",
        "paradigm", "euphemism", "quintessential", "metamorphosis", "pseudonym", "mnemonic",
        "cacophony", "vicissitude", "lachrymose", "philanthropy", "soliloquy", "anachronism",
        "sagacious", "verisimilitude", "bildungsroman", "existentialism", "magnanimous",
        "obstreperous", "susceptibility", "supererogatory", "recalcitrant", "parallelogrammatic",
        "psychology", "antagonist", "audiovisual", "circumference", "cryptography",
        "photosynthesis", "metallurgy", "thermodynamics", "epistemology", "telekinesis",
        "disenfranchisement", "incomprehensible", "institutionalization", "counterintuitive",
        "electromagnetism", "anthropomorphism", "photosensitive", "neurotransmitter",
        "microorganism", "hydrodynamics", "bioengineering"
    ]
}

# none existance word on dict.youdao
# "chargoggagoggmanchauggagoggchaubunagungamaugg"

st.markdown("""
<style>
/* 🎯 Only target sidebar expand button icon */
[data-testid="stExpandSidebarButton"] [data-testid="stIconMaterial"],
[data-testid="stSidebarCollapseButton"] [data-testid="stIconMaterial"] {
    position: relative;
    color: transparent !important; /* hide original */
}

/* 🟢 Replace expand icon */
[data-testid="stExpandSidebarButton"] [data-testid="stIconMaterial"]::after {
    content: "Menu";   /* new expand icon */
    color: rgba(250, 250, 250, 0.6); !important;
    font-size: 24px;
    position: absolute;
    top: 0;
    left: 0;
}

/* 🔵 Replace collapse icon */
[data-testid="stSidebarCollapseButton"] [data-testid="stIconMaterial"]::after {
    content: "Menu";    /* new collapse icon */
    color: rgba(250, 250, 250, 0.6); !important;
    font-size: 24px;
    position: absolute;
    top: 0;
    left: 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
[data-testid="stSidebar"] {
    width: 100px;
    min-width: 100px;
    max-width: 100px;
    overflow-x: hidden;
    overflow-y: auto;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<style>
body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stToolbar"] {{
    cursor: url('data:image/png;base64,{get_base64("assets/pointer.png")}') 16 16, auto !important;
}}

button, a, [role="button"] {{
    cursor: url('data:image/png;base64,{get_base64("assets/link.png")}') 16 16, pointer !important;
}}
</style>
""", unsafe_allow_html=True)

button_sidebar_games = f"""
button {{
    width: 60px;
    height: 60px;
    background-image: url('data:image/png;base64,{get_base64("assets/games.png")}');
    background-repeat: no-repeat;
    background-size: 40px;
    background-position: center;
    background-color: #2b74d4;
    transition: 0.3s;
}}
button:hover {{
    background-color: #1b4f91;
}}
"""

button_sidebar_extras = f"""
button {{
    width: 60px;
    height: 60px;
    background-image: url('data:image/png;base64,{get_base64("assets/extra.png")}');
    background-repeat: no-repeat;
    background-size: 40px;
    background-position: center;
    background-color: #2b74d4;
    transition: 0.3s;
}}
button:hover {{
    background-color: #1b4f91;
}}
"""

button_sidebar_about = f"""
button {{
    width: 60px;
    height: 60px;
    background-image: url('data:image/png;base64,{get_base64("assets/about.png")}');
    background-repeat: no-repeat;
    background-size: 40px;
    background-position: center;
    background-color: #2b74d4;
    transition: 0.3s;
}}
button:hover {{
    background-color: #1b4f91;
}}
"""

with st.sidebar:
    with stylable_container(key="sidebar_games", css_styles=button_sidebar_games):
        if st.button("", key="sidebar_btn_games"):
            st.query_params.clear()
            st.query_params["select"] = "games"
            games_reset()

    st.markdown(
        """
        <div style='display:flex; justify-content:center; align-items:center; padding:10px;'>
                <span style='text-align: center;font-size:0.8rem;'>Games</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    with stylable_container(key="sidebar_tempat_extras", css_styles=button_sidebar_extras):
        if st.button("",key="sidebar_btn_tempat_duduk"):
            st.query_params.clear()
            st.query_params["select"] = "extras"
            games_reset()

    st.markdown(
        """
        <div style='display:flex; justify-content:center; align-items:center; padding:10px;'>
                <span style='text-align: center;font-size:0.8rem;'>Extras</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    with stylable_container(key="sidebar_about", css_styles=button_sidebar_about):
        if st.button("",key="sidebar_btn_about"):
            st.query_params.clear()
            st.query_params["select"] = "about"
            games_reset()

    st.markdown(
        """
        <div style='display:flex; justify-content:center; align-items:center; padding:10px;'>
                <span style='text-align: center;font-size:0.8rem;'>About Us</span>
        </div>
        """,
        unsafe_allow_html=True
    )


if params.get("select", "") == "":
    st.query_params.clear()
    st.query_params["select"] = "games"
    st.rerun()
elif params:
    if params.get("select") == "games":
        match st.session_state.menu_select:
            case 0:
                st.markdown("<h2 style='text-align: center;'>Spelling Bee Game</h2>", unsafe_allow_html=True)
                st.markdown(f"<h4>Score: {'{:.2f}'.format(st.session_state.score)}</h4>", unsafe_allow_html=True)
                # DONT USE st.columns TO CENTER THE BUTTON OR YOU WILL REGRET YOUR DECISION!
                if st.button("Start"): 
                    st.session_state.menu_select = 1
                    st.rerun()
            case 1:
                st.markdown(f"""<h4>Rules:<br><br>1. yap<br>2. yap2</h4>""", unsafe_allow_html=True)
                # DONT USE st.columns TO CENTER THE BUTTON OR YOU WILL REGRET YOUR DECISION!
                if st.button("I'm understand"): 
                    st.session_state.menu_select = 2
                    st.rerun()
            case 2:
                diff = st.selectbox(
                "select difficulty:",
                ["Easy bos", "okayy", "hard", "DESPAIR"])
                # DONT USE st.columns TO CENTER THE BUTTON OR YOU WILL REGRET YOUR DECISION!
                if st.button("Play"): 
                    st.session_state.menu_select = 3
                    st.session_state.diff = diff
                    st.session_state.time = math.floor(time.time())
                    st.session_state.word = random.choice(spelling_bee_words.get("easy" if st.session_state.diff == "Easy bos" else "medium" if st.session_state.diff == "okayy" else "hard" if st.session_state.diff == "hard" else "extreme" if st.session_state.diff == "DESPAIR" else ""))
                    st.rerun()
            case 3:
                games()
            case 4:
                if st.session_state.round != ROUND:
                    st.markdown(f"<h4>Round: {'{:02d}'.format(st.session_state.round+1)}/{ROUND}</h4>", unsafe_allow_html=True)
                    if st.button("Ready"):
                        st.session_state.menu_select = 3
                        st.session_state.round += 1
                        st.session_state.word = random.choice(spelling_bee_words.get("easy" if st.session_state.diff == "Easy bos" else "medium" if st.session_state.diff == "okayy" else "hard" if st.session_state.diff == "hard" else "extreme" if st.session_state.diff == "DESPAIR" else ""))
                        st.session_state.time = math.floor(time.time())
                        st.rerun()
                elif st.session_state.round == ROUND:
                    for i in range(len(st.session_state.answer)):
                        st.markdown(f"""<div style="background-color:{"#173828" if st.session_state.answer[i][1] == 1 else "#3e2328"};border-radius:8px;padding:10px;line-height:1.5;">
                            {"Round:"} {'{:02d}'.format(i+1)}/{ROUND}<br>{"Time out" if st.session_state.answer[i][0] == "" else st.session_state.answer[i][0]}<br>{"Correct answer:"} {st.session_state.answer[i][2]}</div><br>""", unsafe_allow_html=True)
                        
                    if st.button("Back"):
                        games_reset()
                        st.rerun()

    elif params.get("select") == "extras":
        extra.extra_menu()
    elif params.get("select") == "about":
        about_us.abt_us()

