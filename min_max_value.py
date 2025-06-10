import AVL_tree
import binary_tree

#найменший елемент дерева бінарного типу - найбільш лівий елемент дерева
#відповідно, найбільший - найбільш правий
def get_min_value(root):

    if not root:
        return None

    current = root

    while current.left:
        current = current.left

    if isinstance(current, AVL_tree.AVLNode):
        return current.key
    
    return current.val



def get_max_value(root):

    if not root:
        return None

    current = root

    while current.right:
        current = current.right

    if isinstance(current, AVL_tree.AVLNode):
        return current.key
    
    return current.val


# Driver program to test the above functions
root = None
keys = [10, 20, 30, 25, 28, 27, -1, 22, 13, 24, 27, 28, 31, 32]

for key in keys:
    root = AVL_tree.insert(root, key)

print(root)

print(f'min: {get_min_value(root)}')
print(f'max: {get_max_value(root)}')


root = None
keys = [10, 20, 30, 25, 28, 27, -1, 22, 13, 24, 27, 28, 31, 32]

for key in keys:
    root = binary_tree.insert(root, key)

print(root)

print(f'min: {get_min_value(root)}')
print(f'max: {get_max_value(root)}')
