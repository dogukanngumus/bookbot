
path_to_file = "books/frankenstein.txt"

def count_characters(file_content):
    lowered_file_content = list(file_content.lower())
    char_dictionary = {}
    for i in lowered_file_content:
        if i in char_dictionary:
            char_dictionary[i] += 1
        else:
            char_dictionary[i] = 1
    return char_dictionary

def print_report(word_count, char_count):
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    for i in char_count:
        print(f"The '{i}' character was found {char_count[i]} times")
    print("--- End report ---")

def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        char_count = count_characters(file_contents)
        print_report(word_count, char_count)


main()
    