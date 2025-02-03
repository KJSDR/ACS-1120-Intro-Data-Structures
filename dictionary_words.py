import random
import sys

def load_words(file_path="/usr/share/dict/words"):
    """Read words from the dictionary file and return them as a list."""
    with open(file_path, "r") as file:
        words = [line.strip() for line in file.readlines()]
    return words

def generate_sentence(word_list, num_words):
    """Select a random set of words from the list and form a sentence."""
    random_words = random.sample(word_list, num_words)
    return " ".join(random_words) + "."

def main():
    """Main function to execute the script."""
    if len(sys.argv) != 2:
        print("Usage: python3 dictionary_words.py <number_of_words>")
        sys.exit(1)
    
    try:
        num_words = int(sys.argv[1])
        if num_words < 1:
            raise ValueError
    except ValueError:
        print("Please enter a valid positive integer for the number of words.")
        sys.exit(1)
    
    words = load_words()
    sentence = generate_sentence(words, num_words)
    print(sentence)

if __name__ == "__main__":
    main()
