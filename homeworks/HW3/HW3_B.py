#Amina Muumin, muumi002, lab 008, HW3B
def play_game(player1choice, player2choice):
    if player1choice == "R" and player2choice == "SC":
        return 1
    if player1choice == "R" and player2choice == "L":
        return 1
    if player1choice == "SC" and player2choice == "R":
        return 1
    if player1choice == "SC" and player2choice == "L":
        return 1
    if player1choice == "P" and player2choice == "R":
        return 1
    if player1choice == "P" and player2choice == "SP":
        return 1
    if player1choice == "SP" and player2choice == "R":
        return 1
    if player1choice == "SP" and player2choice == "SC":
        return 1
    if player1choice == "L" and player2choice == "P":
        return 1
    if player1choice == "L" and player2choice == "SP":
        return 1
    elif player1choice == player2choice:
        return "T"
    else:
        return 2

    
    
    
def play_round(p1,p2):
    player1win = 0
    player2win = 0
    gamecount= 0
    while player1win < 2 and player2win < 2 and gamecount < 3:
        p1choice = p1[gamecount+1]
        p2choice = p2[gamecount+1]
        x = play_game(p1choice, p2choice)
        if x ==1:
            player1win +=1
            #print("p1 wins")
        elif x ==2:
            player2win +=1
            #print("p2 wins")
        #elif x == "T":
            #print("game tied")
        gamecount = gamecount+1
        
    
    if player1win>player2win:
        return (1)
    elif player2win>player1win:
        return (2)
    elif player1win== player2win:
        return ("T")
    
def main():
    player1 = [1, '', '', '']
    player2 = [2, '', '', '']
    player1[1] = input("Player 1 choose from R, P, SC, SP, L: ")
    player2[1] = input("Player 2 choose from R, P, SC, SP, L: ")
    player1[2] = input("Player 1 choose from R, P, SC, SP, L: ")
    player2[2] = input("Player 2 choose from R, P, SC, SP, L: ")
    player1[3] = input("Player 1 choose from R, P, SC, SP, L: ")
    player2[3] = input("Player 2 choose from R, P, SC, SP, L: ")

   # print("player1: ", player1, " player2: ", player2)
    
    x = play_round(player1, player2)
    if x == 1:
        print ("Player 1 Wins")
    if x == 2:
        print("Player 2 Wins")
    if x == "T":
        print("Tie")
    
if __name__ == "__main__":
    main()
