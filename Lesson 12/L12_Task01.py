class Vector:
    def __init__(self, val_x, val_y):
        self.val_x, self.val_y = val_x, val_y

    def __eq__(self, other):
        return self.val_x == other.val_x and self.val_y == other.val_y

    def __add__(self, other):
        v_res = self.val_x + other.val_x, self.val_y + other.val_y
        return v_res

    def __sub__(self, other):
        v_res = self.val_x - other.val_x, self.val_y - other.val_y
        return v_res

    def __mul__(self, other):

        if type(other) == Vector:
            v_res = self.val_x * other.val_x, self.val_y * other.val_y
            return v_res
        elif type(other) == int:
            v_res = self.val_x * other, self.val_y * other
            return v_res


V1 = Vector(3, 5)
V2 = Vector(1, 2)

print(V1 == V2)
print(V1 - V2)
print(V1 + V2)
print(V1 * V2)
print(V1 * 4)
