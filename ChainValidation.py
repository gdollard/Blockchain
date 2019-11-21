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

    # calculate the gen_hash indepdently and verify it against the stored gen_hash
    def integrity_check(self, blockchain_to_check):
        all_clear = True
        blocks = blockchain_to_check.get_all_blocks()
        print("======= Checking Integrity of Blocks and Data =======")
        for block in blocks:
            the_hasher = hashlib.sha256()
            the_hasher.update(str(block.nonce).encode('utf-8'))
            the_hasher.update(block.data.encode('utf-8'))
            the_hasher.update(str(block.previous_hash).encode('utf-8'))
            the_hasher.update(str(block.blockNo).encode('utf-8'))
            the_hasher.update(str(block.timestamp).encode('utf-8'))
            hash = the_hasher.hexdigest()

            if hash != block.gen_hash():
                print("Block: " + block.data + " has been tampered with since its inital creation, gen_hash does not re-compute")
                all_clear = False
        if all_clear:
            print("--- Blockchain is not tampered ---")
