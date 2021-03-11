# tentti numerot
tGrades = []
tot = 0
print("Syötä Tenttien Määrä: ")
# kuinka monta tenttiä
try:
    tNum = int(input())
except:
    print("Virheellinen syöte! Yritä uudestaan ja käytä kokonaislukuja!")
    quit()

print("Syötä Näiden, " + str(tNum) + " Tentin Lopulliset Tulokset: ")
for i in range(tNum):
    tot2 = tot + i + 1
    print("Tentti", tot2)
    tGrades.append(input())

for i in range(tNum):
    tot = tot + float(tGrades[i])
    alwdived = 1 / tNum
final = alwdived * tot

if final>=90 and final<=100:
    print("Kurssi Numero = 5, erinomainen")
elif final>=80 and final<89.99:
    print("Kurssi Numero = 4, kiitettävä")
elif final>=70 and final<79.99:
    print("Kurssi Numero = 3, hyvä")
elif final>=60 and final<69.99:
    print("Kurssi Numero = 2, tyydyttävä")
elif final>=50 and final<59.99:
    print("Kurssi Numero = 1, välttävä")
elif final>=0 and final<49.99:
    print("Kurssi Numero = 0, hylätty")
else:
    print("Virheellinen syöte!")
print(final)