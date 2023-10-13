'''
Created on 2023/10/13

@author: t21cs061
'''
import random

def Judge(hand_a, hand_b):
    if(hand_a == 0 ):
        if(hand_b == 0):
            print("引き分け")
        elif(hand_b == 1):
            print("勝ち")
        elif(hand_b == 2):
            print("負け")
            
    elif(hand_a == 1):
        if(hand_b == 0):
            print("負け")
        elif(hand_b == 1):
            print("引き分け")
        elif(hand_b == 2):
            print("勝ち")
            
    elif(hand_a == 2):
        if(hand_b == 0):
            print("勝ち")
        elif(hand_b == 1):
            print("負け")
        elif(hand_b == 2):
            print("引き分け")
            
def ShowHand(hand):
    if hand == 0:
        print("グー")
    elif hand == 1:
        print("チョキ")
    elif hand == 2:
        print("パー")
    
if __name__ == '__main__':
    hand_a = random.randint(0,2);
    hand_b = random.randint(0,2);
    
    ShowHand(hand_a);
    ShowHand(hand_b);
    
    Judge(hand_a, hand_b);
        