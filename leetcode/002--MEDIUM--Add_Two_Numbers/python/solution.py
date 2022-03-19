# ---------------------------------------------------------------------------------------
#
#  Title:      Add two numbers
#
#  Link:       https://leetcode.com/problems/add-two-numbers/
#
#  Difficulty: Medium
#
#  Language:   Python
#
# ---------------------------------------------------------------------------------------

class Node():
    def __init__(self, val=0):
        self.val = val
        self.next = None


def recurse(p, l1, l2):
    if l1 != None and l2 != None:
        p = Node(l1.val + l2.val)
        p.next = recurse(p.next, l1.next, l2.next)
    return p

def add_two_numbers(l1,l2):
    return recurse(None,l1,l2)


def push(node, i):
    if node == None:
        node = Node(i)
    else:
        node.next = push(node.next, i)
    return node

def printit(q):
    if q != None:
        print(q.val)
        printit(q.next)

if __name__ == "__main__":
    l1 = None
    l2 = None

    for i in [2,4,3]:
        l1 = push(l1,i)
    for i in [5,6,4]:
        l2 = push(l2,i)

    q = add_two_numbers(l1,l2)
    printit(q)
