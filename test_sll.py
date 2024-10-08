from Singly_Linked_list import s_linked_list as sll

def test_linked_list():
  # 1. 리스트 생성
  ll = sll()
  
  # 2. addHead 테스트
  print("addHead 테스트:")
  ll.addHead(10)
  ll.addHead(20)
  ll.addHead(30)
  ll.print_ll()  # 예상 출력: 30 -> 20 -> 10 -> None, size:3
  assert ll.head.val == 30, "head가 30이 아니면 오류"
  assert ll.tail.val == 10, "tail이 10이 아니면 오류"

  # 3. addLast 테스트
  print("\naddLast 테스트:")
  ll.addLast(40)
  ll.addLast(50)
  ll.print_ll()  # 예상 출력: 30 -> 20 -> 10 -> 40 -> 50 -> None, size:5
  assert ll.tail.val == 50, "tail이 50이 아니면 오류"

  # 4. deleteHead 테스트
  print("\ndeleteHead 테스트:")
  ll.deleteHead()
  ll.print_ll()  # 예상 출력: 20 -> 10 -> 40 -> 50 -> None, size:4
  assert ll.head.val == 20, "head가 20이 아니면 오류"

  # 5. deleteLast 테스트
  print("\ndeleteLast 테스트:")
  ll.deleteLast()
  ll.print_ll()  # 예상 출력: 20 -> 10 -> 40 -> None, size:3
  assert ll.tail.val == 40, "tail이 40이 아니면 오류"

  # 6. swapNodes 테스트 (head와 tail 교환)
  print("\nswapNodes 테스트 (head와 tail 교환):")
  ll.swapNodes(0, 2)  # head와 tail 교환
  ll.print_ll()  # 예상 출력: 40 -> 10 -> 20 -> None, size:3
  assert ll.head.val == 40, "head가 40이 아니면 오류"
  assert ll.tail.val == 20, "tail이 20이 아니면 오류"

  # 7. removeDuplicates 테스트
  print("\nremoveDuplicates 테스트:")
  ll.addLast(20)
  ll.addLast(40)
  ll.print_ll()  # 예상 출력: 40 -> 10 -> 20 -> 20 -> 40 -> None, size:5
  ll.removeDuplicates()
  ll.print_ll()  # 예상 출력: 40 -> 10 -> 20 -> None, size:3
  assert ll.tail.val == 20, "tail이 20이 아니면 오류"

  # 8. addAfter 테스트
  print("\naddAfter 테스트:")
  node = ll.findNodeByValue(10)
  ll.addAfter(node, 15)
  ll.print_ll()  # 예상 출력: 40 -> 10 -> 15 -> 20 -> None, size:4
  assert ll.findNodeByIndex(2).val == 15, "중간에 15가 없으면 오류"
  assert ll.size == 4, "사이즈가 4가 아니면 오류"

  # 9. insertAt 테스트
  print("\ninsertAt 테스트:")
  ll.insertAt(2, 12)
  ll.print_ll()  # 예상 출력: 40 -> 10 -> 12 -> 15 -> 20 -> None, size:5
  assert ll.findNodeByIndex(2).val == 12, "2번째 자리에 12가 없으면 오류"
  assert ll.size == 5, "사이즈가 5가 아니면 오류"

  # 10. deleteAfter 테스트
  print("\ndeleteAfter 테스트:")
  ll.deleteAfter(node)  # 10 다음 노드(12)를 삭제
  ll.print_ll()  # 예상 출력: 40 -> 10 -> 15 -> 20 -> None, size:4
  assert ll.findNodeByIndex(1).next.val == 15, "10의 다음에 15가 없으면 오류"
  assert ll.size == 4, "사이즈가 4가 아니면 오류"

  # 11. deleteAt 테스트
  print("\ndeleteAt 테스트:")
  ll.deleteAt(1)  # 인덱스 1의 노드(10)를 삭제
  ll.print_ll()  # 예상 출력: 40 -> 15 -> 20 -> None, size:3
  assert ll.findNodeByIndex(0).next.val == 15, "40의 다음에 15가 없으면 오류"
  assert ll.size == 3, "사이즈가 3이 아니면 오류"

  # 12. reverse 테스트
  print("\nreverse 테스트:")
  ll.reverse()
  ll.print_ll()  # 예상 출력: 20 -> 15 -> 40 -> None, size:3
  assert ll.head.val == 20, "head가 20이 아니면 오류"
  assert ll.tail.val == 40, "tail이 40이 아니면 오류"

  # 13. toList and llInfoToList 테스트
  val_list = ll.toList()
  info = ll.llInfoToList()
  print(val_list)
  print(info)

  # 14. ll_clear 테스트
  print("\nll_clear 테스트:")
  ll.ll_clear()
  ll.print_ll()
  assert ll.head == None, "head가 None이 아니면 오류"
  assert ll.tail == None, "tail이 None이 아니면 오류"

  # 15. 예외처리 테스트
  print("\n예외처리 테스트:")

  # 빈 리스트에서 삭제 시도 (예외 처리 확인)
  ll.deleteHead()  # 출력: Error: The list is empty. Cannot delete.
  assert ll.size == 0
  assert ll.head == None
  assert ll.tail == None
  ll.deleteLast()  # 정상 작동 (빈 리스트에서는 아무 동작도 하지 않음)
  assert ll.size == 0
  assert ll.head == None
  assert ll.tail == None

  # 유효하지 않은 인덱스에서 삽입/삭제 시도 (예외 처리 확인)
  ll.insertAt(5, 100)  # 인덱스가 길이를 벗어났기 때문에 아무 동작도 하지 않음
  assert ll.size == 0, "잘못된 인덱스에서 삽입 시 리스트에 변화가 없어야 합니다."
  assert ll.head == None
  assert ll.tail == None
  ll.deleteAt(3)  # 인덱스가 유효하지 않음 (리스트가 비어 있음)
  assert ll.size == 0, "잘못된 인덱스에서 삽입 시 리스트에 변화가 없어야 합니다."
  assert ll.head == None
  assert ll.tail == None

  # 값이 없는 경우 인덱스 검색
  index = ll.indexOf(999)
  print(f"값 999의 인덱스: {index}")  # 출력: 값 999의 인덱스: -1

  # 빈 리스트에 인덱스로 노드 찾기 시도 (예외 처리 확인)
  value = ll.valueAt(0)  # 출력: Error: Index out of bounds
  assert value == None

  ll.addLast(10)
  ll.addLast(20)
  ll.addLast(30)
  ll.addAfter(ll.head, 15)  # 헤드 뒤에 15 삽입
  ll.print_ll()  # 출력: 10 -> 15 -> 20 -> 30 -> None

  # 다른 리스트의 노드를 조작하려는 시도 (예외 처리 확인)
  test_ll = sll()
  test_ll.addLast(50)
  ll.addAfter(test_ll.head, 40)  # 출력: Error: Node does not belong to this linked list

  # 삭제 시도 (노드가 없거나 연결리스트에 속하지 않음)
  ll.deleteAfter(test_ll.head)  # 출력: Error: Given node is None or has no next node

  print("\n모든 테스트 성공!")

# 테스트 함수 실행
test_linked_list()
