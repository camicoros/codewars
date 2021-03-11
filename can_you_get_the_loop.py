"""
link: https://www.codewars.com/kata/52a89c2ea8ddc5547a000863
You are given a node that is the beginning of a linked list. 
This list always contains a tail and a loop.

Your objective is to determine the length of the loop.

# Use the `next' attribute to get the following node
node.next
"""


def loop_size(node):
    nodes = []
    while not node in nodes:
        nodes.append(node)
        node = node.next
    return len(nodes) - nodes.index(node)


def main():
    # Make a short chain with a loop of 3
    node1 = Node()
    node2 = Node()
    node3 = Node()
    node4 = Node()
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print(loop_size(node1))

    # Make a longer chain with a loop of 29
    nodes = [Node() for _ in range(50)]
    for node, next_node in zip(nodes, nodes[1:]):
        node.next = next_node
    nodes[49].next = nodes[21]
    print(loop_size(nodes[0]))


if __name__ == "__main__":
    main()
