import main;

def test1():
    assert main.make_tuples([1,2,3,4], [5,6,7,8]) == [(1,5), (2,6), (3,7), (4,8)]
def test2():
    assert main.make_tuples([1,2.5,3,4], [5,6,7,8]) == [(1,5), (2.5,6), (3,7), (4,8)]
def test3():
    assert main.make_tuples(['a','b','c','d'], ['e','f','g','h']) == [('a','e'), ('b','f'), ('c','g'), ('d','h')]
