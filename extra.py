import streamlit as st
import base64

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

ekstra1 = get_base64("sts_tik_extra_img1.jpg")
ekstra2 = get_base64("sts_tik_extra_img2.jpg")
ekstra3 = get_base64("bg106.jpg")
st.markdown("""
            <style>
            @import url('https://fonts.googleapis.com/css2?family=Arima:wght@100..700&family=BBH+Sans+Bogle&family=Exo+2:ital,wght@0,100..900;1,100..900&display=swap');
            </style>
            """, unsafe_allow_html=True)
st.html(f"""  
    <style>
    .exo-2-namaprojek {{
        font-family: "Exo 2", sans-serif;
        font-optical-sizing: auto;
        font-weight: 500;
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
    }}

    .stApp {{
        background-image: linear-gradient(0deg, #242424, #232324);
        background-position: center top;
        background-attachment: fixed;
        background-size: cover;
        background-repeat: no-repeat;
    }}

    h1 {{
        color: white;
        font-size: 7em;
        margin: 0;
        background-image: url(data:image/jpg;base64,{ekstra3});
        background-clip: text;
        background-position: center;
        object-fit: cover;
    }}
    p {{
        color: white;
    }}
    .container {{
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
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
            width: 200%;
            position: absolute;
            height: 200%;
            background-image: conic-gradient(from 90deg, #ff8080, transparent, transparent,transparent, #809dff, transparent,transparent,transparent, #ff8080);
            z-index: 0;
            padding: 10px;
            border-radius: 10px;
            overflow: hidden;
            animation: 8s rotatebg linear infinite;
            }}
            .imgcontainer::before{{
                filter: blur(1em);
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
            animation: 8s rotatebg linear infinite;
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
    
    .link1, .link2 {{
        border-radius: 50px;
        border: 3px solid black;
        background-color: white;
        padding: 10px;
        display: inline-block;
        width: 250px;
        animation: colorchange 5s linear infinite;
    }}
    
    .link1 {{ 
    color: white;
    margin-bottom: 20px;
    transition: all 1s ease; 
    }}
    .link1:hover {{
    box-shadow: 0px 0px 20px #80dbff;
    transition: all 1s ease;
    }}
    .link2 {{
        color: white;
        animation-delay: 0.2s;
        transition: all 1s ease;
    }}
    .link2:hover {{
    box-shadow: 0px 0px 20px #80dbff;
    transition: all 1s ease;
    }}
    a {{
        text-decoration: none;
        font-weight: bold;
        background-image: linear-gradient(90deg, black, #525252);
        background-clip: text;
        color: transparent;
    }}
    
    .title {{
        font-size: 2.1em;
        color: white;
    }}
    
    .divider {{
    height: 0.1rem;
    width: 100%;
    background-image: linear-gradient(90deg, transparent, grey, transparent);
    margin: 20px;
    margin-top: 5px;
    }}
    
    .textcontainer {{
    border-radius: 10px;
    border: 3px solid black;
    background-color: #454545;
    margin: 1.25em;
    }}
    
    .costum-mark {{
    opacity: 1;
    color: white;
    border-radius: 5px;
    background-color: #4b5c70;
    padding: 0px 4px 0px 4px;
    }}
    
    @keyframes colorchange {{
        33% {{ background-color: #91b4eb; }}
        66% {{ background-color: #dae5f7; }}
    }}
    </style>

    <div class="container">
        <h1 class="bbh-sans-bogle-regular">EKSTRA</h1>
        <div class="divider"></div>
        <div class="imgcontainer">
            <img class="img1" src="data:images/jpg;base64,{ekstra1}">
        </div>
        <div class="textcontainer">
            <div class="title exo-2-namaprojek">Tempat Duduk Generator</div>
            <p class="arima-isi">Ini program yang bisa dipake untuk <mark class="costum-mark">ngatur tempat duduk secara otomatis</mark> dengan cowo-cewe selang-seling. Untuk sekarang ini cuma bisa untuk kelas 10, soalnya gw ga ada database buat kelas 11 ama 12.</p>
        </div>
        <span class="link1"><a href="https://layout-tempat-duduk-generator.streamlit.app/" target="_blank">Kunjungi situsnya</a></span>
        <div class="divider"></div>
        <div class="imgcontainer2">
            <img class="img2" src="data:image/jpg;base64,{ekstra2}">
        </div>
        <div class="textcontainer">
            <div class="title exo-2-namaprojek">Kelompok Generator</div>
            <p class="arima-isi">Program yang bisa mbuat kelompok, tapi fitur <mark class='costum-mark'>jumlah cowo sama cewe tiap kelompok dibagi sama rata secara otomatis</mark> ini bikin unik. Ini juga cuma bisa untuk kelas 10 dulu. </p>
        </div>
        <span class="link2"><a href="https://kelompok.streamlit.app/" target="_blank">Kunjungi situsnya</a></span>
    </div>
    
""")
