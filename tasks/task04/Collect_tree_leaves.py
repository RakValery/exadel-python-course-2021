#Task 04: Collect tree leaves
def collect_leaves(node):
    assert isinstance(node, (dict, list)), f"tree structure is broken, \nnode={node}\nnode type is {type(node)}\nexpected type: list or dict" 
    if type(node) == dict:
        res = []
        for item in node.values():
            res += collect_leaves(item)
        return res
    else:
        return node
tree = {
   "node1": {
       "node11": {
           "node111": [1, 2, 3],
           "node112": [4, 5]
       },
       "node12": [6]
   },
   "node2": [7, 8, 9]
}

broken_tree = {
   "node1": {
       "node11": {
           "node111": "broken_branch",
           "node112": [4, 5]
       },
       "node12": [6]
   },
   "node2": [7, 8, 9]
}

expected_leaves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = collect_leaves(tree)
assert result == expected_leaves

expected_leaves = [1, 2, 3]
result = collect_leaves([1, 2, 3])
assert result == expected_leaves

expected_leaves = [4, 5, 6, 7, 8, 9]
result = collect_leaves(broken_tree)
assert result == expected_leaves