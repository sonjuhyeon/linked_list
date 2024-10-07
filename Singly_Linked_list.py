class s_list_node:
  def __init__(self, val, parent_list = None):
    self.val = val
    self.next = None
    self.parent_list = parent_list  # 노드가 속한 리스트를 추적

  # 노드 간 값 교환 메서드
  def swapWith(self, other_node):
    # next 값을 임시로 저장
    temp_next_self = self.next
    temp_next_other = other_node.next

    # 값과 속성을 교환
    self.__dict__, other_node.__dict__ = other_node.__dict__, self.__dict__

    # next 값을 복원
    self.next = temp_next_self
    other_node.next = temp_next_other


class s_linked_list:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  # 값으로 노드 찾기
  def findNodeByValue(self, value):
    current = self.head
    while current:
      if current.val == value:
        return current
      current = current.next
    print("Error: The value is not in the node")
    return None

  # 인덱스로 노드 찾기
  def findNodeByIndex(self, index):
    if index < 0 or index >= self.size:
      print("Error: Index out of bounds")
      return None

    current = self.head
    for _ in range(index):
      current = current.next
    return current
  
  # 값으로 인덱스 찾기
  def indexOf(self, value):
    current = self.head
    index = 0
    while current:
      if current.val == value:
        return index
      current = current.next
      index += 1
    return -1  # 값을 찾지 못한 경우

  # 인덱스로 값 찾기
  def valueAt(self, index):
    if index < 0 or index >= self.size:
      print("Error: Index out of bounds")
      return None
    current = self.head
    for _ in range(index):
      current = current.next
    return current.val

  # 마지막 노드 탐색
  def getLastNode(self):
    current = self.head
    if (current == None):
      return None
    while (current.next != None):
      current = current.next
    return current  # 마지막 노드 반환

  # 가장 앞에 노드 삽입
  def addHead(self, val):
    new_node = s_list_node(val, self)
    new_node.next = self.head  # 새로운 노드를 현재 헤드로 설정
    self.head = new_node  # 새로운 노드를 헤드로 설정
    self.size += 1

  # 가장 뒤에 노드 삽입
  def addLast(self, val):
    new_node = s_list_node(val, self)
    if (self.head == None):
      self.head = new_node  # 리스트가 비어있다면 새 노드가 헤드이자 테일이 됨
      self.tail = new_node
    else:
      self.tail.next = new_node  # 마지막 노드에 새 노드 연결
      self.tail = new_node  # 새 노드를 테일로 업데이트
    self.size += 1

  # 특정 노드 뒤에 노드 삽입
  def addAfter(self, node, val):
    if self.head is None:
      print("Error: The list is empty.")
      return
    if (node == None):
      print("Error: Given node is None")
      return
    if (node.parent_list != self):
      print("Error: Node does not belong to this linked list")
      return
    new_node = s_list_node(val, self)
    new_node.next = node.next  # 새로운 노드의 다음을 현재 노드의 다음으로 설정
    node.next = new_node  # 현재 노드의 다음을 새로운 노드로 설정
    self.size += 1

  # 특정 위치에 노드 삽입
  def insertAt(self, index, val):
    if index < 0 or index > self.size:
      print(f"Error: Index {index} out of bounds. Cannot insert.")
      return
    if index == 0:
      self.addHead(val)
      return
    current = self.head
    for _ in range(index - 1):
      current = current.next
    new_node = s_list_node(val, self)
    new_node.next = current.next
    current.next = new_node
    self.size += 1
    
  # 처음 노드 삭제
  def deleteHead(self):
    if (self.head == None):
      print("Error: The list is empty. Cannot delete.")
      return
    self.head = self.head.next  # 헤드를 다음 노드로 변경
    self.size -= 1
    if self.size < 0:  # 안전한 사이즈 관리
      self.size = 0  # 사이즈가 음수가 되는 것을 방지

  # 마지막 노드 삭제
  def deleteLast(self):
    if (self.head == None):  # 리스트가 비어 있을 경우
      return
    if (self.head.next == None):  # 노드가 하나일 경우
      self.head = None
      self.tail = None
      self.size -= 1
      return
    current = self.head
    while (current.next != self.tail):
      current = current.next
    current.next = None  # 마지막 노드의 이전 노드가 마지막이 됨
    self.tail = current  # tail을 마지막 이전 노드로 업데이트
    self.size -= 1

  # 특정 노드의 다음 노드 삭제
  def deleteAfter(self, node):
    if self.head is None:
      print("Error: The list is empty.")
      return
    if ((node == None) or (node.next == None)):
      print("Error: Given node is None or has no next node")
      return
    if (node.parent_list != self):
      print("Error: Node does not belong to this linked list")
      return
    node.next = node.next.next  # 특정 노드의 다음 노드를 건너뛰어 삭제
    self.size -= 1

  # 특정 위치의 노드 삭제
  def deleteAt(self, index):
    if self.head is None:
      print("Error: The list is empty. Cannot delete.")
      return
    if index < 0 or index >= self.size:
      print(f"Error: Index {index} out of bounds. Cannot delete.")
      return
    if index == 0:
        self.deleteHead()
        return
    current = self.head
    for _ in range(index - 1):
      current = current.next
    current.next = current.next.next
    self.size -= 1

  # linked list 전체 삭제
  def ll_clear(self):
    self.head = None  # head를 None으로 설정하여 리스트 전체 삭제
    self.size = 0

  # 리스트 반전
  def reverse(self):
    prev = None
    current = self.head
    while (current != None):
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    self.head = prev

  # 리스트 내 중복 값 제거
  def removeDuplicates(self):
    current = self.head
    seen_values = set()
    prev = None
    while (current != None):
      if current.val in seen_values:
        prev.next = current.next  # 중복일 경우 삭제
        self.size -= 1
      else:
        seen_values.add(current.val)
        prev = current
      current = current.next

  # 두 인덱스의 노드 값 교환
  def swapNodes(self, index1, index2):
    if index1 == index2:
      print("The two indices are the same. No need to swap.")
      return

    # 인덱스가 유효한지 확인
    if index1 < 0 or index2 < 0 or index1 >= self.size or index2 >= self.size:
      print("Error: One or both indices are out of range.")
      return

    node1 = self.findNodeByIndex(index1)
    node2 = self.findNodeByIndex(index2)

    if node1 and node2:
      node1.swapWith(node2)  # 노드 자체에 값 교환 책임을 위임

  # 리스트 길이 반환
  def getLength(self):
    return self.size
    
  # 모든 노드 출력
  def print_ll(self):
    current = self.head
    while current is not None:
      print(current.val, end=" -> ")
      current = current.next
    print(f"None, size:{self.size}")


