import streamlit as st
import torch
import transformers
import sentence_transformers
from sentence_transformers import SentenceTransformer

# Must be the first Streamlit command
st.set_page_config(page_title="AI Resume Matcher 🚀", page_icon="🤖", layout="wide")

# Now import other modules
from utils.embedding import get_embedding
from utils.file_parser import parse_file
from utils.matcher import compute_similarity
from utils.keyword_matcher import find_matching_keywords, highlight_text_with_keywords
import os
import pandas as pd
import plotly.express as px
from io import BytesIO

# --- Custom CSS/Cyberpunk Theme ---
try:
    with open("assets/custom_style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("CSS file not found. Using default styling.")
except Exception as e:
    st.warning(f"Could not load custom CSS: {e}")

# --- Lottie Animation ---
# (Placeholder for Lottie animation)

# --- Sidebar: Theme Toggle ---
theme = st.sidebar.radio("Theme", ["Neon", "Cyberpunk", "Light"])

# --- Main UI ---
st.title("AI Resume Matcher 🤖✨")
st.markdown("""
Upload a job description and multiple resumes. We'll rank them by AI-powered match %!<br>
<small> Professional. Futuristic. Fast. Fun.</small>
""", unsafe_allow_html=True)

# --- File Uploaders ---
st.subheader("1. Upload Job Description 📝")
jd_file = st.file_uploader("Job Description (PDF or TXT)", type=["pdf", "txt"], key="jd")

st.subheader("2. Upload Resumes 📄")
resume_files = st.file_uploader("Resumes (PDF or TXT, multiple)", type=["pdf", "txt"], accept_multiple_files=True, key="resumes")

# --- Process & Match ---
if jd_file and resume_files:
    with st.spinner("Processing files and matching... 🧠"):
        jd_text = parse_file(jd_file)
        resumes = [(f.name, parse_file(f)) for f in resume_files]
        jd_emb = get_embedding(jd_text)
        resume_embs = [(name, get_embedding(text)) for name, text in resumes]
        scores = compute_similarity(jd_emb, resume_embs)
        
        # Create DataFrame with scores
        df = pd.DataFrame(scores, columns=["Resume", "Match %"])
        df = df.sort_values("Match %", ascending=False).reset_index(drop=True)
        
        # Add keyword matching data
        keyword_data = []
        for name, text in resumes:
            matching_keywords = find_matching_keywords(jd_text, text)
            keyword_data.append({
                "resume_name": name,
                "resume_text": text,
                "matching_keywords": matching_keywords
            })
        
        st.success("Matching complete!")

        # --- Results Section ---
        st.markdown("### Results Table 🏆")
        
        # Display results with gradient progress bars
        for idx, row in df.iterrows():
            resume_name = row["Resume"]
            match_score = row["Match %"]
            
            # Find corresponding keyword data
            keyword_info = next((k for k in keyword_data if k["resume_name"] == resume_name), None)
            
            with st.expander(f"📄 {resume_name} - {match_score}% Match", expanded=idx < 3):
                # Gradient progress bar
                progress_color = f"linear-gradient(90deg, {'#ff4444' if match_score < 50 else '#ffaa00' if match_score < 75 else '#44ff44'}, {'#ffaa00' if match_score < 50 else '#44ff44' if match_score < 75 else '#00ff00'})"
                st.markdown(f"""
                <div style="background: {progress_color}; height: 20px; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; margin: 10px 0;">
                    {match_score}% Match
                </div>
                """, unsafe_allow_html=True)
                
                # Show matching keywords
                if keyword_info and keyword_info["matching_keywords"]:
                    st.markdown("**🎯 Matching Keywords:**")
                    keywords_html = " ".join([f'<span style="background-color: #FFD700; padding: 4px 8px; border-radius: 5px; margin: 2px; display: inline-block;">{kw}</span>' for kw in keyword_info["matching_keywords"]])
                    st.markdown(keywords_html, unsafe_allow_html=True)
                    
                    # Show highlighted resume preview
                    st.markdown("**📝 Resume Preview (Highlighted):**")
                    highlighted_text = highlight_text_with_keywords(keyword_info["resume_text"][:500] + "...", keyword_info["matching_keywords"])
                    st.markdown(f'<div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; max-height: 200px; overflow-y: auto;">{highlighted_text}</div>', unsafe_allow_html=True)
                else:
                    st.info("No significant keyword matches found.")

        # --- Bar Graph ---
        st.markdown("### Visual Rankings 📊")
        fig = px.bar(df, x="Match %", y="Resume", orientation="h", 
                    color="Match %", 
                    color_continuous_scale="RdYlGn",
                    title="Resume Match Rankings")
        fig.update_layout(
            xaxis_title="Match Percentage",
            yaxis_title="Resume",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

        # --- Enhanced CSV Download ---
        st.markdown("### 📥 Download Report")
        
        # Create enhanced CSV with keyword data
        enhanced_data = []
        for idx, row in df.iterrows():
            resume_name = row["Resume"]
            match_score = row["Match %"]
            keyword_info = next((k for k in keyword_data if k["resume_name"] == resume_name), None)
            
            enhanced_data.append({
                "Rank": idx + 1,
                "Resume": resume_name,
                "Match_Percentage": match_score,
                "Matching_Keywords": ", ".join(keyword_info["matching_keywords"]) if keyword_info else "",
                "Keyword_Count": len(keyword_info["matching_keywords"]) if keyword_info else 0
            })
        
        enhanced_df = pd.DataFrame(enhanced_data)
        csv = enhanced_df.to_csv(index=False).encode('utf-8')
        
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                "📊 Download Enhanced Report (CSV)",
                csv,
                "resume_match_report_enhanced.csv",
                "text/csv",
                key="download-enhanced-csv"
            )
        
        with col2:
            # Simple CSV download
            simple_csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                "📄 Download Simple Report (CSV)",
                simple_csv,
                "resume_match_report.csv",
                "text/csv",
                key="download-simple-csv"
            )

else:
    st.info("Please upload a job description and at least one resume to get started.")

# --- Footer ---
st.markdown("<center><small>Made with dedication for modern recruiters</small></center>", unsafe_allow_html=True)

print(torch.__version__)
print(transformers.__version__)
print(sentence_transformers.__version__)
model = SentenceTransformer("all-MiniLM-L6-v2")
print("All good!") 
