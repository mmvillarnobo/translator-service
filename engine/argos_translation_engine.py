from argostranslate.translate import translate


class ArgosTranslationEngine:
    def translate(self, text: str, source_language: str, target_language: str) -> str:
        """
        Receives a text in source_language and converts it into
        target_language before returning the translated text.
        """
        return translate(text, source_language, target_language)
