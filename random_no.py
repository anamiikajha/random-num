import random

randint_input = int(input("Enter a Range for Random Integer: "))

def gen_randint(randint_input):
    randint_val = random.randint(0,randint_input)
    print("The random number is:")
    return randint_val

# output

randint_output = gen_randint(randint_input)
print(randint_output)
