#!/usr/bin/env python
# coding: utf-8

# # Exercise 1

# #### Creature class

# In[1]:


import random as rand
import sys

class Creature():
    def __init__(self,name,abilities,maxHP=10):
        self.maxHP = maxHP
        self.name = name
        self.hp = maxHP
        self.abilities = {'Attack':abilities[0],'Defense':abilities[1],'Speed':abilities[2]}
    def check_life(self):
        if self.hp < 0:
            print(self.name,'died.')
            return 0
        else:
            return self.hp
    def roll(self,x,y):
        num = rand.randint(x,y)
        return num
    def attack(self,target):
        print(self.name,'attacks',str(target.name)+'.')
        a = self.roll(1,20)
        if a < target.abilities['Defense']+target.abilities['Speed']:
            print('Attack missed.')
        else:
            damage = (self.abilities['Attack'] + self.roll(1,4))
            target.hp -= damage
            print('Attack hits for',damage,'damage!')
    def turn(self,round_num,target):
        self.attack(target)
        if target.hp <= 0:
            print(target.name,'died.')
            return True
        else:
            return False


# Script to create creatures Gollum and Bilbo and show them fighting over a maximum of 20 rounds.

# In[2]:


gollum = Creature('Gollum',(1,2,4),4)
bilbo = Creature('Bilbo', (1,4,3))
roundnumber = 1
while roundnumber < 21:
    print('Round '+str(roundnumber)+':')
    gollum.turn(roundnumber,bilbo)
    if bilbo.hp <= 0:
        break
    bilbo.turn(roundnumber,gollum)
    if gollum.hp <= 0:
        break
    roundnumber+=1


# #### Fighter class

# In[63]:


class Fighter(Creature):
    def __init__(self,name):
        Creature.__init__(self,name,abilities=(5,10,3),maxHP=50)
        self.flag = 0
        
    def shield_up(self):
        if self.flag == 0:
            self.abilities['Attack'] -= 5
            self.abilities['Defense'] += 5
            self.flag = 1
            print(self.name,'takes a defensive stance.')
            
    def shield_down(self):
        if self.flag == 1:
            self.abilities['Attack'] += 5
            self.abilities['Defense'] -= 5
            self.flag = 0
            print(str(self.name)+'\'s stance returns to normal.')
        
    def turn(self,round_num,target):
        if round_num % 4 == 1:
            Creature.turn(self,round_num,target)
            if target.hp > 0:
                self.shield_up()
        elif round_num % 4 == 0:
            self.shield_down()
            Creature.turn(self,round_num,target)
        else:
            Creature.turn(self,round_num,target)


# Script creating fighter Aragorn and creature Gollum and showing them fighting over a maximum of 20 rounds.

# In[4]:


fighter = Fighter('Aragorn')
gollum = Creature('Goblin',(1,2,4))
roundnumber = 1
while roundnumber < 21:
    print('Round '+str(roundnumber)+':')
    fighter.turn(roundnumber,gollum)
    if gollum.hp <= 0:
        break
    gollum.turn(roundnumber,fighter)
    if fighter.hp <= 0:
        break
    roundnumber+=1


# #### Archer class

# In[5]:


class Archer(Creature):
    def __init__(self,name,flag=0):
        Creature.__init__(self,name,abilities=(7,8,8),maxHP=30)
        self.flag=flag
        
    def sneak_attack(self,target):
        roll1 = rand.randint(1,20)
        roll2 = rand.randint(1,20)
        maxroll = max(roll1,roll2)
        if self.abilities['Speed'] > target.abilities['Speed']:
            maxroll += (self.abilities['Speed'] - target.abilities['Speed'])
        if self.flag == 0:
            self.abilities['Attack'] += 3
            print(self.name+'\'s attack increased.')
            self.abilities['Defense'] -= 3
            print(self.name+'\'s defense decreased.')
            self.flag = 1
        print(self.name,'sneak attacks',str(target.name)+'.')
        damage = self.roll(1,8) + self.abilities['Attack']
        target.hp -= damage
        print('Sneak attack hits for',damage,'damage.')
        
    def attack(self, target):
        if self.flag == 1:
            self.abilities['Attack'] -= 3
            print(self.name+'\'s attack decreased.')
            self.abilities['Defense'] += 3
            print(self.name+'\'s defense increased.')
            self.flag = 0
        Creature.attack(self,target)
        
    def turn(self,round_num, target):
        if round_num % 4 == 1:
            Creature.turn(self,round_num,target)
        else:
            self.sneak_attack(target)
            if target.hp <= 0:
                print(target.name,'died.')


