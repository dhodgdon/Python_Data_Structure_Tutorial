class Tree:

    class Node:

        def __init__(self, data, children):
            self.data = data
            self.children = children

        def __str__(self):
            return self.data + ', '
    
    def __init__(self):
        self.root = Tree.Node('a', [Tree.Node("b", [Tree.Node("d", []), Tree.Node("e", [])]), Tree.Node("c", [Tree.Node("f", []), Tree.Node("g", [])])])
    
    def traverse_dfs(self):
        node = self.root

        def _traverse_dfs(node):

            print(node, end='')

            if node.children == []:
                return
            
            for child in node.children:
                _traverse_dfs(child)

        _traverse_dfs(node)

tree = Tree()
tree.traverse_dfs()