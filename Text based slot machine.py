import random
#Global constant or something that's not gonna change. Being in all capital makes a constant 
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines
        

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)
# defining columns list 
    columns = []
#generate a column for every single column that we have     
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
#This line selects a random value from the current_symbols list using the random.choice() function. 
# It assigns the selected value to the variable value.
            value = random.choice(current_symbols)
#This line removes the selected value from the current_symbols list so that it won't be chosen again in the same column. 
# This ensures that each value is unique within a column.
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate (columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end= " ")
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        #isdigit to check if the amount is a valid number
        if amount.isdigit():
            #convert to a integer 
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0. ")
            #if the amount is not a digit:
        else:
            print("Please enter a number. ")
    return amount

def get_number_of_lines():
    while True:
# Added MAX_lines into the string with str so they dont get squish together
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        #isdigit to check if the amount is a valid number
        if lines.isdigit():
            #convert to a integer 
            lines = int(lines)
            #to check if a value is in between 2 values. lines greater than or equal to 1 (o que esta a frente do =
            # é que conta primeiro)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines. ")
            #if the amount is not a digit:
        else:
            print("Please enter a number. ")

    return lines 

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        #isdigit to check if the amount is a valid number
        if amount.isdigit():
            #convert to a integer 
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}. ")
            #if the amount is not a digit:
        else:
            print("Please enter a number. ")
    return amount

    
def spin(balance):
    lines = get_number_of_lines()
# so the user doesnt put a amount greater than what he has 
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance} ")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You Won ${winnings}")
    print("You Won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to Play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    

    print(f"You left with ${balance}")
main()
