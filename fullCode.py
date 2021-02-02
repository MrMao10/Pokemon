import time
import numpy as np
import sys

print('Welcome to Pokemon!')

#delay printing

def delay_print(s):
  #print one chracter at a time
  #https://stackoverflow.come/questions/9246076/how-to-print-one-character-at-a-time-on-one-line
  for c in s :
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.05)

#create the class
class Pokemon:
   def _init_(self, name, types, moves, EVs, health='===================='):
     # save variables as attributes
     self.name = name
     self.types = types
     self.moves = moves
     self.attack = EVs ('ATTACK')
     self.defence = EVs ('DEFENCE')
     self.health = EVs ('HEALTH')
     self.bars = 20 # amount of bars


    def fight(self, Pokemon2):
      # allow two pokemon to fight each other

      #print fight information
      print("-----POKEMON BATTLE-----")
      print(f"\n{self.name}")
      print("TYPE/", self.types)
      print("ATTACK/", self.attack)
      print("DEFENCE/", self.defence)
      print("LVL/", 3* (1+np.mean([self.attack, self.defence])))
      print("\nVS")
      print(f"\n{Pokemon2.name}")
      print("TYPE/", Pokemon2.types)
      print("ATTACK/", Pokemon2.attack)
      print("DEFENCE/", Pokemon2.defence)
      print("LVL/", 3* (1+np.mean([Pokemon2.attack, Pokemon2.defence])))
      print("\nVS")

      time.sleep(2)

      # consider type advantages
      version = (Fire, Water, Grass)
      for i,k enumerate(version):
        if self.types == k:
          #both are same type
          if Pokemon2.types == k:
            string_1_attack = '\nIts not very effective...'
            string_2_attack = '\nIts not very effective...'
          

          #Pokemon2 is STRONG
          if Pokemon2.types == version[(i+1)%3]:
            Pokemon2.attack *= 2
            Pokemon2.defence *= 2
            self.attack /= 2
            self.defence /= 2
            string_1_attack = 'Its not very effective...'
            string_2_attack = 'Its super effective!!!'

          #Pokemon2 is WEAK
          if Pokemon2.types == version[(i+2)%3]:
            self.attack *= 2
            self.defence *= 2
            Pokemon2.attack /= 2
            Pokemon2.defence /= 2
            string_1_attack = 'Its super effective!!!'
            string_2_attack = 'Its not very effective...'


     # now for the actual fighting
     #continue while pokemon still have health
     while (self.bars > 0) and (Pokemon2.bars > 0):
       # print the health of each pokemon
       print(f"{self.name}\t\tHLTH\t{self.health}")
       print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

       print(f"Go {self.name}!")
       for i, x in enumerate(self.moves):
         print(f"{i+1}.", x)
         index = int(input("Pick a move: "))
         delay_print(f"{self.name} used {self.moves[index-1]}!")
         time.sleep(1)
         delay_print(string_1_attack)

         # determine damage
         Pokemon2.bars -= self.attack
         Pokemon2.health = ""

         #add back bars plus defence boost
         for j on range(int(Pokemon2.bars.1*Pokemon2.defence)):
           Pokemon2.health += "="

         time.sleep(1)
          print(f"{self.name}\t\tHLTH\t{self.health}")
          print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
          time.sleep(.5)

          #check to see if pokemon has fainted
          if Pokemon2.bars <= 0:
            delay_print("\n..." + Pokemon2.name + 'fainted.')
            break

            #Pokemon2s turn

            print(f"Go {Pokemon2.name}!")
       for i, x in enumerate(Pokemon2.moves):
         print(f"{i+1}.", x)
         index = int(input("Pick a move: "))
         delay_print(f"{Pokemon2.name} used {Pokemon.moves[index-1]}!")
         time.sleep(1)
         delay_print(string_2_attack)

         # determine damage
         self.bars -= Pokemon2.attack
         self.health = ""

         #add back bars plus defence boost
         for j on range(int(Pokemon2.bars.1*Pokemon2.defence)):
           Pokemon2.health += "="

         time.sleep(1)
          print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}")
          print(f"{self.name}\t\tHLTH\t{self.health}\n")
          time.sleep(.5)

          #check to see if pokemon has fainted
          if self.bars <= 0:
            delay_print("\n..." + self.name + 'fainted.')
            break

            money = np.random.choice(5000)
            delay_print(f"\nOpponent paid you £{money}.")



















if __name__=='_main_':
  #create pokemon
  Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENCE':8})
  Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'], {'ATTACK':10, 'DEFENCE':10})
  Venusaur = Pokemon('Venasaur', 'Grass', ['Vine Wip', 'Lazer Leaf', 'Earthquake', 'Frenzy Plant'], {'ATTACK':8 'DEFENCE':12})

  Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'], {'ATTACK':4 'DEFENCE':2})
  Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbut', 'Surf'], {'ATTACK':3 'DEFENCE':3})
  Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leach Seed'], {'ATTACK':2 'DEFENCE':4})

  Charmelon = Pokemon('Charmelon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'], {'ATTACK':6 'DEFENCE':5})
  Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbut', 'Surf'], {'ATTACK':5 'DEFENCE':5})
  Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leach Seed'], {'ATTACK':4 'DEFENCE':6})


  Charizard.fight(Blastoise) #get them to fight
