#**********imports**********#
import time 
import random as r
def alive(name):
  if name<=0:
    
    return 0
  else :
   return 1
def health(name):
  if name==0:
   return 0
  else :
    return 
def buff(name):
   name2 = name+name*0.3
   return name2
  

  
#**********intro************#
print("welcome")
time.sleep(1)
print('to')
time.sleep(1)
print('elcato')
time.sleep(1)
print("****************************")
#**********main menu************#
menu=""

while menu=="":
 menu=input("type anything to start ")
 
#**********Player job************#
 health_1=300#the tanks hp
 basic_1=r.randint(60,90)
 ability11=r.randint(30,50)#fell cleave does 50 damege and increase party dmg by 10% for the next turn
 ability12=300#regen own hp to full
 ability13=3#you enrage and do 100% but only can use basic attack
 ability13U=False
 ability1N="fell clever"
 ability2N="shake it off"
 ability3N="RAGE"
 

 basic_2=50
 ability21=30#reduce dmg taken by all part members by 30%
 ability22=0.3#has 30% chance to makes the boss unable to act for 1 turn and does 50dmg
 ability23=200#makes the whole part invensable for 1 turn 
 ability23U=False
#**********healer************#

 basic_3=50
 ability31=150#heals a party member 100hp
 ability32=50#aoe heal
 ability33=50#raise one fallen ally with 1 hp
 ability33U=False
#**********dancer************#

 basic_4=80
 ability41=200#incrase the potency of an ability by 50%
 ability42=20#boost the potency of all members by 20%
 ability43=100#gives an ally the dance partner buff
 ability43U=False
 #**********health************#
 B_health=3000#boss hp
 health_2=200#the tanks hp
 health_3=250#the healer hp
 health_4=100#the dancer hp
 
 burn=r.random
 posion=r.random
 stun=r.random
 regen=r.random
 alivem=4
 die1=1
 die2=1
 die3=1
 die4=1
 
 
  #**********START************# 
 print("the fight starts ")
 time.sleep(1)
 while alivem!=0:
    #**********Boss info************#
    endsinger="Endsinger"
 
    B_meteior=r.randint(200,300)#aoe splits damege to all party members
    B_regen=50#restore hp to the boss every turn has 50% to be removed each turn
    B_basic=r.randint(60,80)#helps player gain advantege
    B_targeted=r.randint(50,150)
    B_enrage=9999#very rare attack kills the whole party
#**********archer************#

