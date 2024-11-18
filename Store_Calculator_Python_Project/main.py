# Created a store calculator for a simple general store to calculate the total amount 
# Quits the loop when the user presses 'q' and generates a receipt.

prices = []  # List to store prices of items
sum = 0      # Variable to store the total sum of prices

# Infinite loop to keep taking input until the user decides to quit
while True:  
    userinput = input("Enter the item price or press 'q' to quit: ")  # Ask for user input
    if userinput.strip() == "":                                       # Check if the input is empty
        print("Invalid input. Please enter a valid number or 'q' to quit.")
        continue  # Continue the loop

    elif userinput.lower() != "q":
        try:
            price = float(userinput)
            if price < 0:                               # Check if the input is a negative number
                print("Invalid input. Please enter a positive number or 'q' to quit.")
                continue # Continue the loop
            sum = sum + price                           # Add the entered price to the total sum
            prices.append(price)                        # Add the entered price to the prices list
            print(f"The total price so far: {sum}.")    # Display the updated total price

        except ValueError:                              # Handle invalid inputs that cannot be converted to a number
            print("Invalid input. Please enter a valid number or 'q' to quit.")

    else:                                           # If the user input is "q"
        print("\nReceipt Generated:")               # Print a receipt header
        for i, price in enumerate(prices, start=1): # Loop through the prices list with item numbers
            print(f"Item {i}: {price}")             # Display each item number and its price
        print(f"\nThe total price is {sum}. Thanks for shopping.")  # Display the total price and a thank-you message
        break  # Exit the loop
