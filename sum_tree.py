import AVL_tree
import binary_tree


def get_sum(root):

    if root is None:
        return 0
    left_sum = get_sum(root.left)
    current_key = root.key if isinstance(root, AVL_tree.AVLNode) else root.val
    if current_key is None:
        current_key = 0
    
    right_sum = get_sum(root.right)
    total_sum = current_key + left_sum + right_sum
    print(f"Current node: {current_key}, Left sum: {left_sum}, Right sum: {right_sum}, Total for subtree: {total_sum}")

    return total_sum


# Driver program to test the above functions
#Слід відмітити, що наявна реалізація бінарного дерева дозволяє вставляти дублюючі значення
#в той час, як реалізація АВЛ дерева не дозволяє. Тому суми дерев, згенерованих з однакових послідовностей
#будуть відрізнятись якщо в послідовності є дублі
root = None
keys = [10, 20, 30, 25, 28, 27, -1, 22, 13, 24, 31, 32]

for key in keys:
    root = AVL_tree.insert(root, key)

print(root)
print(f'Sum of AVL tree: {get_sum(root)}')


root = None
keys = [10, 20, 30, 25, 28, 27, -1, 22, 13, 24, 31, 32]

for key in keys:
    root = binary_tree.insert(root, key)

print(root)
print(f'Sum of Binary Search tree: {get_sum(root)}')