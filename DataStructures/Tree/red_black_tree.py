import rbt_node as rbt

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
        return rbt.new_node(key, value, "RED") 
    
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
    
    return root

def put (my_rbt, key, value):
    my_rbt['root'] = insert_node(my_rbt['root'], key, value)
    if my_rbt['root'] is not None:
        my_rbt['root']['color'] = "BLACK"
    return my_rbt

    
        
    

        
        
        
        