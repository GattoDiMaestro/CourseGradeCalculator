import colorama
from colorama import Fore, Back, Style
colorama.init()

class mcolors:
    # bright green
    EXCELLENT = "\033[42;1m"
    
    LAUDABLE = "\033[94m"
    GOOD = "\033[96m"
    SATISFYING = "\033[37m"
    PASSABLE = "\033[36m"
    FAIL = "\033[31m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    FCOLOR = "\033[0m"
    WARNING = "\033[31m"
    BWHITE = "\u001b[37;1m"

# tentti numerot
tGrades = []
tot = 0
print("Syötä Tenttien Määrä: ")
# kuinka monta tenttiä
try:
    tNum = int(input())
except:
    print(mcolors.WARNING + "Virheellinen syöte! Yritä uudestaan ja käytä kokonaislukuja!")
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
    print("Kurssi Numero = 5, " + mcolors.EXCELLENT + mcolors.BOLD + " erinomainen " + mcolors.FCOLOR)
elif final>=80 and final<89.99:
    print("Kurssi Numero = 4, " + mcolors.LAUDABLE + mcolors.BOLD + " kiitettävä " + mcolors.FCOLOR)
elif final>=70 and final<79.99:
    print("Kurssi Numero = 3, " + mcolors.GOOD + mcolors.BOLD + " hyvä " + mcolors.FCOLOR)
elif final>=60 and final<69.99:
    print("Kurssi Numero = 2, " + mcolors.SATISFYING + mcolors.BOLD + " tyydyttävä " + mcolors.FCOLOR)
elif final>=50 and final<59.99:
    print("Kurssi Numero = 1, " + mcolors.PASSABLE + mcolors.BOLD + " välttävä " + mcolors.FCOLOR)
elif final>=0 and final<49.99:
    print("Kurssi Numero = 0, " + mcolors.FAIL + mcolors.BOLD + " hylätty " + mcolors.FCOLOR)
else:
    print(mcolors.WARNING + " Virheellinen syöte! " + mcolors.FCOLOR)
print(final)