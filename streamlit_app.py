import streamlit as st
import time
import random
from streamlit_option_menu import option_menu
import base64

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()
ekstra1 = get_base64("image.jpg")
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
#BAGIAN HMTL
selected2 = option_menu("Menu Navigasi", ["Minigame", "Ekstra", "Tentang Kami"],
                        icons=['house', 'tools', "info-square-fill"],
                        menu_icon="cast", default_index=0, orientation="horizontal",
                        styles={"nav-link-selected": {'background-color' : '#e4e800', 'color' : 'black', 'border' : '3px solid #b07f04'},
                                "container" : {'background-color' : '#e8c100', 'color' : 'black', 'border' : '3px solid black'},
                                })
if selected2 == "Minigame": #minigame disini
    st.write('elu milih', selected2) #line 71 cuma testing
    #kode elu
elif selected2 == "Ekstra": # 'ekstra' sama 'tentang kami' full HTML + CSS karna ga perlu backend
    st.markdown(f"""
                <div class='container1'>
                    <div class='imgcontainer1'>
                        <img id="gambar1" src="data:image/jpg;base64,{ekstra1}" alt="gambar random">
                        <div class="linkbtn1"><a href='https://layout-tempat-duduk-generator.streamlit.app/'>Kunjungi Situsnya</a></div>                     
                    </div>
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Culpa cupiditate dolorem doloribus ea error esse fugit illum ipsam laboriosam magni minus molestias nemo, officia omnis optio reiciendis vitae voluptates voluptatum!</p>
                </div>
                """, unsafe_allow_html=True)
elif selected2 == "Tentang Kami":
    st.markdown("""
                
                """, unsafe_allow_html=True)
#BAGIAN CSS
st.markdown("""
            <style>
            .container1 {
            max-width:90%;margin:auto;border: 2px solid blue;text-align: center;height:300px;
            }
            .imgcontainer1 {
            border:2px solid black;
            max-width:30%;
            height:300px;
            float:left;
            }
            
            #gambar1 {
            height: 215px;
            border-radius: 15px;
            border: 5px solid black;
            margin-bottom: 15px;
            text-align: center;
            }
            .linkbtn1 {
            background-color: #3cba64;
            padding: 10px;
            width: 100%;
            border-radius: 8px;
            }
            .linkbtn1 a {
            font-size: 1.15em;
            text-decoration: none;
            }
            </style>
            """, unsafe_allow_html=True)
