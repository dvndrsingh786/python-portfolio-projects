def show_menu():
    print("\n=== Text Utility Toolkit ===")
    print("1. Count words")
    print("2. Count characters")
    print("3. Reverse text")
    print("4. Check palindrome")
    print("5. Split text into words")
    print("6. Find a word")
    print("7. Replace a word")
    print("8. Show unique words")
    print("9. Show word frequency")
    print("10. Exit")


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    return len(text)


def reverse_text(text):
    return text[::-1]


def is_palindrome(text):
    cleaned_text = text.lower().replace(" ", "")
    return cleaned_text == cleaned_text[::-1]


def split_into_words(text):
    return text.split()


def find_word(text, word):
    return word.lower() in text.lower()


def replace_word(text, old_word, new_word):
    return text.replace(old_word, new_word)


def get_unique_words(text):
    words = text.lower().split()
    return set(words)


def get_word_frequency(text):
    words = text.lower().split()

    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def main():
    text = input("Enter your text: ")

    while True:
        show_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            word_count = count_words(text)
            print(f"Word count: {word_count}")

        elif choice == "2":
            character_count = count_characters(text)
            print(f"Character count: {character_count}")

        elif choice == "3":
            reversed_text = reverse_text(text)
            print(f"Reversed text: {reversed_text}")

        elif choice == "4":
            if is_palindrome(text):
                print("This text is a palindrome.")
            else:
                print("This text is not a palindrome.")

        elif choice == "5":
            words = split_into_words(text)
            print(words)

        elif choice == "6":
            word = input("Enter word to find: ")

            if find_word(text, word):
                print(f"'{word}' was found in the text.")
            else:
                print(f"'{word}' was not found in the text.")

        elif choice == "7":
            old_word = input("Enter word to replace: ")
            new_word = input("Enter new word: ")

            text = replace_word(text, old_word, new_word)

            print("Updated text:")
            print(text)

        elif choice == "8":
            unique_words = get_unique_words(text)
            print(sorted(unique_words))

        elif choice == "9":
            frequency = get_word_frequency(text)

            for word, count in frequency.items():
                print(f"{word}: {count}")

        elif choice == "10":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Please choose between 1 and 10.")


if __name__ == "__main__":
    main()