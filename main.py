def main():
    with open("books/frankenstein.txt") as f:
        print(text := f.read())
    print(f"the word count is: {word_count(text)}")


def word_count(text: str):
    return len(text.split())
if __name__ == "__main__":
    main()
