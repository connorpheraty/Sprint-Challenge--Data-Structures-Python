class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    for i in range(self.capacity):
        if self.current == i:
            self.storage[i] = item
            self.current +=1
            return self.storage
    self.current = 0
    return self.append(item)
    

  def get(self):
    for i in self.storage:
        tmp_lst = [i for i in self.storage if i != None]
    return tmp_lst