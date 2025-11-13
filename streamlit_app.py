import streamlit as st
import time
import random
import base64
from streamlit import session_state
from streamlit_extras.stylable_container import stylable_container
import extra
import time
import math
import about_us
import home

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

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def games_reset():
    if st.session_state.round == ROUND and st.session_state.round != 0:
        st.session_state.score += st.session_state.correct / ROUND

    st.session_state.menu_select = 0
    st.session_state.diff = "Easy"
    st.session_state.round = 1
    st.session_state.time = 0
    st.session_state.answer = []
    st.session_state.correct = 0

ROUND = 15

def games():
    TIME_LIMIT = 20 if st.session_state.diff == "Easy" else 18 if st.session_state.diff == "Medium" else 16 if st.session_state.diff == "Hard" else 15 if st.session_state.diff == "EXTREME" else 0.11037

    st.markdown(f"""<div class="round-count rowdies-regular">Round: {'{:02d}'.format(st.session_state.round)}/{ROUND:02d}</div>
                <style>
                .round-count {{
                display: flex;
                text-align: center;
                justify-content: center;
                align-items: center;
                font-size: 2.75em;
                background-image: linear-gradient(#4aa4f7, #183754);
                border-radius: .25em;
                margin-bottom: 1.5rem;
                position: relative;
                z-index: 1;
                border: .15em solid #262a75;
                overflow: hidden;
                color: black;
                transition: all .975s ease;
                }}
                
                .round-count::before, .round-count::after {{
                content: "";
                display: flex;
                flex-direction: row;
                width: 40%;
                height: 100%;
                background-color: #1351bd;
                position: absolute;
                opacity: .820;
                padding: .25em;
                z-index: 0;
                filter: drop-shadow(5px 5px 10px black) drop-shadow(-5px 5px 10px black);
                transition: all .975s ease;
                }}
                .round-count::before{{
                left: -20%;
                animation: skewy1 4s ease infinite;
                }}
                
                .round-count::after {{
                right: -20%;
                animation: skewy2 4s ease infinite;
                }}
                
                @keyframes skewy1 {{
                    25% {{transform: skewX(-60deg);}}
                    50% {{transform: skewX(0deg);}}
                    75% {{transform: skewx(60deg);}}
                }}
                @keyframes skewy2 {{
                    25% {{transform: skewX(60deg);}}
                    50% {{transform: skewX(0deg);}}
                    75% {{transform: skewx(-60deg);}}
                }}
                
                @media (max-width: 600px) {{
                    .round-count{{
                    font-size: 2em;
                    }}
                    
                    .round-count::before {{
                    left: -32%;
                    }}
                    .round-count::after {{
                    right: -32%;
                    }}
                }}
                </style>
                """, unsafe_allow_html=True)

    st.markdown("""""", unsafe_allow_html=True) # don't delete this. cause this fix the gray out button!
    timer_placeholder = st.empty()
    progress_placeholder = st.empty()

    st.audio(f"https://dict.youdao.com/dictvoice?audio={st.session_state.word}&type=2")

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

        timer_placeholder.markdown(f"""<div class="livetimer momo-trust-display-regular">⏳ Time: {elapsed} / {TIME_LIMIT} seconds</div>
                                    <style>
                                    .livetimer {{
                                    display: flex;
                                    justify-content: center;
                                    align-items: center;
                                    font-size: 1.12em;
                                    }}
                                    </style>
                                    """, unsafe_allow_html=True)
        progress_placeholder.progress(elapsed / TIME_LIMIT)
        time.sleep(.5)

    st.session_state.menu_select = 3
    st.rerun()

params = st.query_params
placeholder = st.empty()

if "menu_select" not in st.session_state:
    st.session_state.menu_select = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "diff" not in st.session_state:
    st.session_state.diff = "Easy"
if "diff_chk" not in st.session_state:
    st.session_state.diff_chk = ""
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

