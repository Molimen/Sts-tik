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

#FRONTEND'S TO-DO

st.markdown("""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Arima:wght@100..700&family=BBH+Sans+Bogle&family=Momo+Trust+Display&family=Rowdies:wght@300;400;700&display=swap');            
            .momo-trust-display-regular {
            font-family: "Momo Trust Display", sans-serif;
            font-weight: 400;
            font-style: normal;
            }
            .bbh-sans-bogle-regular {
            font-family: "BBH Sans Bogle", sans-serif;
            font-weight: 400;
            font-style: normal;
            }
            .arima-isi {
            font-family: "Arima", system-ui;
            font-optical-sizing: auto;
            font-weight: 500;
            font-style: normal;
            line-height: 1.75em;
            }
            .rowdies-light {
            font-family: "Rowdies", sans-serif;
            font-weight: 300;
            font-style: normal;
            }
            .rowdies-regular {
            font-family: "Rowdies", sans-serif;
            font-weight: 400;
            font-style: normal;
            }
            .rowdies-bold {
            font-family: "Rowdies", sans-serif;
            font-weight: 700;
            font-style: normal;
            }
            
            * {
            user-select: none;
            }
            
            [data-testid="stMarkdownContainer"] a[href^="#"] {
            display: none !important;
            }
            
            @keyframes divider-spin {
            0% { transform: rotate(0deg); }
            5.88% { transform: rotate(0deg); }
            11.76% { transform: rotate(45deg); }
            17.64% { transform: rotate(45deg); }
            23.52% { transform: rotate(90deg); }
            29.4% { transform: rotate(90deg); }
            35.28% { transform: rotate(135deg); }
            41.16% { transform: rotate(135deg); }
            47.04% { transform: rotate(180deg); }
            52.92% { transform: rotate(180deg); }
            58.8% { transform: rotate(225deg); }
            64.68% { transform: rotate(225deg); }
            70.56% { transform: rotate(270deg); }
            76.44% { transform: rotate(270deg); }
            82.32% { transform: rotate(315deg); }
            88.2% { transform: rotate(315deg); }
            100% { transform: rotate(360deg); }
            }
            @keyframes bg-divider-scale {
            0% { transform:  scale(1); }
            5.88% { transform:  scale(1); }
            11.76% { transform:  scale(1.25); }
            17.64% { transform:  scale(1.25); }
            23.52% { transform:  scale(1); }
            29.4% { transform:  scale(1); }
            35.28% { transform:  scale(1.25); }
            41.16% { transform:  scale(1.25); }
            47.04% { transform:  scale(1); }
            52.92% { transform:  scale(1); }
            58.8% { transform:  scale(1.25); }
            64.68% { transform:  scale(1.25); }
            70.56% { transform:  scale(1); }
            76.44% { transform:  scale(1); }
            82.32% { transform:  scale(1.25); }
            88.2% { transform: scale(1.25); }
            94.08% { transform: scale(1); }
            100% { transform: scale(1); }
            }
            </style>
            """, unsafe_allow_html=True)

