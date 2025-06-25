import re
from collections import Counter
import streamlit as st

# Try to import NLTK with error handling
try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    
    # Download required NLTK data with error handling
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        try:
            nltk.download('punkt', quiet=True)
        except Exception as e:
            st.warning(f"Could not download NLTK punkt data: {e}")
    
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        try:
            nltk.download('stopwords', quiet=True)
        except Exception as e:
            st.warning(f"Could not download NLTK stopwords data: {e}")
    
    # Test if NLTK is working properly
    try:
        test_tokens = word_tokenize("test sentence")
        stop_words = set(stopwords.words('english'))
        NLTK_AVAILABLE = True
    except Exception as e:
        st.warning(f"NLTK not working properly: {e}")
        NLTK_AVAILABLE = False
        
except ImportError as e:
    st.error(f"Error loading NLTK: {e}")
    st.info("Please install NLTK: pip install nltk")
    NLTK_AVAILABLE = False
except Exception as e:
    st.warning(f"Warning: NLTK not available: {e}")
    NLTK_AVAILABLE = False

def extract_keywords(text, top_n=20):
    """Extract top keywords from text using frequency analysis."""
    if not NLTK_AVAILABLE:
        # Fallback: simple word extraction without NLTK
        words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
        # Simple stopwords list
        simple_stopwords = {'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'mine', 'yours', 'hers', 'ours', 'theirs', 'a', 'an', 'as', 'so', 'than', 'too', 'very', 'just', 'now', 'then', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'also', 'well', 'even', 'back', 'still', 'way', 'take', 'every', 'am', 'get', 'through', 'during', 'before', 'after', 'above', 'below', 'up', 'down', 'out', 'off', 'over', 'under', 'again', 'further', 'then', 'once'}
        keywords = [word for word in words if word not in simple_stopwords]
        keyword_freq = Counter(keywords)
        return [word for word, freq in keyword_freq.most_common(top_n)]
    
    try:
        # Convert to lowercase and tokenize
        tokens = word_tokenize(text.lower())
        
        # Remove stopwords and non-alphabetic tokens
        stop_words = set(stopwords.words('english'))
        keywords = [word for word in tokens if word.isalpha() and word not in stop_words and len(word) > 2]
        
        # Count frequencies and return top keywords
        keyword_freq = Counter(keywords)
        return [word for word, freq in keyword_freq.most_common(top_n)]
    except Exception as e:
        st.warning(f"Error in NLTK processing, using fallback: {e}")
        # Fallback to simple method
        words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
        simple_stopwords = {'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'mine', 'yours', 'hers', 'ours', 'theirs'}
        keywords = [word for word in words if word not in simple_stopwords]
        keyword_freq = Counter(keywords)
        return [word for word, freq in keyword_freq.most_common(top_n)]

def find_matching_keywords(jd_text, resume_text, min_length=3):
    """Find matching keywords between job description and resume."""
    try:
        jd_keywords = set(extract_keywords(jd_text))
        resume_keywords = set(extract_keywords(resume_text))
        
        # Find intersection
        matching = jd_keywords.intersection(resume_keywords)
        
        # Filter by minimum length
        matching = {kw for kw in matching if len(kw) >= min_length}
        
        return list(matching)
    except Exception as e:
        st.warning(f"Error finding matching keywords: {e}")
        return []

def highlight_text_with_keywords(text, keywords, highlight_color="#FFD700"):
    """Highlight keywords in text with HTML spans."""
    if not keywords:
        return text
    
    try:
        # Create regex pattern for case-insensitive matching
        pattern = '|'.join(map(re.escape, keywords))
        regex = re.compile(f'({pattern})', re.IGNORECASE)
        
        # Replace matches with highlighted spans
        highlighted_text = regex.sub(
            f'<span style="background-color: {highlight_color}; padding: 2px 4px; border-radius: 3px; font-weight: bold;">\\1</span>',
            text
        )
        
        return highlighted_text
    except Exception as e:
        st.warning(f"Error highlighting keywords: {e}")
        return text 