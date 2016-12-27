
class Node:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    @property
    def isEmpty(self) -> bool:
        return False

class Empty:
    @property
    def isEmpty(self) -> bool:
        return True


class MapperState:
    def __init__(self, l:Node, f):
        self.list = l
        self.f = f
        self.waitTime = 1.0
        self.remainingList = l
        self.resultList = Empty()
        self.s = ""
        self._s = "{}"

        self.state = self._map(lambda x:x)

    def Update(self, dt):
        self.waitTime -= dt
        if self.waitTime < 0.0 and not self.isFinished():
            self.waitTime = 1.0
            self.state = self.state()

    def _map(self, cont):
        if self.remainingList.isEmpty:
            self.s = self._s.format("Empty()")
            return cont(Empty())
        else:
            head = self.remainingList.head
            self.remainingList = self.remainingList.tail
            s = self._s

            def cont_(acc):
                return lambda: cont(Node(self.f(head), acc))
            def f3():
                self.s = s.format("Node(" + str(self.f(head)) + ", map(l.tail, f)))")
                self._s = s.format("Node(" + str(self.f(head)) + ", {}))")
                return self._map(cont_)
            def f2():
                self.s = s.format("Node(f("+str(head)+"), map(l.tail, f))")
                return f3
            def f1():
                self.s = s.format("Node(f(l.head), map(l.tail, f))")
                return f2

            return f1

    def isFinished(self):
        return type(self.state) is Node





