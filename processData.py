import re
import string
from underthesea import word_tokenize

def text_normalizer(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", " ", text)
    text = re.sub("\s+", " ", text).strip()
    return text

def preprocess_text(text, stopwords):
    text = text_normalizer(text)
    tokens = word_tokenize(text, format='text')
    tokens = [word for word in tokens.split() if word not in stopwords]
    return ' '.join(tokens)