from stats import get_book_count, get_character_counts, sort_chars
import sys
def get_book_text(path):
  with open(path) as f:
    return f.read()




def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]
  print("============ BOOKBOT ============")
  print("Analyzing book found at "+book_path)
  book =get_book_text(book_path)
  print("----------- Word Count ----------")
  print(f"Found {get_book_count(book)} total words")
  print("--------- Character Count -------")
  counts = get_character_counts(book)
  sort_chars(counts)
  for char in counts:
    print(f"{char["char"]}: {char["num"]}")
  print("============= END ===============")
main()