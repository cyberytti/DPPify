import streamlit as st
import os
import time
from backend.main_agent import DPPify


# --- PAGE CONFIGURATION (MUST BE THE FIRST STREAMLIT COMMAND) ---
st.set_page_config(
    page_title="DPPify - AI Problem Generator",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- SESSION STATE INITIALIZATION ---
# This is the core of the logic. We initialize a state variable.
if 'app_started' not in st.session_state:
    st.session_state.app_started = False

# --- FUNCTION FOR THE DESCRIPTION PAGE ---
def description_page():
    """
    Displays the initial dark-themed welcome page.
    """
    # Custom CSS for the dark welcome page
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

        .welcome-container {
            background: linear-gradient(135deg, #1e1e1e 0%, #121212 100%);
            color: #E0E0E0;
            padding: 4rem 2rem;
            border-radius: 15px;
            text-align: center;
            font-family: 'Roboto', sans-serif;
            border: 1px solid #333;
        }
        .welcome-title {
            font-size: 3.5rem;
            font-weight: 700;
            color: #FFFFFF;
            margin-bottom: 1rem;
        }
        .welcome-subtitle {
            font-size: 1.5rem;
            color: #a0a0a0;
            margin-bottom: 2.5rem;
            font-weight: 300;
        }
        .welcome-text {
            font-size: 1.1rem;
            line-height: 1.8;
            max-width: 800px;
            margin: 0 auto 2.5rem auto;
            text-align: left;
        }
        .launch-button-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
    """, unsafe_allow_html=True)

    # Page content
    st.markdown(
        """
        <div class="welcome-container">
            <div class="welcome-title">📚 Welcome to DPPify</div>
            <div class="welcome-subtitle">Your Personal AI-Powered Daily Practice Problem Generator</div>
            <div class="welcome-text">
                <p>DPPify is designed to help students and learners generate custom practice problem sets on any topic, instantly. Whether you're preparing for an exam or just want to sharpen your skills, DPPify has you covered.</p>
                <b>Key Features:</b>
                <ul>
                    <li><b>Any Topic:</b> From "Quantum Physics" to "Python List Comprehensions".</li>
                    <li><b>Custom Difficulty:</b> Choose from Easy, Medium, Hard, or Very Hard levels.</li>
                    <li><b>Instant PDF:</b> Get a beautifully formatted PDF, ready for printing or digital use.</li>
                    <li><b>Powered by AI:</b> Leverages advanced language models to create relevant and challenging questions.</li>
                </ul>
                <p style="text-align:center; margin-top: 2rem;"><b>Ready to get started? Click the button below!</b></p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Centered launch button
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        if st.button("🚀 continue", use_container_width=True, type="primary"):
            st.session_state.app_started = True
            st.rerun()


# --- FUNCTION FOR THE MAIN APPLICATION (YOUR CODE) ---
def main_application():
    """
    This function contains the entire code for your main DPPify app.
    """
    # Custom CSS for better styling (from your original code)
    st.markdown("""
    <style>
        /* Main title styling */
        .main-title {
            text-align: center;
            color: #1f77b4;
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        .subtitle {
            text-align: center;
            color: #666;
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }
        /* Sidebar styling */
        .sidebar-header {
            color: #1f77b4;
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        /* Info boxes */
        .info-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem;
            border-radius: 10px;
            color: white;
            margin: 1rem 0;
        }
        /* Button styling */
        .stButton > button {
            border-radius: 25px;
            padding: 0.5rem 2rem;
            font-weight: bold;
            transition: all 0.3s;
        }
        /* Footer */
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            color: #333;
            text-align: center;
            padding: 10px 0;
            font-size: 0.9rem;
        }
        .github-link {
            color: #1f77b4;
            text-decoration: none;
            font-weight: bold;
        }
    </style>
    """, unsafe_allow_html=True)

    def cleanup_file(file_path):
        """Remove the generated file after download"""
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            st.error(f"Error cleaning up file: {e}")

    # Header section
    st.markdown('<h1 class="main-title">📚 DPPify</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">AI-Powered Daily Practice Problems Generator</p>', unsafe_allow_html=True)

    # Project info and GitHub link
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="info-box">
            <center>
                <h3>🌟 Love this project? Give us a star! 🌟</h3>
                <p>Visit our GitHub repository and show your support</p>
                <a href="https://github.com/cyberytti/DPPify" target="_blank" 
                   style="color: #ffd700; text-decoration: none; font-size: 1.1rem; font-weight: bold;">
                   🔗 GitHub Repository - Leave a ⭐
                </a>
            </center>
        </div>
        """, unsafe_allow_html=True)

    # Sidebar configuration
    with st.sidebar:
        st.markdown('<div class="sidebar-header">⚙️ Configuration</div>', unsafe_allow_html=True)
        api_key = st.text_input("🔑 Enter your Cerebras API key:", type="password", help="Get your API key from Cerebras Cloud Platform")
        st.markdown("---")
        st.markdown('<div class="sidebar-header">📋 How to Use</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="background: #f8f9fa; padding: 1rem; border-radius: 10px; margin: 1rem 0;">
            <h4 style="color: #495057; margin-top: 0;">Step-by-Step Guide:</h4>
            <ol style="color: #6c757d; line-height: 1.6;">
                <li><b>Enter API Key:</b> Paste it in the field above</li>
                <li><b>Choose Topic:</b> Enter any subject (Math, Physics, etc.)</li>
                <li><b>Configure:</b> Set questions count & difficulty</li>
                <li><b>Generate:</b> Click the magic button!</li>
                <li><b>Download:</b> Get your beautiful PDF</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
        # Button to go back to the welcome page
        st.markdown("---")
        if st.button("⬅️ Go Back to Welcome Page"):
            st.session_state.app_started = False
            st.rerun()

    # Main content area
    st.markdown("## 🎓 Create Your Practice Problems")
    with st.form("pdf_form", clear_on_submit=False):
        col1, col2 = st.columns([2, 1])
        with col1:
            topic = st.text_input("📚 Topic Name:", placeholder="e.g., Linear Algebra, Organic Chemistry", help="Be as specific as possible for better results")
        with col2:
            total_questions = st.number_input("📊 Total Questions", min_value=1, max_value=200, value=10, step=1, help="Recommended: 5-15 for daily practice")
        col3, col4 = st.columns(2)
        with col3:
            difficulty = st.selectbox("🎯 Difficulty Level", ["Easy", "Medium", "Hard", "Very Hard"], index=1, help="Choose based on your current skill level")
        with col4:
            question_type = st.selectbox("🎯 Question Type", ["Only MCQ", "Only SAQ", "BOTH"], index=2, help="Choose the question type")
        col5,col6 = st.columns(2)
        with col5:
            dpp_language = st.selectbox("Dpp language", ["English", "Bengali", "Hindi"], index=0, help="Choose the dpp language")

        st.markdown("<br>", unsafe_allow_html=True)
        generate_button = st.form_submit_button("✨ Generate My DPP PDF ✨", use_container_width=True, type="primary")

    if generate_button:
        if not api_key:
            st.error("🔑 Please enter your Cerebras API key in the sidebar")
            return
        if not topic.strip():
            st.error("📚 Please enter a topic name")
            return
        
        progress_bar = st.progress(0, text="🔄 Initializing DPP Generator...")
        try:
            progress_bar.progress(20, text="🤖 AI is crafting your questions...")
            pdf_path = DPPify().run(
                topic_name=topic, 
                total_q=total_questions, 
                level=difficulty, 
                api_key=api_key,
                question_type=question_type,
                dpp_language=dpp_language
            )
            progress_bar.progress(90, text="📄 Creating beautiful PDF...")
            time.sleep(1)
            
            progress_bar.progress(100, text="✅ Your DPP is ready!")
            st.success("🎉 Your Daily Practice Problems PDF has been generated successfully!")
            
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="📥 Download Your DPP PDF",
                    data=f.read(),
                    file_name=os.path.basename(pdf_path),
                    mime="application/pdf",
                    key="download_pdf",
                    use_container_width=True,
                    on_click=cleanup_file,
                    args=(pdf_path,)
                )
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            progress_bar.empty()

    # Footer
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="footer">
        Made with ❤️ by cyberytti | 
        <a href="https://github.com/cyberytti/DPPify" class="github-link" target="_blank">
            ⭐ Star us on GitHub
        </a>
    </div>
    """, unsafe_allow_html=True)


# --- MAIN ROUTER ---
# This checks the state and decides which page to show.
if st.session_state.app_started:
    main_application()
else:
    description_page()
