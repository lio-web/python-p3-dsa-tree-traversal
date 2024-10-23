class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        # Helper function to search recursively
        def find_element(node):
            if node.get('id') == id:
                return node
            for child in node.get('children', []):
                result = find_element(child)
                if result:
                    return result
            return None  # Only return None after all children are searched

        return find_element(self.root)
