from random import randint
class Node(object):
    def __init__(self,v):
        self.value = v
        self.left  = None
        self.right = None

def build_Bitree(n):
    assert n > 0
    lb = 0
    ub = 29 if n < 29 else n
    nums = []
    for _ in range(n):
        trial = randint(lb,ub)
        while trial in nums:
            trial = randint(lb,ub)
        nums.append(trial)
    root = Node(nums[0])
    print('nums:',nums)
    for v in nums[1:]:
        p = root
        while True:
            if v < p.value:
                if None == p.left:
                    p.left = Node(v)
                    break
                else:
                    p = p.left
            elif v > p.value:
                if None == p.right:
                    p.right = Node(v)
                    break
                else:
                    p = p.right
            else:
                break
    return root


def bitree_search(root,value):
    assert isinstance(root,Node)
    q = root
    p = root
    while True:
        if value < p.value:
            if None == p.left:
                return q
            q,p = p,p.left
        elif value > p.value:
            if None == p.right:
                return p
            q,p = p,p.right
        else:
            return p
    return None


def print_tree_node(node):
    assert isinstance(node, Node)
    print(node.value)


def print_bitree_simple(root,depth=0):
    if None == root:
        return
    print('   '*depth,root.value)
    print_bitree_simple(root.left,depth+1)
    print_bitree_simple(root.right,depth+1)

def print_tree_horizontally(root, print_func, depth, branch, item_width=3):
    if None == root:
        return
    for i in range(depth):
        twig = '-' if i == depth - 1 else ' '
        if branch[i]:
            print("|",end='');
        else:
            print(twig,end='');

        for _ in range(item_width):
            print(twig,end='');

    print_func(root)

    # print the branch only when the tree has right children.
    if len(branch) <= depth:
        branch.append(False)
    if (root.right):
        branch[depth] = True
    print_tree_horizontally(root.left, print_func, depth+1, branch)
    branch[depth] = False;
    print_tree_horizontally(root.right, print_func, depth+1, branch)


def test():
    n = 13
    root = build_Bitree(n)
    print_bitree_simple(root)
    print_tree_horizontally(root, print_tree_node, 0, [])
    value = randint(2,29)
    node = bitree_search(root,value)
    print(value, ':', node.value)

if __name__ == '__main__':
    test()