ratio = float(input("ratio: "))
sensitivity = float(input("sensitivity: "))
year = 0

while True:
    if ratio >= sensitivity:
        print("Year %d: ratio = %s"%(year, ratio))
        year += 5730
        ratio /= 2 
        if year == 0:
            pass
    elif sensitivity >= ratio:
        break

# Output
# ratio: 1
# sensitivity: 0.001
# Year 0: ratio = 1.0
# Year 5730: ratio = 0.5
# Year 11460: ratio = 0.25
# Year 17190: ratio = 0.125
# Year 22920: ratio = 0.0625
# Year 28650: ratio = 0.03125
# Year 34380: ratio = 0.015625
# Year 40110: ratio = 0.0078125
# Year 45840: ratio = 0.00390625
# Year 51570: ratio = 0.001953125
    
# ratio: 1.2
# sensitivity: 0.004
# Year 0: ratio = 1.2
# Year 5730: ratio = 0.6
# Year 11460: ratio = 0.3
# Year 17190: ratio = 0.15
# Year 22920: ratio = 0.075
# Year 28650: ratio = 0.0375
# Year 34380: ratio = 0.01875
# Year 40110: ratio = 0.009375
# Year 45840: ratio = 0.0046875