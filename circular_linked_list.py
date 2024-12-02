class c_list_node:
  def __init__(self, val, parent_list=None):
    self.val = val
    self.next = None
    self.parent_list = parent_list

  def swapWith(self, other_node):
    if not other_node or self == other_node:
      return
    self.val, other_node.val = other_node.val, self.val


class c_linked_list:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  # --------read method--------

  # 값으로 노드 찾기
  def findNodeByValue(self, value):
    current = self.head
    for _ in range(self.size):
      if current.val == value:
        return current
      current = current.next
    return None

  # 인덱스로 노드 찾기
  def findNodeByIndex(self, index):
    if index < 0 or index >= self.size:
      raise IndexError("Index out of bounds")
    current = self.head
    for _ in range(index):
      current = current.next
    return current

  # 값으로 인덱스 찾기
  def indexOf(self, value):
    current = self.head
    for i in range(self.size):
      if current.val == value:
        return i
      current = current.next
    return -1

  # 인덱스로 값 찾기
  def valueAt(self, index):
    node = self.findNodeByIndex(index)
    return node.val

  # 특정 노드의 바로 앞에 있는 노드를 반환
  def findPreviousNode(self, node):
    if self.size == 0 or not node:
      return None
    current = self.head
    while current.next != node:
      current = current.next
    return current

  # 리스트의 끝에서부터 n번째 노드를 반환 (리스트의 길이를 모를 때 사용)
  def getNthFromEnd(self, n):
    if n <= 0 or n > self.size:
      raise IndexError("Invalid n value")
    return self.findNodeByIndex(self.size - n)

  # 마지막 노드 탐색
  def getLastNode(self):
    return self.tail

  # --------update method--------

  # 가장 앞에 노드 삽입
  def addHead(self, val):
    new_node = c_list_node(val, self)
    if self.size == 0:
      new_node.next = new_node
      self.head = self.tail = new_node
    else:
      new_node.next = self.head
      self.tail.next = new_node
      self.head = new_node
    self.size += 1

  # 가장 뒤에 노드 삽입
  def addLast(self, val):
    if self.size == 0:
      self.addHead(val)
    else:
      new_node = c_list_node(val, self)
      new_node.next = self.head
      self.tail.next = new_node
      self.tail = new_node
      self.size += 1

  # 특정 노드 뒤에 노드 삽입
  def addAfter(self, node, val):
    if not node:
      raise ValueError("Node must not be None")
    new_node = c_list_node(val, self)
    new_node.next = node.next
    node.next = new_node
    if node == self.tail:
      self.tail = new_node
    self.size += 1

  # 특정 위치에 노드 삽입
  def insertAt(self, index, val):
    if index < 0 or index > self.size:
      raise IndexError("Index out of bounds")
    if index == 0:
      self.addHead(val)
    elif index == self.size:
      self.addLast(val)
    else:
      prev_node = self.findNodeByIndex(index - 1)
      self.addAfter(prev_node, val)

  # 두 개의 연결 리스트를 병합
  def mergeWith(self, other_list):
    if other_list.size == 0:
      return
    if self.size == 0:
      self.head, self.tail, self.size = other_list.head, other_list.tail, other_list.size
    else:
      self.tail.next = other_list.head
      other_list.tail.next = self.head
      self.tail = other_list.tail
      self.size += other_list.size

  # --------delete method--------

  # 처음 노드 삭제
  def deleteHead(self):
    if self.size == 0:
      return
    if self.size == 1:
      self.head = self.tail = None
    else:
      self.head = self.head.next
      self.tail.next = self.head
    self.size -= 1

  # 마지막 노드 삭제
  def deleteLast(self):
    if self.size == 0:
      return
    if self.size == 1:
      self.deleteHead()
    else:
      prev_tail = self.findPreviousNode(self.tail)
      prev_tail.next = self.head
      self.tail = prev_tail
      self.size -= 1

  # 특정 노드의 다음 노드 삭제
  def deleteAfter(self, node):
    if self.size == 0 or not node or node.next == node:
      return
    next_node = node.next
    if next_node == self.tail:
      self.tail = node
    node.next = next_node.next
    self.size -= 1

  # 특정 위치의 노드 삭제
  def deleteAt(self, index):
    if index < 0 or index >= self.size:
      raise IndexError("Index out of bounds")
    if index == 0:
      self.deleteHead()
    else:
      prev_node = self.findNodeByIndex(index - 1)
      self.deleteAfter(prev_node)

  # 리스트에서 특정 값을 가진 첫 번째 노드를 제거
  def removeByValue(self, value):
    current = self.head
    prev = self.tail
    for _ in range(self.size):
      if current.val == value:
        if current == self.head:
          self.deleteHead()
        else:
          prev.next = current.next
          if current == self.tail:
            self.tail = prev
          self.size -= 1
        return
      prev = current
      current = current.next

  # 리스트에서 특정 값을 가진 모든 노드를 제거
  def removeAllByValue(self, value):
    for _ in range(self.size):
      self.removeByValue(value)

  # circular linked list 전체 삭제
  def cll_clear(self):
    self.head = None
    self.tail = None
    self.size = 0

  # --------additional features method--------

   # 리스트 반전
  def reverse(self):
    if self.size <= 1:
      return
    prev = self.tail
    current = self.head
    for _ in range(self.size):
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    self.head, self.tail = self.tail, self.head

  # 리스트의 일부를 반전
  def reverseBetween(self, startIndex, endIndex):
    if startIndex < 0 or endIndex >= self.size or startIndex >= endIndex:
      raise ValueError("Invalid indices")
    prev = None if startIndex == 0 else self.findNodeByIndex(startIndex - 1)
    start_node = self.head if startIndex == 0 else prev.next
    current = start_node
    next_node = None
    for _ in range(endIndex - startIndex + 1):
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    if prev:
      prev.next.next = current
    else:
      self.head = prev

  # 리스트 내 중복 값 제거
  def removeDuplicates(self):
    if self.size <= 1:
      return
    seen = set()
    current = self.head
    prev = self.tail
    for _ in range(self.size):
      if current.val in seen:
        prev.next = current.next
        if current == self.tail:
          self.tail = prev
        self.size -= 1
      else:
        seen.add(current.val)
        prev = current
      current = current.next

  # 두 인덱스의 노드 값 교환
  def swapNodes(self, index1, index2):
    if index1 < 0 or index2 < 0 or index1 >= self.size or index2 >= self.size:
      raise IndexError("Invalid indices")
    if index1 == index2:
      return
    node1 = self.findNodeByIndex(index1)
    node2 = self.findNodeByIndex(index2)
    node1.swapWith(node2)

  # 리스트 길이 반환
  def getLength(self):
    return self.size

  # 모든 노드 출력
  def print_ll(self):
    if self.size == 0:
      print("List is empty")
      return
    current = self.head
    for _ in range(self.size):
      print(current.val, end=" -> ")
      current = current.next
    print("(head)")

  # 연결 리스트의 정보를 리스트로 반환
  def llInfoToList(self):
    return {"size": self.size, "head": self.head.val if self.head else None, "tail": self.tail.val if self.tail else None}

  # 연결 리스트의 값들을 리스트로 반환
  def toList(self):
    result = []
    current = self.head
    for _ in range(self.size):
      result.append(current.val)
      current = current.next
    return result