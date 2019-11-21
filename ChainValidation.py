import datetime
import hashlib


class ChainValidation:
    name = None

    # Check to see if the previous (blockD) gen_hash value stored in the current block (blockE) match.
    def head_check(self, blockchain_to_check):
        blocks = blockchain_to_check.get_all_blocks()
        all_clear = True
        print("======= Checking All Block Links =======")
        for da_block in blocks:
            if da_block.get_next_block() is not None:
                if da_block.gen_hash() != da_block.next.previous_hash:
                    print("Blockchain it not linked properly: " + da_block.data + " and " + da_block.get_next_block().data + " have conflicting gen_hash records.")
                    all_clear = False
        if all_clear:
            print("--- All blocks are properly linked ---")

    # This function will dynamically generate the hash for the current block and will compare it
    # to the previous_hash value of the block ahead
    def integrity_check_new(self, blockchain_to_check):
        print("==== Dynamically checking block hash integrity with previous hash ====")
        blocks = blockchain_to_check.get_all_blocks()
        invalid_blocks = 0
        for block in blocks:
            if block.next is not None:
                the_hasher = hashlib.sha256()
                the_hasher.update(str(block.nonce).encode('utf-8'))
                the_hasher.update(block.data.encode('utf-8'))
                the_hasher.update(str(block.previous_hash).encode('utf-8'))
                the_hasher.update(str(block.blockNo).encode('utf-8'))
                the_hasher.update(str(block.timestamp).encode('utf-8'))
                hash = the_hasher.hexdigest()
                if hash != block.next.previous_hash:
                    print("Block integrity check failure for: " + block.data)
                    invalid_blocks += 1
        if invalid_blocks > 0:
            print("The chain has integrity issues, please see messages for details.")
        else:
            print("Blockchain Integrity is good.")
        print("==== Integrity check complete ====")
