import streamlit as st
st.markdown("""
<style>
[data-testid="stToolbar"] {display: none !important;}
</style>
""", unsafe_allow_html=True)

hide_streamlit_elements = """
    <style>
    /* Hide the main hamburger menu */
    #MainMenu {visibility: hidden !important;}
    
    /* Hide the toolbar (new in recent versions) */
    .stToolbar {display: none !important;}
    
    /* Hide Deploy button */
    .stDeployButton {display: none !important;}
    
    /* Hide header bar */
    header {visibility: hidden !important;}
    
    /* Hide footer ("Made with Streamlit") */
    footer {visibility: hidden !important;}
    
    /* Extra safety for any new elements */
    [data-testid="stToolbar"] {display: none !important;}
    [data-testid="manage-app-button"] {display: none !important;}
    </style>
"""
st.markdown(hide_streamlit_elements, unsafe_allow_html=True)

# Optional: make the page look even cleaner


st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
from ui_components import ui_card
st.markdown("""
    <style>
        /* --------------------------------------------------
           GLOBAL APP THEME
           -------------------------------------------------- */
        .stApp {
            background: linear-gradient(139deg, #f6fff8, #e8f5e9);
            color: #1b5e20;
            font-family: "Segoe UI", "Roboto", sans-serif;
        }

        /* Main content container - limit max width and center on large screens */
        .main .block-container {
            max-width: 1200px;
            padding-left: 2rem;
            padding-right: 2rem;
            margin: 0 auto;
        }

        /* --------------------------------------------------
           HEADINGS
           -------------------------------------------------- */
        h1, h2, h3, h4, h5, h6 {
            text-align: center;
            color: #1b5e20 !important;
            font-weight: 700;
        }

        /* --------------------------------------------------
           BUTTON STYLING
           -------------------------------------------------- */
        .stButton > button {
            width: 100%;
            border-radius: 14px;
            background: linear-gradient(135deg, #2e7d32, #66bb6a);
            color: white !important;
            font-size: 18px;
            font-weight: 600;
            padding: 0.75em;
            border: none;
            transition: all 0.2s ease-in-out;
        }

        .stButton > button:hover {
            background: linear-gradient(135deg, #388e3c, #81c784);
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
            transform: translateY(-1px);
        }

        .stButton > button:active {
            background: linear-gradient(135deg, #1b5e20, #43a047) !important;
            transform: scale(0.97);
        }

        button[disabled] {
            background: linear-gradient(135deg, #1b5e20, #66bb6a) !important;
            opacity: 0.75;
            cursor: wait;
        }

        /* --------------------------------------------------
           FILE UPLOADER
           -------------------------------------------------- */
        [data-testid="stFileUploader"] {
            border: 2px dashed #2e7d32;
            border-radius: 16px;
            padding: 1em;
            background-color: #f1f8e9;
            width: 100%;
        }

        /* --------------------------------------------------
           IMAGES
           -------------------------------------------------- */
        img {
            border-radius: 16px;
            max-width: 100%;
            height: auto;
            display: block;
            margin: 0 auto;
        }

        /* --------------------------------------------------
           CARD UI
           -------------------------------------------------- */
        .card {
            background: white;
            border-radius: 18px;
            padding: 20px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.08);
            margin-bottom: 22px;
            color: #1b5e20;
        }

        /* --------------------------------------------------
           FOOTER
           -------------------------------------------------- */
        .footer {
            text-align: center;
            font-size: 13px;
            color: #2e7d32 !important;
            margin-top: 30px;
        }

        /* --------------------------------------------------
           MOBILE & TABLET RESPONSIVENESS
           -------------------------------------------------- */
        @media (max-width: 1024px) { /* Tablets and smaller */
            .main .block-container {
                padding-left: 1.5rem;
                padding-right: 1.5rem;
            }
            
            h1 { font-size: 42px !important; }
            h2 { font-size: 28px !important; }
            
            .stButton > button {
                font-size: 17px;
                padding: 0.7em;
            }
        }

        @media (max-width: 768px) { /* Mobile phones */
            .main .block-container {
                max-width: 100%;
                padding-left: 1rem;
                padding-right: 1rem;
            }
            
            h1 { font-size: 32px !important; }
            h2 { font-size: 26px !important; }
            h3 { font-size: 22px !important; }
            
            .stButton > button {
                font-size: 16px;
                padding: 0.65em;
            }
            
            [data-testid="stFileUploader"] {
                padding: 0.8em;
            }
            
            .card {
                padding: 16px;
            }
        }

        @media (max-width: 480px) { /* Small phones */
            h1 { font-size: 28px !important; }
            .stButton > button {
                font-size: 15px;
            }
        }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Workflow – INSECTIFICA", page_icon="🧠")

ui_card(
    "🧠 How Insectifica Works",
    """
    <b>📸 Step 1: Snap or Upload a Photo</b><br>
    Capture a clear image of the insect or pest.<br><br>

    <b>🤖 Step 2: AI-Powered Analysis</b><br>
    The model analyzes:
    <ul>
        <li>Body shape & size</li>
        <li>Color patterns</li>
        <li>Wing structure</li>
        <li>Antennae & legs</li>
    </ul>

    <b>🐞 Step 3: Identification & Insights</b><br>
    Provides:
    <ul>
        <li>Common & Scientific Name</li>
        <li>Taxonomy</li>
        <li>Habitat & Behaviour</li>
        <li>Pest / Beneficial status</li>
    </ul>
    """
)

st.info("💡 Tip: Ensure the insect is clearly visible and well-lit.")
