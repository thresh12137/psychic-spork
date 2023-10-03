def read_synonym():
    synonym_list = []
    synonym_dictionary = {}
    with open("test-synonyms.txt") as file:
        for lines in file:
            removals = lines.strip()
            synonym_list.append(removals)
        for values in synonym_list:
            key = values.split(':')[0]
            value = values.split(":")[1]
            withoutspace = value.split(',')
            synonym_dictionary[key] = withoutspace
    return synonym_dictionary
test1 = read_synonym()
print((test1))