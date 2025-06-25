import numpy as np
import streamlit as st

# Try to import sentence-transformers with error handling
try:
    from sentence_transformers import SentenceTransformer
    MODEL_NAME = "all-MiniLM-L6-v2"
    model = SentenceTransformer(MODEL_NAME)
    MODEL_LOADED = True
except ImportError as e:
    st.error(f"Error loading sentence-transformers: {e}")
    st.info("Please install required dependencies: pip install sentence-transformers")
    MODEL_LOADED = False
    model = None
except Exception as e:
    st.warning(f"Warning: Could not load model: {e}")
    MODEL_LOADED = False
    model = None

def get_embedding(text):
    """Get embedding for text with error handling."""
    if not MODEL_LOADED:
        st.error("Model not loaded. Please check your installation.")
        return np.zeros((384,))
    
    if not text:
        return np.zeros((384,))
    
    try:
        return model.encode(text, show_progress_bar=False)
    except Exception as e:
        st.error(f"Error generating embedding: {e}")
        return np.zeros((384,)) 