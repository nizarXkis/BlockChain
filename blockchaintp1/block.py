import hashlib
import time
import json

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        prefix = "0" * difficulty
        print(f"Mining Block {self.index}...")
        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block {self.index} mined successfully: {self.hash}\n")

    def __str__(self):
        return f"Block #{self.index}\n Hash: {self.hash}\n Previous Hash: {self.previous_hash}\n Data: {self.data}\n Nonce: {self.nonce}\n"