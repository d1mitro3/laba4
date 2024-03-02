class medium:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __call__(self, func):
        def wrapper(*args):
            self.count += 1
            if self.count <= self.limit:
                return func(*args)
            else:
                pass
        return wrapper
    
# хз как объяснить эту дичь
def first(): 
    unique = set()
    @medium(2) 
    def otbor(*args):
        nonlocal unique
        for _ in args: unique.add(_)
        return list(unique)
    return otbor

f = first()
for _ in range(4):
    print(f(1, 2, 3, 4, 5, 1, 2, 3))

    