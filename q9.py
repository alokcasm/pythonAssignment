# Q9. Demonstrate use of break, continue, and pass in loops.


print("==========break===============")
#break {use of break- after condition match loop will stop }
for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("==========continue===============")
#continue {use of continue- after matching condition , skip that one iteration}
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


print("==========pass===============")
# pass is a null statement → it does nothing
# it is used as a placeholder when we want to add code later
for i in range(1, 4):
    if i == 2:
        pass
    print(i)