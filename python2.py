# datatypes_demo.py

# 1 & 2. Declare variables of different data types
integer_var = 10          # int
float_var = 3.14          # float
string_var = "Hello"      # string
boolean_var = True        # boolean

# 3. Print the type of each variable
print("Data Types:")
print("integer_var:", type(integer_var))
print("float_var:", type(float_var))
print("string_var:", type(string_var))
print("boolean_var:", type(boolean_var))

print("\nArithmetic Operations:")
# 4. Perform arithmetic operations
sum_result = integer_var + float_var
difference = integer_var - float_var
product = integer_var * float_var
division = integer_var / float_var

print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)

print("\nType Casting with User Input:")
# 5 & 6. Convert string input to int and float with error handling
try:
    user_input = input("Enter a number: ")
    int_value = int(user_input)
    float_value = float(user_input)

    print("Integer value:", int_value)
    print("Float value:", float_value)

except ValueError:
    print("Invalid input! Please enter a valid numeric value.")

print("\nString and Number Concatenation:")
# 7. Concatenate strings and numbers properly
age = 25
message = "I am " + str(age) + " years old."
print(message)

print("\nDynamic Typing Demonstration:")
# 8. Demonstrate dynamic typing
dynamic_var = 100
print(dynamic_var, type(dynamic_var))

dynamic_var = "Now I'm a string"
print(dynamic_var, type(dynamic_var))

dynamic_var = 9.81
print(dynamic_var, type(dynamic_var))
