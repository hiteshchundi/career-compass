import re
from collections import Counter


STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "will",
    "your",
    "you",
    "our",
    "are",
    "from",
    "this",
    "that",
    "have",
    "has",
    "their",
}


def extract_keywords(text: str, top_n: int = 25) -> list[str]:
    words = re.findall(r"[a-zA-Z]{3,}", text.lower())

    words = [w for w in words if w not in STOPWORDS]

    counter = Counter(words)

    return [
        word
        for word, _ in counter.most_common(top_n)
    ]