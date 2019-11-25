from Node import Node

node1 = Node(2)
node2 = Node(3)
node3 = Node(3)

nodes = [node1, node2, node3]

# takes the list of nodes and recursively calls a coin toss on them. It will keep
# calling along the list as long as they all toss the same value. If there is one
# failure the entire procedure terminates and -1 is returned. If all nodes successfully
# toss the same number then that number is returned.
def perform_rand_recursion(the_nodes, value):
    if len(the_nodes) == 0:
        print("Reached the end, we have a common random: ", value)
        return value
    else:
        random = the_nodes[0].gen_rand()
        if random == value:
            print("Match found, continue with next node")
            return perform_rand_recursion(the_nodes[1:], value)
        else:
            print("Run of matches ended, start all over again")
            return -1


random_consensus = perform_rand_recursion(nodes, nodes[0].gen_rand())
call_count = 0
while random_consensus < 0:
    call_count += 1
    random_consensus = perform_rand_recursion(nodes, nodes[0].gen_rand())

print("Found a consensus random: ", random_consensus)
print("Call count: ", call_count)
