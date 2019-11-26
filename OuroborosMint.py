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
