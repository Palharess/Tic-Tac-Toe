import random
import os



new_list = [" " for item in range(0,9)]
final_list = [[new_list[0],new_list[1],new_list[2]],[new_list[3],new_list[4],new_list[5]],[new_list[6],new_list[7],new_list[8]]]
player = ""
computer = ""
is_game_on = True
n = 0
rounds = 0
winner = ""

def turn(n, gamemode):
    gamemode = gamemode.upper()
    if n % 2 == 0:
        if gamemode == "PC":
            pass
        else:
            print(f"\nIt's {computer} turn\n")
            place = input("Where do you want to put it? ('Row Column') ")
    else:
        print(f"\nIt's {player} turn\n")
        place = input("Where do you want to put it? ('Row Column') ")
    try:
        place = place.split(" ")
        for item in place:
            index = place.index(item)
            place[index] = int(item)
    except:
        pass
    # pc it's even
    if n % 2 == 0:
        if gamemode.upper() == "TWO":
            if final_list[place[0]][place[1]] == " ":
                final_list[place[0]][place[1]] = computer
            else:
                os.system('cls')
                print("\nPlease choose a valid spot\n")
                return "Failed"
        elif gamemode.upper() == "PC":
            while True:
                n1 = random.randint(0,2)
                n2 = random.randint(0,2)
                if final_list[n1][n2] == " ":
                    final_list[n1][n2] = computer
                    break

    else:
        if final_list[place[0]][place[1]] == " ":
            final_list[place[0]][place[1]] = player
        else:
            os.system('cls')
            print("\nPlease choose a valid spot\n")
            return "Failed"

def check_winner():
    for n in range(0,3):
        pointsh = 0
        pointsv = 0
        pointsd = 0
        for j in range(0,3):
            if final_list[n][j] == final_list[n][0] and final_list[n][j] != " " and final_list[n][0] != " ":
                pointsh += 1
                winner = final_list[n][j]
            if final_list[j][n] == final_list[0][n] and final_list[j][n] != " " and final_list[0][n] != " ":
                pointsv += 1
                winner = final_list[j][n]
            if final_list[0][0] == final_list[1][1] and final_list[0][0] == final_list[2][2] and final_list[0][0] != " ":
                pointsd += 3
                winner = final_list[0][0]
            if final_list[0][2] == final_list[1][1] and final_list[0][2] == final_list[2][0] and final_list[0][2] != " ":
                pointsd += 3
                winner = final_list[0][2]
            if pointsh == 3 or pointsv == 3 or pointsd == 3:
                os.system('cls')
                print("Game Over\n")
                print(f"  {final_list[0][0]}", "|", final_list[0][1], "|", final_list[0][2], "\n", "-----------\n",f" {final_list[1][0]}", "|", final_list[1][1], "|", final_list[1][2], "\n", "-----------\n", f" {final_list[2][0]}", "|", final_list[2][1], "|", final_list[2][2], "\n")
                print(f"The winner is {winner}!")
                return True
            

while is_game_on == True:
    if rounds > 0:
        answer = input("Do you want to play again? (Yes/No) ")
        if answer.upper() == "YES":
            final_list = [[new_list[0],new_list[1],new_list[2]],[new_list[3],new_list[4],new_list[5]],[new_list[6],new_list[7],new_list[8]]]
        else:
            break
    gamemode = input("Two players or against computer? (Two/PC) ")
    choice = input("X or O? ")
    if choice.upper() == "X":
        player = "X"
        computer = "O"

    else:
        player = "O"
        computer = "X"
    first_time = 0
    while True:
        print(f"  {final_list[0][0]}", "|", final_list[0][1], "|", final_list[0][2], "\n", "-----------\n",f" {final_list[1][0]}", "|", final_list[1][1], "|", final_list[1][2], "\n", "-----------\n", f" {final_list[2][0]}", "|", final_list[2][1], "|", final_list[2][2], "\n")

        
        if turn(n, gamemode) != "Failed":
            n += 1
        first_time += 1
        if first_time >= 5:
            if check_winner() == True:
                rounds += 1
                break
        os.system('cls')
        if gamemode == "TWO":
            if n % 2 == 0:
                print(f"\nIt's {computer} turn\n")
            else:
                print(f"\nIt's {computer} turn\n")


