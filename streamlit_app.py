import streamlit as st
import time
import random
import base64
from streamlit_extras.stylable_container import stylable_container
import extra
import time
import math

# TO-DO
# BEFORE RELEASE, PLEASE FIX THE LANG!

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def games_reset():
    print("b")
    st.session_state.start = False
    st.session_state.diff = ""
    st.session_state.play = False
    st.session_state.word = ""
    st.session_state.time = 0
    st.session_state.game_state = 0
    st.session_state.user_input = ""

def games():
    TIME_LIMIT = 10 if st.session_state.diff == "Easy bos" else 8 if st.session_state.diff == "okayy" else 7 if st.session_state.diff == "hard" else 15 if st.session_state.diff == "DESPAIR" else 0.11037
    if st.session_state.game_state == 0:
        timer_placeholder = st.empty()
        progress_placeholder = st.empty()

        st.audio(f"https://dict.youdao.com/dictvoice?audio={st.session_state.word}&type=2")
        st.write(st.session_state.word)

        user_input = st.text_input("Type the word here:")

        while 1:
            elapsed = -(st.session_state.time - math.floor(time.time()) )

            if user_input:
                st.session_state.game_state = 1
                st.session_state.user_input = user_input
                break

            if elapsed > TIME_LIMIT:
                st.session_state.game_state = 3
                break

            timer_placeholder.markdown(f"⏳ **Time left: {elapsed} seconds**")
            progress_placeholder.progress(elapsed / TIME_LIMIT)
            time.sleep(.5)

        st.rerun()
    elif st.session_state.game_state == 1:
        st.text("your input:")
        st.code(st.session_state.user_input)

        if st.button("check"):
            if st.session_state.user_input.strip().lower() == st.session_state.word.lower():
                st.session_state.game_state = 2
            else:
                st.session_state.game_state = 4
            st.rerun()
    elif st.session_state.game_state == 2:
        st.success("YOU WIN!")

        if st.button("Back"):
            st.session_state.score += 1
            games_reset()
            st.rerun()
    elif st.session_state.game_state == 3:
        st.error("TIME UP MY NIG")
        st.markdown(f"The correct spelling was **{st.session_state.word}**")
        if st.button("Back"):
            games_reset()
            st.rerun()
    elif st.session_state.game_state == 4:
        st.error("WRONG WORD")
        st.markdown(f"The correct spelling was **{st.session_state.word}**")

        if st.button("Back"):
            games_reset()
            st.rerun()


params = st.query_params
placeholder = st.empty()

if "start" not in st.session_state:
    st.session_state.start = False
if "diff" not in st.session_state:
    st.session_state.diff = ""
if "play" not in st.session_state:
    st.session_state.play = False
if "word" not in st.session_state:
    st.session_state.word = ""
if "time" not in st.session_state:
    st.session_state.time = 0
if "game_state" not in st.session_state:
    st.session_state.game_state = 0
# -1 mean nothing to do
# 0 mean start
# 1 mean checking
# 2 mean win
# 3 mean lose on time
# 4 mean lose on wrong word

if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "score" not in st.session_state:
    st.session_state.score = 0

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
[data-testid="stSidebar"] {
    width: 100px;
    min-width: 100px;
    max-width: 100px;
    overflow-x: hidden;
    overflow-y: auto;
}
</style>
""", unsafe_allow_html=True)

button_sidebar_games = f"""
button {{
    width: 60px;
    height: 60px;
    background-image: url('data:image/png;base64,{get_base64("games.png")}');
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
    background-image: url('data:image/png;base64,{get_base64("extra.png")}');
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
    background-image: url('data:image/png;base64,{get_base64("about.png")}');
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


if not params:
    st.query_params.clear()
    st.query_params["select"] = "games"
    st.rerun()
elif params:
    if params.get("select") == "games":
        if not st.session_state.start:
            st.markdown(f"### 🏆 Score: {st.session_state.score}")

            if st.button("Start"):
                st.session_state.start = True
                st.rerun()
        elif st.session_state.start and not st.session_state.play:
            diff = st.selectbox(
            "Difficulty:",
            ["Easy bos", "okayy", "hard", "DESPAIR"])

            if st.button("Play"):
                st.session_state.diff = diff
                st.session_state.play = True
                st.session_state.word = random.choice(spelling_bee_words.get("easy" if diff == "Easy bos" else "medium" if diff == "okayy" else "hard" if diff == "hard" else "extreme" if diff == "DESPAIR" else ""))
                st.session_state.time = math.floor(time.time())
                st.rerun()
        elif st.session_state.start and st.session_state.play:
            games()
    elif params.get("select") == "extras":
        extra.extra_menu()




