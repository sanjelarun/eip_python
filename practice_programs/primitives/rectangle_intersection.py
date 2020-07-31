import collections

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def is_intersect(A: Rectangle, B: Rectangle):
    return (A.x <= B.x + B.width and A.x + A.width >= B.x
            and A.y <= B.y + B.height and A.y + A.height >= B.y)


def intersect_rectangle(A: Rectangle, B: Rectangle):
    if not is_intersect(A, B):
        return Rectangle(0, 0, -1, -1)

    return Rectangle(max(A.x, B.x),
                     max(A.y, B.y),
                     min(A.x + A.width, B.x + B.width) - max(A.x, B.x),
                     min(A.y + A.height, B.y + B.height) - max(A.y, B.y),
                     )


r1 = Rectangle(0, 0, 2, 2)
r2 = Rectangle(1, 1, 3, 3)

print(intersect_rectangle(r1, r2))
