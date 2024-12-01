class c_list_node:
  def __init__(self, val, parent_list = None):
    self.val = val
    self.next = val
    self.parent_list = parent_list

  def swapWith(self, other_node):
    pass

class c_linked_list:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  # --------read method--------

  # 값으로 노드 찾기
  def findNodeByValue(self, value):
    pass

  # 인덱스로 노드 찾기
  def findNodeByIndex(self, index):
    pass

  # 값으로 인덱스 찾기
  def indexOf(self, value):
    pass

  # 인덱스로 값 찾기
  def valueAt(self, index):
    pass

  # 특정 노드의 바로 앞에 있는 노드를 반환
  def findPreviousNode(self, node):
    pass

  # 리스트의 끝에서부터 n번째 노드를 반환 (리스트의 길이를 모를 때 사용)
  def getNthFromEnd(self, n):
    pass

  # 마지막 노드 탐색
  def getLastNode(self):
    pass

  # --------update method--------

  # 가장 앞에 노드 삽입
  def addHead(self, val):
    pass

  # 가장 뒤에 노드 삽입
  def addLast(self, val):
    pass

  # 특정 노드 뒤에 노드 삽입
  def addAfter(self, node, val):
    pass

  # 특정 위치에 노드 삽입
  def insertAt(self, index, val):
    pass

  # 두 개의 연결 리스트를 병합
  def mergeWith(self, other_list):
    pass

  # --------delete method--------

  # 처음 노드 삭제
  def deleteHead(self):
    pass

  # 마지막 노드 삭제
  def deleteLast(self):
    pass

  # 특정 노드의 다음 노드 삭제
  def deleteAfter(self, node):
    pass

  # 특정 위치의 노드 삭제
  def deleteAt(self, index):
    pass

  # 리스트에서 특정 값을 가진 첫 번째 노드를 제거
  def removeByValue(self, value):
    pass

  # 리스트에서 특정 값을 가진 모든 노드를 제거
  def removeAllByValue(self, value):
    pass

  # circular linked list 전체 삭제
  def cll_clear(self):
    pass

  # --------additional features method--------

   # 리스트 반전
  def reverse(self):
    pass

  # 리스트의 일부를 반전
  def reverseBetween(self, startIndex, endIndex):
    pass

  # 리스트 내 중복 값 제거
  def removeDuplicates(self):
    pass

  # 두 인덱스의 노드 값 교환
  def swapNodes(self, index1, index2):
    pass

  # 리스트 길이 반환
  def getLength(self):
    pass

  # 모든 노드 출력
  def print_ll(self):
    pass

  # 연결 리스트의 정보를 리스트로 반환
  def llInfoToList(self):
    pass

  # 연결 리스트의 값들을 리스트로 반환
  def toList(self):
    pass