def generator_file(file, words):
    with open(file, "r") as file_:
        for str in file_:
            if set(str.lower().split(' ')) & set(words.lower().split(' ')) != set():
                yield str
