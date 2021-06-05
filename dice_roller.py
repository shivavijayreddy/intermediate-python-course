import random

def main():
    #dice_rolls= 2
    player1_name=input('Enter player1 Name: ')
    player2_name=input('Enter player2 Name: ')

    dice_rolls=int(input('How many dice would you like to roll?: '))
    dice_size=int(input('How many sides are the dice: '))

    while True:
        player_chance=input('Enter player name to roll: ')
        if player_chance == player1_name:
            player1_rolls=[]
            player1_rolls=dice_rolling(player1_name, dice_rolls, dice_size)
        elif player_chance == player2_name:
            player2_rolls=[]
            player2_rolls=dice_rolling(player2_name, dice_rolls, dice_size)
        else:
            print(f'No player name {player_chance} found')

def dice_rolling(name, dice_rolls, dice_size):
        dice_sum= 0
        for i in range(0,dice_rolls):

            #print('You rolled a die')
            #roll = 5
            roll=random.randint(1,dice_size)
            #print(f'you rolled a {roll}')
            dice_sum+=roll
            if roll == 1:
                print(f'{name} have rolled a{roll}! Critical Fail')
            elif roll == dice_size:
                print(f'{name} have rolled a{roll}! Critical Success')
            else:
                print(f'{name} have rolled a{roll}')
        print(f'{name} have rolled a total of {dice_sum}')
        return dice_sum



if __name__== "__main__":
  main()
