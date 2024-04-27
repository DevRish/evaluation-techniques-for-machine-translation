from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np

# Load pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Encode the sentences
sentence1 = "I go to the school"
sentence2 = "He comes from cinema"

inputs = tokenizer([sentence1, sentence2], return_tensors="pt", padding=True, truncation=True)
with torch.no_grad():
    outputs = model(**inputs)

# Get embeddings for [CLS] token (sentence representation)
sentence1_embedding = outputs.last_hidden_state[0][0].numpy()
sentence2_embedding = outputs.last_hidden_state[1][0].numpy()

# Calculate cosine similarity between embeddings
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

similarity_score = cosine_similarity(sentence1_embedding, sentence2_embedding)
print(f"Cosine Similarity: {similarity_score}")
