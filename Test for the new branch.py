def check_weirdness(n):
    if n % 2 == 1:  # Check if n is odd
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:  # Even and in range 2 to 5
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:  # Even and in range 6 to 20
        print("Weird")
    elif n % 2 == 0 and n > 20:  # Even and greater than 20
        print("Not Weird")

# Test the function with some examples
n = int(input("Enter an integer: "))
check_weirdness(n)