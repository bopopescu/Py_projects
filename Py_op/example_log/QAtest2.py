import QAtest1

print("top-level in QAtest2.py")
#QAtest1.func()

if __name__ == "__main__":
    print("QAtest2.py is being run directly")
else:
    print("QAtest2.py is being imported into another module")

"""
top-level in QAtest1.py
QAtest1.py is being imported into another module
top-level in QAtest2.py
QAtest2.py is being run directly

"""