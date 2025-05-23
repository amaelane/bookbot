# note: return here is silent, if you need to see your result in the console, 
#you must use print()

import sys

while len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
#if len(sys.argv) == 2:
#    b_path = sys.argv[1]

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
from stats import get_num_words
from stats import get_num_characters
print("============= END ===============")
