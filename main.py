from stats import get_num_words
from stats import get_times_char
from stats import sort_dict

def get_books_text(path_to_file: str):
  with open(path_to_file) as file:
    book_contents = file.read()
  return book_contents

def output(book_path: str, num_words: int, sorted_chars: list):
  print("============ BOOKBOT ============")
  print(f"Analysing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("------- Character Count ---------")
  for item in sorted_chars:
    if item["char"].isalpha() is False:
      continue
    char = item["char"]
    num = item["num"]
    print(f"{char}: {num}")
  print("============= END ===============")

def main():
  import sys
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    book_path = sys.argv[1]
  num_words = get_num_words(get_books_text(book_path))
  sorted_chars = sort_dict(get_times_char(get_books_text(book_path)))
  
  output(book_path, num_words, sorted_chars)
  

main()