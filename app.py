from datetime import datetime
# name = input("What is your name? \n")
allowedUsers = ['Bello', 'Raj', 'Sola']
allowedPassword = ['passwordBello', 'passwordRaj', 'passwordSola']
accountBalance = [0, 0, 0]
loginTrials = 3
loginCount = 0

while loginCount < loginTrials:
    name = input("What is your name? \n")

    if name in allowedUsers:
        password = input("Your password? \n")
        userId = allowedUsers.index(name)

        if password == allowedPassword[userId]:
            currentTime = datetime.now()
            print('Welcome %s, you logged in at exactly %s ' % (name, currentTime))
            print('These are the available options: ')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Complaint')

            selectedOption = int(input('Please select an option: \n'))

            if selectedOption == 1:
                withdrawalAmount = int(input('How much would you like to withdraw? \n'))
                accountBalance[userId] -= withdrawalAmount
                print(f'You have withdrawn {withdrawalAmount}. Please take your cash.')
                response = input("Would you like to perform another transaction? Y/N \n")
                if response.lower() == 'y':
                    continue
                else:
                    break

            elif selectedOption == 2:
                depositAmount = int(input('How much would you like to deposit? \n'))
                accountBalance[userId] += depositAmount
                print(f'You have deposited {depositAmount}. Your current balance is {accountBalance[userId]}.')
                response = input("Would you like to perform another transaction? Y/N \n")
                if response.lower() == 'y':
                    continue
                else:
                    break

            elif selectedOption == 3:
                complaint = input('What issue will you like to report? \n')
                print('Your complaint has been logged. Thank you for contacting us')
                break

            else:
                print('Invalid option selected, please try again')

        else:
            print('Password Incorrect, please try again')
            loginCount += 1
            print(f'You have {loginTrials - loginCount} attempts left ')
    else:
        print('Name not found, Please try again')
        loginCount += 1
        print(f'You have {loginTrials - loginCount} attempts left ')

