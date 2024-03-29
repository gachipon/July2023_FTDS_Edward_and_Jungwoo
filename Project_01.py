# Import datetime is for importing date/time module for python to easily get time stamps
import datetime

# This function just calculates how much should be deposit in the account each year
def calculate_annual_deposits():
    # Interest rate cannot be zero...because you cannot have a perpetuity account with 0 % interest
    if interest_rate_value != 0:
        annual_deposits = savings_required / (( 1 + interest_rate_value ) * ((( 1 + interest_rate_value) ** number_of_contributions ) - 1 ) / interest_rate_value)
    else:
        annual_deposits = savings_required/number_of_contributions
    return round(annual_deposits, 2) #The '2' represents number of decimal points the result is returned
    # Money is usually counted to cents...this may result in some rounding...but its pretty negligible

# Loop based function to show the value accumulated every year
# Nice to show each value in a table or list
def tabulate_annual_deposits():
    end_of_year_value = 0
    end_of_year_list = []
    # Loop will add the end of year contribution (along with the compounded interest) for each year
    for i in range(number_of_contributions):
        end_of_year_value = (end_of_year_value + calculate_annual_deposits()) * ( 1 + interest_rate_value)
        end_of_year_list.append(round(end_of_year_value, 2))
    return end_of_year_list

# This creates a more visual look at the amount at end of each year
def create_table():
    time_now = datetime.datetime.now().strftime("%c")
    with open(f"Document_on_{time_now}.txt", "w") as my_file:
        my_file.write(f"Created on {time_now}\n\n")
        for i in range(len(end_of_year_values)):
            my_file.write(f"Year {i + 1}\t|\t$ {end_of_year_values[i]} \n")

while True:
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
                        "\n6.\tReset Variables. "
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
            print("Successfully printed Table in a new document. Now shutting down...")
            exit()
        elif options == '5':
            print("Shutting Down...")
            exit()
        elif options == '6':
            print("Reseting to new variables...")
            break
        else:
            if attempts >= 3:
                exit()
            else:
                print(f"That input is not an available option. You have {3 - attempts} more attempts before we shut down.")
                attempts += 1