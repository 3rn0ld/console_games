import os

table = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player_index = 0

def choose_a_field():
    decision = int(input("In which field do you want to place? "))
    
    if decision == 00000:
        quit()
        
    if decision > 9:
        print("This field doesn't exist. Please choose a different field.")
        choose_a_field()
    
    if table[decision-1] == "o" or table[decision-1] == "x":
        print("This field is already taken. Please choose a different field.")
        choose_a_field()
    else:
        table[decision-1] = player_icon
        
def check_winner(value):
    if value == "o":
        print("The winner is player 1.")
    else:
        print("The winner is player 2.") 
    quit()     
    
                        
def check_win():
    if table[0] == table[1] and table[1] == table[2]:
        check_winner(table[0])
    if table[3] == table[4] and table[4] == table[5]:
        check_winner(table[3])
    if table[6] == table[7] and table[7] == table[8]:
        check_winner(table[6])
    
    if table[0] == table[3] and table[3] == table[6]:
        check_winner(table[0])
    if table[1] == table[4] and table [4] == table[7]:
        check_winner(table[1])
    if table[2] == table[5] and table [5] == table[8]:
        check_winner(table[2])
    
    if table[0] == table[4] and table[4] == table[8]:
        check_winner(table[0])
    if table[2] == table[4] and table[4] == table[6]:
        check_winner(table[2])
    

while True:
    os.system("clear")
    check_win()
    print(f"""
         {table[0]} | {table[1]} | {table[2]} 
         {table[3]} | {table[4]} | {table[5]} 
         {table[6]} | {table[7]} | {table[8]}
          """)
    
    player_index += 1
    
    if player_index % 2 == 0:
        print("Player 2 (x) it's your turn.")
        player_icon = "x"   
        
    else:
        print("Player 1 (o) it's your turn.")
        player_icon = "o"
    
    choose_a_field()