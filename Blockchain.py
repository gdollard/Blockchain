from Block import Block
from ChainValidation import ChainValidation


# Author: G. Dollard
# Distributed Ledger Technology - Lab 1

class Blockchain:
    diff = 20;  # difficulty in mining
    maxNonce = 2 ** 32;
    target = 2 ** (256 - diff);
    block = Block('Genesis')
    root = head = block  # linked list thing

    # Adds a block to the blockchain and sets it as the head block
    def add_block(self, block):
        block.previous_hash = self.block.hash
        block.blockNo = self.block.blockNo + 1
        self.block.next = block
        self.block = self.block.next

    # Just delegating to add_block for now
    def mine(self, block):
        for n in range(self.maxNonce):
            self.add_block(block)
            break # break for now, until we have the mine function written

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
            print("Block Data: " + x.get_data())
            print("Block No: " + str(x.get_block_no()))
            print("Creation Date: " + str(x.get_creation_date()))
            print("Hash: " + x.get_hash())
            print("Previous Hash: " + str(x.get_previous_hash()))
            if x.get_next_block() is not None:
                print("Next block: " + x.get_next_block().get_data())
            else:
                print("Next block: - ")
            print("====================================================================")

    def get_all_blocks(self):
        blocks = []
        current_block = self.block
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
