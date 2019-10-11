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
     empty_matrix = MyMatrix([ ])
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
    assert(new_matrix.get_data() == [[4, 5, 6], [1, 2, 3]])
    empty_matrix = MyMatrix([ ])
    e = empty_matrix.flipped_up_down()
    assert(empty_matrix.get_data() == [])
    assert(empty_matrix.size() == (0,0))
    assert(e.get_data() == [])
    
def test_flipped_left_right():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]]) 
    new_matrix = matrix.flipped_left_right()
    assert(matrix.get_data() == [[1, 2, 3], [4, 5, 6]])
    assert(matrix.size() == (2, 3))
    assert(new_matrix.get_data()== [[3, 2, 1], [6, 5, 4]])
    empty_matrix = MyMatrix([ ])
    e = empty_matrix.flipped_left_right()
    assert(empty_matrix.get_data() == [])
    assert(empty_matrix.size() == (0,0))
    assert(e.get_data() == [])

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
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    m = matrix.transposed()
    assert(m.get_data() == [[1, 4], [2, 5], [3, 6]])
    assert(matrix.size() == (2, 3))
    assert(matrix.get_data() == [[1, 2, 3], [4, 5, 6]])
    empty_matrix = MyMatrix([])
    e = empty_matrix.transposed()
    assert(empty_matrix.size() == (0, 0))
    assert(empty_matrix.get_data() == [])
    assert(e.get_data() == [])
    
def test__sub__():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    other = MyMatrix([[12, 2, 3], [900, 67, 4]])
    m = matrix - other
    assert(m.get_data() == [[-11, 0, 0], [-896, -62, 2]])
    assert(matrix.get_data() == [[1, 2 ,3], [4, 5, 6]])
    assert(other.get_data() == [[12, 2, 3], [900, 67, 4]])

def test__add__():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    other = MyMatrix([[12, 2, 3], [900, 67, 4]])
    m = matrix + other
    assert(m.get_data() == [[13, 4, 6], [904, 72, 10]])
    assert(matrix.get_data() == [[1, 2, 3], [4, 5, 6]])
    assert(other.get_data() == [[12, 2, 3], [900, 67, 4]])

def test__iadd__():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    other = MyMatrix([[12, 2, 3], [900, 67, 4]])
    matrix += other
    assert(matrix.get_data() == [[13, 4, 6], [904, 72, 10]])
    assert(other.get_data() == [[12, 2, 3], [900, 67, 4]])
    
def test__isub__():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    other = MyMatrix([[12, 2, 3], [900, 67, 4]])
    matrix -= other 
    assert(matrix.get_data() == [[-11, 0, 0], [-896, -62, 2]])
    assert(other.get_data() == [[12, 2, 3], [900, 67, 4]])
    
def test__getitem__():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    assert(matrix[0][2] == 3)
    assert(matrix[0, 2] == 3)
    
    
def test__setitem__():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    matrix[0][1] = 5
    assert(matrix[0][1] == 5)

def test_rotate_clockwise_90():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    matrix.rotate_clockwise_90()
    assert(matrix.get_data() == [[4,1], [5,2], [6, 3]])
    empty_matrix = MyMatrix([])
    empty_matrix.rotate_clockwise_90()
    assert(empty_matrix.get_data() == [ ])
    
def test_rotate_counterclockwise_90():
    matrix = MyMatrix([[1,2, 3], [4, 5, 6]])
    empty_matrix = MyMatrix( [ ] )
    matrix.rotate_counterclockwise_90()
    empty_matrix.rotate_counterclockwise_90()
    assert(matrix.get_data() == [[3, 6], [2, 5], [1, 4]])
    assert(empty_matrix.get_data() == [])

def test_rotate_180():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    empty_matrix = MyMatrix([])
    matrix.rotate_180()
    empty_matrix.rotate_180()
    assert(matrix.get_data() == [[6, 5, 4], [3, 2,1]])
    assert(empty_matrix.get_data() == [])
    
def test_rotated_clockwise_90():
    matrix = MyMatrix([[1, 2 , 3], [4, 5, 6]])
    new_matrix = matrix.rotated_clockwise_90()
    assert(new_matrix.get_data() == [[4,1], [5,2], [6, 3]])
    assert(matrix.get_data() == [[1, 2, 3], [4, 5, 6]])
    empty_matrix = MyMatrix( [ ])
    e = empty_matrix.rotated_clockwise_90()
    assert(e.get_data() == [])
    assert(empty_matrix.get_data() == [])
    
def test_rotated_counterclockwise_90():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    new_matrix = matrix.rotated_counterclockwise_90()
    assert(matrix.get_data() == [[1, 2, 3], [4, 5, 6]])
    assert(new_matrix.get_data() == [[3, 6], [2, 5], [1, 4]])
    empty_matrix = MyMatrix( [ ])
    e = empty_matrix.rotated_counterclockwise_90()
    assert(e.get_data() == [])
    assert(empty_matrix.get_data() == [])

def test_rotated_180():
    matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
    new_matrix = matrix.rotated_180()
    assert(new_matrix.get_data() == [[6, 5, 4], [3, 2, 1]])
    assert(matrix.get_data() == [[1, 2, 3], [4, 5 ,6]])
    empty_matrix = MyMatrix( [ ])
    e = empty_matrix.rotated_180()
    assert(e.get_data() == [])
    assert(empty_matrix.get_data() == [])

