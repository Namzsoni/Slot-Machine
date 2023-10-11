import random

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

symbol_values = {
    "A": 5,
    "B": 4, 
    "C": 3,
    "D": 2
}

#check if the the user wins on any combination
#if the user bets on one line he is choosing the first line and if the user bets on 2 lines he is betting on both 1 and 2 and so on
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
            winnings += values[symbol]*bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


#generate the outcome of the slot machine 
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = [] #each of our nested list will represent the values in the column
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #since we want a copy we use slicing 
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

#print the rows and columns, since are columns are stored differently we have to essentially transpose the matrix and print 
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|", end=' ')
            else:
                print(column[row])



#user input that gets the deposit of the user
def deposit():
    while True:
        amount = input("What Would you like to deposit? $") #this inputs a string
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be greater than 0")
        else:
            print("Please enter a number.")
    return amount

#user input for the number of lines the user wants to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ") 
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

#user input for what they would like to bet
def get_bet():
    while True:
        amount = input("What Would you like to bet on each line? $") #this inputs a string
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET < amount < MAX_BET:
                break
            else:
                print("Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet =  bet*lines
        if total_bet > balance:
            print(f"you do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    print(COLS) 
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"you won ${winnings}.")
    print(f"you won on lines: ", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print("Current balance is: ${balance}")
        answer = input("Press enter to Play. (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    print("You left with ${balance}")


    
main() 
