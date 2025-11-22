from block import Block

class Blockchain:

    #i made difficult 4 not 1 because im looking for 0 nonce not 000

    def __init__(self):
        self.chain = []
        #hna difficult
        ######################################""
        self.difficulty = 4
        ########################################
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(0, "Genesis Block", "0")
        genesis.mine_block(self.difficulty)
        self.chain.append(genesis)
        
    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_hash = self.get_last_block().hash
        new_block = Block(len(self.chain), data, previous_hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        #n7sab average nonce here
        ###############################################
    def calculate_average_nonce(self):
        total_nonce = sum(block.nonce for block in self.chain)
        num_blocks = len(self.chain)
        if num_blocks > 0:
            average = total_nonce / num_blocks
            return average
        return 0
    ####################################################

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            
            if current_block.previous_hash != previous_block.hash:
                print("Chain validation FAILED: Previous Hash mismatch!")
                return False
            
           
            if not current_block.hash.startswith("0" * self.difficulty):
                print("Chain validation FAILED: Hash difficulty not respected!")
                return False

           
            if current_block.hash != current_block.calculate_hash():
                print("Chain validation FAILED: Block hash is invalid/tampered!")
                return False

        return True