# kata: https://www.codewars.com/kata/5263c6999e0f40dee200059d

# ---
def get_pins(observed):
    adjacent = {
        "0" : ["0", "8"],
        "1" : ["1", "2", "4"],
        "2" : ["1", "2", "3", "5"],
        "3" : ["2", "3", "6"],
        "4" : ["1", "4", "5", "7"],
        "5" : ["2", "4", "5", "6", "8"],
        "6" : ["3", "5", "6", "9"],
        "7" : ["4", "7", "8"],
        "8" : ["0", "5", "7", "8", "9"],
        "9" : ["6", "8", "9"],
    }

    all_pins = adjacent[observed[0]]
    for i in range(1, len(observed)):
        all_pins = [previous + next_digit for previous in all_pins for next_digit in adjacent[observed[i]]]
    
    return all_pins

print(get_pins("300"))