from Node import Node







def addition(array):
    if len(array) == 0:
        return 0;
    else:
        return array[0] + addition(array[1:])


def get_common_toss(random_maximum, nodes_array, value):
    #print("Looking for value: " + str(value))
    if len(nodes_array) == 0:
        #print("Reached the end...")
        return value
    else:
        if nodes_array[0].coin_toss(random_maximum) == value:
            #print("Match found, continue")
            get_common_toss(random_maximum, nodes_array[1:], value)
        else:
            return -1
        return value


# print(addition(x))


def bla():
    #main = RandomWeighted()
    nodeA = Node(9)
    nodeB = Node(5000)
    nodeC = Node(100)
    nodeD = Node(50)
    nodeE = Node(100)
    nodeF = Node(50)
    nodeG = Node(100)
    nodeH = Node(50)

    nodes = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH]

    # populate the array of all elector tickets
    elector_tickets = ['A'] * nodeA.stake + ['B'] * nodeB.stake + ['C'] * nodeC.stake + ['D'] * nodeD.stake + ['E'] * nodeE.stake + ['F'] * nodeF.stake + ['G'] * nodeG.stake + ['H'] * nodeH.stake

    common_toss = get_common_toss(len(elector_tickets), nodes, nodes[0].coin_toss(len(elector_tickets)))
    while common_toss < 0:
        common_toss = get_common_toss(len(elector_tickets), nodes, nodes[0].coin_toss(len(elector_tickets)))

    if common_toss >= 0:
        # create a list of tokens, the greater the stake a node has the greater the number of tokens it has

        print("Selected Leader is: " + elector_tickets[common_toss] + " from tossing a: " + str(common_toss))
    else:
        print("No coin toss value agreeed..")

bla()
