import random

Scissors = """ 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
Paper  = """  
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
rook = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

choices = [ rook , Paper , Scissors ]
pc_c = random.randint(0,2)
num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. : "))

print(choices[num])
print(f"""Computer chose : 
          {choices[pc_c]}
          """)
if num == 0 and pc_c == 2 :
    print("You Win ;] ")
elif num == 2 and pc_c == 0 :
    print("You lose :[ ")
elif num > pc_c :
    print("You Win ;] ")
elif pc_c > num :
    print("You lose :[ ")
elif pc_c == num :
    print(" It's a draw ")
else :
    print(" Hmmm enter 0 to 2 :/ ")