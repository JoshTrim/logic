#!/usr/bin/env python3
from pydantic import BaseModel

class Gate(BaseModel):
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class UnaryGate(Gate):
    def __init__(self, n):
        super().__init__(n)
        self.pin = None
        self.label = self.getLabel()

x = UnaryGate(1)

# class Base:
#     def __init__(self, a: bool, b: bool = None):
#         self.a, self.b = a, b

# class Not(Base):
#     def __init__(self):
#         if self.a:
#             self.out = False
#         else:
#             self.out = True

# class And(Base):
#     def __init__(self):
#         return a * b

# class Or(Base):
#     def __init__(self):
#         return a + b

# class Nand(Base):
#     def __init_(self):
#         return Not(bool(a + b))

# class Nor:
#     def __init_(self):
#         pass

# class Xnor:
#     pass


# x = Not(True)

# print(x.out)
