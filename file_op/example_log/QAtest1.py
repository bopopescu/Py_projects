def func():
    print("func() in QAtest1.py")
print("top-level in QAtest1.py")
#func()
if __name__ == "__main__":
    print("QAtest1.py is being run directly")
else:
    print("QAtest1.py is being imported into another module")
"""
top-level in QAtest1.py
QAtest1.py is being run directly
"""

