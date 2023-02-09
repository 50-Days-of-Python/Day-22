import main;

def test1():
    assert main.remove_underscore(add_underscore(add_hash('Python'))) == 'Python'
def test2():
    assert main.remove_underscore(add_underscore(add_hash('Hello World'))) == 'HelloWorld'
def test3():
    assert main.remove_underscore(add_underscore(add_hash('Foo Bar Baz'))) == 'FooBarBaz'
