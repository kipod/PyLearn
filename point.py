
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
        p1 = Point(x, y)
        p2 = Point(y, x)
        if p1 < p2:
            print "*",
        elif p1:
            print ".",
        else:
            print "o",
    print
