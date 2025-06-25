# 🔧 Troubleshooting Guide

## Common Issues and Solutions

### 1. Keras/TensorFlow Version Conflicts

**Error**: `ValueError: Your currently installed version of Keras is Keras 3, but this is not yet supported in Transformers`

**Solution**:
```bash
# Uninstall conflicting packages
pip uninstall keras tensorflow transformers

# Install compatible versions
pip install tf-keras>=2.12.0
pip install tensorflow>=2.12.0
pip install transformers>=4.21.0
pip install sentence-transformers>=2.2.2
```

### 2. PyTorch Runtime Errors

**Error**: `RuntimeError: Tried to instantiate class '__path__._path', but it does not exist!`

**Solution**:
```bash
# Reinstall PyTorch with compatible version
pip uninstall torch torchvision torchaudio
pip install torch>=1.13.0 torchvision torchaudio
```

### 3. NLTK Data Download Issues

**Error**: `LookupError: Resource punkt not found`

**Solution**:
```bash
# Install NLTK data manually
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

### 4. Streamlit Import Errors

**Error**: `ModuleNotFoundError: No module named 'streamlit'`

**Solution**:
```bash
# Install Streamlit
pip install streamlit>=1.25.0
```

### 5. Memory Issues

**Error**: `OutOfMemoryError` or slow performance

**Solutions**:
- Close other applications to free RAM
- Use smaller model: Change `all-MiniLM-L6-v2` to `paraphrase-MiniLM-L3-v2`
- Process fewer files at once

### 6. File Upload Issues

**Error**: `File not supported` or upload fails

**Solutions**:
- Ensure files are PDF or TXT format
- Check file size (max 200MB per file)
- Try converting PDFs to text first

## Environment Setup

### Clean Installation
```bash
# Create fresh virtual environment
python -m venv resume-matcher-env
source resume-matcher-env/bin/activate  # On Windows: resume-matcher-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Alternative: Conda Environment
```bash
# Create conda environment
conda create -n resume-matcher python=3.9
conda activate resume-matcher

# Install packages
pip install -r requirements.txt
```

## Platform-Specific Issues

### Windows
- **Issue**: Long path names
- **Solution**: Use shorter directory paths or enable long path support

### macOS
- **Issue**: Permission denied for NLTK downloads
- **Solution**: Use `sudo` or install in user directory

### Linux
- **Issue**: Missing system libraries
- **Solution**: Install development tools: `sudo apt-get install build-essential`

## Performance Optimization

### For Slow Processing:
1. **Use smaller model**:
   ```python
   # In utils/embedding.py, change:
   MODEL_NAME = "paraphrase-MiniLM-L3-v2"  # Smaller, faster
   ```

2. **Enable caching**:
   ```python
   # Add to app.py
   @st.cache_data
   def cached_embedding(text):
       return get_embedding(text)
   ```

3. **Process in batches**:
   - Upload fewer files at once
   - Use smaller text samples for testing

## Streamlit Cloud Specific

### Deployment Issues:
1. **Build fails**: Check `requirements.txt` for incompatible versions
2. **App crashes**: Review logs in Streamlit Cloud dashboard
3. **Slow loading**: First run downloads models (1-2 minutes)

### Environment Variables:
```bash
# Add to Streamlit Cloud secrets if needed
NLTK_DATA=/tmp/nltk_data
TRANSFORMERS_CACHE=/tmp/transformers_cache
```

## Getting Help

### Debug Mode
Run with debug information:
```bash
streamlit run app.py --logger.level=debug
```

### Check Versions
```bash
python -c "import streamlit; print(f'Streamlit: {streamlit.__version__}')"
python -c "import torch; print(f'PyTorch: {torch.__version__}')"
python -c "import transformers; print(f'Transformers: {transformers.__version__}')"
```

### Logs
- **Local**: Check terminal output
- **Streamlit Cloud**: View in app dashboard
- **File logs**: Check `.streamlit/logs/` directory

## Still Having Issues?

1. **Check GitHub Issues**: Search for similar problems
2. **Community Forum**: Ask on [discuss.streamlit.io](https://discuss.streamlit.io)
3. **Create Issue**: Report bugs with error logs and system info

---

**Remember**: Most issues are resolved by using compatible package versions and clean environments! 🚀 