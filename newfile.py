
# Get the operation choice from the user
op = int(input("Enter the operation (1 for +, 2 for -, 3 for *, 4 for /): "))
print("Press 'e' to get the result and exit.")

if op == 1:
    
    num = 1000

    # Initialize the counter and sum
    i = 0
    total_sum = 0

    # Use a while loop to add the numbers
    while i < num:
        dum = input("Enter a number: ")
        if dum == 'e':
            print(f"The total sum is: {total_sum}")
            break  # Exit the loop if 'e' is entered

        total_sum += int(dum)  # Add the input number to the sum
        i += 1  # Increment the counter

elif op == 2:
    
    num = 1000

    # Initialize the counter and total_sum
    i = 0
    total_sum = int(input("Enter the first number: "))  # Initialize total_sum with the first number

    # Use a while loop to subtract the numbers
    while i < num - 1:  # Subtract the remaining numbers
        dum = input("Enter a number: ")
        if dum == 'e':
            print(f"The total sum is: {total_sum}")
            break  # Exit the loop if 'e' is entered

        total_sum -= int(dum)  # Subtract the input number from total_sum
        i += 1  # Increment the counter
    
elif op == 3:
    num = 1000

    # Initialize the counter and total_multi
    i = 0
    total_multi = int(input("Enter the first number: "))  # Initialize total_multi with the first number

    # Use a while loop to multiply the numbers
    while i < num - 1:  # Multiply the remaining numbers
        dum = input("Enter a number: ")
        if dum == 'e':
            print(f"The result of multiplication is: {total_multi}")
            break  # Exit the loop if 'e' is entered

        total_multi *= int(dum)  # Multiply the input number with total_multi
        i += 1  # Increment the counter

elif op == 4:
    num = 1000

    # Initialize the counter and total_div
    i = 0
    total_div = int(input("Enter the initial number: "))  # Initialize total_div with the initial number

    # Use a while loop to divide the numbers
    while i < num - 1:  # Divide by the remaining numbers
        dum = input("Enter a number to divide by: ")
        if dum == 'e':
            print(f"The result of division is: {total_div}")
            break  # Exit the loop if 'e' is entered

        total_div /= int(dum)  # Divide total_div by dum
        i += 1  # Increment the counter  
    
    print(f"The result of division is: {total_div}")