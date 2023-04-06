class A:
    def sum(self):
        a=int(input("Enter value of A:"))
        b=int(input("Enter value of B:"))
        print("Sum is:",a+b)
class B(A):
    def mul(self):
        a = int(input("Enter value of A:"))
        b = int(input("Enter value of B:"))
        print("Mul Ans is:", a * b)

class C(B):
    def sub(self):
        a = int(input("Enter value of A:"))
        b = int(input("Enter value of B:"))
        print("Sub Ans is:", a - b)
obj = C()
obj.sum()
obj.mul()
obj.sub()
