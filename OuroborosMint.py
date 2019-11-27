from OuroborosNode import OuroborosNode
import random
# Author: Glenn Dollard.

# See ref: https://cardanodocs.com/cardano/proof-of-stake/

# This recursive function represents the MPC which is a part of the Ouroboros PoS algorithm.
# It takes a list of nodes and tells each one to toss a coin. It will then
# compare the result with the next node's toss. If they match it will proceed to check the next node's
# toss etc. The function will return if and only if all nodes randomly toss the same number.
def get_multiparty_computation(nodes_array, value):
    if len(nodes_array) == 0:
        # print("Reached the end, common toss is: ", value)
        return value
    else:
        random = nodes_array[0].coin_toss()
        if random == value:
            # print("Match found, continue to next node")
            return get_multiparty_computation(nodes_array[1:], value)
        else:
            # print("Run of matches ended, start all over again")
            return -1


# Does the bootstrapping for Ouroboros, gets the number of nodes and initialises them with stake
def bootstrap_ouroboros():
    nodes = []
    num_nodes = input("Enter the number of Nodes: ")
    try:
        num_nodes = int(num_nodes)
    except ValueError:
        print("Invalid argument supplied, quitting.")
        # quit the program if we have invalid data
        exit()
    counter = 0
    while counter < num_nodes:
        new_node = OuroborosNode(random.randrange(1,101), "ouroboros_node_" + str(counter))
        nodes.append(new_node)
        counter += 1
    return nodes

# This function takes a list of nodes and produces a list of tickets, each ticket has its node as the entry
def get_tickets_for_nodes(nodes):
    tickets = []
    for node in nodes:
        for index in range(node.stake):
            tickets.append(node.id)
    return tickets


