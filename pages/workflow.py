import streamlit as st
from ui_components import ui_card

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
