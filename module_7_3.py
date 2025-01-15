



class WordsFinder:
    file_names = []
    def __init__(self, *files):
        self.files = list(files)
        for i in self.files:
            self.file_names.append(i)


    global all_words
    all_words = {}

    def get_all_words(self):
        for i in self.files:
            with open(i, encoding="utf-8") as file:
                all_words[i] = file.read().lower().split()
        return all_words

    def find(self, word):
        new_dict = {}
        finder2.get_all_words()
        for name, list_ in all_words.items():
            for i in list_:
                if str(i) == word.lower():
                    new_dict[name] = list_.index(i) + 1
        return new_dict


    def count(self, word):
        new_dict = {}
        count = 0
        finder2.get_all_words()
        for name, list_ in all_words.items():
            for i in list_:
                if str(i) == word.lower():
                    count += 1
                    new_dict[name] = count
        return new_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT'))