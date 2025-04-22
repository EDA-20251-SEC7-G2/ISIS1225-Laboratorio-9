from DataStructures.Tree import rbt_node as rbtn
from DataStructures.List import single_linked_list as sl
from DataStructures.List import array_list as al

def new_map():
    dev = {
        'root': None,
        'type': 'RBT'
    }
    return dev

def flip_node_color(node_rbt):
    if node_rbt['color'] == "RED":
        node_rbt['color'] = "BLACK"
    else:
        node_rbt['color'] = "RED"
    return node_rbt

def flip_colors(node_rbt):
    if node_rbt["left"] and node_rbt["right"]:
        node_rbt["color"] = "RED"
        node_rbt["left"]["color"] = "BLACK"
        node_rbt["right"]["color"] = "BLACK"
    return node_rbt

def rotate_right(node_rbt):
    izq = node_rbt['left']
    node_rbt['left'] = izq['right']
    izq['right'] = node_rbt
    izq['color'] = node_rbt['color']
    node_rbt['color'] = "RED"
    return izq

def rotate_left(node_rbt):
    der = node_rbt['right']
    node_rbt['right'] = der['left']
    der['left'] = node_rbt
    der['color'] = node_rbt['color']
    node_rbt['color'] = "RED"
    return der

def insert_node(root, key, value):
    if root is None:
        return rbtn.new_node(key, value, "RED") 
    if root['key'] == key:
        root['value'] = value
        return root
    if key < root['key']:
        root['left'] = insert_node(root['left'], key, value)
    else:
        root['right'] = insert_node(root['right'], key, value)
    
    
    if (root['right'] is not None and root['right']['color'] == "RED" and 
        (root['left'] is None or root['left']['color'] == "BLACK")):
        root = rotate_left(root)
    
    if (root['left'] is not None and root['left']['color'] == "RED" and 
        root['left']['left'] is not None and root['left']['left']['color'] == "RED"):
        root = rotate_right(root)
        
    if (root['left'] is not None and root['right'] is not None and
        root['left']['color'] == "RED" and root['right']['color'] == "RED"):
        root = flip_colors(root)
    izquierda = size_tree(root['left'])
    derecha = size_tree(root['right'])
    root['size']= 1 + izquierda + derecha
    return root

def put (my_rbt, key, value):
    my_rbt['root'] = insert_node(my_rbt['root'], key, value)
    if my_rbt['root'] is not None:
        my_rbt['root']['color'] = "BLACK"
    return my_rbt
def get_node(root, key):
    if root is None:  
        return None
    elif key < root['key']:  
        if 'left' in root and root['left'] is not None:
            return get_node(root['left'], key)
        else:
            return None  
    elif key > root['key']:
        if 'right' in root and root['right'] is not None:
            return get_node(root['right'], key)
        else:
            return None  
    else:  
        return root

def get(my_rbt, key):
    if 'root' not in my_rbt or my_rbt['root'] is None:
        return None
    node = get_node(my_rbt['root'], key)
    if node is None:
        return None
    else:
        return node['value']

def contains(my_rbt, key):
    search = get(my_rbt,key)
    return True if search is not None else False

def size_tree(root):
    return 0 if root is None else root['size']

def is_empty(my_rbt):
    return True if my_rbt['root'] == None else False

def size(my_rbt):
    return size_tree(my_rbt['root'])

def get_max_node(root):
    if root['right'] is None:
        return root
    else:
        return get_max_node(root['right'])

def get_min_node(root):
    if root['left'] is None:
        return root
    else:
        return get_min_node(root['left'])
def get_max(my_rbt):
    if my_rbt['root'] is not None:
        return get_max_node(my_rbt['root'])['key']  
    return None

def get_min(my_rbt):
    if my_rbt['root'] is not None:
        return get_min_node(my_rbt['root'])['key']
    return None

def height(my_rbt):
    altura = height_tree(my_rbt['root'])
    return altura

def height_tree(root):
    if root is None:
        return 0
    else:
        return 1 + max(height_tree(root['left']), height_tree(root['right']))

def key_set(my_rbt):
    lista = sl.new_list()
    lista = key_set_tree(my_rbt['root'], lista)
    return lista

def key_set_tree(root, list):
    if root is not None:
        sl.add_last(list, root['key'])
        key_set_tree(root['left'], list)
        key_set_tree(root['right'], list)
    return list

def value_set(my_rbt):
    lista = sl.new_list()
    lista = value_set_tree(my_rbt['root'], lista)
    return lista

def value_set_tree(root, list):
    if root is not None:
        sl.add_last(list, root['value'])
        value_set_tree(root['left'], list)
        value_set_tree(root['right'], list)
    return list

def keys_range(root, key_initial, key_final, list_key):
    if root is None:
        return list_key
    if key_initial < root['key']:
        keys_range(root['left'], key_initial, key_final, list_key)
    if key_initial <= root['key'] <= key_final:
        sl.add_last(list_key, root['key'])
    if root['key'] < key_final:
        keys_range(root['right'], key_initial, key_final, list_key)

def keys(my_rbt, key_initial, key_final):
    key_list = sl.new_list()
    keys_range(my_rbt['root'], key_initial, key_final, key_list)
    return key_list

def values_range(root, key_initial, key_final, list_values):
    if root is None:
        return list_values
    if key_initial < root['key']:
        values_range(root['left'], key_initial, key_final, list_values)
    if key_initial <= root['key'] <= key_final:
        al.add_last(list_values, root['value'])
    if root['key'] < key_final:
        values_range(root['right'], key_initial, key_final, list_values)

def values(my_rbt, key_initial, key_final):
    values_list = al.new_list()
    values_range(my_rbt['root'], key_initial, key_final, values_list)
    return values_list
        
    

        
        
        
        