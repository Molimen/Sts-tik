import streamlit as st
import time

spelling_bee_words = [
    # Easy 🍎
    "apple", "banana", "orange", "grape", "table", "chair", "window", "garden", "river", "school",
    "music", "happy", "friend", "family", "ocean", "mountain", "forest", "animal", "summer", "winter",
    "teacher", "computer", "flower", "planet", "light", "shadow", "rain", "cloud", "dream", "story",

    # Medium 🌟
    "bicycle", "elephant", "library", "umbrella", "chocolate", "whisper", "journey", "mystery", "adventure", "fantasy",
    "puzzle", "courage", "energy", "festival", "galaxy", "gravity", "language", "memory", "moment", "parallel",
    "rhythm", "silence", "trophy", "village", "voyage", "wonderful", "balance", "discovery", "horizon", "imagination",

    # Hard 🔥
    "phenomenon", "ambiguous", "onomatopoeia", "entrepreneur", "acquaintance", "benevolent", "miscellaneous",
    "superfluous", "conscientious", "magnificent", "nostalgia", "quarantine", "silhouette", "symphony", "vocabulary",
    "catastrophe", "consequence", "hypothesis", "perception", "persuasion", "renaissance", "subconscious",
    "synchronous", "transcend", "vulnerability", "xenophobia", "dichotomy", "aesthetic", "charisma", "dilemma", "eloquent",

    # Very Hard 👑
    "pneumonoultramicroscopicsilicovolcanoconiosis", "floccinaucinihilipilification", "antidisestablishmentarianism",
    "sesquipedalian", "xylophonist", "schadenfreude", "hippopotomonstrosesquipedaliophobia", "juxtaposition", "zephyr",
    "synecdoche", "ubiquitous", "pulchritudinous", "lugubrious", "perspicacious", "idiosyncrasy", "circumlocution",
    "paradigm", "euphemism", "quintessential", "metamorphosis", "pseudonym", "mnemonic", "cacophony", "vicissitude",
    "cryptocurrency", "lachrymose", "philanthropy", "soliloquy", "anachronism", "sagacious", "verisimilitude",
    "labyrinthine", "bildungsroman"
]
#hmtl
st.markdown("""
            <h3>Spelling Bee Minigame</h3>
            """)
#css
st.markdown("""
            <style>
            </style>
            """)