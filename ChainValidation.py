import datetime
import hashlib


class ChainValidation:
    name = None

    # Check to see if the previous (blockD) hash value stored in the current block (blockE) match.
    def head_check(self, blockchain_to_check):
        blocks = blockchain_to_check.get_all_blocks()
        all_clear = True
        print("======= Checking All Block Links =======")
        for da_block in blocks:
            if da_block.get_next_block() is not None:
                if da_block.get_hash() != da_block.get_next_block().get_previous_hash():
                    print("Blockchain it not linked properly: " + da_block.get_data() + " and " + da_block.get_next_block().get_data() + " have conflicting hash records.")
                    all_clear = False
        if all_clear:
            print("--- All blocks are properly linked ---")

    # calculate the hash indepdently and verify it against the stored hash
    def integrity_check(self, blockchain_to_check):
        all_clear = True
        blocks = blockchain_to_check.get_all_blocks()
        print("======= Checking Integrity of Blocks and Data =======")
        for block in blocks:
            the_hasher = hashlib.sha256()
            the_hasher.update(block.get_data().encode('utf-8'))
            the_hasher.update(str(block.get_block_no()).encode('utf-8'))
            the_hasher.update(str(block.get_creation_date()).encode('utf-8'))
            hash = the_hasher.hexdigest()
            if hash != block.get_hash():
                print("Block: " + block.get_data() + " has been tampered with since its inital creation, hash does not re-compute")
                all_clear = False
        if all_clear:
            print("--- Blockchain is not Tempered ---")
