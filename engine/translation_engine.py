from typing import Protocol


class TranslationEngine(Protocol):
    def translate(self, text: str, source_language: str, target_language: str) -> str:
        """
        Receives a text in source_language and converts it into
        target_language before returning the translated text.
        """
        pass
