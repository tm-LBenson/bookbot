import string

def remove_punctuation(story):
    translator = str.maketrans('', '', string.punctuation)
    return story.translate(translator)

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
    list_of_lets = [{"letter": x, "num": char_count[x]} for x in string.ascii_lowercase if x in char_count]
    list_of_lets.sort(reverse=True, key=lambda d: d["num"])
    return list_of_lets

def build_report(char_count):
    letters = letter_sort(char_count)
    for let in letters:
        print(f"The '{let['letter']}' character was found {let['num']} times")

def words_with_z(book):
    words = book.split()
    zwords = {}
    for word in words:
        if "z" in word:
            if word not in zwords:
                zwords[word] = 1
            else:
                zwords[word] = zwords[word] + 1
    list_of_words = [{"word": word, "num": zwords[word]} for word in zwords]
    list_of_words.sort(reverse=True, key=lambda d: d["num"])
    for word in list_of_words:
        print(f"{word['word']} appears {word['num']} times")

def unique_word_count(book):
    words = book.split()
    unique_words = set(words)
    return len(unique_words)

def main(book):
    with open(f'./books/{book}') as f:
        storyWp = f.read()
        story = remove_punctuation(storyWp)

        word_count = get_word_count(story)
        unique_words = unique_word_count(story)
        char_count = count_characters(story)

        print(f"--- Begin report of books/{book} ---")
        print(f"{word_count} words found in the document")
        print(f"{unique_words} unique words found in the document")
        print()
        build_report(char_count)
        print()
        # words_with_z(story)
        print("--- End report ---")

main('frankenstein.txt')
