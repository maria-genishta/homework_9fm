from mymatrix import MyMatrix
def test_repr():
     m = [[12, 2, 3], [900, 67, 4]]
     matrix = MyMatrix(m)
     assert(repr(matrix) == '12  2   3\n900 67  4')
     empty_matrix = MyMatrix([ ])
     assert(repr(empty_matrix) == '')
     
def test_size():
	 m = [[12,3,4]]
	 matrix = MyMatrix(m)
	 assert(matrix.size() == (1, 3))
	 empty_matrix = MyMatrix([ ])
	 assert(empty_matrix.size( ) == (0, 0))
	 
def test_flip_up_down():
     m = [[1, 2, 3], [4, 5, 6]]
     matrix = MyMatrix(m)
     matrix.flip_up_down()
     assert(matrix.size() == (2, 3))
     assert(matrix.get_data() == [[4, 5, 6], [1, 2, 3]])
     empty_matrix = MyMatrix([])
     assert(empty_matrix.get_data() == [ ])
     
def test_flip_left_right():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    m = matrix.flip_left_right()
    empty_matrix = MyMatrix([ ])
    assert(m.get_data() == [[3, 2, 1], [6, 5, 4]])
    empty_matrix.flip_left_right()
    assert(empty_matrix.get_data() == [])
    

def test_flipped_up_down():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    new_matrix = matrix.flipped_up_down()
    assert(matrix.get_data() == [[1, 2, 3], [4, 5, 6]])
    assert(matrix.size() == (2, 3))
    assert(new_matrix == [[4, 5, 6], [1, 2, 3]])
    empty_matrix = MyMatrix([ ])
    e = empty_matrix.flipped_up_down()
    assert(empty_matrix.get_data() == [])
    assert(empty_matrix.size() == (0,0))
    assert(e == [])
    
def test_flipped_left_right():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]]) 
    new_matrix = matrix.flipped_left_right()
    assert(matrix.get_data() == [[1, 2, 3], [4, 5, 6]])
    assert(matrix.size() == (2, 3))
    assert(new_matrix == [[3, 2, 1], [6, 5, 4]])
    empty_matrix = MyMatrix([ ])
    e = empty_matrix.flipped_left_right()
    assert(empty_matrix.get_data() == [])
    assert(empty_matrix.size() == (0,0))
    assert(e == [])

def test_transpose():
    data = [[1, 2, 3], [4, 5, 6]]
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    matrix.transpose() 
    assert(matrix.get_data() == [[1, 4], [2, 5], [3, 6]])
    assert(matrix.size() == (3, 2))
    empty_matrix = MyMatrix([])
    empty_matrix.transpose()
    assert(empty_matrix.size() == (0, 0))
    assert(empty_matrix.get_data() == [])

def test_transposed():
    data = [[1, 2, 3], [4, 5, 6]]
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    m = matrix.transposed()
    assert(m == [[1, 4], [2, 5], [3, 6]])
    assert(matrix.size() == (2, 3))
    assert(matrix.get_data() == data)
    empty_matrix = MyMatrix([])
    empty_matrix.transposed()
    assert(empty_matrix.size() == (0, 0))
    assert(empty_matrix.get_data() == [])

def test__sub__():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    other = [[12, 2, 3], [900, 67, 4]]
    assert(matrix - other == [[-11, 0, 0], [-896, -62, 2]])
    assert(matrix.get_data() == [[1, 2 ,3], [4, 5, 6]])
    assert(other == [[12, 2, 3], [900, 67, 4]])

def test__add__():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    other =[[12, 2, 3], [900, 67, 4]]
    assert(matrix + other == [[13, 4, 6], [904, 72, 10]])
    assert(matrix.get_data() == [[1, 2, 3], [4, 5, 6]])
    assert(other == [[12, 2, 3], [900, 67, 4]])

def test__iadd__():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    other =[[12, 2, 3], [900, 67, 4]]
    matrix+=other
    assert(matrix == [[13, 4, 6], [904, 72, 10]])
    assert(other == [[12, 2, 3], [900, 67, 4]])
    
def test__isub__():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    other = [[12, 2, 3], [900, 67, 4]]
    matrix -= other 
    assert(matrix == [[-11, 0, 0], [-896, -62, 2]])
    assert(other == [[12, 2, 3], [900, 67, 4]])

