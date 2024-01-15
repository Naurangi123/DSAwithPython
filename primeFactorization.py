
def prime_factorization(n):
    for i in range(2, n+1):
        if i <= n:
            while n % i == 0:
                n = n//i
                print(i)
        else:
            i = i+1


n = int(input("Enter User Number :"))
prime_factorization(n)

# def prime_factor(n):
#     i = 2
#     while i*i <= n:
#         if n % i == 0:
#             n = n // i
#             print(i)
#         else:
#             i = i + 1
#     if n != 1:
#         print(n)


# n = int(input("Enter User Number :"))
# prime_factor(n)
