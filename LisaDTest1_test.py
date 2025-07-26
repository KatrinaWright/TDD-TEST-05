import LisaDTest1 as L1;


# Example Passing Test
def test_hello_pass():
    assert L1.hello_world() == "Hello!"

# Example Failed Test
# Uncomment, run once & then comment out again
#def test_hello_fail():
#    assert L1.hello_world() == "Hello World!"

#########################
#  HW Assignment Tests  #
#########################

# Problem 1 Tests
def test_function_one():
    assert L1.function_1( 1 ) == 1

def test_function_five():
    assert L1.function_1( 5 ) == 15

def test_function_ten():
    assert L1.function_1( 10 ) == 55

def test_function_eleven():
    assert L1.function_1( 11 ) == 66

def test_function_str():
    assert L1.function_1( "twelve" ) == None

def test_function_two():
    assert L1.function_1( 2 ) == 3

def test_function_list():
    list = list = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]
    for i in range(20):
        assert L1.function_1( i + 1  ) == list[i]

