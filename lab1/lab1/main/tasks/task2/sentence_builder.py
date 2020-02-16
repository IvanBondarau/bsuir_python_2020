from lab1.main.tasks.task1.text_wrapper import TextWrapper


class SentenceBuilder(TextWrapper):

    def build_sentence_from_frequent_words(self, max_num_of_words):
        super().assert_text_not_null()

        words_with_numbers = super().count_words()

        print(words_with_numbers)

        sorted_words_with_numbers = {key_: value for key_, value in
                                     sorted(words_with_numbers.items(), key=lambda item: item[1])}

        print(sorted_words_with_numbers)

        sorted_counts_keys = reversed(list(sorted_words_with_numbers.keys())[-max_num_of_words:])

        print(sorted_counts_keys)

        sentence = ''

        for word in sorted_counts_keys:
            sentence += word + ' '

        return sentence.strip()
