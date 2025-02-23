from collections import Counter


def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
    print_report("books/frankenstein", text)


def print_report(title: str, text: str):
    print(f"--- Begin report of {title}\n")
    print(f"{word_count(text)} words found in document")
    print()
    for k, v in char_count(text).items():
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")
    print("--- End report ---")


def word_count(text: str):
    return len(text.split())


def char_count(text: str):
    c = Counter(text.lower())
    return dict(c)


if __name__ == "__main__":
    main()
