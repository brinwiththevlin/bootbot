from collections import Counter

def main():
    with open("books/frankenstein.txt") as f:
        print(text := f.read())
    print(f"the word count is: {word_count(text)}")
    print(char_count(text))


def word_count(text: str):
    return len(text.split())


def char_count(text: str):
    c = Counter(text.lower())
    return dict(c)



if __name__ == "__main__":
    main()
