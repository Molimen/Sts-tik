import streamlit as st
import base64

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

text1 = """Spelling Bee adalah kompetisi mengeja kata dalam bahasa Inggris, di mana peserta harus menyebutkan huruf demi huruf dari sebuah kata yang diberikan oleh juri dengan benar. Lomba ini melatih kemampuan kosakata, pelafalan, dan konsentrasi."""

text2 = """Kata “bee” dalam Spelling Bee tidak berarti lebah 🐝.<br>
Dalam bahasa Inggris lama, “bee” berarti perkumpulan orang untuk melakukan suatu kegiatan bersama, seperti quilting bee (acara menjahit bersama). Jadi, Spelling Bee berarti acara bersama untuk mengeja."""

text3 = """<h3>1700-an (Abad ke-18)</h3>
- Tradisi mengeja sudah populer di sekolah-sekolah di Amerika dan Inggris untuk melatih ejaan bahasa Inggris yang rumit. <br>
- Buku terkenal "The Blue-backed Speller" karya Noah Webster (1786) digunakan secara luas untuk mengajar ejaan.
<h3>1825</h3>
- Istilah “spelling bee” mulai digunakan secara umum di Amerika Serikat untuk menyebut lomba mengeja di sekolah-sekolah."""

text4 = """- Setelah sukses di Amerika, Spelling Bee mulai menyebar ke negara-negara lain seperti Kanada, Australia, India, Filipina, dan bahkan Indonesia.<br>
- Sekolah-sekolah internasional dan lembaga bahasa Inggris di berbagai negara kini rutin mengadakan kompetisi Spelling Bee untuk anak-anak dan pelajar."""

text5 = """1. Melatih kemampuan berbahasa Inggris — terutama dalam ejaan, pengucapan, dan pemahaman arti kata. <br>
2. Menumbuhkan minat belajar bahasa sejak dini agar peserta lebih mencintai bahasa Inggris. <br>
3. Mendorong kebiasaan membaca dan memperluas kosakata. <br>
4. Melatih fokus dan konsentrasi tinggi saat mendengarkan dan mengeja kata."""

