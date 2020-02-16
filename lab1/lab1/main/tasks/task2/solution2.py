from lab1.main.tasks.task2.sentence_builder import SentenceBuilder


class Solution2:
    def __init__(self):
        self.__sentence_builder = SentenceBuilder()

    def set_input(self, text):
        self.__sentence_builder.text = text

    def execute(self):
        return self.__sentence_builder.build_sentence_from_frequent_words(10)
