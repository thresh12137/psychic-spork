#A4 Word Spinner solo work Shijie Quan
from Spinner import Spinner
import string


def clean_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    text_without_punctuation = text.translate(translator)    # Use translate to remove punctuation
    return text_without_punctuation

def main():
    with open('eassy.txt', 'r') as file:
        ori_text = file.read()
        ori_text = clean_punctuation(ori_text.lower())
        spinner = Spinner("synonyms-simplified (1).txt")
        print("Original:", ori_text)
        changed_text = spinner.random_spinner(ori_text)
        cleaned_changed_text = clean_punctuation(changed_text)  # Clean the modified text from punctuation
        print("Modified:", cleaned_changed_text)


if __name__ == "__main__":
    main()