from hashlib import sha256
from datetime import datetime
class Blockchain:
    blocks = []
    def AddBlock(self, block):
        self.blocks.append(block)
    def GetPrevHash(self):
        return self.blocks[-1].GetHash() 
    def __init__(self, difficulty):
        self.difficulty = difficulty
    def GetDifficulty(self):
        return self.difficulty
class Block:
    def __init__(self, index, prev_hash, text, difficulty):
        self.index = str(index)
        self.date = str(datetime.now())
        self.text = text
        self.prev_hash = str(prev_hash)
        self.hash = str(self.GenerateHash(difficulty))
    def GenerateHash(self, difficulty):
        self.minig_operations = 0
        hash = str(sha256((self.index + self.text + self.date + self.prev_hash + str(self.minig_operations)).encode()).hexdigest())
        IsDone = False
        while(not IsDone):
            IsDone = len([el for el in hash[0:difficulty] if el != '0']) == 0
            if(IsDone):
                return hash
            self.minig_operations+=1
            hash = str(sha256((self.index + self.text + self.date + self.prev_hash + str(self.minig_operations)).encode()).hexdigest())
    def GetHash(self):
        return self.hash

if __name__ == "__main__":
    difficulty = int(input("Enter difficulty: "))
    blockchain = Blockchain(difficulty)
    print(f"Mining block 0...")
    blockchain.AddBlock(Block(0, 0, f"Blok0", blockchain.GetDifficulty()))
    for i in range(1,10):
        print(f"Mining block {i}...")
        blockchain.AddBlock(Block(i, blockchain.GetPrevHash(), f"Blok{i}", blockchain.GetDifficulty()))

    for block in blockchain.blocks:
        print(f'Index: {block.index}')
        print(f'Date: {block.date}')
        print(f'Text: {block.text}')
        print(f'Hash: {block.hash}')
        print(f'Prev_hash: {block.prev_hash}')
        print(f'Mining Operations: {block.minig_operations}')