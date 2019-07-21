#Sam Lyons
#CIS-294
#1/29/19
#Assignment 1

"""A program designed to calculate wages given user input of
tax rates, hours of work, gross pay, and net pay
and then prints that information to the user."""

TAX_RATE = 27.0/100

def main(): 

        wage = 0
        hours = 0
        gross = 0
        taxAmount = 0
        netPay = 0

        print('Please Enter your Hourly Wage: ', end = ' ')
        wage = float(input())

        print('Please Enter the Number of Hours Worked: ', end = ' ')
        hours = float(input())

        gross = (wage * hours)
        taxAmount = (TAX_RATE * gross)
        netPay = (gross - taxAmount)

        print('Wage: ', wage)
        print('Hours Worked: ', hours)
        print('Tax Rate: ', (TAX_RATE * 100), '%')
        print('Gross Pay: $', gross)
        print('Tax Amount: $', taxAmount)
        print('Net Pay: $', netPay)

main()




