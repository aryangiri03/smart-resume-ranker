from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def compute_similarity(jd_emb, resume_embs):
    results = []
    for name, emb in resume_embs:
        score = float(cosine_similarity([jd_emb], [emb])[0][0])
        match_pct = round(score * 100, 2)
        results.append((name, match_pct))
    return results 