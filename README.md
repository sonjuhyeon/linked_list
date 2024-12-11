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

### read method

- **`findNodeByValue`**: 특정 값으로 노드를 찾습니다.
- **`findNodeByIndex`**: 특정 인덱스의 노드를 찾습니다.
- **`indexOf`**: 값으로 인덱스를 찾습니다.
- **`valueAt`**: 인덱스로 값을 찾습니다.
- **`findPreviousNode`**: 특정 노드의 바로 앞에 있는 노드를 반환합니다. (단일 연결 리스트에서는 이전 노드를 추적하기 어렵기 때문에, 이 메서드는 노드를 삭제하거나 수정할 때 도움이 됩니다.)
- **`getNthFromEnd`**: 리스트의 끝에서부터 n번째 노드를 반환합니다.
- **`getLastNode`**:   # 마지막 노드를 반환합니다.
 
---

### update method

- **`addHead`**: 가장 앞에 노드를 삽입합니다.
- **`addLast`**: 가장 뒤에 노드 삽입합니다.
- **`addAfter`**: 특정 노드 뒤에 노드를 삽입합니다.
- **`addAfter`**: 특정 위치에 노드를 삽입합니다.
- **`mergeWith`**: 두 개의 연결 리스트를 병합합니다.

---

### delete method

- **`deleteHead`**: 처음 노드를 삭제합니다.
- **`deleteLast`**: 마지막 노드를 삭제합니다.
- **`deleteAfter`**: 특정 노드의 다음 노드를 삭제합니다.
- **`deleteAt`**: 특정 위치의 노드를 삭제합니다.
- **`removeByValue`**: 리스트에서 특정 값을 가진 첫 번째 노드를 삭제합니다.
- **`removeAllByValue`**: 리스트에서 특정 값을 가진 모든 노드를 삭제합니다.
- **`ll_clear`**: linked list 내 모든 노드를 삭제합니다.

---

### additional features method

- **`reverse`**: 리스트를 반전시킵니다.
- **`reverseBetween`**: 리스트의 일부를 반전시킵니다.
- **`removeDuplicates`**: 리스트 내 중복 값을 처음 하나만 남기고 제거합니다.
- **`swapNodes`**: 두 인덱스의 노드 간 값을 교환합니다.
- **`getLength`**: 리스트 길이를 반환합니다.
- **`print_ll`**: 모든 노드를 출력합니다.
- **`llInfoToList`**: 연결 리스트의 정보를 리스트로 반환합니다.
- **`toList`**: 연결 리스트의 값들을 리스트로 반환합니다.
