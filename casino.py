import time
import random
import os

money = 10000
loan_taken = False
debt = 0
debug_mode = False

print("Welcome to the Totally Not Rigged Casino™ (TNRC™)! (Game by Luminosity)\nWe've recently had an expansion of our domain, so we offer new, revamped games.")

# =======================Functions=============================

# Coding Necessities
def betting(money):
    """Handles betting input."""
    while True:
        bet = input("How much would you like to bet? (Enter to cancel) ")
        if bet == "":
            print("Betting canceled.")
            return 0, money
        if bet.isdigit():
            bet = int(bet)
            if 0 < bet <= money:
                return bet, money - bet
            print(f"Invalid bet. Your balance: ${money}.")
        if bet == "all in":
            bet = int(money)
            if 0 < bet <= money:
                return bet, money - bet
        else:
            print("Enter a valid number.")

# Player Features
def take_a_loan(money):
    """We WANT you to not be able to pay it back."""
    global debt, loan_taken
    max_loan, interest = 1_000_000, 1.15

    while True:
        amount = input(f"Loan amount? (Max: ${max_loan}, Interest: {interest}x) (Enter to cancel) ")
        if amount == "":
            print("Loan canceled.")
            return money
        if amount.isdigit():
            amount = int(amount)
            if 0 < amount <= max_loan:
                loan_taken, debt = True, debt + amount * interest
                print(f"Loan approved! You received ${amount}. Payback: ${debt}.")
                return money + amount
            print(f"Max loan: ${max_loan}.")
        else:
            print("Enter a valid number.")

def sign_in(money):
    """Handles special accounts."""
    users = {"yzsgrandpa": 0, "gijoe": 10000, "iamsteve": 100000000, "iamsteveasachildiyearnedfortheslotmachines": float('inf')}
    
    while True:
        user = input("Username? (Enter to cancel) ")
        if user == "":
            print("Sign in canceled.")
            return money
        if user in users:
            print(f"Welcome {user}!")
            return users[user]
        print("Invalid username.")

def show_rankings():
    """Displays the top players."""
    print("\n=== TOP PLAYERS ===\n1. iamsteve - $32,500,000\n2. Luminosity - $15,000,000")
    print("3. skibi - $10,000,000\n4. LuckyCharm777 - $7,500,000\n5. HighRoller69 - $5,000,000\n")
    
def dev_log():
    print("v1.6: THE SLOTS UPDATE\n1. Slots have been revamped\n2. Coin flip has been added!\n3. Devlog has been added!")
    
def commands():
    """Displays available games and commands."""
    print("\n=== CASINO GAMES ===\n1. Slots\n2. Blackjack\n3. Russian Roulette")
    print("4. Poker (Coming Soon!)\n5. Coin Flip\n\nOther commands:\n'loan' - Take a loan")
    print("'rankings' - View top players\n'sign in' - Log into an account\n'quit' - Exit the casino\n'devlog' - Access the update log")

# Games

