from GeometricAux import *


class Parser(object):
    """
        This class is responsible for transforming the given input file to
        a set of entries {i -> setOfSegments(i)} , for i=0,1,..
    """
    def __init__(self, fileDir):

        self.testCases = {}

        with open(fileDir) as file:
            numOfSets = int(file.readline().strip(' '))
            for numOfTestCase in range(numOfSets):
                numOfSeg = int(file.readline().strip(' '))
                setOfSegments = set()
                for _ in range(numOfSeg):
                    points = [float(num) for num in file.readline().split(' ')]
                    segment = Segment(Point(points[0], points[1]), Point(points[2], points[3]))
                    setOfSegments.add(segment)
                self.testCases[numOfTestCase] = setOfSegments

    def getResult(self):
        return self.testCases

