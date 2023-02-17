from collections import deque


class Stack:

    def __init__(self):
        self.contrainer = deque()

    def push(self, val):
        self.contrainer.append(val)

    def pop(self):
        return self.contrainer.pop()

    def peek(self):
        return self.contrainer[-1]

    def is_empty(self):
        return len(self.contrainer) == 0

    def size(self):
        return len(self.contrainer)


def reverse_strings(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''

    while stack.size() !=0:
        rstr += stack.pop()

    return rstr


if __name__ == '__main__':
    # print(reverse_strings("We will conquere COVID-19"))
    # print(reverse_strings("I am the King"))
    print(reverse_strings("I will crack down the Python Data Structure and Algorithms"))
