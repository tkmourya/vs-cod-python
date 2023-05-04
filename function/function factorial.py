#n! = 1 x 2 x 3 x 4 x 5..x n
#n! = [1 x 2 x 3 x 4...n-1] x n
#n! = (n-1)! x n

# n = 0
# product = 1

# for i in range(n):
#     product = product * (i+1)
# print(product)




def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
        return product

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n* factorial_recursive(n-1)



f = factorial_recursive(5)
print(f)