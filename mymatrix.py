import copy


class MyMatrix:
    def __init__(self, data: list):
        """
        Create matrix of given data.
        Example of data:
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
        ]
        Return TypeError if data is not list.
        """
        self.__data = copy.deepcopy(data)

    def __repr__(self):
        """
        Return visual presentation of matrix.
        Example:
          1  20   3   4
          5   6 100   8
        NO SPACE before first column.
        E.g.: repr(MyMatrix([[1, 2]])) == '1 2'
        Hint: use '\n' for line break
        """
        mass = []
        matrix = copy.deepcopy(self.__data)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                mat = str(matrix[i][j])
                count = len(mat)
                mass.append(count)
        s = ''
        for row in self.__data:
            for elem in row:
                s +=  str(elem) + ' ' * (max(mass) + 1 - len(str(elem)))
            if row != self.__data[len(self.__data)-1]:      
                s = s[:-3] + '\n'
            elif row == self.__data[len(self.__data)-1]:
                s = s[:-3]
        return s

    def size(self) -> tuple:
        """
        Return tuple(height, width) for matrix.
        Example: (2, 4)
        """
        height = 0
        width = 0
        if len(self.__data) == 0:
            size = (0, 0)
        else:
            height = len(self.__data)
            width = len(self.__data[0])
            size = (height, width)
        return size

    def flip_up_down(self):
        """
        E.g. modify
        1, 2, 3, 4   to   5, 6, 7, 8
        5, 6, 7, 8        1, 2, 3, 4
        """
        x = len(self.__data)
        matrix = self.__data
        counter = 0
        while counter < x // 2:
            matrix[counter], matrix[x - counter - 1] = matrix[x - counter - 1], matrix[
                counter]
            counter += 1
        return self

    def flip_left_right(self):
        """
        E.g. modify
        1, 2, 3, 4   to   4, 3, 2, 1
        5, 6, 7, 8        8, 7, 6, 5
        """
        matrix = self.__data
        for i in range(len(matrix)):
            counter = 0
            while counter < len(matrix[i]) // 2:
                matrix[i][counter], matrix[i][len(matrix[i]) - counter - 1] = matrix[i][len(matrix[i]) - counter - 1], \
                                                                              matrix[i][counter]
                counter += 1
        return self

        # методы flip_ ИЗМЕНЯЮТ матрицу

    # методы flipped_ по сути делают то же самое,
    # но возвращают изменённую КОПИЮ матрицы
    def flipped_up_down(self):
        new_matrix = MyMatrix(copy.deepcopy(self.__data))
        return new_matrix.flip_up_down()
        
    def flipped_left_right(self):
       matrix_copy = MyMatrix(copy.deepcopy(self.__data))
       return matrix_copy.flip_left_right()
        
    def transpose(self):
        """
        E.g. modify
                          1, 5
        1, 2, 3, 4   to   2, 6
        5, 6, 7, 8        3, 7
                          4, 8
        """
        matrix = []
        m = self.__data
        count = 0
        for j in range(len(m)):
            while count < len(m[j]):
                d = []
                for i in range(len(m)):
                    d.append(m[i][count])
                matrix.append(d)
                count += 1
        self.__data = matrix
        return self
        
    def transposed(self):
        """
        Return transposed copy of MyMatrix.
        """
        new_matrix = MyMatrix(copy.deepcopy(self.__data))
        return new_matrix.transpose()

    def get_data(self):
        return copy.deepcopy(self.__data)
        
    def __add__(self, other):        
        sum_matrix = []
        matrix = copy.deepcopy(self.__data) 
        other = copy.deepcopy(other.get_data())
        for i in range(len(matrix)):
            s = []
            for j in range(len(matrix[i])):
                s.append(matrix[i][j] + other[i][j])
            sum_matrix.append(s)
        sum_matrix = MyMatrix(copy.deepcopy(sum_matrix))
        return sum_matrix

    def __sub__(self, other):       
        difference = []
        other = copy.deepcopy(other.get_data())
        for i in range(len(self.__data)):
            s = []
            for j in range(len(self.__data[i])):
                s.append(self.__data[i][j] - other[i][j])
            difference.append(s)
        difference = MyMatrix(copy.deepcopy(difference))
        return difference
        
    def __iadd__(self, other):
        self = self.__add__(other)
        return self
    
    def isub(self, other):
        self = self.__sub__(other)
        return self

