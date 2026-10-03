from collections import deque


class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return []
        queue = deque([root])
        results = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            results.append(level)
        return results[::-1]