def slots(money):
    """For the next 4 minutes and 11 seconds..."""
    
    progressive_jackpot_pool = 50000
    print(f"\n💰 Your current balance: ${money}")

    symbols = ["🍒", "🍋", "🍊", "🍇", "🔔", "💎", "7️⃣", "🍀", "🪙"]

    # Jackpot odds
    small_jackpot_chance = 0.05  # 5% chance → 5x bet
    regular_jackpot_chance = 0.01  # 1% chance → 20x bet
    progressive_jackpot_chance = 0.001  # 0.1% chance → Wins the progressive pool

    while money > 0:
        bet, money = betting(money)
        if bet == 0:
            print("Exiting slots...\n")
            return money  # Return to main menu if canceled

        # Every spin contributes 1% of bet to the progressive jackpot
        progressive_jackpot_pool += bet * 0.01  

        print("Spinning...")
        time.sleep(1.5)
        spin = [random.choice(symbols) for _ in range(3)]
        print(f"[{spin[0]}] [{spin[1]}] [{spin[2]}]")

        # Jackpot Logic
        random_roll = random.random()

        if random_roll < progressive_jackpot_chance:
            winnings = progressive_jackpot_pool
            money += winnings
            print(f"🔥 PROGRESSIVE JACKPOT! You won ${winnings}!")
            progressive_jackpot_pool = 50000  # Reset jackpot after win
        
        elif random_roll < regular_jackpot_chance:
            winnings = bet * 20
            money += winnings
            print(f"💎 JACKPOT! You won ${winnings}!")

        elif random_roll < small_jackpot_chance:
            winnings = bet * 5
            money += winnings
            print(f"🎰 Small Jackpot! You won ${winnings}!")

        # Regular Win (All 3 symbols match)
        elif len(set(spin)) == 1:
            winnings = bet * 10
            if "💎" in spin:
                winnings *= 2  # Wild symbol doubles winnings
            money += winnings
            print(f"💰 JACKPOT MATCH! You won ${winnings}!")

        # Near-Win (2 matching symbols)
        elif spin[0] == spin[1] or spin[1] == spin[2] or spin[0] == spin[2]:
            winnings = bet * 2
            money += winnings
            print(f"Almost! You won ${winnings}.")

        # Bonus Round (~10%)
        elif random.random() < 0.1:
            print("🎲 BONUS ROUND ACTIVATED! Double or Nothing?")
            bonus_choice = input("Take the risk? (yes/no) ").lower()
            if bonus_choice == "yes":
                if random.random() < 0.5:
                    money += bet * 2
                    print(f"✅ WIN! You doubled your bet to ${bet * 2}!")
                else:
                    print("❌ LOSS! You lost your bet.")
            else:
                print("Skipping bonus round.")

        else:
            print(f"You lost ${bet}.")

        if money <= 0:
            print("You're out of money! Returning to the main menu...\n")
            return money

        time.sleep(1)
        print(f"💰 Your balance: ${money}.")
        play_again = input("Play again? (yes/no) ").lower()
        if play_again != "yes":
            break
    
    print(f"💰 Your new balance: ${money}\n")
    return money

def blackjack(money):
    """You are only 32 games of Blackjack away from Elon Musk."""

    while True:
        print(f"\n💰 Your balance: ${money}")

        # Place a bet
        bet, money = betting(money)
        if bet == 0:
            print("Exiting Blackjack...\n")
            return money  # Exit if they cancel the bet
        
        # Create & shuffle deck before each round
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        random.shuffle(deck)

        def deal():
            """Deals a hand with two cards."""
            return [deck.pop(), deck.pop()]

        def total(hand):
            """Calculates the total value of a hand, adjusting for Aces."""
            total_value = sum(hand)
            aces = hand.count(11)
            while total_value > 21 and aces:
                total_value -= 10  # Convert an Ace from 11 to 1
                aces -= 1
            return total_value

        # Initial hands
        dealer_hand = deal()
        player_hand = deal()

        # Adjust double Aces (player starts with two)
        if player_hand == [11, 11]:
            player_hand[1] = 1  # Change second Ace to 1

        print(f"\nDealer shows: [{dealer_hand[0]}, ?]")
        print(f"Your hand: {player_hand} (Total: {total(player_hand)})")

        # Player's turn
        while total(player_hand) < 21:
            move = input("Do you want to [H]it or [S]tand? ").lower()
            if move == "h":
                player_hand.append(deck.pop())
                print(f"Your hand: {player_hand} (Total: {total(player_hand)})")
            elif move == "s":
                break
            else:
                print("Invalid choice, enter H or S.")

        # Dealer's turn (hits until at least 17)
        while total(dealer_hand) < 17 or (total(dealer_hand) == 17 and 11 in dealer_hand):
            dealer_hand.append(deck.pop())

        print(f"\nDealer's hand: {dealer_hand} (Total: {total(dealer_hand)})")

        # Determine the winner
        player_total, dealer_total = total(player_hand), total(dealer_hand)

        if player_total > 21:
            print("You busted! Dealer wins.")
        elif dealer_total > 21 or player_total > dealer_total:
            print(f"You win ${bet * 2}!")
            money += bet * 2
        elif player_total < dealer_total:
            print("Dealer wins.")
        else:
            print("It's a tie! Your bet is returned.")
            money += bet  # Return the bet for a tie

        # Offer replay
        if money <= 0:
            print("You're out of money! Returning to the main menu...\n")
            return money
        
        time.sleep(1)
        if input("Play again? (yes/no) ").lower() != "yes":
            print("Exiting Blackjack...\n")
            return money

