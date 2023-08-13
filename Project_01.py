import os.path

# The different variables
current_age = int(input("How old are you right now?: "))
retiring_age = int(input("At what age do you wish to retire?: "))
interest_rate = float(input("What is your expected annual return rate?: "))
annual_dividends = float(input("How much will you spend per year after you retire?: "))

number_of_contributions = retiring_age - current_age
interest_rate_value = interest_rate/100
savings_required = annual_dividends/interest_rate_value

# Fast calculation of end result for users interested only in end value
# Uses an existing financial equation for annuity/perpetuity calculator
def calculate_annual_deposits():
    annual_deposits = savings_required / (( 1 + interest_rate_value ) * ((( 1 + interest_rate_value) ** number_of_contributions ) - 1 ) / interest_rate_value)
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

annual_deposits = calculate_annual_deposits()
list_of_year_end_values = tabulate_annual_deposits()

def create_table():
    with open("Test.txt", "w") as my_file:
        for i in range(len(list_of_year_end_values)):
            my_file.write(f"Year {i + 1}    |   $ {list_of_year_end_values[i]} \n")

print(create_table())