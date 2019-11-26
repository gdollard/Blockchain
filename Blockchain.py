from Block import Block
from Node import Node
from OuroborosMint import get_common_toss
import random
import time

from ChainValidation import ChainValidation


# Author: G. Dollard
# Distributed Ledger Technology - Lab 1

class Blockchain:
    diff = 15;  # difficulty in mining
    maxNonce = 2 ** 32;
    target = 2 ** (256 - diff);
    block = Block('Genesis')
    root = head = block  # linked list thing

    # Ouroboros nodes
    nodeA = Node(9)
    nodeB = Node(5)
    nodeC = Node(100)
    nodeD = Node(50)
    nodeE = Node(100)
    nodeF = Node(50)
    nodeG = Node(1100)
    nodeH = Node(50)
    nodes = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH]

    # populate the array of all elector tickets
    elector_tickets = ['A'] * nodeA.stake + ['B'] * nodeB.stake + ['C'] * nodeC.stake + ['D'] * nodeD.stake + [
        'E'] * nodeE.stake + ['F'] * nodeF.stake + ['G'] * nodeG.stake + ['H'] * nodeH.stake

    # Adds a block to the blockchain and sets it as the head block
    def add_block(self, block):
        block.previous_hash = self.block.gen_hash()
        block.blockNo = self.block.blockNo + 1
        self.block.next = block
        self.block = self.block.next

    # Just delegating to add_block for now
    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.gen_hash(), 16) <= self.target:
                self.add_block(block)
                print("Block " + block.data + " successfully mine. It took " + str(block.nonce) + " hashes to mine.")
                break # break for now, until we have the mine function written
            else:
                block.nonce += 1

    # This is the Ouroborous implementation of the mining/mint function
    def ouroboros_mint(self, block):
        call_count = 1
        common_toss = get_common_toss(self.nodes, self.nodes[0].coin_toss())
        while common_toss < 0:
            call_count += 1
            common_toss = get_common_toss(self.nodes, self.nodes[0].coin_toss())

        if common_toss >= 0:
            # use the common toss to iteratively that number of times to produce a random number within the range of elector_tickets
            winning_ticket = 0
            for i in range(common_toss):
                winning_ticket = random.randrange(len(self.elector_tickets))

            # create a list of tokens, the greater the stake a node has the greater the number of tokens it has
            print("Selected Leader is: " + self.elector_tickets[winning_ticket] + " Winning Ticket: " + str(winning_ticket))
            print("Block: " + block.data + " successfully mined, it took : " + str(call_count) + " toin cosses across all nodes.")
            self.add_block(block)
        else:
            print("No coin toss value agreeed..")


    # Utility function to print out all the blocks and their details
    def print_all_blocks(self):
        blocks = []
        current_block = self.root
        blocks.append(current_block)
        print('\n')
        print("--- Printout Blocks --- ")
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
        #chain.mine(block)
        chain.ouroboros_mint(block)
        counter += 1
    return chain


def validate_blocks(blockchain):
    valiator = ChainValidation()
    valiator.head_check(blockchain)
    valiator.integrity_check(blockchain)

start_time = time.time()
the_blockchain = create_some_blocks()
validate_blocks(the_blockchain)
the_blockchain.print_all_blocks()
elapsed_time = time.time() - start_time
print("Elapsed time: ", elapsed_time)
