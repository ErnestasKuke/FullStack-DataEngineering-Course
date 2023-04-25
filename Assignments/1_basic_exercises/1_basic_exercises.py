# Exercise nr. 1
def find_sum(a, b):
    return a + b


print(find_sum(5, 7))


# Exercise nr. 2
def celsius_to_fahrenheit(celsius):
    return f"Temperature in Fahrenheit: {celsius * 1.8 + 32}"


print(celsius_to_fahrenheit(25))


# Exercise nr. 3
def fibonacci(n):
    nterms = n
    n1, n2 = 0, 1
    count = 0
    if nterms <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        while n1 <= n:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1


fibonacci(50)


# Exercise nr. 4
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(even_or_odd(3))

# Exercise nr. 5
list = [10, 20, 15]


def largest_number(number_list):
    return max(number_list)


print(largest_number(list))
