#LisaDtest1.py
# NAME:         FIXME
# GUESS: What are we making? ___________________

# Example
def hello_world():
    return "Hello!"

def function_1(data):
    if data == 5:
        return data*3
    replacements = {
        10: 55,
        11: 66,
        "twelve": None
        }
        
    return replacements.get(data, data)

def main():
    print(function_1(1))

main()
