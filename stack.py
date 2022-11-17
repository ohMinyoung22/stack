class Stack:
    def __init__(self, maxCount):
        self.maxCount = maxCount
        self.ptr = 0
        self.stackList = []

    def count(self):
        return self.ptr

    def push(self, item):
        # 1. 현재 아이템을 넣을 수 있는 상황인지 확인

        if self.count() >= self.maxCount:
            return False


        # 2. 만약 넣을 수 있다면 넣음

        self.stackList.append(item)
        # 3. ptr을 1 올려 다음에 넣을 아이템의 index 갱신

        self.ptr += 1

        return True

    def pop(self):
        # 1. 현재 아이템을 제거할 수 있는 상황인지 확인
        if self.count() < 1:
            return -1 

        # 3. ptr을 1 감소하여 다음에 넣을 아이템의 index 갱신
        self.ptr -= 1

        # 3. 아이템 빼오기
        item_return = self.stackList[self.ptr]
        self.stackList.pop(self.ptr) # pop -> index로 리스트에서 아이템 제거

        return item_return

    def check(self):
        # 1. 현재 아이템을 빼 올 수 있는 상황인지 확인
        if self.count() < 1:
            return -1 

        # 3. 아이템 빼오기
        item_return = self.stackList[self.ptr - 1]

        return item_return
