class SqMatrix:
    def __init__(self, elements: list):

        # detecting the order of the matrix through the elements
        # the order is defined by mxn, where m is the number of lines (vert.) and n is the number of collumns (hor.)

        nperline = []
        self.elements = []
        for i in elements:
            nperline.append(len(i))
            self.elements.append(i)
        nperline.sort()
        if nperline[0] != nperline[-1]:
            raise SyntaxError("Matrix columns must have same size")
        self.m = len(elements)
        self.n = nperline[0]
        if self.m != self.n:
            raise SyntaxError("Matrix must be square. We currently do not support non-square matrices.")

    # Functions for displaying matrix in string and list form

    def matrixf(self):
        mf = ''
        for c in self.elements:
            for i in c:
                mf += str(i) + f' \t'
            mf += """
"""
        return mf.strip()

    def matrixl(self):
        return self.elements

    def determinant(self):

        # Should be optimized in the future

        d = 0
        det = []
        if self.n == 1 and self.m == 1:
            return self.elements[0][0]
        for i in range(0, self.n):
            lc = self.elements[0][i]
            ne = [x.copy() for x in self.elements]
            ne.pop(0)
            for c in ne:
                c.pop(i)
            det.append((-1)**(1 + 1 + i) * lc * SqMatrix(ne.copy()).determinant())
        for x in det:
            d += x
        return d
