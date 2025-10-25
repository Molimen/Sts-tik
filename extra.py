import streamlit as st
import base64

def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

ekstra1 = get_base64("sts_tik_extra_img1.jpg")

def extra_menu():
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
            background-image: linear-gradient(0deg, #242424, #3d3d3d);
            background-position: center top;
            background-attachment: fixed;
            background-size: cover;
            background-repeat: no-repeat;
        }}

        h1 {{
            color: white;
            font-size: 3em;
        }}
        p {{
            color: white;
        }}
        .container {{
            text-align: center;
            margin: auto;
        }}

        img {{
            width: 175px;
            box-sizing: border-box;
            padding: 6px;
            border-radius: 12px;
            animation: glow 2s ease infinite;
        }}
        .img1 {{
            background-image: linear-gradient(120deg,#23c902, #db221f, #49dbde, #fcba03);
            animation-delay: 0.33s;
        }}
        .img2 {{
            background-image: linear-gradient(188deg,#1f4edb, #db451f, #b2db1f, #db1f74);
            animation-delay: 0.95s;
        }}

        /* === LINKS === */
        .link1, .link2 {{
            border-radius: 50px;
            border: 3px solid black;
            background-color: white;
            padding: 10px;
            display: inline-block;
            width: 250px;
            animation: colorchange 5s linear infinite;
        }}
        .link1 {{ color: green; }}
        .link2 {{
            color: white;
            animation-delay: 0.45s;
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

        @keyframes glow {{
            25% {{ box-shadow: 0px 0px 40px #4b68eb; }}
            50% {{ box-shadow: 0px 0px 40px yellow; }}
            75% {{ box-shadow: 0px 0px 40px #a655ed; }}
        }}
        @keyframes colorchange {{
            33% {{ background-color: #355fe8; }}
            66% {{ background-color: white; }}
        }}
        </style>

        <div class="container">
            <h1 class="bbh-sans-bogle-regular">EKSTRA</h1>
            <hr style="background-color: white; margin:25px;">

            <img class="img1" src="data:image/jpg;base64,{ekstra1}">
            <div class="title exo-2-namaprojek">Tempat Duduk Generator</div>
            <p class="arima-isi">Lorem ipsum dolor sit amet, consectetur adipisicing elit. A alias consequatur doloremque doloribus illo ipsam minus quae repudiandae. Amet consequatur deleniti eum inventore, laudantium neque quis quod repellendus soluta veniam.</p>
            <span class="link1"><a href="https://layout-tempat-duduk-generator.streamlit.app/" target="_blank">Kunjungi situsnya</a></span>

            <hr style="background-color: white; margin:25px;">

            <img class="img2" src="data:image/jpg;base64,{ekstra1}">
            <div class="title exo-2-namaprojek">Kelompok Generator</div>
            <p class="arima-isi">Lorem ipsum dolor sit amet, consectetur adipisicing elit. A alias consequatur doloremque doloribus illo ipsam minus quae repudiandae. Amet consequatur deleniti eum inventore, laudantium neque quis quod repellendus soluta veniam.</p>
            <span class="link2"><a href="https://kelompok.streamlit.app/" target="_blank">Kunjungi situsnya</a></span>
        </div>
    """)