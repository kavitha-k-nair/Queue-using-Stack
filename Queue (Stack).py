class Stack:
    def __init__(self):
        self.stack = [''] * 10
        self.top = 0

    def insert(self,ele):
        self.ele = ele
        if self.top < 10:
            self.stack[self.top] = self.ele
            self.top += 1

        else:
            print("Queue Full")

    def delete(self):
        if self.top == 0:
            print("Queue Empty")
            return
        
        self.new = [''] * 9
        self.duptop = 0
        
        for i in range(self.top-1,0,-1):
            self.new[self.duptop] = self.stack[i]
            self.duptop += 1

        self.stack[self.top-1] = ''

        self.top = 0
        for j in range(self.duptop-1,-1,-1):
            self.stack[self.top] = self.new[j]
            self.top += 1

    def peek(self):
        if self.top == 0:
            print("Queue Empty")
            return

        print("Top-Most Element:",self.stack[0])

    def contains(self,ele):
        self.ele = ele
        for i in range(self.top):
            if self.stack[i] == self.ele:
                return True
        return False

    def isEmpty(self):
        if self.top==0:
            return True
        return False

    def isFull(self):
        if self.stack[9]:
            return True
        return False

    def display(self):
        for i in range(self.top):
            print(self.stack[i],end='  ')
        print()
        



s1 = Stack()

print("\n1.Enqueue  2.Dequeue  3.Peek  4.Contains  5.IsEmpty  6.IsFull  7.Display  8.Exit")

while True:
    choice = int(input("\nChoice: "))
    if choice==1:
        ele = input("Element: ")
        s1.insert(ele)

    elif choice==2:
        s1.delete()

    elif choice==3:
        s1.peek()

    elif choice==4:
        ele = input("Element: ")
        print(s1.contains(ele))

    elif choice==5:
        print(s1.isEmpty())

    elif choice==6:
        print(s1.isFull())

    elif choice==7:
        s1.display()

    else:
        exit()
