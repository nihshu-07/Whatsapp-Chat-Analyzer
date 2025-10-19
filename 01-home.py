import streamlit as st 

st.markdown("""
    <div class="hero-section">
        <div class="hero-title"><h1>💬 WhatsApp Chat Analyzer</h1></div>
        <div class="hero-subtitle">Transform Your Conversations into Powerful Insights</div>
        <p style="font-size: 1rem; color: #cbd5e1;">Analyze message patterns, discover trends, and understand your communication behavior with beautiful visualizations</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="about-section">
        <div class="about-title"><h3>📖 About This Project</h3></div>
        <div class="about-text">
            <span class="highlight">WhatsApp Chat Analyzer</span> is a powerful data analytics tool designed to extract meaningful insights from your WhatsApp conversations. Whether you're curious about your messaging habits, want to understand group dynamics, or simply explore your communication patterns, this tool provides comprehensive analysis with beautiful visualizations.
        </div>
        <div class="about-text">
            This project combines modern data processing with intuitive visualization to make chat analysis accessible to everyone. No technical knowledge required – just export your chat and discover fascinating patterns about how you communicate.
        </div>
        <div class="about-text">
            <strong style="color: #e2e8f0;">🔒 Privacy First:</strong> Your data is processed locally and never stored on any external servers. Complete privacy and security guaranteed.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: #e2e8f0; margin: 3rem 0 2rem 0;'>✨ Key Features</h2>", unsafe_allow_html=True)
    
col1, col2, col3 = st.columns(3)
    
with col1:
    st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Message Statistics</div>
            <div class="feature-description">Get detailed insights about total messages, word count, media shared, and links exchanged in your conversations.</div>
        </div>
        """, unsafe_allow_html=True)
    
with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📈</div>
            <div class="feature-title">Timeline Analysis</div>
            <div class="feature-description">Visualize your chat activity over time with monthly and daily timeline charts to see your communication trends.</div>
        </div>
        """, unsafe_allow_html=True)
    
with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔥</div>
            <div class="feature-title">Activity Heatmap</div>
            <div class="feature-description">Discover your most active days and months with beautiful heatmap visualizations showing peak activity times.</div>
        </div>
        """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
    
with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">☁️</div>
            <div class="feature-title">Word Cloud</div>
            <div class="feature-description">See your most frequently used words visualized in an interactive word cloud that highlights your vocabulary.</div>
        </div>
        """, unsafe_allow_html=True)
    
with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">✉️</div>
            <div class="feature-title">Emoji Analysis</div>
            <div class="feature-description">Analyze which emojis you use most and their frequency in conversations, revealing your communication style.</div>
        </div>
        """, unsafe_allow_html=True)
    
with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">👥</div>
            <div class="feature-title">User Insights</div>
            <div class="feature-description">Compare activity across different users in group chats and find who's the most active participant.</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
    <div style="background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(139, 92, 246, 0.1) 100%); border-radius: 16px; padding: 3rem 2rem; margin: 3rem 0; text-align: center; border: 1px solid rgba(99, 102, 241, 0.2);">
        <h2 style="color: #e2e8f0; margin-bottom: 1rem;">Ready to Analyze Your Chats?</h2>
        <p style="color: #cbd5e1; font-size: 1.1rem; margin-bottom: 1.5rem;">Get started now and discover fascinating insights about your communication patterns and habits</p>
        <p style="color: #6366f1; font-weight: 600;">👉 Go to the Analyzer page in the sidebar to begin your analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
st.markdown("""
    <div style="text-align: center; padding: 2rem; color: #94a3b8; border-top: 1px solid rgba(99, 102, 241, 0.2); margin-top: 3rem;">
        <p style="font-size: 0.9rem;">💡 <strong style="color: #cbd5e1;">Pro Tip:</strong> For best results, export your most active chats to get richer data and more interesting visualizations</p>
        <p style="font-size: 0.85rem; margin-top: 1rem; opacity: 0.7;">Made with ❤️ for WhatsApp enthusiasts | Privacy-First Data Analysis</p>
    </div>
    """, unsafe_allow_html=True)