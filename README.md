# 🚀 AI Resume Matcher

A Gen-Z, AI-powered web app to match and rank resumes against a job description using state-of-the-art NLP (Sentence-BERT). Built with Streamlit for recruiters who want fast, fun, and futuristic UX.

![Demo Screenshot](assets/demo_screenshot.png)

## ✨ Features
- 🧠 Upload a job description (PDF/TXT)
- 📄 Upload multiple resumes (PDF/TXT)
- 🤖 AI-powered semantic matching (Sentence-BERT)
- 🎯 **NEW**: Keyword highlighting with matching terms
- 📊 Ranked results with gradient progress bars
- 🎨 Gen-Z UI: neon/cyberpunk/light themes, animated, emoji-rich
- 📥 **NEW**: Enhanced CSV reports with keyword data
- ✨ Visual keyword matching with highlighted resume previews

## 🛠️ Tech Stack
- **Python** + **Streamlit**
- **HuggingFace Sentence-Transformers** (all-MiniLM-L6-v2)
- **NLTK** for keyword extraction
- **Scikit-learn** for cosine similarity
- **Pandas** + **Plotly** for data visualization
- **Streamlit Extras**: Lottie, Tags, etc.

## 🚀 Quick Start

### Local Development
1. **Clone this repo**
   ```bash
   git clone https://github.com/YOUR_USERNAME/resume-matcher.git
   cd resume-matcher
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

### Streamlit Cloud Deployment
See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

**Quick Deploy:**
1. Push to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo and deploy!

## 📊 Demo Data
Use the sample files in `assets/`:
- `dummy_job_description.txt` - Sample job posting
- `dummy_resume1.txt` - Software Engineer resume
- `dummy_resume2.txt` - Data Analyst resume  
- `dummy_resume3.txt` - AI Intern resume

## 🎯 How It Works

1. **Upload Files**: Job description + multiple resumes
2. **AI Processing**: 
   - Extract text from PDFs/TXT files
   - Generate embeddings using Sentence-BERT
   - Calculate cosine similarity scores
   - Extract and match keywords
3. **Results**: 
   - Ranked list with match percentages
   - Gradient progress bars (red→yellow→green)
   - Highlighted matching keywords
   - Resume previews with keyword highlights
   - Downloadable CSV reports

## 📁 Project Structure
```
resume-matcher/
├── app.py                 # Main Streamlit app
├── requirements.txt       # Dependencies
├── utils/                 # Utility modules
│   ├── embedding.py       # BERT embedding logic
│   ├── file_parser.py     # PDF/text parsing
│   ├── matcher.py         # Similarity computation
│   └── keyword_matcher.py # Keyword extraction & highlighting
├── assets/               # Static assets
│   ├── custom_style.css  # Gen-Z UI styling
│   └── demo files...     # Sample data
├── DEPLOYMENT.md         # Deployment guide
└── README.md
```

## 🎨 UI Features
- **Theme Toggle**: Neon, Cyberpunk, Light modes
- **Gradient Progress Bars**: Visual match scores
- **Keyword Highlights**: Yellow highlighting for matching terms
- **Expandable Results**: Detailed view for each resume
- **Animated Elements**: Smooth transitions and hover effects
- **Responsive Design**: Works on desktop and mobile

## 📈 Performance
- **Fast Processing**: Optimized for quick results
- **Memory Efficient**: Processes files in memory only
- **Scalable**: Handles multiple resumes efficiently
- **Caching**: Smart caching for repeated operations

## 🔒 Privacy & Security
- **No Data Storage**: Files processed in memory only
- **Secure Uploads**: File type validation
- **Privacy First**: No data sent to external services (except HuggingFace for model)

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support
- **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/resume-matcher/issues)
- **Documentation**: [Streamlit Docs](https://docs.streamlit.io)
- **Community**: [Streamlit Forum](https://discuss.streamlit.io)

## 📄 License
MIT License - see [LICENSE](LICENSE) file for details.

---

**Made with ❤️ for Gen-Z recruiters** 🚀✨ 