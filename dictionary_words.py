import sys
import random


def random_set(number):
    """Open file and read words. Join words into a sentence."""
    with open('/usr/share/dict/words', 'r') as file:
        words = file.readlines()  
    words = [word.strip() for word in words]
    random_words = random.sample(words, number)  
    sentence = ' '.join(random_words) + '.'  
    return sentence  


if __name__ == "__main__":
    number = int(sys.argv[1])
    print(random_set(number))