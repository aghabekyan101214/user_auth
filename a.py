class A:
    def test(self):
        print("TEST A")

class B(A):
    def test(self):
        print("TEST B")


class C(A):
    def test(self):
        print("TEST C")


class D(B, C):
    def test(self):
        super().test()
        print("TEST D")


D().test()