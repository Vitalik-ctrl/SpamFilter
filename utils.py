def read_classification_from_file(filename):
    with open(filename, 'r', encoding="UTF-8") as file:
        classifications = {}
        for line in file.readlines():
            name_class = line.split()
            classifications[name_class[0]] = name_class[1]
        return classifications


def write_dict_to_file(file, dictionary):
    with open(file, 'w', encoding='UTF-8') as file:
        for key, value in dictionary.items():
            file.write(f"{key} {value}\n")
