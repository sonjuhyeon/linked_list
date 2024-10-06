# 1. Singly_linked_list

## `s_list_node` 클래스

- **`__init__`**: 리스트 노드의 생성자입니다.
  - 노드는 값(`val`)과 다음 노드를 가리키는 포인터(`next`), 그리고 그 노드가 속한 부모 리스트(`parent_list`)를 저장합니다.
- **`swapWith`**: 두 노드 간에 값을 교환할 수 있도록 합니다.

```python
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
```

---

## `s_linked_list` 클래스

### 기본 CRUD 연산

- **`addHead`**: 리스트의 맨 앞에 노드를 삽입합니다.
- **`addLast`**: 리스트의 맨 뒤에 노드를 삽입합니다.
- **`insertAt`**: 특정 인덱스에 노드를 삽입합니다.
- **`deleteHead`**: 리스트의 첫 번째 노드를 삭제합니다.
- **`deleteLast`**: 리스트의 마지막 노드를 삭제합니다.
- **`deleteAt`**: 특정 인덱스의 노드를 삭제합니다.

---

### 찾기 및 조작

- **`findNodeByValue`**: 특정 값으로 노드를 찾습니다.
- **`findNodeByIndex`**: 특정 인덱스의 노드를 찾습니다.
- **`indexOf`**: 값으로 인덱스를 찾습니다.
- **`valueAt`**: 인덱스로 값을 찾습니다.

---

### 추가 기능

- **`reverse`**: 리스트를 반전시킵니다.
- **`removeDuplicates`**: 리스트에서 중복된 값을 제거합니다.
- **`swapNodes`**: 두 인덱스의 노드 간 값을 교환합니다.
- **`ll_clear`**: 리스트를 초기화합니다.

---

### 추가하고 싶은 기능

- **`removeByValue`**: 리스트에서 특정 값을 가진 첫 번째 노드를 찾아 제거하는 메서드
- **`removeAllByValue`**: 리스트에서 특정 값을 가진 모든 노드를 제거하는 메서드
- **`isEmpty`**: 리스트가 비어있는지 확인하는 메서드
- **`contains`**: 리스트에 특정 값이 존재하는지 여부를 반환하는 메서드
- **`findPreviousNode`**: 특정 노드의 바로 앞에 있는 노드를 찾는 메서드 (단일 연결 리스트에서는 이전 노드를 추적하기 어렵기 때문에, 이 메서드는 노드를 삭제하거나 수정할 때 도움이 됩니다.)
- **`mergeWith`**: 두 개의 단일 연결 리스트를 병합하는 메서드
- **`reverseBetween(startIndex, endIndex)`**: 리스트의 일부분(지정된 인덱스 범위)을 반전시키는 메서드
- **`getNthFromEnd(n)`**: 리스트의 끝에서부터 n번째 노드를 반환하는 메서드
- **`toList`**: 단일 연결 리스트를 파이썬 리스트 자료형으로 변환하는 메서드
