

def get_common_toss(random_maximum, nodes_array, value):
    #print("Looking for value: " + str(value))
    if len(nodes_array) == 0:
        #print("Reached the end, common toss is: ", value)
        return value
    else:
        random = nodes_array[0].coin_toss(random_maximum)
        if random == value:
            #print("Match found, continue to next node")
            return get_common_toss(random_maximum, nodes_array[1:], value)
        else:
            #print("Run of matches ended, start all over again")
            return -1