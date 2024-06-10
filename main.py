import string
def get_word_count(book):

  return len(book.split())

def count_characters(book):
  lowered = book.lower()
  chars = {}
  for letter in lowered:
    if letter not in chars:
      chars[letter] = 1
    else:
      chars[letter] = chars[letter] + 1
  return chars

def letter_sort(char_count):
  list_of_lets = [{"letter": x, "num":char_count[x]} for x in string.ascii_lowercase]
  def sort_on(dict):
    return dict["num"]
  list_of_lets.sort(reverse=True, key=sort_on)
  return list_of_lets

def build_report(char_count):
  letters = letter_sort(char_count)
  for let in letters:
    print(f"The '{let["letter"]}' character was found {let["num"]} times")

def main(book):
  with open(f'./books/{book}') as f:
    story = f.read()
    print(f"--- Begin report of books/{book} ---")
    print(f"{get_word_count(story)} words found in the document")
    print()
    build_report(count_characters(story))
    print("--- End report ---")

main('frankenstein.txt')