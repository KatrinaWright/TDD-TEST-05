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

def test_function_one():
    assert L1.function_1( 5 ) == 15

def test_function_one():
    assert L1.function_1( 10 ) == 55
