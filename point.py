
class Point(object):
    """
    class Point
    """

    def __init__(self, x0, y0):
        self.coord = (x0, y0)

    def __nonzero__(self):
        return self.coord[0] != 0 or self.coord[1] != 0

    def __cmp__(self, point):
        return cmp(self.coord, point.coord)


for x in range(-3, 4):
    for y in range(-3, 4):
        if Point(x, y) < Point(y, x):
            print "*",
        elif Point(x, y):
            print ".",
        else:
            print "o",
    print
