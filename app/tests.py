from engines.ctranslate2_engine import CTranslate2Engine

if __name__ == "__main__":
    translator_engine = CTranslate2Engine()
    print(translator_engine.translate("Eu sou uma frase sendo traduzida", "pt", "en"))
