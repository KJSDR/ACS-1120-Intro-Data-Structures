import re
from collections import Counter

def histogram(source_text):
    """Generate a histogram (word frequency dictionary) from the given text file or string."""
    if isinstance(source_text, str):
        words = re.findall(r'\b\w+\b', source_text.lower())
    else:
        with open(source_text, 'r', encoding='utf-8') as file:
            words = re.findall(r'\b\w+\b', file.read().lower())
    
    return Counter(words)

def unique_words(histogram):
    """Return the count of unique words in the histogram."""
    return len(histogram)

def frequency(word, histogram):
    """Return the frequency of a specific word in the histogram."""
    return histogram.get(word.lower(), 0)

if __name__ == "__main__":
    source_file = "flowersofevil.txt"
    hist = histogram(source_file)
    
    print(f"Total unique words: {unique_words(hist)}")
    
    test_word = "the"
    print(f"Frequency of '{test_word}': {frequency(test_word, hist)}")
    
    most_common = hist.most_common(5)
    print("Most common words:", most_common)
    
    least_common = sorted(hist.items(), key=lambda x: x[1])[:5]
    print("Least common words:", least_common)
