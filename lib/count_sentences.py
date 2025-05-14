#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        """Returns True if the value ends with a period, False otherwise."""
        return self._value.endswith(".")

    def is_question(self):
        """Returns True if the value ends with a question mark, False otherwise."""
        return self._value.endswith("?")

    def is_exclamation(self):
        """Returns True if the value ends with an exclamation mark, False otherwise."""
        return self._value.endswith("!")

    def count_sentences(self):
        """Returns the number of sentences in the value."""
        if not self._value:
            return 0
        # Normalize sentence-ending punctuation and split by periods
        sentences = [s for s in self._value.replace("!", ".").replace("?", ".").split(".") if s.strip()]
        return len(sentences)
