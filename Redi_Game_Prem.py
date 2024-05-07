import random

# Define the class (Character) with properties for name, health, attack power and healing power.
class Character:
    def __init__(self, name, health, attack_power, heal_power):
        self.name = name  # Name of the character
        self.health = health  # Health points of the character
        self.attack_power = attack_power  # Maximum damage the character can inflict
        self.heal_power = heal_power  # Maximum health the character can restore

    # Method for attacking another character
    def attack(self, other):
        damage = random.randint(0, self.attack_power)  # Determine random attack power within range
        other.health -= damage  # Subtract the damage from the other character's health
        print(f"{self.name} attacks {other.name} for {damage} damage.")  # Display attack info

    # Method for healing the character
    def heal(self):
        heal_amount = random.randint(0, self.heal_power)  # Determine random heal amount within range
        self.health += heal_amount  # Add the heal amount to the character's health
        print(f"{self.name} heals for {heal_amount} HP.")  # Display healing info

    # Check if the character is still alive
    def is_alive(self):
        return self.health > 0  # Return True if health is above 0

    # Display the current stats of the character
    def show_stats(self):
        print(f"{self.name} - Health: {self.health}")

# Main function to run the game
def game():
    player = Character("Captain America", 50, 10, 8)  # Create a player character
    enemy = Character("Thanos", 30, 15, 5)  # Create an enemy character

    # Game loop that continues until one of the characters dies
    while player.is_alive() and enemy.is_alive():
        player.show_stats()  # Show player stats
        enemy.show_stats()  # Show enemy stats
        
        # Prompt the user to choose an action
        choice = input("Do you want to (a)ttack or (h)eal? ")
        if choice.lower() == 'a':
            player.attack(enemy)  # Player attacks enemy
        elif choice.lower() == 'h':
            player.heal()  # Player heals themselves
        else:
            print("Invalid input. Please choose 'a' to attack or 'h' to heal.")

        # If the enemy is still alive after the player's turn, it attacks the player
        if enemy.is_alive():
            enemy.attack(player)

        print("")

    # Check who won the game
    if player.is_alive():
        print("You defeated the Goblin!")  # Player wins
    else:
        print("You have been defeated by the Goblin!")  # Enemy wins

game()