def home():
    st.markdown("""
                <style>
                @import url('https://fonts.googleapis.com/css2?family=Arima:wght@100..700&family=BBH+Sans+Bogle&family=Momo+Trust+Display&display=swap');            
                </style>
                """, unsafe_allow_html=True)
    st.html(f"""  
        <style>
        * {{
        user-select: none;
        }}
        .momo-trust-display-regular {{
        font-family: "Momo Trust Display", sans-serif;
        font-weight: 400;
        font-style: normal;
        }}
        .bbh-sans-bogle-regular {{
            font-family: "BBH Sans Bogle", sans-serif;
            font-weight: 400;
            font-style: normal;
        }}
        .arima-isi {{
            font-family: "Arima", system-ui;
            font-optical-sizing: auto;
            font-weight: 500;
            font-style: normal;
            line-height: 1.75em;
        }}

        .stApp {{
            background-image: linear-gradient(0deg, #242424, #232324);
            background-position: center top;
            background-attachment: fixed;
            background-size: cover;
            background-repeat: no-repeat;
        }}

        .container-h1 {{
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
        padding: 1px;
        position: relative;
        z-index: 1;
        margin: 0;
        }}
        
        .container-h1::before, .container-h1::after {{
        content: "";
        width: 200px;
        height: 95%;
        position: absolute;
        background-color: #232324;
        z-index: 12;
        filter: blur(.8em);
        }}
        
        .container-h1::after {{
        content: "";
        opacity: 1;
        transform: translate(-200%, 0);
        }}
        .container-h1::before {{
        content: "";
        opacity: 1;
        transform: translate(200%, 0);
        }}
        
        h1 {{
        font-size: 6em;
        letter-spacing: 4px;
        z-index: 10;
        background-image: url(data:image/jpg;base64,{get_base64("assets/missing_texture.png")});
        background-position: left;
        background-size: cover;
        background-repeat: no-repeat;
        padding: 65px .7em;
        text-align: center;
        line-height: 1em;
        border: 4px solid lightblue;
        color: white;
        }}
        
        p {{
            color: white;
        }}
        .container, .container2 {{
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            max-width: 100%;
            margin: 0;
            flex-wrap: wrap;
            height: 100%;
            position: relative;
        }}
        
        .img1 {{
                width: 15em;
                height: 16em;
                z-index: 6;
                border-radius: 10px;
                }}

                .imgcontainer {{
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                position: relative;
                margin: 0 auto;
                border-radius: 10px;
                z-index: 5;
                overflow: hidden;
                padding: 8px;
                }}
                .imgcontainer::after, .imgcontainer::before {{
                content: "";
                width: 150%;
                position: absolute;
                height: 150%;
                background-image: conic-gradient(from 90deg, #ff8080, transparent, transparent,transparent, #809dff, transparent,transparent,transparent, #ff8080);
                z-index: 0;
                padding: 15px;
                border-radius: 10px;
                animation: 6s rotatebg linear infinite;
                }}
                .imgcontainer::before{{
                content: "";
                filter: blur(2em);
                opacity: 0;
                }}
                
        .img2 {{
                width: 15em;
                height: 16em;
                z-index: 6;
                border-radius: 10px;
                }}

                .imgcontainer2 {{
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                position: relative;
                margin: 0 auto;
                border-radius: 10px;
                z-index: 5;
                overflow: hidden;
                padding: 8px;
                }}
                .imgcontainer2::after, .imgcontainer2::before {{
                content: "";
                width: 200%;
                position: absolute;
                height: 200%;
                background-image: conic-gradient(from 0deg, #ffff80, transparent, transparent,transparent, #86ff80, transparent,transparent,transparent, #ffff80);
                z-index: 0;
                padding: 10px;
                border-radius: 10px;
                overflow: hidden;
                animation: 6s rotatebg linear infinite;
                }}
                .imgcontainer2::before{{
                    filter: blur(1em);
                }}

                @keyframes rotatebg {{
                    from {{
                        transform: rotate(0deg);
                    }}
                    to {{
                        transform: rotate(360deg);
                    }}
                }}

        a {{
            text-decoration: none;
            font-weight: bold;
            color: black;
            padding: 0.75em 5em;
            z-index: 5;
            font-size: 1em;
        }}
        
        .linkbtn {{ 
        margin: 1em 1em 1em 1em;
        border-radius: 99px;
        background-color: #66a0bd;
        border: 4px solid #24ADF2;
        padding: 10px 0;
        position: relative;
        overflow: hidden;
        transition: all .5s ease;
        box-sizing: border-box;
        }}
        .linkbtn::before, .linkbtn::after {{
        content: "";
        position: absolute;
        width: 100%;
        height: 120%;
        top: -10%;
        z-index: 0;
        pointer-events: none;
        transition: all .5s ease;
        }}
        .linkbtn::before {{
        left: 110%;
        transform: skewX(-30deg);
        }}
        .linkbtn::after {{
        left: -110%;
        transform: skewX(30deg);
        }}
        .linkbtn:has(a:hover)::before {{
        transform: translateX(-70%) skewX(-45deg);
        transition: all .5s ease .05s;
        background-color: #43de7b;
        }}
        .linkbtn:has(a:hover)::after {{
        transform: translateX(70%) skewX(45deg);
        transition: all .5s ease .05s;
        background-color: #43de7b;
        }}
        .linkbtn:has(a:hover) {{
        border: 4px solid #23a151;
        transition: all .5s ease;
        }}
        
        .after-hover {{
        font-size: 2em;
        display: block;
        background-color: transparent;
        height: 1.5em;
        width: 3em;
        position: absolute;
        left: 35%;
        top: 120%;
        transform: translate(-40% -50%);
        z-index: 6;
        letter-spacing: 0.3rem;
        text-align: center;
        transition: all .2s ease;
        color: black;
        }}
        .linkbtn:has(a:hover) .after-hover {{
        transform: translateY(-120%);
        transition: all .5s ease 0.2s;
        pointer-events: none;
        }}
        
        
        .title {{
            font-size: 2.1em;
            color: white;
            margin-bottom: 15px;
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
                margin: 1.5em;
                }}
        
        .textcontainer {{
        border-radius: 10px;
        border: 3px solid black;
        background-color: #383839;
        margin: 1.25em;
        line-height: 2.25em;
        padding: 10px 10px 0px 10px;
        max-width: 90%;
        }}

        .textcontainernolimit {{
        border-radius: 10px;
        border: 3px solid black;
        background-color: #383839;
        margin: 1.25em;
        line-height: 2.25em;
        padding: 10px 10px 0px 10px;
        max-width: 90%;
        }}
        
        .grand-imgcontainer {{
        text-align: center;
        width: 100%;
        }}
        
        @keyframes colorchange {{
            33% {{ background-color: #91b4eb; }}
            66% {{ background-color: #dae5f7; }}
        }}
        
        @media (min-width: 700px) {{
            .container, .container2 {{
            display: flex;
            align-items: center;
            text-align: center;
            padding: 0;
            justify-content: center;
            margin: 0;
            }}
            .container {{
            float: left;
            flex-wrap: wrap;
            flex-direction: row;
            }}
            .container2 {{
            float: right;
            flex-wrap: wrap;
            flex-direction: row-reverse;
            }}
            
            .imgcontainer {{
            text-align: center;
            float: left;
            }}
            
            .textcontainer {{
            max-width: 50%;
            }}

            .textcontainernolimit {{
            max-width: 100%;
            }}
        }}
        
        @keyframes divider-spin {{
                0% {{ transform: rotate(0deg); }}
                5.88% {{ transform: rotate(0deg); }}
                11.76% {{ transform: rotate(45deg); }}
                17.64% {{ transform: rotate(45deg); }}
                23.52% {{ transform: rotate(90deg); }}
                29.4% {{ transform: rotate(90deg); }}
                35.28% {{ transform: rotate(135deg); }}
                41.16% {{ transform: rotate(135deg); }}
                47.04% {{ transform: rotate(180deg); }}
                52.92% {{ transform: rotate(180deg); }}
                58.8% {{ transform: rotate(225deg); }}
                64.68% {{ transform: rotate(225deg); }}
                70.56% {{ transform: rotate(270deg); }}
                76.44% {{ transform: rotate(270deg); }}
                82.32% {{ transform: rotate(315deg); }}
                88.2% {{ transform: rotate(315deg); }}
                100% {{ transform: rotate(360deg); }}
                }}
            @keyframes bg-divider-scale {{
                0% {{ transform:  scale(1); }}
                5.88% {{ transform:  scale(1); }}
                11.76% {{ transform:  scale(1.25); }}
                17.64% {{ transform:  scale(1.25); }}
                23.52% {{ transform:  scale(1); }}
                29.4% {{ transform:  scale(1); }}
                35.28% {{ transform:  scale(1.25); }}
                41.16% {{ transform:  scale(1.25); }}
                47.04% {{ transform:  scale(1); }}
                52.92% {{ transform:  scale(1); }}
                58.8% {{ transform:  scale(1.25); }}
                64.68% {{ transform:  scale(1.25); }}
                70.56% {{ transform:  scale(1); }}
                76.44% {{ transform:  scale(1); }}
                82.32% {{ transform:  scale(1.25); }}
                88.2% {{ transform: scale(1.25); }}
                94.08% {{ transform: scale(1); }}
                100% {{ transform: scale(1); }}
                }}
        </style>
        
        <div class="container-h1 bbh-sans-bogle-regular">
            <h1>Spelling Bee</h1>
        </div>
        
        <div class="container"> 
            <div class="divider-container">
                <div class="divider"></div>
            </div>
                <div class="imgcontainer">
                    <img class="img1" src="data:images/jpg;base64,{get_base64("assets/missing_texture.png")}">
                </div>
            <div class="textcontainer">
                <div class="title momo-trust-display-regular">Spelling Bee</div>
                <p class="arima-isi">{text1}</p>
            </div>
        </div>

        <div class="container2">   
            <div class="divider-container2">
                <div class="divider"></div>
            </div>
            <div class="textcontainernolimit">
                <div class="title momo-trust-display-regular">Asal-usul Nama</div>
                <p class="arima-isi">{text2}</p>
            </div>
        </div>

        <div class="container2">   
            <div class="divider-container2">
                <div class="divider"></div>
            </div>
            <div class="imgcontainer2">
                <img class="img2" src="data:image/jpg;base64,{get_base64("assets/missing_texture.png")}">
            </div>
            <div class="textcontainer">
                <div class="title momo-trust-display-regular">Sejarah Awal</div>
                <p class="arima-isi">{text3}</p>
            </div>
        </div>

        <div class="container2">   
            <div class="divider-container2">
                <div class="divider"></div>
            </div>
            <div class="textcontainernolimit">
                <div class="title momo-trust-display-regular">Perkembangan Internasional</div>
                <p class="arima-isi">{text4}</p>
            </div>
        </div>

        <div class="container"> 
            <div class="divider-container">
                <div class="divider"></div>
            </div>
                <div class="imgcontainer">
                    <img class="img1" src="data:images/jpg;base64,{get_base64("assets/missing_texture.png")}">
                </div>
            <div class="textcontainer">
                <div class="title momo-trust-display-regular">Tujuan dan Manfaat</div>
                <p class="arima-isi">{text5}</p>
            </div>
        </div>
    """)