# Script creating fighter Aragorn and archer Legolas and showing them fighting over a maximum of 20 rounds.

# In[6]:


fighter = Fighter('Aragorn')
archer = Archer('Legolas')
roundnumber = 1
while roundnumber < 21:
    print('Round '+str(roundnumber)+':')
    archer.turn(roundnumber,fighter)
    if fighter.hp <= 0:
        break
    fighter.turn(roundnumber,archer)
    if archer.hp <= 0:
        break
    roundnumber+=1
if roundnumber == 21:
    print('Fight over, nobody was killed.')


# # Exercise 2

# #### Goblin and Orc classes

# In[7]:


class Goblin(Creature):
    def __init__(self,name):
        Creature.__init__(self,name,abilities=(4,6,6),maxHP=15)
        self.flag = 0
        
class Orc(Creature):
    def __init__(self,name):
        Creature.__init__(self,name,abilities=(10,6,2),maxHP=50)
        self.flag = 0
        
    def heavy_attack(self,target):
        if self.flag == 0:
            self.abilities['Attack'] += 5
            self.abilities['Defense'] -= 3
            print(self.name,'is in rage.')
            self.flag = 1
        Creature.attack(self,target)
    
    def attack(self,target):
        if self.flag == 1:
            self.abilities['Attack'] -= 5
            self.abilities['Defense'] += 3
            print(self.name,'cooled down.')
            self.flag = 0
        Creature.attack(self,target)
            
    def turn(self,round_num,target):
        if round_num % 4 != 0:
            Creature.turn(self,round_num,target)
        else:
            self.heavy_attack(target)
            if target.hp <= 0:
                print(target.name,'died.')


# Script creating Goblin and Orc and showing them fighting over a maximum of 20 rounds.

# In[8]:


goblin = Goblin('Goblin')
orc = Orc('Orc')
roundnumber = 1
while roundnumber < 21:
    print('Round '+str(roundnumber)+':')
    goblin.turn(roundnumber,orc)
    if orc.hp <= 0:
        break
    orc.turn(roundnumber,goblin)
    if goblin.hp <= 0:
        break
    roundnumber+=1
if roundnumber == 21:
    print('Fight over, nobody was killed.')


# #### OrcGeneral and GoblinKing classes

# In[9]:


class OrcGeneral(Orc,Fighter):
    def __init__(self,name):
        Creature.__init__(self,name,abilities=(10,6,2),maxHP=100)
        self.flag = 0

    def turn(self,round_num,target):
        if round_num % 4 == 1:
            Creature.turn(self,round_num,target)
            if target.hp > 0:
                self.shield_up()
        elif round_num % 4 == 2:
            Creature.attack(self,target)
            if target.hp <= 0:
                print(target.name,'died.')
        elif round_num % 4 == 3:
            self.shield_down()
            Creature.turn(self,round_num,target)
        else:
            self.heavy_attack(target)
            if target.hp <= 0:
                print(target.name,'died.')

class GoblinKing(Goblin,Archer):
    def __init__(self,name):
        Creature.__init__(self,name,abilities=(4,6,6),maxHP=50)
        self.flag = 0
        
    def turn(self,round_num,target):
        Archer.turn(self,round_num,target)


# Script creating OrcGeneral Azog and GoblinKing Great Goblin and showing them fighting over a maximum of 20 rounds.

# In[10]:


