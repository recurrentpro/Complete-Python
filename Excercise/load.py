a = 55

def info():
    print("This is load module")

def add(a, b):
    result = a+b
    return result

print("Name Attribute:", __name__)


if __name__ == "__main__":
    print(add(5, 8))