#Task 04: Collect tree leaves
def collect_leaves(node):
    assert isinstance(node, (dict, list))  
    if type(node) == dict:
        res = []
        for item in node.values():
            res.extend(collect_leaves(item))
        return res
    elif type(node) == list:
        return node
    else:
        return "tree structure is broken" 

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
    [broken_tree, "Assertion Error: Tree structure is broken"]
    ]

for test in tests:
    try:
        collect_leaves(test[0]) == test[1]
        result = True
    except AssertionError:
        result = False     
    assert result, f"{test[0]}\n{test[1]}"
