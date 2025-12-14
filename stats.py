def get_book_count(book):
  return len(book.split())

def get_character_counts(book):
  my_map = {}
  final_map = []
  for letter in book:
    letter = letter.lower()
    if letter in my_map:
        my_map[letter] = my_map[letter] + 1
    else:
        my_map[letter] = 1
  for key in my_map:
    final_map.append({"char": key, "num": my_map[key]})

  return final_map

def sort_on(items):
  return items["num"]

def sort_chars(char_list):
  char_list.sort(reverse=True, key=sort_on)
  return char_list