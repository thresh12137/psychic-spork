from Spinner import Spinner
import string
def clean_punctuation(text):
    words = [word for word in text.split() if word.strip(string.punctuation)]
    return " ".join(words)

def main():
    with open('eassy.txt', 'r') as file:
        ori_text = file.read()
        ori_text = clean_punctuation(ori_text.lower())
        spinner = Spinner("synonyms-simplified (1).txt")
        print("Original:", ori_text)
        changed_text = spinner.random_spinner(ori_text)
        print("Modified:", changed_text)


if __name__ == "__main__":
    main()