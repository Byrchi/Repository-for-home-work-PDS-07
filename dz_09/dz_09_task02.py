class TextProcessor:
    def __init__(self):
        self._punctuation_marks = [',', '.', '!', '?', ';', ':', '-', '(', ')', '[', ']', '{', '}', "'", '"', "/", "\\"]

    def get_clean_string(self, text):
        clean_text = ''
        for i in text:
            if not self._is_punctuation(i):
                clean_text += i
        return clean_text

    def _is_punctuation(self, marks):
        return marks in self._punctuation_marks


class TextLoader:
    def __init__(self):
        self._text_processor = TextProcessor()
        self._clean_string = ''

    def set_clean_text(self, text):
        self._clean_string = self._text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print("Виводиться очищений текст : ")
        return self._clean_string


class DataInterface:
    def __init__(self):
        self._text_loader = TextLoader()

    def process_text(self, list_of_text):
        for text in list_of_text:
            self._text_loader.set_clean_text(text)
            print(self._text_loader.clean_string)


# Приклад використання класів

data_interface = DataInterface()
texts = ["Lorem ipsum, (or lipsum) as it!", ";Привіт, Світ!\\",]
data_interface.process_text(texts)
