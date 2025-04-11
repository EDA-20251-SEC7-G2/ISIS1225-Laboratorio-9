import DataStructures.Map.map_functions as mp
import DataStructures.Map.map_entry as me
import random
import DataStructures.List.array_list as ar
def new_map(num_elements,load_factor,prime= 109345121):
    capacity = mp.next_prime(int(num_elements//load_factor))
    elements = ar.new_list()
    for entry in range(capacity):
        ar.add_last(elements,me.new_map_entry(None, None))
    map = {
        'prime': prime,
        'capacity': capacity,
        'scale':random.randint(1, prime - 1), #1
        'shift': random.randint(0, prime - 1), #0
        'table': elements,
        'current_factor': 0,
        'size':0,
        'limit_factor': load_factor
    }
    return map

def is_empty(my_map):
    if my_map['size'] == 0:
        return True
    return False

def is_available(table, pos):
    entry = ar.get_element(table, pos)
    if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
    return False

def default_compare(key, entry):
   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def find_slot(my_map, key, hash_value):
    first_avail = None
    found = False
    ocupied = False
    while not found:
       if is_available(my_map["table"], hash_value):
             if first_avail is None:
                first_avail = hash_value
             entry = ar.get_element(my_map["table"], hash_value)
             if me.get_key(entry) is None:
                found = True
       elif default_compare(key, ar.get_element(my_map["table"], hash_value)) == 0:
             first_avail = hash_value
             found = True
             ocupied = True
       hash_value = (hash_value + 1) % my_map["capacity"]
    return ocupied, first_avail

def remove(my_map,key):
    hash_value = mp.hash_value(my_map,key)
    position = find_slot(my_map, key, hash_value)
    if position[0] == True:
        entry = ar.get_element(my_map["table"],position[1])
        me.set_key(entry, None)
        me.set_value(entry, None)
        my_map["size"] -= 1
    return my_map

def rehash(my_map):
    prev_capacity = my_map["capacity"]
    capacity = mp.next_prime(my_map["capacity"]*2)
    my_map["capacity"] = capacity
    my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    table_copy = my_map["table"]
    new_table = ar.new_list()
    for i in range(capacity):
        ar.add_last(new_table, me.new_map_entry(None, None))
    my_map["table"] = new_table
    my_map["size"] = 0
    for pos in range(prev_capacity):
        new_pos = ar.get_element(table_copy,pos) 
        if me.get_key(new_pos) != None:
          key = me.get_key(new_pos)
          value = me.get_value(new_pos)
          put(my_map,key,value)         
    return my_map

def get(my_map,key):
    hash_value = mp.hash_value(my_map,key)
    position = find_slot(my_map, key, hash_value)
    if position[0]:
        entry = ar.get_element(my_map["table"],position[1])
        return me.get_value(entry)
    else:
        return None
    
def put(my_map,key, value):
    hash_v = mp.hash_value(my_map,key)
    ocupied, available = find_slot(my_map, key, hash_v)
    entry = ar.get_element(my_map["table"],available)
    if ocupied:
        me.set_value(entry, value)
    else: 
        me.set_key(entry, key)
        me.set_value(entry, value)
        my_map['size'] +=1
        my_map['current_factor'] = my_map['size']/ my_map['capacity']
        if my_map['current_factor'] > my_map['limit_factor']:
            return rehash(my_map)
    return my_map

def size(my_map):
    return my_map['size']

def contains(my_map, key):
    table = my_map["table"]
    i = 0
    encontro = False
    while i < (table["size"] - 1) and encontro == False:
        if key == table["elements"][i]["key"]:
            encontro = True
        i += 1
    return encontro

def key_set(my_map):
  dev = ar.new_list()
  for entry in range(ar.size(my_map["table"])):
    key = me.get_key(ar.get_element(my_map["table"],entry))
    if key != None:
      ar.add_last(dev, key)
  return dev    

def value_set(my_map):
  dev = ar.new_list()
  for entry in range(my_map["capacity"]):
    value = me.get_value(ar.get_element(my_map["table"],entry))
    if value != None:
      ar.add_last(dev, value)
  return dev