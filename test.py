import time
from random import randint

goals = 150
assists = 120
saves = 200
shots = 210
mvp = 40
wins = 50

while True:
    goals += randint(0, 7)
    assists += randint(0, 12)
    saves += randint(0, 9)
    shots += randint(0,15)
    mvp += randint(0,4)
    wins += randint(0,5)
    print(goals, assists, saves, shots, mvp, wins)
    time.sleep(5)