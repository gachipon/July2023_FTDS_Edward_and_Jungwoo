import os.path

def calculate_annual_deposits():
    if interest_rate_value != 0:
        annual_deposits = savings_required / (( 1 + interest_rate_value ) * ((( 1 + interest_rate_value) ** number_of_contributions ) - 1 ) / interest_rate_value)
    else:
        annual_deposits = savings_required/number_of_contributions
    return round(annual_deposits, 2)

# Loop based function to show the value accumulated every year
# Nice to show each value in a table or list
def tabulate_annual_deposits():
    end_of_year_value = 0
    end_of_year_list = []
    for i in range(number_of_contributions):
        end_of_year_value = (end_of_year_value + calculate_annual_deposits()) * ( 1 + interest_rate_value)
        end_of_year_list.append(round(end_of_year_value, 2))
    return end_of_year_list

def create_table():
    with open("Test.txt", "w") as my_file:
        for i in range(len(end_of_year_values)):
            my_file.write(f"Year {i + 1}\t|\t$ {end_of_year_values[i]} \n")

# The different variables
current_age = int(input("How old are you right now?: "))
retiring_age = int(input("At what age do you wish to retire?: "))
if retiring_age < current_age:
    print("You shouldn't be using this if you are already retired.")
    exit()
interest_rate = float(input("What is your expected annual return rate?: "))
if interest_rate == 0:
    print("Perpetuity cannot have 0% interest..., You might as well store money under your bed.")
    exit()
annual_dividends = float(input("How much will you spend per year after you retire?: "))

number_of_contributions = retiring_age - current_age
interest_rate_value = interest_rate/100

savings_required = annual_dividends/interest_rate_value


annual_deposits = calculate_annual_deposits()
end_of_year_values = tabulate_annual_deposits()

attempts = 0
while True:
    options = input("\nWhat would you like to see?: "
                    "\n1.\tAnnual deposits. "
                    "\n2.\tTotal Expected Savings. "
                    "\n3.\tBalance at end of each year. "
                    "\n4.\tTabulate in a document. "
                    "\n5.\tClose program. "
                    "\nSelect your option:\t")
    if options == '1':
        print(f"You will need to deposit ${annual_deposits} every year for {number_of_contributions} years.")
    elif options == '2':
        print(f"Your total savings at the end of {number_of_contributions} years will be ${savings_required}. This value is rounded down.")
    elif options == '3':
        for i in end_of_year_values:
            print("Year ", end_of_year_values.index(i)+1, "\t:\t", i)
    elif options == '4':
        create_table()
        print("Successfully printed Table in a new document.")
    elif options == '5':
        print("Shutting Down...")
        break
    else:
        if attempts >= 3:
            break
        else:
            print(f"That input is not an available option. You have {3 - attempts} more attempts before we shut down.")
            attempts += 1