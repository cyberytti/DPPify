import streamlit as st
import os
import time
from backend.main_agent import DPPify

# Set page config
st.set_page_config(
    page_title="DPPify - Daily Practice Problems Generator",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
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
    
    .feature-box {
        background: #f8f9fa;
        border: 2px solid #e9ecef;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        transition: transform 0.2s;
    }
    
    .feature-box:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    /* Form styling */
    .stSelectbox > div > div {
        border-radius: 10px;
    }
    
    .stTextInput > div > div {
        border-radius: 10px;
    }
    
    .stNumberInput > div > div {
        border-radius: 10px;
    }
    
    /* Footer */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #1f77b4;
        color: white;
        text-align: center;
        padding: 10px 0;
        font-size: 0.9rem;
    }
    
    .github-link {
        color: #ffd700;
        text-decoration: none;
        font-weight: bold;
    }
    
    .github-link:hover {
        color: #ffed4e;
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

def main():
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
        
        # API Key input
        api_key = st.text_input(
            "🔑 Enter your Cerebras API key:", 
            type="password",
            help="Get your API key from Cerebras Cloud Platform"
        )
        
        st.markdown("---")
        
        # Instructions section
        st.markdown('<div class="sidebar-header">📋 How to Use</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: #f8f9fa; padding: 1rem; border-radius: 10px; margin: 1rem 0;">
            <h4 style="color: #495057; margin-top: 0;">Step-by-Step Guide:</h4>
            <ol style="color: #6c757d; line-height: 1.6;">
                <li><b>Get API Key:</b> Sign up at Cerebras Cloud Platform</li>
                <li><b>Enter API Key:</b> Paste it in the field above</li>
                <li><b>Choose Topic:</b> Enter any subject (Math, Physics, etc.)</li>
                <li><b>Configure:</b> Set questions count & difficulty</li>
                <li><b>Generate:</b> Click the magic button!</li>
                <li><b>Download:</b> Get your beautiful PDF</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
        # Features section
        st.markdown("### 🚀 Features")
        features = [
            "🎯 Custom topic selection",
            "📊 Multiple difficulty levels", 
            "📝 Various question types",
            "🎨 Beautiful PDF formatting",
            "⚡ Instant generation",
        ]
        
        for feature in features:
            st.markdown(f"• {feature}")
        
        st.markdown("---")
        
        # Tips section
        st.markdown("### 💡 Pro Tips")
        st.markdown("""
        - **Be Specific**: "Linear Equations" vs "Math"
        - **Start Small**: Try 5-10 questions first
        - **Mix Levels**: Combine Easy & Medium
        - **Save Time**: Bookmark this page!
        """)
    
    # Main content area
    st.markdown("## 🎓 Create Your Practice Problems")
    
    # Input form with better layout
    with st.form("pdf_form", clear_on_submit=False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            topic = st.text_input(
                "📚 Topic Name:", 
                placeholder="e.g., Linear Algebra, Organic Chemistry, Python Programming",
                help="Be as specific as possible for better results"
            )
        
        with col2:
            total_questions = st.number_input(
                "📊 Total Questions", 
                min_value=1, 
                max_value=50, 
                value=10,
                step=1,
                help="Recommended: 5-15 for daily practice"
            )
        
        col3, col4 = st.columns(2)
        
        with col3:
            difficulty = st.selectbox(
                "🎯 Difficulty Level", 
                ["Easy", "Medium", "Hard", "Very Hard"],
                index=1,
                help="Choose based on your current skill level"
            )
        
        
        # Generate button with custom styling
        st.markdown("<br>", unsafe_allow_html=True)
        generate_button = st.form_submit_button(
            "✨ Generate My DPP PDF ✨",
            use_container_width=True
        )
    
    # Processing and results
    if generate_button:
        # Validation
        if not api_key:
            st.error("🔑 Please enter your Cerebras API key in the sidebar")
            st.info("💡 Don't have an API key? Get one from [Cerebras Cloud Platform](https://cloud.cerebras.ai)")
            return
            
        if not topic.strip():
            st.error("📚 Please enter a topic name")
            return
        
        # Processing with enhanced UI
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Step 1: Initialize
            status_text.text("🔄 Initializing DPP Generator...")
            progress_bar.progress(20)
            time.sleep(0.5)
            
            # Step 2: Generate content
            status_text.text("🤖 AI is crafting your questions...")
            progress_bar.progress(60)
            
            # Generate PDF
            pdf_path = DPPify().run(
                topic_name=topic,
                total_q=total_questions,
                level=difficulty,
                api_key=api_key
            )
            
            # Step 3: Creating PDF
            status_text.text("📄 Creating beautiful PDF...")
            progress_bar.progress(90)
            time.sleep(0.5)
            
            # Step 4: Complete
            status_text.text("✅ Your DPP is ready!")
            progress_bar.progress(100)
            
            # Success message with download
            st.success("🎉 Your Daily Practice Problems PDF has been generated successfully!")
            
            # Download section
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                with open(pdf_path, "rb") as f:
                    pdf_bytes = f.read()
                
                st.download_button(
                    label="📥 Download Your DPP PDF",
                    data=pdf_bytes,
                    file_name=f"DPP_{topic.replace(' ', '_')}_{difficulty}.pdf",
                    mime="application/pdf",
                    key="download_pdf",
                    use_container_width=True,
                    on_click=cleanup_file,
                    args=(pdf_path,)
                )
            
            # Additional info
            st.info(f"""
            📋 **Your DPP Details:**
            - **Topic:** {topic}
            - **Questions:** {total_questions}
            - **Difficulty:** {difficulty}  
            - **File:** {os.path.basename(pdf_path)}
            """)
            
            # Clear progress indicators
            time.sleep(2)
            progress_bar.empty()
            status_text.empty()
            
        except FileNotFoundError:
            st.error("❌ PDF file generation failed. Please try again.")
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.info("💡 Try checking your API key or internet connection")

    # Footer
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="footer">
        Made with ❤️ by cyberytti | 
        <a href="https://github.com/cyberytti/DPPify" class="github-link" target="_blank">
            ⭐ Star us on GitHub
        </a> | 
        © 2025 DPPify
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()