from Block import Block


class Blockchain:
    diff = 20; # difficulty in mining
    maxNonce = 2 ** 32;
    target = 2 ** (256-diff);

    def __init__(self):
        self.genesis = Block('Genesis', 0)
        self.head = self.genesis
        self.size = 1

    # Adds a block to the blockchain and sets it as the head block
    def add_block(self, data):
        self.size += 1;
        new_block = Block(data, self.size)
        new_block.set_hash()
        current_block = self.head

        while current_block.next is not None:
            current_block = current_block.get_next_block()
        current_block.set_next_block(new_block)

    def get_size(self):
        return self.size

    def print_all_blocks(self):
        blocks = []
        current_block = self.genesis
        blocks.append(current_block)
        while current_block.next is not None:
            current_block = current_block.next
            blocks.append(current_block)
        for x in blocks:
            print("-----------------------------------------")
            print(x.get_data())
            print(x.get_hash())
        print("================================================")

    def get_genesis(self):
        return self.genesis


def create_some_blocks():
    chain = Blockchain();

    # create come blocks
    counter = 0
    while counter < 9:
        chain.add_block('SampleBlock_' + counter)

    print(chain.get_size())
    chain.print_all_blocks()


create_some_blocks()




