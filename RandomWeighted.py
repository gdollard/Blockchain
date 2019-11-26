from OuroborosNode import OuroborosNode
import random







def addition(array):
    if len(array) == 0:
        return 0;
    else:
        return array[0] + addition(array[1:])


def get_common_toss(random_maximum, nodes_array, value):
    #print("Looking for value: " + str(value))
    if len(nodes_array) == 0:
        print("Reached the end, common toss is: ", value)
        return value
    else:
        random = nodes_array[0].coin_toss(random_maximum)
        if random == value:
            #print("Match found, continue to next node")
            return get_common_toss(random_maximum, nodes_array[1:], value)
        else:
            #print("Run of matches ended, start all over again")
            return -1


# print(addition(x))


def bla():
    #main = RandomWeighted()
    nodeA = OuroborosNode(9)
    nodeB = OuroborosNode(5)
    nodeC = OuroborosNode(100)
    nodeD = OuroborosNode(50)
    nodeE = OuroborosNode(100)
    nodeF = OuroborosNode(50)
    nodeG = OuroborosNode(1100)
    nodeH = OuroborosNode(50)

    nodes = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH]

    # populate the array of all elector tickets
    elector_tickets = ['A'] * nodeA.stake + ['B'] * nodeB.stake + ['C'] * nodeC.stake + ['D'] * nodeD.stake + ['E'] * nodeE.stake + ['F'] * nodeF.stake + ['G'] * nodeG.stake + ['H'] * nodeH.stake

    call_count = 1
    common_toss = get_common_toss(len(elector_tickets), nodes, nodes[0].coin_toss(len(elector_tickets)))
    while common_toss < 0:
        call_count += 1
        common_toss = get_common_toss(len(elector_tickets), nodes, nodes[0].coin_toss(len(elector_tickets)))

    if common_toss >= 0:
        #use the common toss to iteratively that number of times to produce a random number within the range of elector_tickets
        winning_ticket = 0
        for i in range(common_toss):
            winning_ticket = random.randrange(len(elector_tickets))

        # create a list of tokens, the greater the stake a node has the greater the number of tokens it has
        print("Selected Leader is: " + elector_tickets[winning_ticket] + " Winning Ticket: " + str(winning_ticket))
        print("Number of independent coin toss rounds needed: ", call_count)
    else:
        print("No coin toss value agreeed..")

bla()
