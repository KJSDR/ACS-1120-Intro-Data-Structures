import random
import re
from collections import defaultdict

class MarkovChain:
    def __init__(self, file_path):
        """Initialize and build the Markov chain from the given text file."""
        self.chain = defaultdict(list)
        self.words = self._read_and_process(file_path)
        self._build_chain()

    def _read_and_process(self, file_path):
        """Read and process the text file, returning a list of words."""
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read().lower()
            words = re.findall(r"\b\w+\b", text)  # Extract words
        return words

    def _build_chain(self):
        """Build the Markov chain from the words list using trigrams."""
        for i in range(len(self.words) - 2):
            key = (self.words[i], self.words[i + 1])  # Use bigram as key
            next_word = self.words[i + 2]  # Word that follows
            self.chain[key].append(next_word)

    def generate_sentence(self, length=15):
        """Generate a random sentence using the Markov chain."""
        if not self.chain:
            return "Error: Markov chain is empty."
        
        start_key = random.choice(list(self.chain.keys()))
        sentence = [start_key[0], start_key[1]]
        
        for _ in range(length - 2):  # Already have 2 words
            key = (sentence[-2], sentence[-1])
            if key in self.chain:
                next_word = random.choice(self.chain[key])
                sentence.append(next_word)
            else:
                break
        
        return " ".join(sentence).capitalize() + "."

if __name__ == "__main__":
    markov = MarkovChain("Code/data/corpus.txt")
    print(markov.generate_sentence(20))
