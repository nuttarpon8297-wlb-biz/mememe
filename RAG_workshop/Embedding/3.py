from sentence_transformers import SentenceTransformer

# 1. Load a pretrained Sentence Transformer model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# The sentences to encode
sentences = [
    "Linkin Park",
    "Linkined Park",
    "Tung tung tung sahur",
]

# 2. Calculate embeddings by calling model.encode()
embeddings = model.encode(sentences, clean_up_tokenization_spaces=True)
print(embeddings.shape) # (item=3, dimension=384)

# 3. Calculate the embedding similarities
similarities = model.similarity(embeddings, embeddings)
print(model.similarity_fn_name)
print(similarities)
