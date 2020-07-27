# This Problem is about Callatz Guest
guestNum = eval(input())
paces = 0  # The number of steps in while loop
while guestNum > 1:
    if guestNum % 2 == 0:
        guestNum /= 2
        paces += 1
    else:
        guestNum = (guestNum * 3 + 1) / 2
        paces += 1
print(paces)