def russian_roulette(money):
    """Let's play a little game..."""
    
    while True:
        print(f"\n💰 Your current balance: ${money}")
        time.sleep(0.5)
        print("⚠️ WARNING! HIGH RISK GAME! IF YOU LOSE YOU LOSE EVERYTHING! ⚠️")
        time.sleep(0.5)
        print("Bet is automatically all in.")
        
        # Explicit prompt at the beginning
        start_game = input("Would you like to continue? (yes/no) ").strip().lower()
        if start_game != "yes":
            print("Exiting Russian Roulette...\n")
            return money  

        bet = money  # Automatically all in
        money -= bet  

        # Get the number of chambers
        while True:
            chambers_input = input("Enter the number of chambers (2-6, default = 6): ").strip()
            if chambers_input == "":
                chambers = 6  
                break
            elif chambers_input.isdigit():
                chambers = int(chambers_input)
                if 2 <= chambers <= 6:
                    break
                print("Invalid choice! Must be between 2 and 6.")
            else:
                print("Invalid input! Enter a number between 2 and 6.")

        # Set multipliers based on chamber count
        multipliers = {2: 5.0, 3: 4.0, 4: 3.0, 5: 2.0, 6: 1.5}
        multiplier = multipliers[chambers]

        while True:  # Allows continuous play
            fatal_bullet = random.randint(1, chambers)
            current_bet = bet  

            print(f"\n🔫 A revolver with {chambers} chambers is loaded... One bullet is inside. Good luck!\n")

            for shot in range(1, chambers + 1):
                user_input = input("Press Enter to pull the trigger, or type 'quit' to cash out: ").strip().lower()

                if user_input in ["quit", "exit"]:
                    print(f"\n💰 You walked away with ${current_bet}!\n")
                    money += current_bet  
                    return money  

                if shot == fatal_bullet:
                    print("\n💀 *BANG!* You lost everything!")
                    time.sleep(1)
                    quit()

                print("💨 *Click*... You live to see another day!\n")

                # Increase the bet by the multiplier for the next round
                current_bet = int(current_bet * multiplier)
                print(f"🔥 Your bet has increased to ${current_bet}!")

            else:
                print(f"🎉 You survived! You won ${current_bet}!\n")
                money += current_bet  

            print(f"💰 Your new balance: ${money}\n")

            if money <= 0:
                print("You're out of money! Returning to the main menu...\n")
                return money  

            if input("Play again? (yes/no) ").strip().lower() != "yes":
                print("Exiting Russian Roulette...\n")
                return money




def coin_flip(money):
    """For the love of god, stop trying to shoot with 1 charge."""
    print(f"\n💰 Your current balance: ${money}")

    bet, money = betting(money)
    if bet == 0:
        print("Exiting Coin Flip...\n")
        return money  # Return to main menu if the player cancels

    choice = input("Heads or tails? ").lower()
    result = random.choice(["heads", "tails"])
    
    print(f"The coin landed on {result}!")

    if choice == result:
        winnings = bet * 2  # Adjust as needed
        money += winnings
        print(f"You won! You gained ${winnings}.")
    else:
        print(f"You lost ${bet}.")
    
    return money

#========================Game Loop===============================
while True:
    if money <= 0:
        time.sleep(1)
        if loan_taken:
            print("No more loans available. Game over.")
            break
        if input("Take a loan? (yes/no) ").lower() == "yes":
            money = take_a_loan(money)
        else:
            print("Thanks for visiting TNRC™! You leave with $0.")
            break
        continue  # Restart loop after loan

    time.sleep(0.5)
    print(f"💰 Your balance: ${money}.")
    choice = input("What would you like to play? ").lower()
    

    games = {
    "slots": slots,
    "blackjack": blackjack,
    "rankings": show_rankings,
    "russian roulette": russian_roulette,
    "coin flip": coin_flip,
    "commands": commands,
    "info": commands,
    "help": commands,
    "devlog": dev_log,
    }

    
    if choice in games:
        if choice == "slots":
            money = games[choice](money)
        elif choice == "blackjack":
            money = games[choice](money)
        elif choice == "russian roulette":
            money = games[choice](money)
        elif choice == "coin flip":
            money = games[choice](money)
        else:
            games[choice]()
        
    
    elif choice == "sign in":
        money = sign_in(money)
    
    elif choice == "loan":
        money = take_a_loan(money)

    elif choice in ["quit", "exit"]:
        print(f"Thanks for playing! You leave with ${max(0, money - debt)}{' in debt' if money < debt else ''}.")
        break
    
    else:
        print("Invalid choice. Type 'help' for options.")
