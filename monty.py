import random

#monty hall problem
#no switch
noSwitchWins = 0;
SwitchWins = 0;
for i in range(9999999):
    doors = [0,1,2]
    winingDoor = random.randint(0,2)
    selectedDoor_stay =  doors.pop(random.randrange(len(doors)))
    selectedDoor_switch = 0

    if selectedDoor_stay == winingDoor:
        noSwitchWins +=1
    else:
        SwitchWins +=1


print("switch wins: ", SwitchWins , "\n noSwitch Wins: ",noSwitchWins)

if SwitchWins == noSwitchWins:
    print("tie");
    exit();


if SwitchWins > noSwitchWins:
    print("Switching Won!")
else:
    print("not Switching Won!")