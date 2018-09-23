import hashlib as hasher
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()

def genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")

def new_block(old_block):
    new_index = old_block.index + 1
    new_timestamp = date.datetime.now()
    new_data = "Block #" + str(new_index)
    new_previous_hash = old_block.hash_block()
    return Block(new_index, new_timestamp, new_data, new_previous_hash)

blockchain = [genesis_block()]
previous_block = blockchain[0]

for i in range(0, 20):
    block_to_add = new_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    print(block_to_add.index)
