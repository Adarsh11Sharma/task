from collections import Counter
import os

def find_file(file_name):
    for root, dirs, files in os.walk('.'):
        if file_name in files:
            return os.path.join(root, file_name)

    return None

def find_word_positions(file_path, target_word):
    positions = []
    if file_path:
        with open(file_path, 'r') as file:
            line_number = 0
            for line in file:
                line_number += 1
                words = line.split()
                for position, word in enumerate(words):
                    if word == target_word:
                        positions.append((line_number, position + 1))
    return positions

def count_duplicate_words(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
            word_counts = Counter(words)
            duplicate_words = {word: count for word, count in word_counts.items() if count > 1}
            return duplicate_words
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return {}
    except Exception as e:
        print("An error occurred:", e)
        return {}

if __name__ == '__main__':
    file_name = input("Enter the file name to search for: ")
    file_path = find_file(file_name)

    if file_path:
        target_word = input("Enter the word to find its positions: ")
        word_positions = find_word_positions(file_path, target_word)
        if word_positions:
            print(f"The word '{target_word}' was found at the following positions:")
            for position in word_positions:
                print(f"Line: {position[0]}, Position: {position[1]}")
        else:
            print(f"The word '{target_word}' was not found in the file.")
        
        duplicate_words = count_duplicate_words(file_path)
        if duplicate_words:
            print("Duplicate words and their counts:")
            for word, count in duplicate_words.items():
                print(f"{word}: {count}")
        else:
            print("No duplicate words found in the file.")
    else:
        print(f"File '{file_name}' not found.")

