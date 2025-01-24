class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 구현해보세요!

        # 1. 원소를 맨 끝에 추가한다.
        self.items.append(value)

        cur_index = len(self.items) - 1
        # 현재 인덱스가 1이 아닐때까지만 반복을 한다.
        # 현재 인덱스가 1이라는 얘기는 루트 노드이기떄문에 더이상 확인할 값이 없다는 말이다.
        while cur_index != 1:
            # 2. 부모 노드랑 비교해서ㅏ 내가 더 크다면 위치를 바꾼다.
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index
            else:
                break


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!