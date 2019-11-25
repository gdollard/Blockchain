from Node import Node


class RandomWeighted:

    def run_coin_toss(self, nodes):
        coins_match = False
        while not coins_match:
            initial_value = nodes[0].coin_toss()
            for node in nodes:
                if node.coin_toss() == initial_value:
                    continue
            if coins_match:
                return initial_value


#x = [1, 2, 3, 4]
#node1 = Node(5)
#node2 = Node(10)
#nodes = [node1, node2]


def addition(array):
    if len(array) == 0:
        return 0;
    else:
        return array[0] + addition(array[1:])


def get_common_toss(nodes_array, value):
    print("Looking for value: " + str(value))
    if len(nodes_array) == 0:
        print("Reached the end...")
        return value
    else:
        if nodes_array[0].coin_toss() == value:
            print("Match found, continue")
            get_common_toss(nodes_array[1:], value)
        else:
            return -1
        return value


# print(addition(x))


def bla():
    main = RandomWeighted()
    node1 = Node(5)
    node2 = Node(10)
    nodes = [node1, node2]

    need to update the random number gen to ensure any number from the size of my_list can be generated

    common_toss = get_common_toss(nodes, nodes[0].coin_toss())
    while common_toss < 0:
        common_toss = get_common_toss(nodes, nodes[0].coin_toss())

    if common_toss >= 0:
        # create a list of tokens, the greater the stake a node has the greater the number of tokens it has
        my_list = ['A'] * node1.stake + ['B'] * node2.stake
        print("Selected Leader is: " + my_list[common_toss])
    else:
        print("No coin toss value agreeed..")

bla()