st.markdown("""
<style>
div[data-testid="stStatusWidget"] div button {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

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

ROUND = 10

def games():
    TIME_LIMIT = 10 if st.session_state.diff == "Easy" else 8 if st.session_state.diff == "Medium" else 7 if st.session_state.diff == "Hard" else 15 if st.session_state.diff == "EXTREME" else 0.11037

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
                st.session_state.correct += 1 if st.session_state.diff == "Easy" else 2 if st.session_state.diff == "Medium" else 4 if st.session_state.diff == "Hard" else 8 if st.session_state.diff == "EXTREME" else 0
            break

        if elapsed > TIME_LIMIT:
            st.session_state.answer.append([user_input,2, st.session_state.word])
            break

        timer_placeholder.markdown(f"⏳ Time: {elapsed} seconds")
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
    "Hard": [
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
        "antidisestablishmentarianism", "sesquipedalian", "schadenfreude",
        "juxtaposition", "synecdoche", "ubiquitous",
        "pulchritudinous", "lugubrious", "perspicacious", "idiosyncrasy", "circumlocution",
        "paradigm", "euphemism", "quintessential", "metamorphosis", "pseudonym", "mnemonic",
        "cacophony", "vicissitude", "lachrymose", "philanthropy", "soliloquy", "anachronism",
        "sagacious", "verisimilitude", "bildungsroman", "existentialism", "magnanimous",
        "obstreperous", "susceptibility", "supererogatory", "recalcitrant",
        "psychology", "antagonist", "audiovisual", "circumference", "cryptography",
        "photosynthesis", "metallurgy", "thermodynamics", "epistemology", "telekinesis",
        "disenfranchisement", "incomprehensible", "institutionalization", "counterintuitive",
        "electromagnetism", "anthropomorphism", "photosensitive", "neurotransmitter",
        "microorganism", "hydrodynamics", "bioengineering"
    ]
}

# none existance word on dict.youdao
#

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
    background-color: #66a0bd;
    border: 0.2rem solid #24ADF2;
    transition: 0.3s;
}}
button:hover {{
    background-color: #1b4f91;
    border: 3px solid #999999;
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
    background-color: #66a0bd;
    border: 0.2rem solid #24ADF2;
    transition: 0.3s;
}}
button:hover {{
    background-color: #1b4f91;
    border: 3px solid #999999;
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
    background-color: #66a0bd;
    border: 0.2rem solid #24ADF2;
    transition: 0.3s;
}}
button:hover {{
    background-color: #1b4f91;
    border: 3px solid #999999;
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

css_style = """ 
                    button {
                    display: flex; 
                    justify-content: center;
                    align-items: center;
                    color: white;
                    width: 200px;
                    height: 10px;
                    background-color: #66a0bd;
                    border: 0.2rem solid #24ADF2;
                    border-radius: 50px;
                    padding: 20px;
                    box-shadow: 2px 2px 8px rgba(0,0,0,0.2);
                    transition: all .25s ease;
                    font-weight: bold;
                    }

                    button:hover {
                    border: 3px solid #999999;
                    transition: all .25s ease;
                    }
                    """

if params.get("select", "") == "":
    st.query_params.clear()
    st.query_params["select"] = "games"
    st.rerun()
elif params:
    if params.get("select") == "games":
        match st.session_state.menu_select:
            case 0:
                judul = """Spelling bee adalah sebuah kontes edukasi dan kompetitif di mana peserta diuji kemampuannya mengeja kata-kata (umumnya bahasa Inggris) secara lisan. 
                Seorang pembaca akan memberikan kata, dan peserta harus menyebutkan urutan huruf-hurufnya dengan benar untuk maju ke babak berikutnya. 
                Kompetisi ini bertujuan untuk meningkatkan penguasaan kosa kata, ejaan, dan pemahaman bahasa secara mendalam. (Tapi dalam konteks di game ini katanya di ketik full)"""
                st.html(f"""
                        <div class="title-container">
                            <div class="title-spelling bbh-sans-bogle-regular">Spelling</div>
                            <div class="title-bee bbh-sans-bogle-regular">Bee</div>
                            <img class="title-image" src='data:image/png;base64,{get_base64("assets/games-title-art-img.jpg")}' alt="Bee image here">
                        </div>
                        
                        <div class"text-container">
                            <div class="text-title momo-trust-display-regular">Apa itu Spelling Bee?</div>
                            <div class="text-content arima-isi">{judul}</div>
                        </div>
                        
                        <div class="grand-divider-container">
                            <div class="divider-container">
                                <div class="divider"></div>
                            </div>
                        </div>
                        
                        <div class="rainbow-text momo-trust-display-regular">Cobain minigame Spelling Bee!</div>
                        
                        <style>
                        .grand-divider-container {{
                        position: relative;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        padding-top: 1em;
                        padding-bottom: 0;
                        }}
                        
                        .rainbow-text {{
                        display: flex;
                        justify-content:center;
                        align-items:center;
                        font-size: 2rem;
                        text-align: center;
                        background-color: white;
                        background-clip: text;
                        color: transparent;
                        margin: 0;
                        animation: rainbow 5s linear infinite;
                        }}
                        
                        .title-container {{
                        display: flex;
                        flex-direction: column;
                        text-align: center;
                        height: 15em;
                        max-width: 100%;
                        position: relative;
                        justify-content: center;
                        align-items: left;
                        left: 1em;
                        flex-wrap: wrap;
                        left: 0;
                        padding-left: 2.25em;
                        padding-right: 2.25em;
                        margin-bottom: 2.15em;
                        background-image: url('data:image/png;base64,{get_base64("assets/games-title-img.jpg")}');
                        z-index: 2;
                        border-radius: 2em;
                        border: 8px solid darkorange;
                        }}
                        
                        .title-spelling, .title-bee {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        max-width: 6.55em;
                        min-width: 4em;
                        height: 1.65em;
                        font-size: 2.55em;
                        border-radius: .5rem;
                        z-index: 2;
                        margin: 0.3rem;
                        }}
                        
                        .title-spelling {{
                        background-color: #e8b125;
                        color: black;
                        border: 6px solid #a88019;
                        border-radius: 1.5em .25em .65em 0em; 
                        }}
                        
                        .title-bee {{
                        background-color: #8c6500;
                        color: white;
                        border: 6px solid #5e4401;
                        border-radius: .65em 0em 1.5em .25em;
                        }}
                        
                        .title-image {{
                        display: flex;
                        height: 135px;
                        margin: 1rem;
                        text-align: center;
                        padding: auto;
                        object-fit: contain;
                        transform: rotate(-7deg);
                        animation: bee 2.25s ease-in-out infinite;
                        }}
                        
                        .text-container {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        }}
                        
                        .text-title {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        font-size: 1.3em;
                        }}
                        
                        .text-content {{
                        text-align: center;
                        }}
                        
                        .divider-container, .divider-container2 {{
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        text-align: center;
                        padding: 1px;
                        z-index: 1;
                        width: 100%;
                        height: .5rem;
                        position: relative;
                        margin: 3em;
                        margin-top: 1.25em;
                        }}
                        
                        .divider-container::before, .divider-container::after, .divider-container2::before, .divider-container2::after {{
                        transition: all 1s ease;
                        }}
                        .divider-container::before {{
                        content: "";
                        top: -197%;
                        width: 40px;
                        height: 40px;
                        background-color: #232324;
                        position: absolute;
                        transform: rotate(45deg);
                        animation: bg-divider-scale 7s ease-out infinite;
                        }}
                        .divider-container2::before {{
                        content: "";
                        content: "";
                        top: -197%;
                        width: 40px;
                        height: 40px;
                        background-color: #232324;
                        position: absolute;
                        transform: rotate(45deg);
                        animation: bg-divider-scale 7s ease-out reverse infinite;
                        }}
                        .divider-container::after {{
                        content: "";
                        width: 20px;
                        height: 20px;
                        background-color: white;
                        position: absolute;
                        transform: rotate(45deg);
                        animation: divider-spin 7s ease infinite;
                        }}
                        .divider-container2::after {{
                        content: "";
                        width: 20px;
                        height: 20px;
                        background-color: white;
                        position: absolute;
                        transform: rotate(45deg);
                        animation: divider-spin 7s ease reverse infinite;
                        }}
                        .divider {{
                        height: .35rem;
                        width: 100%;
                        background-image: linear-gradient(90deg, transparent, white,white, transparent);
                        margin: 1.5em 0;
                        }}
                        
                        @keyframes bee {{
                            0% {{
                            transform: rotate(-7deg);
                            }}
                            50% {{
                            transform: rotate(18deg);
                            }}
                        }}
                        @keyframes rainbow {{
                        0% {{background-color: white}}
                        12.5% {{background-color: red}}
                        25% {{background-color: orange}}
                        37.5% {{background-color: yellow}}
                        50% {{background-color: green}}
                        62.5% {{background-color: cyan}}
                        75% {{background-color: blue}}
                        87.5% {{background-color: purple}}
                        100% {{background-color: white}}
                        }}
                        
                        @media (max-width: 650px) {{
                            .title-image {{
                            display: none;
                            }}
                            
                            .title-spelling, .title-bee {{
                            max-width: 100%;
                            }}
                        }}
                        </style>
                        """)
                st.markdown(f"""<h4 class="heading4">Score: {'{:.2f}'.format(st.session_state.score)}<br><sup>(skornya gak permanen btw)</sup></h4>
                            <style>
                            .heading4 {{
                            text-align: center;
                            }}
                            
                            sup {{
                            font-size: .55em;
                            }}
                            </style>
                            """, unsafe_allow_html=True)

                with stylable_container(key="style", css_styles=css_style):
                    with stylable_container(key="center1",
                                            css_styles='''{display: flex; justify-content: center;align-items: center;font-weight: bold;}'''):
                        if st.button("Mulai Permainan"):
                            st.session_state.menu_select = 1
                            st.rerun()
            case 1:
                instruction = """
