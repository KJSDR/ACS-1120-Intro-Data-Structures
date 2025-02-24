import re
from collections import Counter

def histogram(source_text):
  with open(source_text, 'r') as file:
    text = file.read().lower()
    words = re.findall(r"\b[a-zA-Z']+\b", text)

    hist = {}  
    for word in words:
        hist[word] = hist.get(word, 0) + 1 
    return hist


def unique_words(histogram):
    """Return the count of unique words in the histogram."""
    return len(histogram)

def frequency(word, histogram):
    """Return the frequency of a specific word in the histogram."""
    return histogram.get(word.lower(), 0)

if __name__ == "__main__":
    source_text = "Code/data/corpus.txt"
    hist = histogram(source_text)
    
    print(f"Total unique words: {unique_words(hist)}")
    
    test_word = "the"
    print(f"Frequency of '{test_word}': {frequency(test_word, hist)}")
    
    most_common = hist.most_common(5)
    print("Most common words:", most_common)
    
    least_common = sorted(hist.items(), key=lambda x: x[1])[:5]
    print("Least common words:", least_common)
