import streamlit as st

st.set_page_config(
    page_title="WhatsApp Chat Analyzer",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 25%, #1a1f35 50%, #0f172a 75%, #1e293b 100%);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        min-height: 100vh;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a 0%, #1a1f35 50%, #0f172a 100%);
        border-right: 1px solid rgba(99, 102, 241, 0.2);
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("📱 Navigation")
home = st.Page("01-home.py", title="Home", icon="🏠")
analyzer = st.Page("02-analyzer.py",title="Analyzer",icon = "🕵️")

pg = st.navigation([home, analyzer])

pg.run()