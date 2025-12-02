#Advent of Code 2025 Day 1 part 1


def movedial(current_dial_value, input_value, direction, dial_max):  
    if direction == "L": input_value = input_value *-1
    new_dial_value = (current_dial_value + input_value) % (dial_max+1)
    return new_dial_value

password = 0
current_dial_value = 50
dial_max = 99
dial_min = 0

with open('Day 1 input.txt') as f:
    for line in f:
        direction = line[0]
        input_value = line[1:]
        input_value = int(input_value)
        current_dial_value = movedial(current_dial_value, input_value, direction, dial_max)  
        #print (current_dial_value)
        if current_dial_value == 0:
            password += 1

print("Password is:")    
print (password)


