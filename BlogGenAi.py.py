import streamlit as st
import time

# Configure the page
st.set_page_config(
    page_title="BlogGen - AI Blog Generator",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark mode, navbar, and improved layout with no blank blocks
st.markdown("""
<style>
    /* Base Dark Theme */
    .main {
        background-color: #0f1117;
        color: #e0e0e0;
        padding: 0 !important;
        margin: 0 !important;
    }
    .stApp {
        font-family: 'Inter', sans-serif;
    }
    
    /* Custom Navbar */
    .navbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: linear-gradient(90deg, #1a1a2e, #16213e);
        padding: 1rem 2rem;
        border-bottom: 1px solid #30336b;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
    .nav-logo {
        display: flex;
        align-items: center;
        gap: 0.8rem;
    }
    .nav-logo h1 {
        margin: 0;
        font-size: 1.8rem;
        background: linear-gradient(90deg, #00b0ff, #9c27b0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
   # /* Content Containers */
    .content-box {
        background-color: #1a1a2e;
        border-radius: 8px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        border: 1px solid #30336b;
    }
    
    /* Form Elements */
    input, select, textarea, .stTextInput > div > div > input {
        background-color: #232741 !important;
        color: #e0e0e0 !important;
        border: 1px solid #30336b !important;
        border-radius: 5px !important;
    }
    .stTextInput > div > div > input::placeholder {
        color: #8e8e8e !important;
    }
    .stSelectbox > div > div > div {
        background-color: #232741 !important;
        color: #e0e0e0 !important;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(90deg, #0072ff, #00c6ff);
        color: white;
        border-radius: 5px;
        border: none;
        padding: 0.5rem 1.2rem;
        font-weight: 500;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #0088ff, #00d0ff);
        box-shadow: 0 0 15px rgba(0, 114, 255, 0.5);
        transform: translateY(-2px);
    }
    
    /* Result Box */
    .result-box {
        border-left: 4px solid #00c6ff;
        background-color: #232741;
        padding: 1.2rem;
        margin: 1.2rem 0;
        border-radius: 0 8px 8px 0;
    }
    
    /* Tabs Styling */
    .stTabs {
        background-color: #1a1a2e;
        border-radius: 8px;
        padding: 1rem;
        border: 1px solid #30336b;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        background-color: #232741;
        border-radius: 8px;
        padding: 5px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 5px;
        color: #e0e0e0 !important;
        padding: 8px 16px;
        margin: 0 2px;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #0072ff, #00c6ff);
        color: white !important;
    }
    
    /* Settings Panel */
    .settings-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
        margin-bottom: 1.5rem;
    }
    .settings-section {
        background-color: #232741;
        border-radius: 8px;
        padding: 1.2rem;
        border: 1px solid #30336b;
    }
    .settings-heading {
        font-size: 1.2rem;
        margin-bottom: 1rem;
        color: #00c6ff;
        border-bottom: 1px solid #30336b;
        padding-bottom: 0.5rem;
    }
    
    /* Metrics Display */
    .metrics {
        display: flex;
        justify-content: space-between;
        margin-bottom: 1.2rem;
    }
    .metric-item {
        text-align: center;
        padding: 1rem;
        background-color: #232741;
        border-radius: 8px;
        flex: 1;
        margin: 0 0.5rem;
        border: 1px solid #30336b;
    }
    .metric-item:first-child {
        margin-left: 0;
    }
    .metric-item:last-child {
        margin-right: 0;
    }
    .metric-value {
        font-weight: bold;
        font-size: 1.3rem;
        color: #00c6ff;
    }
    
    /* History Items */
    .history-item {
        background-color: #232741;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
        border: 1px solid #30336b;
        transition: all 0.2s ease;
    }
    .history-item:hover {
        transform: translateX(5px);
        border-left: 3px solid #00c6ff;
    }
    .history-actions {
        display: flex;
        gap: 0.8rem;
        margin-top: 0.5rem;
    }
    .history-action {
        background-color: #1a1a2e;
        color: #e0e0e0;
        padding: 0.3rem 0.8rem;
        border-radius: 4px;
        font-size: 0.8rem;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    .history-action:hover {
        background-color: #30336b;
    }
    
    /* Switch Toggle */
    .switch-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 1rem;
    }
    .switch {
        position: relative;
        display: inline-block;
        width: 50px;
        height: 24px;
    }
    .switch input {
        opacity: 0;
        width: 0;
        height: 0;
    }
    .slider {
        position: absolute;
        cursor: pointer;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: #1a1a2e;
        transition: .4s;
        border-radius: 24px;
        border: 1px solid #30336b;
    }
    .slider:before {
        position: absolute;
        content: "";
        height: 16px;
        width: 16px;
        left: 4px;
        bottom: 3px;
        background-color: #e0e0e0;
        transition: .4s;
        border-radius: 50%;
    }
    input:checked + .slider {
        background: linear-gradient(90deg, #0072ff, #00c6ff);
    }
    input:checked + .slider:before {
        transform: translateX(26px);
    }
    
    /* Progress Bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #0072ff, #00c6ff);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 1.5rem;
        background-color: #1a1a2e;
        border-top: 1px solid #30336b;
        margin-top: 2rem;
    }
    
    /* Remove default paddings causing blank spaces */
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100% !important;
    }
    section[data-testid="stSidebar"] > div {
        background-color: #1a1a2e;
        padding-top: 2rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    
    /* Remove extra whitespace */
    .stMarkdown {
        margin-bottom: 0 !important;
    }
    .css-18e3th9 {
        padding: 0 !important;
    }
    .css-1d391kg {
        padding: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# Function to simulate AI blog generation
def generate_blog(topic, tone, length, keywords):
    # Simulate API call to AI service
    progress_bar = st.progress(0)
    
    # Simulate processing with colorful progress
    for i in range(1, 101):
        progress_bar.progress(i/100)
        time.sleep(0.02)
    
    # Ensure we have at least 3 keywords to prevent index errors
    while len(keywords) < 3:
        keywords.append(topic)  # Use the topic as a fallback keyword
    
    # Sample blog post generation - would be replaced with actual AI API call
    blog_title = f"The Ultimate Guide to {topic.title()}"
    
    paragraphs = [
        f"In today's fast-paced digital landscape, understanding {topic} has become crucial for success. This comprehensive guide explores the essential aspects and provides actionable insights you won't find elsewhere.",
        
        f"When approaching {topic}, it's vital to consider multiple perspectives. Industry leaders consistently emphasize the importance of integrating {keywords[0]} into their strategic framework, creating a foundation for sustainable growth.",
        
        f"Recent innovations in {topic} have introduced revolutionary methodologies centered around {keywords[1]}. These cutting-edge approaches have fundamentally transformed implementation strategies, opening new possibilities for those willing to adapt.",
        
        f"The synergy between {keywords[0]} and {keywords[2]} cannot be overstated. Extensive research indicates that effectively leveraging both concepts leads to significantly improved outcomes and competitive advantage in today's market.",
        
        f"Looking toward the horizon, the future of {topic} appears incredibly promising. By focusing on {keywords[1]} and its practical applications, you can position yourself at the forefront of industry trends and capitalize on emerging opportunities."
    ]
    
    # Adjust length
    if length == "Short":
        paragraphs = paragraphs[:2]
    elif length == "Medium":
        paragraphs = paragraphs[:4]
    
    # Adjust tone
    tone_adjustments = {
        "Professional": f"This analysis is based on comprehensive research and established {topic} industry best practices, providing you with reliable, actionable insights.",
        "Casual": f"Let's dive into {topic} together! There's so much to explore and I'm excited to share these ideas with you in a way that's easy to understand and implement.",
        "Humorous": f"Who knew that {topic} could be this entertaining? Buckle up for a wild ride through some seriously important concepts with a not-so-serious delivery!",
        "Persuasive": f"You simply cannot afford to ignore these critical {topic} insights if you truly want to excel. Your competitors are already implementing these strategies – can you afford to fall behind?"
    }
    
    paragraphs.append(tone_adjustments[tone])
    
    return {
        "title": blog_title,
        "content": "\n\n".join(paragraphs),
        "reading_time": f"{len(paragraphs) * 2} min",
        "word_count": len(" ".join(paragraphs).split())
    }

# Custom Navbar (simplified without buttons)
st.markdown("""
<div class="navbar">
    <div class="nav-logo">
        <span style="font-size: 2rem;">✨</span>
        <h1>MiniBlog AI</h1>
    </div>
</div>
""", unsafe_allow_html=True)

# Redesigned tab interface
tabs = st.tabs(["✍️ Create Content", "📚 My Library", "⚙️ Settings"])

with tabs[0]:
    # Left column for form, right column for result
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("<div class='content-box'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #00c6ff; margin-bottom: 1.2rem;'>Generate New Content</h3>", unsafe_allow_html=True)
        
        topic = st.text_input("Blog Topic", placeholder="e.g., Digital Marketing, AI Technology")
        
        tone = st.selectbox("Content Tone", ["Professional", "Casual", "Humorous", "Persuasive"])
        length = st.selectbox("Content Length", ["Short", "Medium", "Long"])
        
        keywords = st.text_input("Keywords (comma separated)", placeholder="e.g., SEO, content, strategy")
        
        # Options toggles
        st.markdown("<div style='margin: 1.2rem 0;'>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class="switch-container">
            <span>SEO Optimization</span>
            <label class="switch">
                <input type="checkbox" checked>
                <span class="slider"></span>
            </label>
        </div>
        
        <div class="switch-container">
            <span>Advanced Grammar Check</span>
            <label class="switch">
                <input type="checkbox" checked>
                <span class="slider"></span>
            </label>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        generate_button = st.button("✨ Generate Content")
        
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        # Initial state or generated content
        if 'generated' not in st.session_state:
            st.session_state.generated = False
            
        if generate_button:
            if not topic:
                st.error("Please enter a blog topic")
            else:
                # Handle empty keywords gracefully
                if keywords:
                    keywords_list = [k.strip() for k in keywords.split(",") if k.strip()]
                else:
                    keywords_list = []
                
                with st.spinner("Creating your content with AI magic..."):
                    blog_data = generate_blog(topic, tone, length, keywords_list)
                    st.session_state.generated = True
                    st.session_state.blog_data = blog_data
        
        if st.session_state.generated:
            # Display result with enhanced styling
            st.markdown("<div class='content-box'>", unsafe_allow_html=True)
            
            # Metrics row with improved styling
            st.markdown("<div class='metrics'>", unsafe_allow_html=True)
            st.markdown(f"<div class='metric-item'><div>Words</div><div class='metric-value'>{st.session_state.blog_data['word_count']}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='metric-item'><div>Reading Time</div><div class='metric-value'>{st.session_state.blog_data['reading_time']}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='metric-item'><div>Quality Score</div><div class='metric-value'>9.2/10</div></div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Title with styling
            st.markdown(f"<h2 style='color: #00c6ff;'>{st.session_state.blog_data['title']}</h2>", unsafe_allow_html=True)
            
            # Content with enhanced styling
            st.markdown("<div class='result-box'>", unsafe_allow_html=True)
            for paragraph in st.session_state.blog_data["content"].split("\n\n"):
                st.markdown(paragraph)
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Action buttons with improved layout
            col1, col2, col3 = st.columns(3)
            with col1:
                st.download_button(
                    label="💾 Download",
                    data=st.session_state.blog_data["content"],
                    file_name=f"{topic.lower().replace(' ', '_')}_blog.txt",
                    mime="text/plain"
                )
            with col2:
                st.button("✏️ Edit", key="edit_button")
            with col3:
                st.button("🔄 Regenerate", key="regenerate_button")
            
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            # Display placeholder content
            st.markdown("<div class='content-box' style='display: flex; flex-direction: column; justify-content: center; align-items: center; height: 400px;'>", unsafe_allow_html=True)
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
            st.markdown("<span style='font-size: 3rem;'>✨</span>", unsafe_allow_html=True)
            st.markdown("<h3 style='color: #00c6ff;'>Your AI-Generated Content Will Appear Here</h3>", unsafe_allow_html=True)
            st.markdown("<p>Fill in the form and click 'Generate Content' to create your blog post</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

with tabs[1]:
    # Improved library/history view
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #00c6ff; margin-bottom: 1.2rem;'>Your Content Library</h3>", unsafe_allow_html=True)
    
    # Search and filter row
    col1, col2 = st.columns([3, 1])
    with col1:
        st.text_input("Search your content", placeholder="Enter keywords to search...")
    with col2:
        st.selectbox("Sort by", ["Newest First", "Oldest First", "Title A-Z", "Title Z-A"])
    
    # Sample history items with improved styling and actions
    history_items = [
        {"title": "The Ultimate Guide to Digital Marketing", "date": "March 3, 2025", "words": 850, "tone": "Professional"},
        {"title": "Website Optimization: Tips & Tricks", "date": "March 1, 2025", "words": 620, "tone": "Casual"},
        {"title": "Content Marketing Strategies That Work", "date": "February 27, 2025", "words": 950, "tone": "Persuasive"},
        {"title": "The Future of AI in Business", "date": "February 25, 2025", "words": 780, "tone": "Professional"}
    ]
    
    if history_items:
        for item in history_items:
            st.markdown(f"""
            <div class="history-item">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="font-weight: 600; font-size: 1.1rem;">{item['title']}</div>
                    <div style="color: #8e8e8e; font-size: 0.9rem;">{item['date']}</div>
                </div>
                <div style="margin-top: 8px; display: flex; justify-content: space-between; align-items: center;">
                    <div style="color: #00c6ff; font-size: 0.9rem;">{item['tone']} · {item['words']} words</div>
                    <div class="history-actions">
                        <div class="history-action">✏️ Edit</div>
                        <div class="history-action">🔄 Clone</div>
                        <div class="history-action">💾 Download</div>
                        <div class="history-action" style="color: #ff4757;">🗑️ Delete</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Your content library is empty. Generate your first content piece!")
    
    # Pagination
    st.markdown("""
    <div style="display: flex; justify-content: center; margin-top: 1.5rem;">
        <div style="display: flex; gap: 0.5rem;">
            <div class="nav-button">Previous</div>
            <div class="nav-button" style="background: linear-gradient(90deg, #0072ff, #00c6ff); color: white;">1</div>
            <div class="nav-button">2</div>
            <div class="nav-button">3</div>
            <div class="nav-button">Next</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

with tabs[2]:
    # Redesigned settings tab with grid layout
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #00c6ff; margin-bottom: 1.2rem;'>Personalize Your Experience</h3>", unsafe_allow_html=True)
    
    # Grid layout for settings
    st.markdown("<div class='settings-grid'>", unsafe_allow_html=True)
    
    # Content Preferences Section
    st.markdown("""
    <div class="settings-section">
        <div class="settings-heading">Content Preferences</div>
    """, unsafe_allow_html=True)
    
    st.selectbox("Default Content Tone", ["Professional", "Casual", "Humorous", "Persuasive"])
    st.selectbox("Default Content Length", ["Short", "Medium", "Long"])
    st.selectbox("Industry Focus", ["Technology", "Marketing", "Finance", "Healthcare", "Education", "E-commerce", "General"])
    
    st.markdown("""
        <div class="switch-container">
            <span>Always Use SEO Optimization</span>
            <label class="switch">
                <input type="checkbox" checked>
                <span class="slider"></span>
            </label>
        </div>
        
        <div class="switch-container">
            <span>Include Call to Action</span>
            <label class="switch">
                <input type="checkbox" checked>
                <span class="slider"></span>
            </label>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # AI Engine Settings Section
    st.markdown("""
    <div class="settings-section">
        <div class="settings-heading">AI Engine Settings</div>
    """, unsafe_allow_html=True)
    
    st.slider("Creativity Level", 1, 10, 7)
    st.slider("Detail & Depth", 1, 10, 5)
    st.slider("Language Formality", 1, 10, 6)
    
    st.markdown("""
        <div class="switch-container">
            <span>Advanced Language Model</span>
            <label class="switch">
                <input type="checkbox" checked>
                <span class="slider"></span>
            </label>
        </div>
        
        <div class="switch-container">
            <span>Fact Checking</span>
            <label class="switch">
                <input type="checkbox" checked>
                <span class="slider"></span>
            </label>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Export Options Section
    st.markdown("""
    <div class="settings-section">
        <div class="settings-heading">Export Options</div>
    """, unsafe_allow_html=True)
    
    st.radio("Default Export Format", ["Plain Text", "Markdown", "HTML", "PDF"])
    st.selectbox("Character Encoding", ["UTF-8", "ASCII", "ISO-8859-1"])
    
    st.markdown("""
        <div class="switch-container">
            <span>Include Metadata</span>
            <label class="switch">
                <input type="checkbox">
                <span class="slider"></span>
            </label>
        </div>
        
        <div class="switch-container">
            <span>Auto-Download After Generation</span>
            <label class="switch">
                <input type="checkbox">
                <span class="slider"></span>
            </label>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Interface Settings Section
    st.markdown("""
    <div class="settings-section">
        <div class="settings-heading">Interface Settings</div>
    """, unsafe_allow_html=True)
    
    st.selectbox("Color Theme", ["Deep Space (Current)", "Ocean Blue", "Emerald Green", "Ruby Red", "Amethyst Purple"])
    st.selectbox("Font Size", ["Small", "Medium (Default)", "Large", "Extra Large"])
    
    st.markdown("""
        <div class="switch-container">
            <span>Compact View</span>
            <label class="switch">
                <input type="checkbox">
                <span class="slider"></span>
            </label>
        </div>
        
        <div class="switch-container">
            <span>Show Word Count</span>
            <label class="switch">
                <input type="checkbox" checked>
                <span class="slider"></span>
            </label>
        </div>
        
        <div class="switch-container">
            <span>Enable Animations</span>
            <label class="switch">
                <input type="checkbox" checked>
                <span class="slider"></span>
            </label>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Save button
    if st.button("💾 Save All Settings"):
        st.success("✅ Your settings have been saved successfully!")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Improved footer
st.markdown("""
<div class="footer">
    <div style="color: #00c6ff; font-weight: 600; margin-bottom: 0.5rem;">
        ✨ MiniBlog AI Content Generator © 2025
    </div>
    <div style="color: #8e8e8e; font-size: 0.9rem; display: flex; justify-content: center; gap: 1.5rem; margin-top: 0.8rem;">
        <span>Terms</span>
        <span>Privacy</span>
        <span>Support</span>
    </div>
</div>
""", unsafe_allow_html=True)