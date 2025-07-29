from sentence_transformers import SentenceTransformer

# Load SciBERT once
model = SentenceTransformer("allenai-specter")

def generate_embedding(text):
    return model.encode(text)
