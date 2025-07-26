#LisaDtest1.py
# NAME:         FIXME
# GUESS: What are we making? ___________________

# Example
def hello_world():
    return "Hello!"

def function_1(data):
    print(type(data), data)

    if data == 5:
        return data*3
    

    replacements = {
        2:3,
        10: 55,
        11: 66,
        "twelve": None
        }
    if isinstance(data, int) and 1 <= data <= 20:
        return data * (data + 1) // 2

        
    return replacements.get(data, data)

def main():

    print(function_1(1))

main()
