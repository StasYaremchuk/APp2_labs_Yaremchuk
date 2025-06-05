class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree_from_input(filename):
    with open(filename, 'r') as f:
        levels = []

        for line in f:
            stripped_line = line.strip()
            if stripped_line:
                parts = stripped_line.split()
                levels.append(parts)

    if not levels:
        return None

    root = Node(levels[0][0])
    queue = [root]
    idx = 1

    while idx < len(levels):
        current_level = levels[idx]
        next_queue = []
        i = 0

        for node in queue:

            if i < len(current_level) and current_level[i] != 'None':
                node.left = Node(current_level[i])
                next_queue.append(node.left)
            i += 1
            if i < len(current_level) and current_level[i] != 'None':
                node.right = Node(current_level[i])
                next_queue.append(node.right)
            i += 1

        queue = next_queue
        idx += 1

    return root


def min_depth(root):
    if not root:
        return 0

    queue = [(root, 1)]
    while queue:
        node, depth = queue.pop(0)
        if not node.left and not node.right:
            return depth
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return 0


tree_root = build_tree_from_input("input.txt")
depth = min_depth(tree_root)

with open("output.txt", "w") as f:
    f.write(str(depth))

print("Мінімальна глибина дерева:", depth)
