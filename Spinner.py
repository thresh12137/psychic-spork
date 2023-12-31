#A4 Word Spinner solo work Shijie Quan
#https://github.com/thresh12137/psychic-spork.git
import random


class Spinner:
    def __init__(self, synonym_file):
        self.synonym_dict = self.load_synonyms(synonym_file)

    def load_synonyms(self, synonym_file):
        synonyms = {}
        with open(synonym_file, 'r') as file:
            for lines in file:
                removals = lines.strip()
                key = removals.split(':')[0]
                value = removals.split(':')[1]
                withoutspace = value.split(',')  # use split again to turn into a list
                synonyms[key] = withoutspace
        return synonyms

    def random_spinner(self, text, Change_word_probability=30):
        words = text.split()  #Split the input text into words
        spun_element = []

        for word in words:
            if word in self.synonym_dict:     #Randomly choose a synonym
                if random.randint(1, 100) <= Change_word_probability:
                    synonym_list = self.synonym_dict[word]
                    substitutes = random.choice(synonym_list)
                    spun_element.append(substitutes)
                else:
                    spun_element.append(word)
            else:
                spun_element.append(word)

        spun_text = ""
        for word in spun_element:
            spun_text += word + " "

        return spun_text
