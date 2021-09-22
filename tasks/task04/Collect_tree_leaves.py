#Task 04: Collect tree leaves
def collect_leaves(node):
    if not isinstance(node, (dict, list)):
        raise ValueError("ValueError: Tree structure is broken")
    if type(node) == dict:
        res = []
        for item in node.values():
            res.extend(collect_leaves(item))
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

tests = [
    [tree, [1, 2, 3, 4, 5, 6, 7, 8, 9]], 
    [[1, 2, 3], [1, 2, 3]], 
    [broken_tree, "ValueError: Tree structure is broken"]
    ]

for test in tests:
    result = False
    try:
        collect_leaves(test[0]) == test[1]
        result = True
    except ValueError as err:
        if str(err) == test[1]:
            result = True
    assert result
