class Heap(object):
    def __init__(self, comp):
        self.items = []
        self.comp = comp

    def __repr__(self):
        return str(self.items)

    def add(self, i):
        print "\nAdding %i" % i
        self.items.append(i)
        self._bubble_up()
        print "\nAdded %i -- %s" % (i, str(self.items))

    def _left_child(self, i):
        return (i * 2) + 1

    def _right_child(self, i):
        return (i * 2) + 2

    def _parent(self, i):
        return (i / 2) if i % 2 == 1 else (i / 2) - 1

    def get_peak(self):
        print "Removing peak: %i" % self.items[0]
        peak = self.items[0]
        if len(self.items) > 1:
            self._bubble_down()
        else:
            self.items = []
        return peak

    def _bubble_up(self):
        i = len(self.items) - 1

        while i > 0:
            print self.items
            parent_i = self._parent(i)
            print "---node %i and parent %i" % (self.items[i], self.items[parent_i])
            # compare to parent
            if self.comp(self.items[i], self.items[parent_i]):
                self.items[i], self.items[parent_i] = self.items[parent_i], self.items[i]
            i = parent_i

    def _bubble_down(self):
        last_item = self.items.pop(-1)
        self.items[0] = last_item
        i = 0
        while i < len(self.items):
            left_child = self._left_child(i)
            right_child = self._right_child(i)
            swap_child = None
            if left_child < len(self.items) and right_child < len(self.items):
                if self.comp(self.items[left_child], self.items[right_child]):
                    swap_child = left_child
                else:
                    swap_child = right_child
            elif left_child < len(self.items) and not self.comp(self.items[i], self.items[left_child]):
                    swap_child = left_child

            elif right_child < len(self.items) and not self.comp(self.items[i], self.items[right_child]):
                    swap_child = right_child
            else:
                break
            if swap_child:
                self.items[i], self.items[swap_child] = self.items[swap_child], self.items[i]
                i = swap_child


        # parent[i] = (i / 2) if i % 2 == 1 else (i / 2) - 1
        # left_child[i] = (i * 2) + 1
        # right_child[i] = (i * 2) + 2

def greater(x, y):
    if x > y:
        return True
    return False

def less(x, y):
    if x < y:
        return True
    return False

if __name__ == "__main__":
    # h = Heap(greater)
    # h.add(15)
    # h.add(19)
    # h.add(10)
    # h.add(7)
    # h.add(17)
    # h.add(16)
    # h.add(100)
    # print h
    # print "REMOVING"
    # # from pudb import set_trace; set_trace()
    # h.get_peak()
    # print h

    h = Heap(less)
    l = [6, 5, 3, 1, 8, 7, 2, 4]
    sorted = []
    print l
    for el in l:
        h.add(el)
    # from pudb import set_trace; set_trace()
    while h.items:
        sorted.append(h.get_peak())
    print sorted
