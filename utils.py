def read_classification_from_file(filename):
    with open(filename, 'r', encoding="UTF-8") as file:
        classifications = {}
        for line in file.readlines():
            name_class = line.split()
            classifications[name_class[0]] = name_class[1]
        return classifications
    