# 🚀 Streamlit Cloud Deployment Guide

## Quick Deploy to Streamlit Cloud

### 1. Prepare Your Repository
Ensure your project structure looks like this:
```
resume-matcher/
├── app.py                 # Main Streamlit app
├── requirements.txt       # Dependencies
├── utils/                 # Utility modules
│   ├── embedding.py
│   ├── file_parser.py
│   ├── matcher.py
│   └── keyword_matcher.py
├── assets/               # Static assets
│   ├── custom_style.css
│   ├── dummy_resume1.txt
│   ├── dummy_resume2.txt
│   ├── dummy_resume3.txt
│   └── dummy_job_description.txt
└── README.md
```

### 2. Deploy to Streamlit Cloud

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: AI Resume Matcher"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/resume-matcher.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository: `YOUR_USERNAME/resume-matcher`
   - Set main file path: `app.py`
   - Click "Deploy"

### 3. Configuration

**Streamlit Cloud Settings:**
- **Main file path**: `app.py`
- **Python version**: 3.9+ (auto-detected)
- **Requirements file**: `requirements.txt` (auto-detected)

**Environment Variables** (if needed):
- No API keys required for basic functionality
- NLTK data will be downloaded automatically

### 4. Post-Deployment

**Your app will be available at:**
```
https://YOUR_APP_NAME-YOUR_USERNAME.streamlit.app
```

**Example:**
```
https://resume-matcher-johndoe.streamlit.app
```

## Troubleshooting

### Common Issues:

1. **NLTK Data Download Error**
   - The app automatically downloads required NLTK data
   - First run might take 1-2 minutes

2. **Memory Issues**
   - Sentence transformers require ~500MB RAM
   - Streamlit Cloud provides 1GB RAM (sufficient)

3. **File Upload Issues**
   - Ensure file types are PDF or TXT
   - Maximum file size: 200MB per file

### Performance Tips:

1. **Optimize for Speed:**
   - Use smaller models (already using `all-MiniLM-L6-v2`)
   - Cache embeddings with `@st.cache_data`

2. **Reduce Memory Usage:**
   - Process files in batches
   - Clear cache periodically

## Monitoring

- **Logs**: Available in Streamlit Cloud dashboard
- **Usage**: Monitor in your Streamlit Cloud account
- **Performance**: Check app response times

## Custom Domain (Optional)

1. **Add Custom Domain:**
   - Go to Streamlit Cloud dashboard
   - Select your app
   - Go to "Settings" → "Custom domain"
   - Add your domain

2. **DNS Configuration:**
   - Add CNAME record pointing to your Streamlit app
   - Wait for DNS propagation (up to 24 hours)

## Security Best Practices

1. **File Upload Security:**
   - Validate file types
   - Limit file sizes
   - Sanitize file content

2. **Data Privacy:**
   - Files are processed in memory only
   - No permanent storage on Streamlit Cloud
   - Consider adding data retention policies

## Support

- **Streamlit Documentation**: [docs.streamlit.io](https://docs.streamlit.io)
- **Community Forum**: [discuss.streamlit.io](https://discuss.streamlit.io)
- **GitHub Issues**: Report bugs in your repository

---

**Happy Deploying! 🎉** 