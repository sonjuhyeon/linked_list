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

  # --------read method--------

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
  
  # 특정 노드의 바로 앞에 있는 노드를 반환
  def findPreviousNode(self, node):
    if not self.head or node == self.head:
      print("Error: Node has no previous node or does not belong to this list.")
      return None
    
    current = self.head
    while current and current.next != node:
      current = current.next

    if current is None:
      print("Error: Node not found in the list.")
      return None
    
    return current
  
  # 리스트의 끝에서부터 n번째 노드를 반환 (리스트의 길이를 모를 때 사용)
  def getNthFromEnd(self, n):
    if n <= 0 or n > self.size:
      print("Error: Invalid n value.")
      return None
    
    fast = self.head
    slow = self.head

    for _ in range(n):
      fast = fast.next
    
    while fast:
      slow = slow.next
      fast = fast.next

    return slow

  # 마지막 노드 탐색
  def getLastNode(self):
    current = self.head
    if (current == None):
      return None
    while (current.next != None):
      current = current.next
    return current  # 마지막 노드 반환

  # --------update method--------

  # 가장 앞에 노드 삽입
  def addHead(self, val):
    new_node = s_list_node(val, self)
    new_node.next = self.head  # 새로운 노드를 현재 헤드로 설정
    if self.size == 0:
      self.tail = new_node
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
    if self.head == None:
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

  # 두 개의 단일 연결 리스트를 병합
  def mergeWith(self, other_list):
    if not isinstance(other_list, s_linked_list):
        print("Error: Input is not a valid linked list.")
        return

    if self.head is None:
        self.head = other_list.head
        self.tail = other_list.tail
    elif other_list.head is not None:
        self.tail.next = other_list.head
        self.tail = other_list.tail

    # 병합된 노드들의 parent_list를 업데이트
    current = other_list.head
    while current:
        current.parent_list = self
        current = current.next

    self.size += other_list.size
    other_list.ll_clear()
    
  # --------delete method--------

  # 처음 노드 삭제
  def deleteHead(self):
    if (self.head == None):
      print("Error: The list is empty. Cannot delete.")
      return
    if self.head == self.tail:  # 노드가 하나만 있는 경우
      self.tail = None  # tail도 None으로 설정
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
    if self.head == None:
      print("Error: The list is empty.")
      return
    if ((node == None) or (node.next == None)):
      print("Error: Given node is None or has no next node")
      return
    if (node.parent_list != self):
      print("Error: Node does not belong to this linked list")
      return
    if node.next == self.tail:
      self.tail = node
    node.next = node.next.next  # 특정 노드의 다음 노드를 건너뛰어 삭제
    self.size -= 1

  # 특정 위치의 노드 삭제
  def deleteAt(self, index):
    if self.head == None:
      print("Error: The list is empty. Cannot delete.")
      return
    if index < 0 or index >= self.size:
      print(f"Error: Index {index} out of bounds. Cannot delete.")
      return
    if index == 0:
      if self.size == 1:
        self.head == None
        self.tail == None
      else:
        self.deleteHead()
      self.size -= 1
      return
    current = self.head
    for _ in range(index - 1):
      current = current.next
    # 만약 마지막 노드를 삭제하는 경우
    if current.next == self.tail:
      self.tail = current
    current.next = current.next.next
    self.size -= 1
  
  # 리스트에서 특정 값을 가진 첫 번째 노드를 제거
  def removeByValue(self, value):
    current = self.head
    prev = None

    while current:
      if current.val == value:
        if current == self.head:
          self.deleteHead()
        elif current == self.tail:
          self.deleteLast()
        else:
          prev.next = current.next
          self.size -= 1
        return
      prev = current
      current = current.next
    print("Error: Value not found in the list.")

  # 리스트에서 특정 값을 가진 모든 노드를 제거
  def removeAllByValue(self, value):
    current = self.head
    prev = None

    while current:
      if current.val == value:
        if current == self.head:
          self.deleteHead()
          current = self.head
        elif current == self.tail:
          self.deleteLast()
          current = None
        else:
          prev.next = current.next
          current = current.next
          self.size -= 1
      else:
        prev = current
        current = current.next

  # linked list 전체 삭제
  def ll_clear(self):
    self.head = None  # head를 None으로 설정하여 리스트 전체 삭제
    self.tail = None  # tail도 초기화
    self.size = 0

  # --------additional features method--------

  # 리스트 반전
  def reverse(self):
    prev = None
    current = self.head
    self.tail = self.head  # 원래의 head가 새로운 tail이 됨
    while (current != None):
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node
    self.head = prev # 마지막으로 방문한 노드가 새로운 head가 됨

  # 리스트의 일부를 반전
  def reverseBetween(self, startIndex, endIndex):
    if startIndex < 0 or endIndex >= self.size or startIndex >= endIndex:
      print("Error: Invalid index range.")
      return
    
    dummy = s_list_node(0)
    dummy.next = self.head
    prev_start = dummy
    for _ in range(startIndex):
      prev_start = prev_start.next
    
    current = prev_start.next
    prev = None

    for _ in range(endIndex - startIndex + 1):
      next_node = current.next
      current.next = prev
      prev = current
      current = next_node

    prev_start.next.next = current
    prev_start.next = prev

    if startIndex == 0:
      self.head = prev
    if endIndex == self.size - 1:
      self.tail = self.findNodeByIndex(endIndex)

  # 리스트 내 중복 값 제거
  def removeDuplicates(self):
    current = self.head
    seen_values = set()
    prev = None
    while (current != None):
      if current.val in seen_values:
        prev.next = current.next  # 중복일 경우 삭제
        if current == self.tail:
          self.tail = prev
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

      # head 업데이트 (만약 index1 또는 index2가 0인 경우)
      if index1 == 0:
        self.head = node1
      elif index2 == 0:
        self.head = node2

      # tail 업데이트 (만약 node1 또는 node2가 tail인 경우)
      if index1 == self.size - 1:
        self.tail = node1
      elif index2 == self.size - 1:
        self.tail = node2

  # 리스트 길이 반환
  def getLength(self):
    return self.size
    
  # 모든 노드 출력
  def print_ll(self):
    current = self.head
    while current != None:
      print(current.val, end=" -> ")
      current = current.next
    print(f"None, size:{self.size}")
    # print(f"None, size:{self.size}, head:{self.head.val}, tail:{self.tail.val}, tail.next:{self.tail.next}")

  # 연결 리스트의 정보를 리스트로 반환
  def llInfoToList(self):
    result = []
    current = self.head
    while (current != None):
      node_info = current.__dict__.copy()  # __dict__로 노드의 속성을 딕셔너리로 변환
      result.append(node_info)
      current = current.next
    return result
  
  # 연결 리스트의 값들을 리스트로 반환
  def toList(self):
    result = []
    current = self.head
    while (current != None):
      value = current.val
      result.append(value)
      current = current.next
    return result