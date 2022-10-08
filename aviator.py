"""
ALGORITHM
sprint 1
1. user makes deposit- done
2. user places bet- done
3. bet amount is deducted from the deposit made- done
3. program starts counting from 1.0 to any random figure within a given range- done
4. program ends  after random figure is reached automatically- done
5. user can choose to withdraw anytime as long as the game is in progress- done
6. if user chooses to withdraw before an event ends, figure reached is multiplied with his bet amount- done
7. the new bet amount is added to the old bet amount- done
8.

sprint 2
1. code refactoring- done
2.random speed(range from 0.1 - 0.4s where 0.1 occurs most)- done
3.reduce decimal place to 2- done
4.introduce auto cashout- done

sprint 3
1.code refactoring
2.setting limit to hit smaller values often
"""

import random
import sys
import time
import keyboard


def main():

    deposit = float(input("deposit-:"))
    while True:
        print("================================================================")
        print("Balance : GHc ", deposit)
        bet = float(input("bet-:"))
        autocashout = (input('do you want to set autocashout, yes or no? ')).lower()
        if autocashout == "yes":
            set_value = float(input('set value:'))

        seconds_array = [0.01, 0.01, 0.01, 0.03, 0.03, 0.04, 0.04, 1, 2]
        limits_array = [1.2, 1.3, 2.0, 3.0, 10.0, 100.0]
        # Alert and stop app for over betting
        if bet > deposit:
            print('insufficient amount')
            sys.exit(main())
        # Subtract bet from deposit
        deposit -= bet
        run = random.randint(0, len(limits_array)-1)
        limit = limits_array[run]
        start = 1.00
        has_pressed = False

        while start < limit:
            print('{:.2f}'.format(start))
            if autocashout == 'yes' and start == set_value:
                won_bonus = start * bet
                deposit += won_bonus
                print(f'''==========================================
                You have cashed out Ghc ',{won_bonus}
                ====================================================''')

            if keyboard.is_pressed("a") and not has_pressed and autocashout != 'yes':
                won_bonus = bet * start
                deposit += won_bonus
                print("========================================")
                print('You have cashed out Ghc ', won_bonus)
                print("========================================")
                has_pressed = True  # saving that user has pressed

            start += 0.01
            random_array_index = random.randint(0, len(seconds_array)-1)
            time.sleep(seconds_array[random_array_index])

        print(f"new deposit: GHc{deposit}")


main()









