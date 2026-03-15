from ctranslate2 import Translator
from data.constants import models_paths
from data.loaded_translation_pair import LoadedTranslationPair
from sentencepiece import SentencePieceProcessor


class CTranslate2Engine:
    """Translator engine class CTranslate2 library implementation"""

    def __init__(self):
        self.loaded_pairs = {}

        for model_key in models_paths:
            translator = Translator(models_paths[model_key]["translator"], device="cpu")

            source_processor = SentencePieceProcessor()
            source_processor.load(models_paths[model_key]["source_processor"])

            target_processor = SentencePieceProcessor()
            target_processor.load(models_paths[model_key]["target_processor"])

            self.loaded_pairs[model_key] = LoadedTranslationPair(
                translator=translator,
                source_processor=source_processor,
                target_processor=target_processor,
            )

    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        model_key = f"{source_lang}-{target_lang}"
        if f"{source_lang}-{target_lang}" not in models_paths:
            raise ValueError(
                f"Model path for {source_lang}-{target_lang} language pair not availiable."
            )
        elif f"{source_lang}-{target_lang}" not in self.loaded_pairs:
            raise ValueError(
                f"Loaded model for {source_lang}-{target_lang} language pair not availiable."
            )

        source_tokens = self.loaded_pairs[model_key].source_processor.encode(
            text, out_type=str
        )
        results = self.loaded_pairs[model_key].translator.translate_batch(
            [source_tokens]
        )
        target_tokens = results[0].hypotheses[0]
        return self.loaded_pairs[model_key].target_processor.decode(target_tokens)
