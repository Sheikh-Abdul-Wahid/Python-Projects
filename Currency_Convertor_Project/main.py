# Open the file containing currency data and read its contents
with open("CurrencyData.txt") as f:
    lines = f.readlines()  # Read all lines from the file

# Create an empty dictionary to store currency names and their conversion rates
currencyDict = {}

# Process each line from the file
for line in lines:
    parsed = line.split("\t")  # Split the line into currency name and conversion rate using tab
    currencyDict[parsed[0].lower()] = parsed[1]  # Store the currency name in lowercase as key and conversion rate as value

# Prompt the user to enter an amount in INR
while True:  # Keep asking until a valid number is entered
    try:
        amount = float(input("Enter the amount: "))  # Convert user input to a float
        break  # Exit the loop if input is valid
    except ValueError:  # Handle non-numeric input
        print("Invalid amount. Please enter a numeric value.")

# Display the available currency options
print("Please enter the name of the currency you want to convert to. Available Options are:")
for item in currencyDict.keys(): 
    print(item.upper())  # Print each available currency name in uppercase

# Ask the user to choose a currency for conversion
while True:  # Keep asking until a valid currency name is entered
    try:
        currency = input("Write/Paste the name from the above options: ").lower()  # Convert input to lowercase
        # Calculate the converted amount by multiplying with the conversion rate
        result = amount * float(currencyDict[currency])
        # Display the converted amount
        print(f"{amount} INR is equal to {result} {currency.upper()}")  # Display the currency in uppercase
        break  # Exit the loop if everything is successful
    except KeyError:  # Handle cases where the entered currency is not in the dictionary
        print("Invalid currency name. Please try again.")
        
        
