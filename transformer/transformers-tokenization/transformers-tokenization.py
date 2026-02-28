import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        
        # Step 1: Special tokens पहले add करो
        special_tokens = [
            self.pad_token,   # 0
            self.unk_token,   # 1
            self.bos_token,   # 2
            self.eos_token    # 3
        ]
        
        for token in special_tokens:
            self.word_to_id[token] = self.vocab_size
            self.id_to_word[self.vocab_size] = token
            self.vocab_size += 1
        
        # Step 2: Real words add करो
        for text in texts:
            for word in text.lower().split():
                if word not in self.word_to_id:  # duplicate नहीं
                    self.word_to_id[word] = self.vocab_size
                    self.id_to_word[self.vocab_size] = word
                    self.vocab_size += 1
    
    def encode(self, text: str) -> List[int]:
        ids = []
        for word in text.lower().split():
            if word in self.word_to_id:
                ids.append(self.word_to_id[word])  # word मिला ✅
            else:
                ids.append(self.word_to_id[self.unk_token])  # UNK ❌
        return ids
    
    def decode(self, ids: List[int]) -> str:
        words = []
        for id in ids:
            if id in self.id_to_word:
                words.append(self.id_to_word[id])  # ID मिली ✅
            else:
                words.append(self.unk_token)  # UNK ❌
        return " ".join(words)