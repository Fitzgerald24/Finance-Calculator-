import math
#Creatin a financial program that calculates investmenent and home loans
'''its going to ask user to choose between investment or bond. Depending on chioce if bond they go to bond calculatios
if it is investment they again get to choose between simple or compound interest caculations'''
#and the program should print out appropriate results after every calculation
print ("Investment - to calculate the amount of interest you'll earns on your investment")
print("Bond        - to calculate the amount you will pay on home loan bond")
print("")
invest_bond = input("Please enter either 'investment' or 'bond' from the menu above to proceed: ").lower()#appropriate caps or not 
#First if statement gets input from user and creates variables activeted if chioce is investment or otherwise
if invest_bond == "investment": 
    deposit = float(input("Enter the amount of money that you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    years = int(input("Enter the number of years you plan on Investing for: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()
    ''' 
    print(invest_bond + "innvestment interest")'''
#next if and else if statements calculate simple interest or compound interest depending on interest_type chioce 
    if interest_type == "simple ":
        interest = deposit * (1 + interest_rate * years)
    elif interest_type == "compound  ":
        interest = deposit * math.pow((1 + interest_rate), years)

    print(f"The interest earned over {years} years will be £{interest_type :.2f}")
#this else if activeted when invest_bond inputs bond    
elif invest_bond == "bond":
    house_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate: ")) / 100
    months = int(input("Enter the number of months you plan to repay the bond: "))

    monthly_payment = (interest_rate / 12) * house_value / (1 - math.pow((1 + (interest_rate / 12)), (-months)))

    print(f"Your monthly repayment will be £{monthly_payment:.2f}")
#this promps correct input if there is an invalid input
else:
    print("Invalid entry. Please enter either 'investment' or 'bond'.")