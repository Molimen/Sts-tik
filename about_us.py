import streamlit as st
import base64
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()
img1 = get_base64("assets/bg106.jpg")

abt_us_1 = '''A hobbyist who is trying to learn programming!<br>I'm contributing on backend stuff like how the game logic work, etc. also i'm good at C and Python.<br><br>My quote:<br>"I'm gonna find the truth."'''

abt_us_2 = '''Gw ceplox21, alias murid yang namanya cuma sekata itu. Kontribusiku di sini ngerjain bagian <b>Frontend</b> karena aku sendiri dah lumayan paham dan ada pengalaman HTML sama CSS.<br><br>--- Quote kecil ---<br>"Don't be afraid of a rejection, because it's a path to success."'''
def abt_us():
    st.markdown(
        '''
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Arima:wght@100..700&family=BBH+Sans+Bogle&family=Momo+Trust+Display&display=swap');            
        </style>
        ''', unsafe_allow_html=True)
    st.html(
        f"""
        <div class="maincontainer bbh-sans-bogle-regular">
            <div class="container-h1">
                <h1>TENTANG KAMI</h1>
            </div>
            <div class="divider-container">
                <div class="divider"></div>
            </div>  
        </div>
        
        <div class="maincontainer">
                <div class="imagecontainer1">
                    <img src="https://avatars.githubusercontent.com/u/95009791?v=4">
                </div>
                <div class="expandable-info">
                    <div class="desktop-only"><div class="info-title1 momo-trust-display-regular">Hover mouse ke sini!</div></div>
                    <div class="mobile-only"><div class="info-title1 momo-trust-display-regular">Pencet ke sini!</div></div>
                    <div class="info-content arima-isi">{abt_us_1}</div>
                </div>
            <div class="divider-container2">
                <div class="divider"></div>
            </div>
                <div class="imagecontainer2">
                    <img src="https://avatars.githubusercontent.com/u/230108871?v=4">
                </div>
                <div class="expandable-info">
                    <div class="desktop-only"><div class="info-title2 momo-trust-display-regular">Hover mouse ke sini!</div></div>
                    <div class="mobile-only"><div class="info-title2 momo-trust-display-regular">Pencet ke sini!</div></div>
                    <div class="info-content arima-isi">{abt_us_2}</div>
                </div>
        </div>

       <style>
            .grand-container {{
            display: flex;
            }}
            
            .keterangan {{
            max-width: 80%;
            margin: 1.5em;
            }}
            
            .imagecontainer1, .imagecontainer2 {{
            position: relative;
            }}
            .imagecontainer1::before, .imagecontainer2::before {{
            position: absolute;
            background-color: #4858A8;
            padding: .1em .25em;
            border-radius: 5px;
            transform: translate(-50%);
            left: 50%;
            border: 5px solid #6674BD;
            font-weight: bold;
            }}
            .imagecontainer1::before {{
            content: "Molimen (X-6/13)";
            }}
            .imagecontainer2::before {{
            content: "Ceplox21 (X-6/18)";
            }}
            .imagecontainer1 img, .imagecontainer2 img {{
            box-sizing: border-box;
            margin: 1em 1em 2.1em 1em;
            height: 9.25em;
            aspect-ratio: 16:9;
            border: 5px solid #6674BD;
            border-radius: 1.25em 0em 2.65em 0em;
            }}
            
            .info-content {{
            margin: 1.25em;
            font-size: 1em;
            }}
            
            .info-title1::after {{
            content: "Info Tentang Molimen";
            }}
            .info-title2::after {{
            content: "Info Tentang Ceplox21";
            }}
            .info-title1::after, .info-title2::after {{
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: row;    
            background-color: #D38D2C;
            height: 105%;
            width: 0%;
            z-index: 3;
            top: 50%;
            left: -40%;
            transform: translate(0%, -50%);
            position: absolute;
            transition: all .9s ease;
            overflow: hidden;
            white-space: nowrap;
            font-size: 1.38rem;
            
            }}
            .expandable-info:hover .info-title1::after, .expandable-info:hover .info-title2::after {{
            width: 180%;
            transition: all .9s ease;
            }}
            
            .expandable-info {{
            display: flex;
            flex-direction: column;
            height: 3em;
            width: 80%;
            background-color: #353536;
            max-width: 90%;
            margin-bottom: 2em;
            border-radius: .5rem;
            transition: all .35s ease;
            border: 0.2rem solid #24ADF2;
            overflow: hidden;
            }}
            .expandable-info:hover {{
            height: 20em;
            transition: all .35s ease-out;
            border: 0.2rem solid #996620;
            }}
            
            .expandable-info .info-title1, .expandable-info .info-title2 {{
            padding: .18em;
            font-size: 1.42em;
            background-color: #66a0bd;
            transition: all .5s ease-out;
            position: relative;
            }}
            
            .stApp {{
            background-color: #232324;
            background-position: center top;
            background-attachment: fixed;
            background-size: cover;
            background-repeat: no-repeat;
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
            
            .maincontainer, .maincontainer2 {{
            color: white;
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            }}
            
            .container-h1 {{
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            width: 90%;
            padding: 1px;
            position: relative;
            z-index: 1;
            }}
            
            .container-h1::before, .container-h1::after {{
            content: "";
            width: 200px;
            height: 100%;
            position: absolute;
            background-color: #232324;
            z-index: 12;
            filter: blur(.8em);
            }}
            
            .container-h1::after {{
            content: "";
            opacity: 1;
            transform: translate(-127%, 0);
            }}
            .container-h1::before {{
            content: "";
            opacity: 1;
            transform: translate(127%, 0);
            }}
            
            h1 {{
            font-size: 5em;
            letter-spacing: 4px;
            z-index: 10;
            background-image: url(data:image/jpg;base64,{img1});
            background-position: top center;
            background-size: cover;
            background-repeat: no-repeat;
            padding: 25px 135px;
            text-align: center;
            line-height: 1em;
            border: 4px solid lightblue;
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
            
            body {{
            user-select: none;
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
            
            @media (max-width: 700px) {{
                .info-content {{
                font-size: 0.85em;
                margin: .95em;
                }}
                .info-title1::after, .info-title2::after {{
                font-size: 0.85em;
                }}
            }}

            @media (max-width: 768px) {{
                .mobile-only {{display: block;}}
                .desktop-only {{display: none;}}
            }}
            @media (min-width: 769px) {{
                .mobile-only {{display: none;}}
                .desktop-only {{display: block;}}
            }}
        </style>
        """)
