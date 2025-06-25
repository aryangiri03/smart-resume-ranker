#!/usr/bin/env python3
"""
NLTK Data Setup Script for Resume Matcher
Run this script to download required NLTK data manually.
"""

import nltk
import sys

def download_nltk_data():
    """Download required NLTK data."""
    print("🚀 Setting up NLTK data for Resume Matcher...")
    
    required_data = [
        'punkt',
        'stopwords',
        'averaged_perceptron_tagger',
        'maxent_ne_chunker',
        'words'
    ]
    
    for data in required_data:
        try:
            print(f"📥 Downloading {data}...")
            nltk.download(data, quiet=False)
            print(f"✅ {data} downloaded successfully!")
        except Exception as e:
            print(f"❌ Error downloading {data}: {e}")
    
    print("\n🎉 NLTK setup complete!")
    print("You can now run: streamlit run app.py")

if __name__ == "__main__":
    try:
        download_nltk_data()
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        print("Try running: pip install nltk")
        sys.exit(1) 