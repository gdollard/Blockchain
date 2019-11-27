import random
import time

from Block import Block
from OuroborosMint import get_tickets_for_nodes
from OuroborosMint import get_multiparty_computation
from OuroborosMint import bootstrap_ouroboros
from Tendermint import Tendermint
from ChainValidation import ChainValidation


# Author: G. Dollard
# Distributed Ledger Technology - Assignment 2 - Part B

class Blockchain:
    diff = 15;  # difficulty in mining
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

    # This is the original mine function from lab 4
    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.gen_hash(), 16) <= self.target:
                self.add_block(block)
                print("Block " + block.data + " successfully mine. It took " + str(block.nonce) + " hashes to mine.")
                break # break for now, until we have the mine function written
            else:
                block.nonce += 1

    # # perform the mining using the Ouroborous implementation of the mining/mint function
    def ouroboros_mint(self, block, ouroboros_nodes):
        elector_tickets = get_tickets_for_nodes(ouroboros_nodes)
        call_count = 1
        common_toss = get_multiparty_computation(ouroboros_nodes, ouroboros_nodes[0].coin_toss())
        while common_toss < 0:
            call_count += 1
            common_toss = get_multiparty_computation(ouroboros_nodes, ouroboros_nodes[0].coin_toss())

        if common_toss >= 0:
            # use the common toss to iteratively that number of times to produce a random number within the range of elector_tickets
            winning_ticket = 0
            for i in range(common_toss):
                winning_ticket = random.randrange(len(elector_tickets))

            # create a list of tokens, the greater the stake a node has the greater the number of tokens it has
            print("Selected Leader is: " + elector_tickets[winning_ticket] + " Winning Ticket: " + str(winning_ticket))
            print("Block: " + block.data + " successfully mined, it took : " + str(call_count) + " toin cosses across all nodes.")
            self.add_block(block)
        else:
            print("No coin toss value agreeed..")

    # perform the mining using the Tendermint implementation
    def tendermint_mint(self, block, tendermint_object):
        should_add = tendermint_object.begin(block)
        if should_add:
            self.add_block(block)
        else:
            print("Tendermint did not come to a consensus, block not added.")


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


def start_ouroboros_algorithm():
    start_time = time.time()
    chain = Blockchain()
    nodes = bootstrap_ouroboros()
    for i in range(10):
        block = Block('OuroborosBlock_' + str(i))
        chain.ouroboros_mint(block, nodes)
    elapsed_time = time.time() - start_time
    return (chain, elapsed_time)

def start_tendermint_algorithm():
    chain = Blockchain()
    tenderint = Tendermint()
    tenderint.bootstrap_tendermint()
    start_time = time.time()
    for i in range(10):
        block = Block('TendermintBlock_' + str(i))
        chain.tendermint_mint(block, tenderint)
    elapsed_time = time.time() - start_time
    return (chain, elapsed_time)

def start():
    print("Welcome, this will mine 10 blocks using one of the algorithms below, please enter required information: ")
    algorithm = input(
        "Select your Consensus Algorithm:\n 1. Ouroboros \n 2: Tendermint \n 3: Casper ")
    try:
        algorithm = int(algorithm)
    except ValueError:
        print("Invalid algorithm entered, quitting.")
        exit()

    if algorithm == 1:
        return start_ouroboros_algorithm()
    if algorithm == 2:
        return start_tendermint_algorithm()
    else:
        print("Invalid algorithm code entered, quitting.")
        exit(-1)

def validate_blocks(blockchain):
    valiator = ChainValidation()
    valiator.head_check(blockchain)
    valiator.integrity_check(blockchain)


tuple = the_blockchain = start()
validate_blocks(tuple[0])
tuple[0].print_all_blocks()
print(" >>>>> Elapsed Time >>>>>>: ", tuple[1])