📜 Aturan Permainan: <br>

1. Ada suara menyebutkan kata dengan jelas. <br>
2. Peserta harus menulis kata tersebut, misalnya: <br>
   > “despair.” <br>
3. Jika ejaan benar, peserta mendapat poin. Jika salah, tidak mendapat poin. <br>
4. Ada batas waktu untuk mengejaan kata tersebut. <br>
5. Ada total 15 ronde permainan.
"""

                note = """
1. Anda bisa memilih kesusahan ejaan kata. <br>
2. Untuk memasukan kata di kolom yang sudah di sediakan. <br>
3. Jika kata sudah dimasukan, klik "Enter" atau klik halaman yang kosong. <br>
4. Kata yang di ejaan itu dalam bahasa inggris. <br>
"""
                st.html(f"""
                        <div class="instruksi">
                            <div class="instruksi-title momo-trust-display-regular">📋INSTRUKSI📋</div>
                            <div class="instruksi-text-wrapper">    
                                <div class="instruksi-text arima-isi">{instruction}</div>
                            </div>
                        </div>
                        <div class="catatan">
                            <div class="catatan-title momo-trust-display-regular">📓CATATAN📓</div>
                            <div class="catatan-text-wrapper">    
                                <div class="catatan-text arima-isi">{note}</div>
                            </div>
                        </div>
                        <style>
                        .instruksi, .catatan {{
                        max-width: 100%;
                        height: auto;
                        z-index: 0;
                        }}
                        
                        .instruksi-title, .catatan-title {{
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-size: 3em;
                        background-color: orange;
                        max-width: 100%;
                        border-radius: .55em .55em 0em 0em;
                        border: .15em solid #ba7213;
                        z-index: 3;
                        color: black;
                        background-image: linear-gradient(rgba(255,165,0,0.1),rgba(255,165,0,0.1)), url('data:image/png;base64,{get_base64("assets/games-title-img.jpg")}');
                        }}
                        .instruksi-title {{
                        background-position: left bottom;
                        object-fit: cover;
                        }}
                        .catatan-title {{
                        background-position: center top;
                        object-fit: cover;
                        }}
                        
                        .instruksi-text-wrapper, .catatan-text-wrapper {{
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        }}
                        
                        .instruksi-text, .catatan-text {{
                        display: flex;
                        border: .5em solid #e38a14;
                        border-top: 0;
                        max-width: 90%;
                        z-index: 1;
                        padding: 1em;
                        margin-bottom: 2em;
                        border-radius: 0 0 1.35em 1.35em ;
                        background-color: #473602;
                        }}
                        .instruksi-text {{
                        animation: color-pulse 2s ease infinite
                        }}
                        .catatan-text {{
                        animation: color-pulse 2s ease reverse infinite
                        }}
                        
                        @keyframes color-pulse {{
                            50% {{
                            background-color: #785a01;
                            }}
                        }}
                        
                        @media (max-width: 700px) {{
                            .instruksi-title, .catatan-title {{
                            font-size: 2.15em;
                            }}
                        }}
                        </style>""")
                with stylable_container(key="style", css_styles=css_style):
                    with stylable_container(key="center1",css_styles='''{display: flex; justify-content: center;align-items: center;font-weight: bold;}'''):
                        if st.button("Saya sudah paham"):
                            st.session_state.menu_select = 2
                            st.rerun()
            case 2:
                st.html(f"""
                        <div class="diff-container">
                            <div class='diff-title'></div>
                            <div class='diff-title-text bbh-sans-bogle-regular'>Pilih level kesusahan</div>
                        </div>    
                        
                        <style>
                        .diff-container {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        position: relative;
                        height: 8em;
                        z-index: 0;
                        margin-bottom: 1em;
                        }}
                        
                        .diff-title {{
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-size: 3em;
                        background-image: url('data:image/png;base64,{get_base64("assets/games-title-img.jpg")}');
                        background-position: left bottom;
                        object-fit: contain;
                        border-radius: 0em;
                        text-align: center;
                        line-height: 1.15em;
                        height: 100%;
                        width: 95%;
                        border-radius: 4rem;
                        position: relative;
                        border: .4rem solid #c97704;
                        overflow: hidden;
                        animation: border-curve 2s ease infinite;
                        }}
                        .diff-title::before, .diff-title::after {{
                        content: '';
                        width: 5em;
                        height: 3em;
                        z-index: 1;
                        position: absolute;
                        background-color: orange;
                        opacity: .8;
                        filter: blur(.65em);
                        transition: all 500ms ease;
                        
                        }}
                        .diff-title::before {{
                        transform: translate(7em);
                        animation: slide1 1.75s ease-in-out infinite
                        }}
                        .diff-title::after {{
                        transform: translate(-7em);
                        animation: slide2 1.75s ease-in-out infinite
                        }}
                        
                        .diff-title-text {{
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-size: 3.45em;
                        border-radius: .55em;
                        text-align: center;
                        line-height: 1.15em;
                        padding: .45rem 0;
                        width: 77%;
                        height: 60%;
                        position: absolute;
                        color: #5c4d02;
                        z-index: 2;
                        }}
                        @keyframes border-curve {{
                            50% {{border-radius: 0;}}
                        }}
                        @keyframes slide1 {{
                            from {{
                            transform: translate(110%);
                            }}
                            to {{
                            transform: translate(-110%);
                            }}
                        }}
                        @keyframes slide2 {{
                            from {{
                            transform: translate(-110%);
                            }}
                            to {{
                            transform: translate(110%);
                            }}
                        }}
                        
                        @media (max-width: 650px) {{
                            .diff-title-text {{
                            font-size: 2.85em;
                            }}
                        }}
                        </style>
                        """)
                diff = st.selectbox(
                "Pilih Difficulty (level kesusahan gamenya)",
                ["Easy", "Medium", "Hard", "EXTREME"])
                st.html("""
                        <div class="diff-label momo-trust-display-regular">Difficulty yang dipilih:</div>
                        <style>
                        .diff-label {
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        font-size: 1.55em;
                        margin: 1em 0 0 0;
                        }
                        </style>
                        """)
                if diff == "Easy":
                    st.html("""
                            <div class="grand-easy-container">
                                <div class="easy-container">
                                    <div class='easy-decorator1'></div>
                                    <div class='e rowdies-bold'>E</div>
                                    <div class='a rowdies-bold'>a</div>
                                    <div class='s rowdies-bold'>s</div>
                                    <div class='y rowdies-bold'>y</div>
                                    <div class='easy-decorator2'></div>
                                </div>
                            </div>
                            
                            <style>
                            .easy-decorator1, .easy-decorator2 {
                            width: 2rem;
                            height: 2rem;
                            margin: 1.1em;
                            border-radius: 99em;
                            border: 2px solid #11360c;
                            }
                            .easy-decorator1 {
                            background-image: linear-gradient(90deg,#195d0a,#88ec72);
                            }
                            .easy-decorator2 {
                            background-image: linear-gradient(-90deg, #195d0a,#88ec72);
                            }
                            
                            .grand-easy-container {
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            overflow: visible;
                            margin: 0 0 1.5em 0;
                            }
                            
                            .easy-container {
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            background-color: #35ca00;
                            height: 4em;
                            width: 15em;
                            border-radius: 4em;
                            border: 5px solid green;
                            box-shadow: 4px 4px 4px 4px #404040;
                            }
                            
                            .e, .a, .s, .y {
                            margin: .2rem;
                            font-size: 2em;
                            color: black;
                            }
                            .e {animation: letter-pulse 1.5s ease infinite;margin-left: 0;}
                            .a {animation: letter-pulse 1.5s ease infinite .2s}
                            .s {animation: letter-pulse 1.5s ease infinite .4s}
                            .y {animation: letter-pulse 1.5s ease infinite .6s;margin-right: 0;}
                            
                            @keyframes letter-pulse {
                            50% {transform: scale(1.3);}
                            }
                            </style>
                            """)
                elif diff == "Medium":
                    st.html("""
                            <div class='great-grand-medium-container'>
                                <div class="grand-medium-container">
                                    <div class="medium-decorator1"></div>
                                    <div class="medium-decorator2"></div>
                                    <div class="medium-container">
                                        <div class='medium rowdies-bold'>Medium</div> 
                                    </div>
                                </div>
                            </div>
                            
                            <style>
                            .great-grand-medium-container {
                            display: flex;
                            align-items: center;
                            justify-content: center;}
                            
                            .grand-medium-container {
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            overflow: visible;
                            margin: 0 0 1.5em 0;
                            z-index: 0;
                            position: relative;
                            max-width: 100%;
                            }
                            
                            .medium-container {
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            background-color: #ffd601;
                            height: 4em;
                            width: 15em;
                            border-radius: 2em 0 2em 0;
                            border: 5px solid #ba9c00;
                            box-shadow: 4px 4px 4px 4px #404040;
                            z-index: 1;
                            overflow: hidden;
                            position: relative;
                            }
                            
                            .medium {
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            font-size: 2em;
                            color: #d6a12d;
                            mix-blend-mode: difference;
                            z-index: 3;
                            height: 4em;
                            width: 5em;
                            position: relative;
                            overflow: hidden;
                            }
                            .medium::before {
                            content: "";
                            height: 32%;
                            width: 9rem;
                            background-color: yellow;
                            position: absolute;
                            z-index: 0;
                            mix-blend-mode: difference;
                            left: 0;
                            transform: translate(-95%);
                            animation: blendmode-slide 4s ease-in-out infinite;
                            }
                            
                            .medium-decorator1 {
                            width: 2.25em;
                            height: 2.25em;
                            background-color: #d67f2d;
                            position: absolute;
                            box-shadow: inset -2px 2px 2px 2px #87490f;
                            border: 2px solid black;
                            top: -15%;
                            left: 90%;
                            z-index: 9;
                            }
                            .medium-decorator2 {
                            content: "";
                            width: 2.25em;
                            height: 2.25em;
                            background-color: #d67f2d;
                            position: absolute;
                            box-shadow: inset 2px -2px 2px 2px #87490f;
                            border: 2px solid black;
                            bottom: -15%;
                            right: 90%;
                            z-index: 9;
                            }
                            
                            @keyframes blendmode-slide {
                                50% {transform: translate(105%);}
                            }
                            
                            </style>
                            """)
                elif diff == "Hard":
                    st.html("""<div></div>""")
                elif diff == "EXTREME":
                    st.html("""<div></div>""")
                with stylable_container(key="style", css_styles=css_style):
                    with stylable_container(key="center1",css_styles='''{display: flex; justify-content: center;align-items: center;font-weight: bold;}'''):
                        if st.button("Play"):
                            st.session_state.menu_select = 3
                            st.session_state.diff = diff
                            st.session_state.time = math.floor(time.time())
                            st.session_state.word = random.choice(spelling_bee_words.get("easy" if st.session_state.diff == "Easy" else "medium" if st.session_state.diff == "Medium" else "Hard" if st.session_state.diff == "Hard" else "extreme" if st.session_state.diff == "EXTREME" else ""))
                            st.rerun()
            case 3:
                games()
            case 4:
                if st.session_state.round != ROUND:
                    st.markdown(f"<h4>Round: {'{:02d}'.format(st.session_state.round+1)}/{ROUND}</h4>", unsafe_allow_html=True)
                    if st.button("Ready"):
                        st.session_state.menu_select = 3
                        st.session_state.round += 1
                        st.session_state.word = random.choice(spelling_bee_words.get("easy" if st.session_state.diff == "Easy" else "medium" if st.session_state.diff == "Medium" else "Hard" if st.session_state.diff == "Hard" else "extreme" if st.session_state.diff == "EXTREME" else ""))
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

