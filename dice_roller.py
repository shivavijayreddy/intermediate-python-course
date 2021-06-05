import random

def main():
    #dice_rolls= 2
    dice_rolls=int(input('How many dice would you like to roll?'))
    dice_size=int(input('How many sides are the dice'))
    dice_sum= 0
    for i in range(0,dice_rolls):

            #print('You rolled a die')
            #roll = 5
            roll=random.randint(1,dice_size)
            #print(f'you rolled a {roll}')
            dice_sum+=roll
            if roll == 1:
                print(f'you have rolled a{roll}! Critical Fail')
            elif roll == dice_size:
                print(f'you have rolled a{roll}! Critical Success')
            else:
                print(f'you have rolled a{roll}')
    print(f'you have rolled a total of {dice_sum}')
if __name__== "__main__":
  main()
