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


x = [1, 2, 3, 4]
node1 = Node(5)
node2 = Node(10)
nodes = [node1, node2]


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
            print("No match found")
            return -1
        return value


# print(addition(x))
common_toss = get_common_toss(nodes, nodes[0].coin_toss())
while common_toss < 0:
    common_toss = get_common_toss(nodes, nodes[0].coin_toss())

print("What do I have?: " + str(common_toss))
def bla():
    main = RandomWeighted()
    node1 = Node(5)
    node2 = Node(10)

    nodes = [node1, node2]
    coin_toss = main.run_coin_toss(nodes)
    if (coin_toss >= 0):
        my_list = ['A'] * node1.stake + ['B'] * node2.stake
        print("Selected Leader is: " + my_list[coin_toss])
    else:
        print("No coin toss value agreeed..")

# bla()
