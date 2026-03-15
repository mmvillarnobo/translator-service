from dataclasses import dataclass

from ctranslate2 import Translator
from sentencepiece import SentencePieceProcessor


@dataclass
class LoadedTranslationPair:
    translator: Translator
    source_processor: SentencePieceProcessor
    target_processor: SentencePieceProcessor
