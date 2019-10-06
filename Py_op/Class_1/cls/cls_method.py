class A:
    message="Class Message"

    @classmethod
    def cfoo(cls,):
        print(cls.message)
    
    def foo(self, msg):
        self.message=msg
        print(self.message)
    
    def __str__(self):
        return self.message


if __name__ == "__main__":

    a = A()
    print(a)  # Class Message

    print(a.cfoo())

    print(A.cfoo())