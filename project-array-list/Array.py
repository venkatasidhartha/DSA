#  Calculating the Average Temperature


number_days = int(input("How many day's Temperature: "))
total = 0
temp = []
for i in range(0,number_days):
    nextDays = float(input("Day "+ str(i+1) + "'s high Temperature: "))
    temp.append(nextDays)
    total += temp[i]

avg = round(total/number_days,2)
print(f"\nAverage = {avg}")
above = 0
for i in temp:
    if i > avg:
        above += 1

print(f"{above} days's above average")