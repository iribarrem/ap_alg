def boolean(pack_weight, objects):
  items = len(objects)

  table = [[0 for i in range(pack_weight + 1)] for i in range(items + 1)]

  for i in range(items + 1):
    for w in range(pack_weight + 1):
      if i == 0 or w == 0:
        table[i][w] = 0
      elif objects[i-1][1] <= w:
        table[i][w] = max(objects[i-1][0] + table[i-1][w-objects[i-1][1]], table[i-1][w])
      else:
        table[i][w] = table[i-1][w]

  return table[items][pack_weight]

def fractional(pack_weight, objects):
  obj = []
  for i in range(len(objects)):
    obj.append((objects[i][0], objects[i][1], objects[i][0] / objects[i][1]))

  obj.sort(key=lambda obj: obj[2])

  total_value = 0
  for i in range(len(obj)): 
    if pack_weight - objects[i][1] >= 0: 
      pack_weight -= objects[i][1] 
      total_value += objects[i][0] 
    else: 
      fraction = pack_weight / objects[i][1]  
      total_value += objects[i][0]  * fraction 
      pack_weight = int(pack_weight - (objects[i][1] * fraction)) 
      break 
  return total_value 

objects1 = [(60, 10),
           (100, 20),
           (120, 30)]

objects2 = [(60, 10),
            (40, 40),
            (100, 20),
            (120, 30)]

W = 50

print(boolean(W, objects1))
print(fractional(W, objects2))