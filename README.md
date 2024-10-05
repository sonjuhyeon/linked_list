# 1. Singly_linked_list

## `s_list_node` 클래스

- **`__init__`**: 리스트 노드의 생성자입니다. 노드는 값(`val`)과 다음 노드를 가리키는 포인터(`next`), 그리고 그 노드가 속한 부모 리스트(`parent_list`)를 저장합니다.
- **`swapWith`**: 두 노드 간에 값을 교환할 수 있도록 합니다.

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