azog = OrcGeneral('Azog')
goblinking = GoblinKing('Great Goblin')
roundnumber = 1
while roundnumber < 21:
    print('Round '+str(roundnumber)+':')
    azog.turn(roundnumber,goblinking)
    if goblinking.hp <= 0:
        break
    goblinking.turn(roundnumber,azog)
    if azog.hp <= 0:
        break
    roundnumber+=1
if roundnumber == 21:
    print('Fight over, nobody was killed.')


# # Exercise 3

# #### Wizard class

# In[50]:


class Wizard(Creature):
    def __init__(self,name,maxHP=20,mana=100):
        Creature.__init__(self,name,abilities=(3,5,5),maxHP=20)
        self.abilities = self.abilities|{'Arcana':10}
        self.mana = mana
        self.maxHP = maxHP
        self.hp = maxHP
        
    def attack(self,target):
        if self.mana > 80:
            self.mana = 100
        else:
            self.mana += 20
        Creature.attack(self,target)
        
    def recharge(self):
        initial = self.mana
        if self.mana == 100:
            print('Mana is already full.')
        elif self.mana > 70:
            print('Gandalf channels magical energy...')
            self.mana = 100
            change = self.mana-initial
            print('Mana: +'+str(change))
        else:
            print('Gandalf channels magical energy...')
            self.mana += 30
            print('Mana: +30')
            
    def firebolt(self,target):
        a = self.roll(1,20)
        print(self.name,'fires a fire bolt at',str(target.name)+'.')
        if a < target.abilities['Defense']+target.abilities['Speed']:
            print('Fire bolt missed.')

        else:
            damage = (self.abilities['Attack'] + self.roll(1,4) + (self.abilities['Arcana']//2))
            target.hp -= damage
            print('Fire bolt hits for',damage,'fire damage!')
            if self.mana == 100:
                print('Mana is full.')
            elif self.mana > 90:
                self.mana = 100
            else:
                self.mana += 10
        
    def heal(self,target):
        if self.mana >= 20:
            initialhp = target.hp
            a = self.roll(0,8) + (self.abilities['Arcana']//2)
            target.hp += a
            if target.hp > target.maxHP:
                target.hp = target.maxHP
            self.mana -= 20
            heal = target.hp - initialhp
            if heal == 0:
                print(target.name,'already has full HP.')
            else:
                print(self.name,'heals',target.name,'for',heal,'HP.')
        else:
            print(self.name,'does not have enough mana to heal',str(target.name)+'.')
            
    def mass_heal(self,allies):
        if self.mana >= 30:
            print('Mana: -30')
            for ally in allies:
                initialhp = ally.hp
                a = self.roll(0,10) + (self.abilities['Arcana']//2)
                ally.hp  += a
                if ally.hp > ally.maxHP:
                    ally.hp = ally.maxHP
                heal = ally.hp - initialhp
                if heal == 0:
                    print(ally.name,'already has full HP.')
                else:
                    print(self.name,'heals',ally.name,'for',heal,'HP.')
            self.mana -= 30
        else:
            print(self.name,'does not have enough mana to heal allies.')
            
    def fire_storm(self,enemies):
        if self.mana >= 50:
            print('Mana: -50')
            self.mana = self.mana - 50
            for enemy in enemies:
                a = self.roll(1,20) + self.abilities['Speed']
                damage = self.roll(5,20) + self.abilities['Arcana']
                if a >= self.abilities['Arcana']:
                    enemy.hp -= damage//2
                    print('Fire Storm deals',damage//2,'damage to',str(enemy.name)+'!')
                    if enemy.hp <= 0:
                        print(enemy.name,'died.')
                else:
                    enemy.hp -= damage
                    print('Fire Storm deals',damage,'damage to',str(enemy.name)+'!')
        else:
            print(self.name,'does not have enough mana to use Fire Storm')


# Script showing all Wizard methods.

# In[56]:


wizard = Wizard('Gandalf')
fighter = Fighter('Aragorn')
archer = Archer('Legolas')
allies = (wizard,fighter,archer)
orcgeneral = OrcGeneral('Azog')
orc = Orc('Bolg')
enemies = (orcgeneral,orc)

print('-------------')
print('Using attack:')
print('-------------')
wizard.attack(orc)
print('---------------')
print('Using recharge:')
print('---------------')
wizard.recharge()
print('----------------')
print('Using fire bolt:')
print('----------------')
wizard.firebolt(orcgeneral)
print('-----------')
print('Using heal:')
print('-----------')
wizard.heal(fighter)
print('----------------')
print('Using mass heal:')
print('----------------')
wizard.mass_heal(allies)
print('-----------------')
print('Using fire storm:')
print('-----------------')
wizard.fire_storm(enemies)


# # Exercise 4

# #### Battle class

# In[96]:


class Battle():
    def __init__(self):
        global heroes, enemies, allies, goblinking, orcgeneral, orc, goblin, wizard, fighter, fighter2, fighter3, archer
        heroes, enemies, allies = [], [], []
        orcgeneral, orc, orc2 = OrcGeneral('Azog'), Orc('Bolg'), Orc('Shagrat')
        goblinking, goblin = GoblinKing('Great Goblin'), Goblin('Snaga')
        wizard, archer = Wizard('Gandalf',40), Archer('Legolas') # Gave Gandalf 40 HP because he kept dying with 20
        fighter, fighter2 = Fighter('Aragorn'),Fighter('Boromir')
        enemies.extend([goblinking,orcgeneral,orc,orc2,goblin])
        allies.extend([fighter,fighter2,archer])
        heroes.extend([fighter,fighter2,archer,wizard])
        
    def auto_select(self,target_list):
        alive = list(filter(lambda x: x.hp > 0, target_list))
        rand.shuffle(alive)
        if len(alive) > 0:
            return alive[0]
        else:
            return None
            
    def select_target(self,target_list):
        alive = list(filter(lambda x: x.hp > 0, target_list))
        numlist = []
        num = 1
        print('Select target:')
        for i in alive:
            print(str(num)+':',str(i.name)+', HP: '+str(i.hp)+'/'+str(i.maxHP))
            numlist.append(num)
            num+=1
        x = 0
        while x not in numlist:
            x = int(input('Enter choice: '))
            if x not in numlist:
                print(x,'is not a valid choice. Enter choice: ')
        print(alive[x-1].name,'chosen.')
        return alive[x-1]
    
    def start(self):
        print('THE BATTLE BEGINS')
        roundnum = 1
        players = []
        for i in enemies:
            players.append(i)
        for j in heroes:
            players.append(j)
        living_enemies = list(filter(lambda x: x.hp > 0, enemies))
        living_allies = list(filter(lambda x: x.hp > 0, allies))
        living_heroes = list(filter(lambda x: x.hp > 0, heroes))
        while len(living_enemies) > 0 and wizard.hp > 0 and len(living_allies) > 0:
            print('========================================================')
            print('Round',str(roundnum)+'.')
            print('========================================================')
            alive = list(filter(lambda x: x.hp > 0, players))
            sequence = sorted(alive, key=lambda x: x.abilities['Speed'], reverse=True)
            for i in sequence:
                living_allies = list(filter(lambda x: x.hp > 0, allies))
                living_enemies = list(filter(lambda x: x.hp > 0, enemies))
                living_heroes = list(filter(lambda x: x.hp > 0, heroes))
                if i in living_allies:
                    if len(living_enemies) != 0:
                        g = self.auto_select(living_enemies)
                        i.turn(roundnum,g)
                elif i.name == 'Gandalf' and i.hp > 0:
                    if len(living_enemies) != 0:
                        g = self.auto_select(living_enemies)
                        self.player_turn(i)
                elif i in living_enemies:
                    if len(living_heroes) != 0:
                        g = self.auto_select(living_heroes)
                        i.turn(roundnum,g)
                        living_allies = list(filter(lambda x: x.hp > 0, allies))
                        if wizard.hp <= 0 or len(living_heroes) == 0 :
                            break
            living_enemies = list(filter(lambda x: x.hp > 0, enemies))
            living_allies = list(filter(lambda x: x.hp > 0, allies))
            living_heroes = list(filter(lambda x: x.hp > 0, heroes))
            print('========================================================')
            print('End of round',str(roundnum)+'.')
            roundnum += 1
        print('========================================================')
        if len(living_enemies) == 0:
            print('Battle over! The good guys won!')
        elif wizard.hp <= 0:
            print('Battle over! Player died!')
        elif len(living_allies) == 0:
            print('Battle over! All your allies are dead!')
        print('========================================================')
        
    def player_turn(self,player):
        print('========================================================')
        print('Player:',player.name,'HP:',str(player.hp)+'/'+str(player.maxHP), 'Mana:'+str(player.mana)+'/100')
        print()
        print('Allies:')
        living_allies = list(filter(lambda x: x.hp > 0, allies))
        living_heroes = list(filter(lambda x: x.hp > 0, heroes))
        for i in living_allies:
            print('',i.name,'HP:'+str(i.hp)+'/'+str(i.maxHP))
        print()
        print('Enemies:')
        living_enemies = list(filter(lambda x: x.hp > 0, enemies))
        for i in living_enemies:
                print('',i.name,'HP:'+str(i.hp)+'/'+str(i.maxHP))
        print('========================================================')
        print('Actions. F: Attack      R: Recharge Mana')
        print('Spells. \n 1: Heal (Costs 20 mana) \n 2: Firebolt \n 3: Mass Heal (Costs 30 mana) \n 4: Fire Storm (Costs 50 mana)')
        print('To Quit game type: Quit')
        print('========================================================')
        input1 = 'p'
        options = ['F','f','R','r','1','2','3','4','Quit','quit']
        while input1 not in options: 
            input1 = str(input('Enter action: '))
        
        
        if input1 == 'F' or input1 == 'f':
            print('Select target:')
            living_enemies = list(filter(lambda x: x.hp > 0, enemies))
            living_heroes = list(filter(lambda x: x.hp > 0, heroes))
            num = 1
            mylist = []
            for i in living_enemies:
                print(str(num)+':',i.name,'HP:'+str(i.hp)+'/'+str(i.maxHP))
                mylist.append(i)
                num += 1
            input2 = int(input('Enter choice: '))
            enemy = mylist[input2-1]
            player.attack(enemy)
            if enemy.hp <= 0:
                print(enemy.name,'died.')
            
        elif input1 == '2':
            print('Select target:')
            living_enemies = list(filter(lambda x: x.hp > 0, enemies))
            num = 1
            mylist = []
            for i in living_enemies:
                print(str(num)+':',i.name,'HP:'+str(i.hp)+'/'+str(i.maxHP))
                mylist.append(i)
                num += 1
            input2 = int(input('Enter choice: '))
            enemy = mylist[input2-1]
            player.firebolt(enemy)
            if enemy.hp <=0:
                print(enemy.name,'died.')
                
        elif input1 == '1':
            print('Select target:')
            living_heroes = list(filter(lambda x: x.hp > 0, heroes))
            num = 1
            mylist = []
            for i in living_heroes:
                print(str(num)+':',i.name,'HP:'+str(i.hp)+'/'+str(i.maxHP))
                mylist.append(i)
                num += 1
            input2 = int(input('Enter choice: '))
            hero = mylist[input2-1]
            player.heal(hero)
            
        elif input1 == 'R' or input1 == 'r':
            player.recharge()
        elif input1 == '3':
            player.mass_heal(living_heroes)
        elif input1 == '4':
            player.fire_storm(living_enemies)
            
        elif input1 == 'Quit' or input1 == 'quit':
            print('You have quit the game.')
            sys.exit(0)
            
        #elif input1 == 'Quit':                 # Use this Quit command instead of sys.exit(0) if not running in Jupyter
            #print('You have quit the game.')
            #quit()
battle = Battle()
battle.start()


# In[ ]:




