'''
Created on 2023/10/13

@author: t21cs061
'''
import random

class Player:
    def __init__(self, name):
        self._name = name
        self._wincount = 0
    
    def show_hand(self):
        return random.randrange(3)
    
    def notify_result(self, result):
        if True == result:
            self._wincount += 1
             
    def get_wincount(self):
        return self._wincount
    
    def get_name(self):
        return self._name
    
class Judge:
    def print_hand(self, hand):
        if hand == 0:
            return 'グー'
        elif hand == 1:
            return 'チョキ'
        elif hand == 2:
            return 'パー'
        
    def judge_janken(self, player1, player2):
        winner = None
        
        player1Hand = player1.show_hand()
        player2Hand = player2.show_hand()
        print(player1.get_name(),'：',Judge.print_hand(self,player1Hand), ' v.s. ', player2.get_name(),'：',Judge.print_hand(self, player2Hand) )
        
        if (player1Hand == 0 and player2Hand == 1) or (player1Hand == 1 and player2Hand == 2) or (player1Hand == 2 and player2Hand == 0):
            winner = player1
        elif (player2Hand == 0 and player1Hand == 1) or (player2Hand == 1 and player1Hand == 2) or (player2Hand == 2 and player1Hand == 0):
            winner = player2
        
        return winner
    
    def judge_finalwinner(self,player1,player2):
        winner = None
        
        player1Wincount = player1.get_wincount();
        player2Wincount = player2.get_wincount();
        
        if player1Wincount > player2Wincount:
            winner = player1
        
        elif player2Wincount > player1Wincount:
            winner = player2
        
        return winner

    def start_janken(self, player1, player2):
        print('【じゃんけん開始】')
        
        for x in {1,2,3}:
            print('【',x,'回戦目】')
            winner = Judge.judge_janken(self,player1,player2)
            if winner != None:
                print(winner.get_name(),'の勝ち')
                winner.notify_result(True)
            else:
                print('引き分け')
            
        print('¥n【じゃんけん終了】')
        finalWinner = Judge.judge_finalwinner(self,player1,player2)
        print(player1.get_wincount(),'対',player2.get_wincount(),'で')
        if finalWinner != None:
            print(finalWinner.get_name(),'の勝ちです')
        else:
            print('引き分けです')

"""     
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
"""
  
"""          
def ShowHand(hand):
    if hand == 0:
        print("グー")
    elif hand == 1:
        print("チョキ")
    elif hand == 2:
        print("パー")
"""
    
if __name__ == '__main__':
    judge = Judge()
    playerA = Player('山本')
    playerB = Player('鈴木')
    judge.start_janken(playerA, playerB)
        