# removeByValue
# 리스트에서 특정 값을 가진 첫 번째 노드를 찾아 제거하는 메서드입니다. 이 메서드는 값을 기반으로 노드를 삭제하는데 유용합니다.

# removeAllByValue
# 리스트에서 특정 값을 가진 모든 노드를 제거하는 메서드입니다. 여러 노드가 동일한 값을 가질 수 있을 때 유용합니다.

# isEmpty
# 리스트가 비어있는지 확인하는 메서드입니다. 리스트의 크기를 빠르게 확인하거나 특정 작업 전에 리스트가 비어있는지 여부를 검사할 때 사용됩니다.

# contains
# 리스트에 특정 값이 존재하는지 여부를 반환하는 메서드입니다. 값이 존재하면 True, 없으면 False를 반환합니다.

# findPreviousNode
# 특정 노드의 바로 앞에 있는 노드를 찾는 메서드입니다. 단일 연결 리스트에서는 이전 노드를 추적하기 어렵기 때문에, 이 메서드는 노드를 삭제하거나 수정할 때 도움이 됩니다.

# mergeWith
# 두 개의 단일 연결 리스트를 병합하는 메서드입니다. 하나의 리스트 끝에 다른 리스트를 연결하여 리스트를 합칠 수 있습니다.

# reverseBetween(startIndex, endIndex)
# 리스트의 일부분(지정된 인덱스 범위)을 반전시키는 메서드입니다. 리스트의 특정 구간만 역순으로 바꾸는 작업이 필요할 때 유용합니다.

# getNthFromEnd(n)
# 리스트의 끝에서부터 n번째 노드를 반환하는 메서드입니다. 리스트의 길이를 모를 때도 사용할 수 있어 마지막에서부터 특정 노드를 찾을 때 유용합니다.

# toList
# 단일 연결 리스트를 파이썬 리스트로 변환하는 메서드입니다. 이 메서드는 리스트의 데이터를 빠르게 처리하거나 외부 함수에 넘길 때 유용합니다.