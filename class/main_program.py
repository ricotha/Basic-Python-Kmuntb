# # 1 - option to call packages
# import packages.a_function as aa
# import packages.b_function as bb

# # packages. a_function.greeting()
# aa.greeting()
# print(bb.adding(4,5))

# # 2 - option to call function
# from packages.a_function import greeting
# from packages.b_function import adding

# import math

# greeting()
# print(adding(4,5))

# print(math.sqrt(16))
# print(math.pi)
# print(math.log(20))

# Recursion 
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))