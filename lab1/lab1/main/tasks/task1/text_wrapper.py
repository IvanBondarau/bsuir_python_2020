import logging


class TextWrapper:
    def __init__(self):
        self.__text = None

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        logging.info('New text is set')
        self.__text = value

    def count_words(self):
        self.assert_text_not_null()

        words = self.text.split()
        word_counts = dict()
        for word in words:
            if word in word_counts.keys():
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        return word_counts

    def assert_text_not_null(self):
        if self.text is None:
            logging.error('ValueError: trying to call method before setting input')
            raise ValueError('Input is not set')
