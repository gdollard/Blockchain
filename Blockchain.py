from Block import Block
from ChainValidation import ChainValidation


# Author: G. Dollard
# Distributed Ledger Technology - Lab 1

class Blockchain:
    diff = 1;  # difficulty in mining
    maxNonce = 2 ** 32;
    target = 2 ** (256 - diff);
    block = Block('Genesis')
    root = head = block  # linked list thing

    # Adds a block to the blockchain and sets it as the head block
    def add_block(self, block):
        block.previous_hash = self.block.gen_hash()
        block.blockNo = self.block.blockNo + 1
        self.block.next = block
        self.block = self.block.next

    # Just delegating to add_block for now
    def mine(self, block):
        print("Mining block: " + block.data)
        for n in range(self.maxNonce):
            if int(block.gen_hash(), 16) <= self.target:
                self.add_block(block)
                print("Block Mined...")
                break # break for now, until we have the mine function written
            else:
                block.nonce += 1

    # Utility function to print out all the blocks and their details
    def print_all_blocks(self):
        blocks = []
        current_block = self.root
        blocks.append(current_block)
        print('\n')
        print("--- Blocks --- ")
        while current_block.next is not None:
            current_block = current_block.next
            blocks.append(current_block)
        for x in blocks:
            print("Block Data: " + x.data)
            print("Block No: " + str(x.blockNo))
            print("Creation Date: " + str(x.timestamp))
            print("Hash: " + x.gen_hash())
            print("Previous Hash: " + str(x.previous_hash))
            if x.get_next_block() is not None:
                print("Next block: " + x.get_next_block().data)
            else:
                print("Next block: - ")
            print("====================================================================")

    def get_all_blocks(self):
        blocks = []
        current_block = self.root
        blocks.append(current_block)
        while current_block.next is not None:
            current_block = current_block.next
            blocks.append(current_block)
        return blocks


# Create some blocks and return the entire blockchain
def create_some_blocks():
    chain = Blockchain()

    # create come blocks
    counter = 0
    while counter < 9:
        block = Block('SampleBlock_' + str(counter))
        chain.mine(block)
        counter += 1
    return chain


def validate_blocks(blockchain):
    valiator = ChainValidation()
    valiator.head_check(blockchain)
    valiator.integrity_check(blockchain)


the_blockchain = create_some_blocks()
validate_blocks(the_blockchain)
the_blockchain.print_all_blocks()