st.markdown("""
<style>
div[data-testid="stStatusWidget"] div button {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

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
# chargoggagoggmanchauggagoggchaubunagungamaugg

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

button_sidebar_home = f"""
button {{
    width: 60px;
    height: 60px;
    background-image: url('data:image/png;base64,{get_base64("assets/home.png")}');
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
    with stylable_container(key="sidebar_home", css_styles=button_sidebar_home):
        if st.button("", key="sidebar_btn_home"):
            st.query_params.clear()
            games_reset()

    st.markdown(
        """
        <div style='display:flex; justify-content:center; align-items:center; padding:1px;padding-bottom: 30px;'>
                <span style='text-align: center;font-size:0.8rem;line-height:1rem;'>Utama</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    with stylable_container(key="sidebar_tempat_extras", css_styles=button_sidebar_extras):
        if st.button("",key="sidebar_btn_tempat_duduk"):
            st.set_page_config(layout="centered")
            st.query_params.clear()
            st.query_params["select"] = "extras"
            games_reset()

    st.markdown(
        """
        <div style='display:flex; justify-content:center; align-items:center; padding:1px;padding-bottom: 30px;'>
                <span style='text-align: center;font-size:0.8rem;line-height:1rem;'>Ekstra</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    with stylable_container(key="sidebar_about", css_styles=button_sidebar_about):
        if st.button("",key="sidebar_btn_about"):
            st.set_page_config(layout="centered")
            st.query_params.clear()
            st.query_params["select"] = "about"
            games_reset()

    st.markdown(
        """
        <div style='display:flex; justify-content:center; align-items:center; padding:1px;padding-bottom: 30px;'>
                <span style='text-align: center;font-size:0.8rem;line-height:1rem;'>Tentang kami</span>
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
    home.home()
    st.html(f"""
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
            if st.button("Mainin minigamenya!"):
                st.query_params.clear()
                st.query_params["select"] = "games"
                st.set_page_config(layout="centered")
                st.rerun()
elif params:
    if params.get("select") == "games":
        match st.session_state.menu_select:
            case 0:
                instruction = """
📜 Aturan Permainan: <br>

1. Ada suara menyebutkan kata dengan jelas. <br> ------------------------- <br>
2. Peserta harus menulis kata tersebut, misalnya: <br>
   > “despair” <br>
   (huruf besar atau kecil itu bebas, tapi jangan ada karakter lain selain huruf) <br> ------------------------- <br>
3. Jika ejaan benar, peserta mendapat poin. Jika salah, tidak mendapat poin. <br> ------------------------- <br>
4. Ada batas waktu untuk mengejaan kata tersebut. <br>
    Easy = 20 detik<br>Medium = 18 detik<br>Hard = 16 detik<br>Extreme = 15 detik<br> ------------------------- <br>
5. Ada total 15 ronde permainan.
"""

                note = """
1. Anda bisa memilih kesusahan ejaan kata. <br> ------------------------- <br>
2. Untuk menjawab, masukan kata dalam kolom yang sudah di sediakan. <br> -------------------------<br>
3. Jika kata sudah dimasukan, klik "Enter" atau klik bagian halaman yang kosong. <br> -------------------------<br>
4. Kata yang di eja (diketik si kalo di sini) itu dalam bahasa inggris. <br>
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
                        background-color: #785a01;
                        text-align: center;
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
                            st.session_state.menu_select = 1
                            st.rerun()
            case 1:
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
                        border-radius: 0rem;
                        position: relative;
                        border: .65rem solid #c97704;
                        border-top: .65rem solid #875100;
                        border-bottom: .65rem solid #875100;
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
                        
                        @media (max-width: 650px) {{
                            .diff-title-text {{
                            font-size: 2.85em;
                            }}
                        }}
                        </style>
                        """)

                st.markdown(f"""<style>
                [data-testid="stSelectbox"] {{
                  background-color: {"#35ca00" if st.session_state.diff == "Easy" else "#ffd601" if st.session_state.diff == "Medium" else "#ff3c19" if st.session_state.diff == "Hard" else "#7315bf" if st.session_state.diff == "EXTREME" else ""};
                  padding: 20px;
                  border-radius: 10px;
                  width: relative;
                  text-align: center;
                  border: 5px solid {"green" if st.session_state.diff == "Easy" else "#ba9c00" if st.session_state.diff == "Medium" else "#ba0000" if st.session_state.diff == "Hard" else "#9673ff" if st.session_state.diff == "EXTREME" else ""};
                }}
                            
                .st-emotion-cache-lyi571 {{
                    color: {"white" if st.session_state.diff in ["Hard", "EXTREME"] else "black"};
                }}
                </style>""", unsafe_allow_html=True)

                st.session_state.diff = st.selectbox(
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
                
                if st.session_state.diff != st.session_state.diff_chk:
                    st.session_state.diff_chk = st.session_state.diff
                    st.rerun()

                match st.session_state.diff:
                    case "Easy":
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
                    case "Medium":
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
                    case "Hard":
                        st.html("""<div class="grand-hard-container">
                                    <div class='hard-decorator1'></div>
                                    <div class='hard-decorator2'></div>
                                    <div class="hard-container">
                                        <div class='hard rowdies-bold'>Hard</div>
                                    </div>
                                </div>
                                
                                <style>
                                .hard-decorator1, .hard-decorator2 {
                                width: 2.3rem;
                                height: 2.3rem;
                                margin: 1.1em;
                                border-radius: 99em;
                                position: absolute;
                                z-index: 5;
                                background-color: black;
                                clip-path: polygon(50% 0%, 61% 35%, 98% 35%, 68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
                                animation: hard-star-pulse 1.5s ease-in-out infinite;
                                }
                                .hard-decorator1 {
                                transform: translate(-293%);
                                }
                                .hard-decorator2 {
                                transform: translate(293%);
                                }
                                
                                
                                .grand-hard-container {
                                display: flex;
                                align-items: center;
                                justify-content: center;
                                overflow: visible;
                                margin: 0 0 1.5em 0;
                                }
                                
                                .hard-container {
                                display: flex;
                                justify-content: center;
                                align-items: center;
                                background-color: #ff3c19;
                                height: 4em;
                                width: 15em;
                                border-radius: 0em;
                                border: .4rem solid #ba0000;
                                box-shadow: 4px 4px 4px 4px #404040;
                                position: relative;
                                animation: hard-color-pulse 2s ease infinite;
                                }
                                
                                .hard {
                                font-size: 2em;
                                color: black
                                }
                                
                                .hard-container::before {
                                content: "";
                                width: 25%;
                                height: 170%;
                                left: -10%;
                                background-color: #6c0202;
                                position: absolute;
                                border-radius: .35em;
                                border: 3px solid black;
                                box-shadow: inset 2px 2px 3px 3px darkred;
                                }
                                .hard-container::after {
                                content: "";
                                width: 25%;
                                height: 170%;
                                right: -10%;
                                background-color: #6c0202;
                                position: absolute;
                                border-radius: .35em;
                                border: 3px solid black;
                                box-shadow: inset -2px 2px 3px 3px darkred;
                                }
                                
                                @keyframes hard-color-pulse {
                                    50% {background-color: #6e0404;}
                                }
                                @keyframes hard-star-pulse {
                                    50% {background-color: #d90404;}
                                }
                                </style>
                                """)
                    case "EXTREME":
                        st.html("""
                                <div class="great-grand-extreme-container">
                                    <div class="grand-extreme-container">
                                        <div class="extreme-container">
                                            <div class='extreme-decorator2'></div>
                                            <div class='extreme-decorator1'></div>
                                        </div>
                                        <div class='extreme rowdies-bold'>EXTREME</div>
                                    </div>
                                </div>
                                
                                <style>
                                .great-grand-extreme-container {
                                display: flex;
                                align-items: center;
                                justify-content: center;
                                overflow: hidden;
                                }
                                
                                .extreme-decorator1, .extreme-decorator2 {
                                width: 60px;
                                height: 40px;
                                background-color: #7315bf;
                                position: absolute;
                                border-radius: .35em 0 0 .35em;
                                z-index: 0;
                                animation: spike 1.15s ease infinite;
                                clip-path: polygon(100% 0, 75% 50%, 100% 100%);
                                }
                                .extreme-decorator1 {
                                transform: translate(-250%);
                                }
                                .extreme-decorator2 {
                                transform:translate(250%) rotateZ(180deg)
                                }

                                .grand-extreme-container {
                                display: flex;
                                align-items: center;
                                justify-content: center;
                                overflow: hidden;
                                padding: 1.25em;
                                position: relative;
                                height: auto;
                                width: 55%;
                                border: 2px solid transparent;
                                animation: extreme-card .5s ease infinite;
                                }
                                
                                .extreme-container {
                                display: flex;
                                justify-content: center;
                                align-items: center;
                                background-color: #9002d4;
                                height: 4em;
                                width: 15em;
                                border-radius: 0em;
                                border: .4rem solid #9673ff;
                                position: relative;
                                mix-blend-mode: difference;
                                animation: extreme-color-pulse 1.45s ease-in-out infinite;
                                z-index: 0;
                                box-shadow: 0px 0px 12px 12px rgba(252, 62, 196, .5);
                                }
                                
                                .extreme {
                                font-size: 2em;
                                color: #b726fc;
                                mix-blend-mode: difference;
                                position: absolute;
                                z-index: 0;                     
                                }
                                
                                @keyframes extreme-color-pulse {
                                    50% {background-color: #45155c;}
                                }
                                @keyframes spike {
                                    33% {clip-path: polygon(100% 0, 75% 50%, 100% 100%);}
                                    66% {clip-path: polygon(100% 0, 25% 50%, 100% 100%);}
                                }
                                @keyframes extreme-card {
                                    33% {transform: rotateZ(3deg);}
                                    58% {transform: rotateZ(-5deg);}
                                    78% {transform: rotateZ(2deg);}
                                }
                                
                                @media (max-width: 600px) {
                                    .grand-extreme-container {
                                    width: 100%;
                                    }
                                }
                                </style>""")
                with stylable_container(key="style", css_styles=css_style):
                    with stylable_container(key="center1",css_styles='''{display: flex; justify-content: center;align-items: center;font-weight: bold;}'''):
                        if st.button("Play"):
                            st.session_state.menu_select = 2
                            st.session_state.time = math.floor(time.time())
                            st.session_state.word = random.choice(spelling_bee_words.get("easy" if st.session_state.diff == "Easy" else "medium" if st.session_state.diff == "Medium" else "Hard" if st.session_state.diff == "Hard" else "extreme" if st.session_state.diff == "EXTREME" else ""))
                            st.rerun()
            case 2:
                games()
            case 3:
                if st.session_state.round != ROUND:
                    st.markdown(f"""
                                <div class="round-count rowdies-regular">Round: {'{:02d}'.format(st.session_state.round+1)}/{ROUND:02d}</div>
                                
                                <style>
                                .round-count {{
                                display: flex;
                                text-align: center;
                                justify-content: center;
                                align-items: center;
                                font-size: 2.75em;
                                background-image: linear-gradient(#fcf047, #cf7e04);
                                border-radius: .25em;
                                margin-bottom: 1.5rem;
                                position: relative;
                                z-index: 1;
                                border: .15em solid #9e3200;
                                overflow: hidden;
                                color: black;
                                transition: all .975s ease;
                                }}
                                
                                .round-count::before, .round-count::after {{
                                content: "";
                                display: flex;
                                flex-direction: row;
                                width: 40%;
                                height: 100%;
                                background-color: #c95f2e;
                                position: absolute;
                                opacity: .820;
                                padding: .25em;
                                z-index: 0;
                                filter: drop-shadow(5px 5px 10px black) drop-shadow(-5px 5px 10px black);
                                transition: all .975s ease;
                                }}
                                .round-count::before{{
                                left: -20%;
                                animation: skewy1 4s ease infinite;
                                }}
                                
                                .round-count::after {{
                                right: -20%;
                                animation: skewy2 4s ease infinite;
                                }}
                                
                                @keyframes skewy1 {{
                                    25% {{transform: skewX(-60deg);}}
                                    50% {{transform: skewX(0deg);}}
                                    75% {{transform: skewx(60deg);}}
                                }}
                                @keyframes skewy2 {{
                                    25% {{transform: skewX(60deg);}}
                                    50% {{transform: skewX(0deg);}}
                                    75% {{transform: skewx(-60deg);}}
                                }}
                                
                                @media (max-width: 600px) {{
                                    .round-count{{
                                    font-size: 2em;
                                    }}
                                    
                                    .round-count::before {{
                                    left: -32%;
                                    }}
                                    .round-count::after {{
                                    right: -32%;
                                    }}
                                }}
                                </style>
                                """, unsafe_allow_html=True)
                    with stylable_container(key="style", css_styles=css_style):
                        with stylable_container(key="center1",
                                                css_styles='''{display: flex; justify-content: center;align-items: center;font-weight: bold;}'''):
                            if st.button("Ready"):
                                st.session_state.menu_select = 2
                                st.session_state.round += 1
                                st.session_state.word = random.choice(spelling_bee_words.get("easy" if st.session_state.diff == "Easy" else "medium" if st.session_state.diff == "Medium" else "Hard" if st.session_state.diff == "Hard" else "extreme" if st.session_state.diff == "EXTREME" else ""))
                                st.session_state.time = math.floor(time.time())
                                st.rerun()
                elif st.session_state.round == ROUND:
                    if st.session_state.diff == "Easy":
                        colors = ['rgba(53, 202, 0, .35)', 'rgba(0, 128, 0, 1)']
                    elif st.session_state.diff == "Medium":
                        colors = ['rgba(255, 214, 1, .35)', 'rgba(186, 156, 0, 1)']
                    elif st.session_state.diff == "Hard":
                        colors = ['rgba(255, 60, 25, .35)', 'rgba(186, 0, 0, 1)']
                    elif st.session_state.diff == "EXTREME":
                        colors = ['rgba(133, 17, 188, .35)', 'rgba(83, 2, 116, 1)']

                    st.html(f"""
                            <div class="result-title bbh-sans-bogle-regular">Hasil Performa Permainan</div>
                            
                            <style>
                            .result-title {{
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            font-size: 2.85em;
                            background-image: url('data:image/png;base64,{get_base64("assets/games-title-img.jpg")}');
                            background-position: left center;
                            border: .15em solid #ba7213;
                            border-radius: 7em 7em 2em 2em;
                            color: black;
                            padding: .35em;
                            text-align: center;
                            line-height: 2.5rem;
                            }}
                            @media (max-width: 700px) {{
                                .result-title {{
                                font-size: 2.25em;
                                padding: .1em;
                                }}
                            }}
                            </style>
                            """)
                    for i in range(len(st.session_state.answer)):
                        st.markdown(f"""<div class="arima-isi" style="background-color:{"#173828" if st.session_state.answer[i][1] == 1 else "#3e2328"};border-radius:10px;padding:10px;line-height:1.5;border: 3px solid {"#71d46e" if st.session_state.answer[i][1] == 1 else "#d46e6e"}">
                            {"Ronde:"} {'{:02d}'.format(i+1)}/{ROUND:02d}<br>{"-- Waktu Habis --" if st.session_state.answer[i][0] == "" else st.session_state.answer[i][0]}<br>{"Correct answer:"} {st.session_state.answer[i][2]}</div><br>""", unsafe_allow_html=True)
                    st.html(f"""
                            <div class="skor momo-trust-display-regular">💯 Skor Akhir 💯<br>+ {st.session_state.correct / ROUND:.2f}</div>
                            <style>
                            .skor {{
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            font-size: 1.5em;
                            text-align: center;
                            background-color: #0d0173;
                            border: 3px solid #4032bf;
                            border-radius: 2em 2em 8em 8em;
                            margin-bottom: 1rem;
                            }}
                            </style>
                            """)
                    with stylable_container(key="style", css_styles=css_style):
                        with stylable_container(key="center1",
                                                css_styles='''{display: flex; justify-content: center;align-items: center;font-weight: bold;}'''):
                            if st.button("Back"):
                                st.query_params.clear()
                                games_reset()
                                st.rerun()

    elif params.get("select") == "extras":
        extra.extra_menu()
    elif params.get("select") == "about":
        about_us.abt_us()

