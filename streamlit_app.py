import streamlit as st
import time
import random
import base64
from streamlit_extras.stylable_container import stylable_container
import extra

# TO-DO
# BEFORE RELEASE, PLEASE FIX THE LANG!

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

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

    # 👑 VERY HARD — kata super panjang, akademik, atau tricky banget dieja (±55 kata)
    "very_hard": [
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
        "microorganism", "hydrodynamics", "bioengineering", "chargoggagoggmanchauggagoggchaubunagungamaugg"
    ]
}

params = st.query_params

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
            st.query_params["start"] = "false"

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

    st.markdown(
        """
        <div style='display:flex; justify-content:center; align-items:center; padding:10px;'>
                <span style='text-align: center;font-size:0.8rem;'>About Us</span>
        </div>
        """,
        unsafe_allow_html=True
    )

if params:
    if params.get("select") == "games":
        if params.get("start") == "false":
            if st.button("start"):
                st.query_params["start"] = "true"
                st.rerun()
        elif params.get("start") == "true":
            diff = st.selectbox(
            "Difficulty:",
            ["Easy bos", "okayy", "hard", "DESPAIR"])

            if st.button("Play"):
                st.query_params.clear()
                st.query_params["select"] = "games"
                st.query_params["play"] = diff
                st.rerun()
    elif params.get("select") == "extras":
        extra.extra_menu()
