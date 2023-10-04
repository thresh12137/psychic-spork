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
                withoutspace = value.split(',')
                synonyms[key] = withoutspace
        return synonyms
