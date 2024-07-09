class A:
    def feature1(self):
        print("Feature A-1 working")

    def feature2(self):
        print("Feature A-2 working")

class B(A):
    def feature3(self):
        print("Feature B-1 working")
    def feature4(self):
        print("Feature B-2 working")

class C(B):
    def feature5(self):
        print("Feature C-1 working")
    def feature6(self):
        print("Feature C-2 working")

c1 = C()
c1.feature1()
c1.feature3()
c1.feature5()
