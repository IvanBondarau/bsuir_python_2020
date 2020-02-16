from lab1.main.tasks.task1.text_wrapper import TextWrapper


class Solution1:

    def __init__(self):
        self.__text_wrapper = TextWrapper()

    def set_input(self, text):
        self.__text_wrapper.text = text

    def execute(self):
        return self.__text_wrapper.count_words()
