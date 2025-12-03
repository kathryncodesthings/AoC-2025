
def movedial(current_dial_value, input_value, direction, hit_zero):
    
    input_value = int(input_value)

    for x in range(input_value):
        if direction == "L": current_dial_value = current_dial_value  - 1
        else: current_dial_value = current_dial_value + 1
        
        if current_dial_value == 100: current_dial_value = 0
        if current_dial_value == -1: current_dial_value = 99
        
        if current_dial_value == 0: hit_zero += 1
        
    # print (f"Initial dial value: {current_dial_value} \n Input value: {input_value} \n Times on zero rotations: {hit_zero}")

    return  current_dial_value, hit_zero



password = 0
current_dial_value = 50
hit_zero = 0

with open('Day 1 input.txt') as f:
    for line in f:
        direction = line[0]
        input_value = line[1:]
        input_value = int(input_value)
        # print (direction)
        # print (input_value)
        current_dial_value, hit_zero = movedial(current_dial_value, input_value, direction, hit_zero)  
              
print("Password:")
print (hit_zero)


