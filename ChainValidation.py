import datetime
import hashlib


class ChainValidation:
    name = None

    def __init__(self):
        self.name = "hello"

    # Check to see if the previous (blockD) hash value stored in the current block (blockE) match.
    def head_check(self, blockchain_to_check):
        blocks = blockchain_to_check.get_all_blocks()
        chain_length = len(blocks)
        chain_index = chain_length-1
        previous_hash = None
        for da_block in blocks:
            if da_block.get_next_block() is not None:
                if da_block.get_hash() != da_block.get_next_block().get_previous_hash():
                    print("Blockchain it not linked properly: " + da_block.get_data() + " and " + da_block.get_next_block().get_data() + " have conflicting hash records.")
                    return
        print("All blocks are properly linked.")

    #def integrity_check(self):