#**********statis effect************#
    if B_health>=0 :
       #**********boss attacks************#
   #enrage
       roll=r.randint(1,100)
       alivem=die1+die2+die3+die4

       if roll<=5:
        health_2 = health_1 = health_3 = health_4 = 0
        print("dragon used enarge and it did 9999 damege to each player")
        time.sleep(1)
        print("Warrior",health_1,"archer",health_2,"healer", health_3,"Sowrdsmen",health_4)
        time.sleep(1)

        die1=alive(health_1)
        die2=alive(health_2)
        die3=alive(health_3)
        die4=alive(health_4)

        if die1==0:
          health_1=0
        else :
          health_1+=5
        if die2==0:
           health_2=0
        else :
         health_2+=5
        if die3==0:
         health_3=0
        else :
         health_3+=10
        if die4==0:
          health_4=0
        else :
          health_4+=15

     
        print("Warrior",health_1,"archer",health_2,"healer", health_3,"Sowrdsmen",health_4)
        time.sleep(1)
        alivem=die1+die2+die3+die4
        print(alivem)
       #meteior
       elif roll <=10:
        B_meteiorN=int(B_meteior/alivem)
        health_1-=B_meteiorN
        health_2-=B_meteiorN
        health_3-=B_meteiorN
        health_4-=B_meteiorN
        print("dragon used meterior and it did",B_meteiorN,"damege to each player")
        time.sleep(1)

        die1=alive(health_1)
        die2=alive(health_2)
        die3=alive(health_3)
        die4=alive(health_4)

        if die1==0:
           health_1=0
        else :
           health_1+=5
        if die2==0:
           health_2=0
        else :
          health_2+=5
        if die3==0:
          health_3=0
        else :
          health_3+=10
        if die4==0:
          health_4=0
        else :
          health_4+=20

     
        print("Warrior",health_1,"archer",health_2,"healer", health_3,"Sowrdsmen",health_4)
        time.sleep(1)
        alivem=die1+die2+die3+die4
        print(alivem)
      #target

       elif roll<=30:
        target=r.randint(1,4)
        if target==1 :
          health_1-=B_targeted
          print("drahon used targeted attack and it did",B_targeted,"damege to warrior")
          time.sleep(1)
        elif target==2:
          health_2-=B_targeted
          print("dragon used targeted attack and it did",B_targeted,"damege to archer")
          time.sleep(1)
        elif target==3:
          health_3-=B_targeted
          print("dragon used targeted attack and it did",B_targeted,"damege to healer")
          time.sleep(1)
        elif target==4:
          health_4-=B_targeted
          print("dragon used targeted attack and it did",B_targeted,"damege to sowrdsmen")
          time.sleep(1)
        die1=alive(health_1)
        die2=alive(health_2)
        die3=alive(health_3)
        die4=alive(health_4)

        if die1==0:
          health_1=0
        else :
          health_1+=5
        if die2==0:
          health_2=0
        else :
          health_2+=5
        if die3==0:
          health_3=0
        else :
          health_3+=10
        if die4==0:
          health_4=0
        else :
          health_4+=20

     
        print("Warrior",health_1,"archer",health_2,"healer", health_3,"Sowrdsmen",health_4)
        time.sleep(1)
        alivem=die1+die2+die3+die4
        print(alivem)

     #basic
       else:

        target=r.randint(1,4)
        if target==1 :
          health_1-=B_basic
          print("dragon used basic and it did",B_basic,"damege to warrior")
          time.sleep(1)
        elif target==2:
          health_2-=B_basic
          print("dragon used basic and it did",B_basic,"damege to archer")
          time.sleep(1)
        elif target==3:
          health_3-=B_basic
          print("dragon used basic and it did",B_basic,"damege to healer")
          time.sleep(1)
        elif target==4:
          health_4-=B_basic
          print("dragon used basic and it did",B_basic,"damege to Sowrdsmen")
          time.sleep(1)
        die1=alive(health_1)
        die2=alive(health_2)
        die3=alive(health_3)
        die4=alive(health_4)
  
        if die1==0:
          health_1=0
        else :
          health_1+=5
        if die2==0:
           health_2=0
        else :
          health_2+=5
        if die3==0:
          health_3=0
        else :
          health_3+=10
        if die4==0:
          health_4=0
        else :
          health_4+=20

     
        print("Warrior",health_1,"archer",health_2,"healer", health_3,"Sowrdsmen",health_4)
        time.sleep(1)
        alivem=die1+die2+die3+die4
     #**********cheak for party************#
    else :
      print("YOU WON") 
      time.sleep(1) 
    if die1==1:
      print("1/basic attack\n2/",ability1N,"\n3/",ability2N,"\n4/",ability3N)
      time.sleep(1)
      move=int(input())
      if move==1:
        B_health-=basic_1
        print("you used basic attack and it did",basic_1,"damege")
        time.sleep(1)
      elif move==2:
        B_health-=ability11
        basic_1 = basic_1+basic_1*0.05
        print("you used fell celver  and it did",ability11,"damege\n your basic attack is stronger")
        time.sleep(1)
      elif move ==3:
        health_1=300
        print("you used Shake it off , your back to full health")
        time.sleep(1)
      elif move ==4:
        if ability13U==False :
          basic_1=basic_1+basic_1
          ability11=0
          ability12=0
          ability13U=True
          print("you used RAGE , your basic attack does douple the damege")
          time.sleep(1)
        else:
          print("you already used RAGE , nothing changed")
          time.sleep(1)
      
      time.sleep(1)
    if die2==1:
      print("1/basic attack\n2/poison shot\n3/motivate")
   
      move=int(input())
      if move==1:
        B_health-=basic_2
        print("you used basic attack and it did",basic_2,"damege")
        time.sleep(1)
      elif move==2:
        B_health-=ability21
        posionc=r.randint(1,100)
        if posionc>=50:
          print("you used poison shot and it did",ability21,"damege\n your Poisoned the dragon")
          time.sleep(1)
          posion=True
        else:
          print("you used poison shot and it did",ability21,"damege\n your couldn't Poisone the dragon")
          time.sleep(1)
          posion=False
      elif move ==3:
        basic_1 = buff(basic_1)
        basic_2 = buff(basic_2)
        basic_3 = buff(basic_3)
        basic_4 = buff(basic_4)
        print("you incressed all basic attacks damege by 30%")
        time.sleep(1)
    if die3==1:
      print("1/basic attack\n2/cure\n3/heal")
      time.sleep(1)
      move=int(input())
      if move==1:
        B_health-=basic_3
        print("you used basic attack and it did",basic_3,"damege")
        time.sleep(1)
      elif move==2:
       print("1/warrior\n2/archer\n3/healer \n4/swordsmen")
   
       cure=int(input())
       if cure==1:
          if die1==1:
           health_1+=ability32
           print("you restored warrior hp by ",ability32)
       elif cure==2:
          if die2==1:
           health_2+=ability32
           print("you restored archer hp by ",ability32)
       elif cure==3:
          if die3==1:
           health_3+=ability32
           print("you restored healer hp by ",ability32)    
       elif cure==4:
          if die4==1:
           health_4+=ability32
           print("you restored archer hp by ",ability32,)             
          time.sleep(1)
          
      elif move ==3:
        if die1==1:
           health_1+=ability33
        if die2==1:
           health_2+=ability33
        if die3==1:          
           health_3+=ability33
        if die4==1:
           health_4+=ability33
        print("you restored party hp by",ability33,"for each member")
        time.sleep(1)


    if die4==1:
      print("1/basic attack\n2/backstap\n3/regen")
  
      move=int(input())
      if move==1:
        B_health-=basic_4
        print("you used basic attack and it did",basic_4,"damege")
        time.sleep(1)
      elif move==2:
        B_health-=ability41
        health_4-=50
        if health_4<=0:
          health_4=1
        print("you used backstap and it did",ability41,"damege\n it caused you to take some damege")

      elif move ==3:
        health_4+=100
        print("you restored 100 hp")
        time.sleep(1)
      print("endsinger hp is",B_health,"/3000")
      time.sleep(1)
    if posion==True:
      B_health-=r.randint(50,100)
      ("the dragon took poison damege")
      posionc==r.randint(1,100)
      if posionc >=50:
        posion=False
        print("the dragon is no longer poisoned")
    if B_health<=0:
      print("YOU WON !")
      break
    if alivem==0 :
      print('you lost')
      break

