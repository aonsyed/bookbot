def count_words(book_string):
    words = book_string.split()
    count = len(words)
    return count

def read_book(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_characters(book_string):
    low_string = book_string.lower()
    char_count = {}
    for char in low_string:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] =1
    return char_count

def alpha_count(char_count):
    alpha_list = []
    for letter in char_count:
        if letter.isalpha():
            alpha_list.append({"char": letter, "num": char_count[letter]}) 
    alpha_list.sort(key=sort_on, reverse=True)
    return alpha_list
    

def sort_on(dict):
    return dict["num"]

def report(path, word_count, alpha_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    for alpha in alpha_list:
        print(f"The '{alpha['char']}' character was found {alpha['num']} times")
    print("--- End report ---")

def main():
    path = "books/frankenstein.txt"

    file_contents = read_book(path)
    count = count_words(file_contents)
    char_count = count_characters(file_contents)
    alpha_list=alpha_count(char_count)
    report(path,count,alpha_list)

main()