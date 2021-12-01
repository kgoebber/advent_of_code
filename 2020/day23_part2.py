def get_destination(check_cup, next_three):
    destination = check_cup - 1
    if destination < 1:
        destination = 1000000
    while destination in next_three:
        destination -= 1
        if destination < 1:
            destination = 1000000
    return destination


cups = list(map(int, list('523764819'))) + list(range(10, 1000001))
for _ in range(10000000):
    current_cup = cups.pop(0)
    #print(current_cup)
    next_three = cups[:3]
    #print(next_three)
    del cups[:3]
    destination = get_destination(current_cup, next_three)
    #print(destination)
    cups.append(current_cup)
    for i, val in enumerate(next_three):
        cups.insert(cups.index(destination)+1+i, val)
    #print(cups)
    #print()
#print(cups)
final_order = cups[cups.index(1)+1:]+cups[:cups.index(1)]
print(final_order[:3])
