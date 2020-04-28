import os, re
os.chdir('/home/joao/Desktop/Imagens/')
import pyautogui, time, random, sys, pytesseract, pyperclip, re
from PIL import Image
from random import randint
from pynput.mouse import Button, Controller as MouseController
mouse = MouseController ()
import subprocess
pyautogui.FAILSAFE = False

global score, score_test_draw

score = 0
##score_test_draw = ([0, 0, 0, 0, 0, 0, 0, 0], None, None, None, None, None, None, None, None)

##out_the_game = []
##table = ['2C', '2H', '12S', '12H', '12C']
##table_stable = []
##table_stable[:] = table[:]
##players = {
##    'player0' : {'name':'player0', 'hand':['3S', '3H'], 'score':0, 'test_draw':(None, None, None, None, None, None, None, None, None)},
##    'player1' : {'name':'player1', 'hand':['9H', '6H'], 'score':0, 'test_draw':(None, None, None, None, None, None, None, None, None)},
##    'player2' : {'name':'player2', 'hand':['13S', '4C'], 'score':0, 'test_draw':(None, None, None, None, None, None, None, None, None)}}

##score_test_draw_1_time = 0
def check_cards(players, table, out_the_game, score_test_draw):
    winner = []
    scores = []
    test_draw = ()
    unchanged = []
    total_highest_score = 0
    unchanged[:] = table[:]
    for player in players:
##        if score_test_draw_1_time == 0:
##            print('score_test_draw_1_time was used')
##            score_test_draw = ([0, 0, 0, 0, 0, 0, 0, 0], None, None, None, None, None, None, None, None)
        hand = []
        if player in out_the_game:
            pass
        else:
            table[:] = unchanged[:]
            hand = [x for x in list(players[player]['hand'])]
            print('HAND :', hand)
            global sequenced
            sequenced = ['0']
            infinite_sequenced = []
            sequence_count = 0
            highest_kicker = []
            confirm_that_flush_is_strait = []
            global score
            score = 0
            def scoring(self):
                global score
                if self > score:
                    score = self
            def find(self):
                q = counts[self]
                if q >= 5:
                    if len(sequenced) >= 5:
                        for player in sequenced:
                            e = str(str(i)+str(self))
                            qe = str(e.replace('count', ''))
                            confirm_that_flush_is_strait.append(qe)
                        print('confirm_that_flush_is_strait : ', confirm_that_flush_is_strait)
                        if confirm_that_flush_is_strait in combined:
                            print('if confirm_that_flush_is_strait is in combined:')
                            straight_flush.append(self)
                        flush.append(self)
                    else:
                        flush.append(self)
                else:
                    if self not in ['countC', 'countD', 'countH', 'countS']:
                        if q == 4:
                            four_of_a_kind.append(self)
                        if q == 3:
                            trio.append(self)
                            if pair1 is not None:
                                full_house.append(self)
                        if q == 2:
                            try:
                                a = pair1[-1]
                                pair2.append(self)
                            except:
                                pair1.append(self)
                                
                                if trio is not None:
                                    full_house.append(self)
                        else:
                            highest_kicker.append(self)
            #################################################################################################
            #################################################################################################

            def say_number(self):
                try:
                    q = self[0]
                    qe = int(q.replace('count', ''))
                    return qe
                except:
                    return

            def sort(self):
                if self is not None:
                    try:
                        self.replace('count', '')
                    except:
                        pass
                    self.sort
                    self[:]=self[::-1]
                    return self
                else:
                    return

            def highest_from_flush(self):
                print('flush : ', self)
                table3 = []
                try:
                    s = str(self[-1])
                    print('1')
                    simbol = str(s.replace('count', ''))
                    print('2') 
                    #simbol = s.translate({ord(i): None for i in 'count'})
                    print('simbol:', simbol)
                    print('3')
                    table2 = table
                    print('table2 : ', table2)
                    print('5')
                    for player in table2:
                        v = str(i)
                        if simbol in player != -1:
                            b = int(i.translate({ord(w): None for w in 'CSHD'}))
                            print('BBBB : ', b)
                            table3.append(b)
                    table3.sort()
                    print('table3 : ', table3)
                    print('6')
                    to_return = int(table3[-1])
                    print('7')
                    print('to_return : ', to_return)
                    return to_return
                except:
                    return

            def highest_from_pairs(pair1, pair2):
                if say_number(pair1) is not None:
                    p1 = say_number(pair1)
                    if say_number(pair2) is not None:
                        p2 = say_number(pair2)
                        if p1>p2:
                            return p1
                        else:
                            return p2
                    else:
                        return
                else:
                    return


            def split_cards(table):
                return list(table)


            combined = table
            combined.extend(hand)
            print(combined)
            splitable = ''
            for a in combined:
                splitable += a
            splitable.split()
            print(splitable)
            sequence = []

            countC = 0
            countD = 0
            countH = 0
            countS = 0
            count2 = 0
            count3 = 0
            count4 = 0
            count5 = 0
            count6 = 0
            count7 = 0
            count8 = 0
            count9 = 0
            count10 = 0
            count11 = 0
            count12 = 0
            count13 = 0
            count14 = 0
                
            counts = {'countC':countC, 'countD':countD, 'countH':countH, 'countS':countS, 'count2':count2, 'count3':count3, 'count4':count4, 'count5':count5, 'count6':count6, 'count7':count7, 'count8':count8, 'count9':count9, 'count10':count10, 'count11':count11, 'count12':count12, 'count13':count13, 'count14':count14}
            aglutinate = False
            for i in splitable:
                if aglutinate == True:
                    aglutinate = False
                    if i in ['C', 'D', 'H', 'S']:
                        pass
                    else:
                        i = str('1'+i)
                if i == '1':
                    aglutinate = True
                else:
                    add = str('count'+i)
                    counts[add] = counts[add]+1
                    r = {add : counts[add]}
                    if i not in ['C', 'D', 'H', 'S']:
                        sequence.append(int(i))
                    counts.update(r)

            sequence.sort()
            print('sequence.sort() : ', sequence)
            if int(sequence[-1]) == 14:
                sequence.insert(0, 1)
                print('sequence.insert(0, 1) : ', sequence)
            sequenced[0] = int(sequence[0])
            print('sequenced.append(sequence[0]) : ', sequenced)
            last = -1
            for i in sequence:
                if int(i) == int(last+1):
                    sequenced.append(i)
                    if int(sequence_count) == 5:
                        sequenced.sort()
                        highest_from_sequence = i

                last = sequenced[-1]

            sequenced.pop(0)
            reps = 0
            for a in sequenced:
                if reps == 0:
                    b = a
                else:
                    if int(a) == int(b+1):
                        b = a
                    else:
                        sequenced.clear()
                reps = reps + 1
                
            if len(sequenced)<5:
                sequenced.clear()

            print('sequenced : ', sequenced)

            analized = []
            straight_flush = []
            flush = []
            four_of_a_kind = []
            full_house = []
            trio = []
            pair1 = []
            pair2 = []

            for i in counts:
                find(i)

            if len(sequenced) >= 5:
                h_sequence = int(sequenced[-1])
            else:
                h_sequence = None
            h_flush = highest_from_flush(flush)
            h_trio = say_number(trio)
            try:
                a = trio[-1]
                b = pair1[-1]
                h_trio_if_full_house = h_trio
            except:
                h_trio_if_full_house = None
            h_4 = say_number(four_of_a_kind)
            h_pair1 = say_number(pair1)
            h_pair2 = say_number(pair2)
            h_kicker = sort(sequence)
            if len(confirm_that_flush_is_strait) >= 5:
                try:
                    resolve_recurring_error = -1 #sometimes, after thousands of games, the error "ValueError: invalid literal for int() with base 10: ''" occured
                    while True:
                        a = str(confirm_that_flush_is_strait[int(resolve_recurring_error)])
                        try:
                            h_strait_flush = int(a.translate({ord(i): None for i in 'CDSH'}))
                        except:
                            resolve_recurring_error = resolve_recurring_error -1
                except:
                    h_strait_flush = None
            else:
                h_strait_flush = None

            test_draw = (h_kicker, h_pair1, h_pair2, h_trio, h_sequence, h_flush, h_trio_if_full_house, h_4, h_strait_flush)
            
            reps = 0
            for i in test_draw:
                reps = reps + 1
                if i is None:
                    pass
                else:
                    if reps == 9:
                        if flush is not None:
                            scores.append(reps)
                    else:
                        scores.append(reps)
                        
            print('scores : ', scores)
            score = scores[int(len(scores)-1)]

            print('(h_kicker, h_pair1, h_pair2, h_trio, h_sequence, h_flush, h_trio, h_4, h_strait_flush)')
            print('test_draw : ', test_draw)
            print('score_test_draw : ', score_test_draw)
            try:
                a = score_test_draw[0]
            except:
                print('score_test_draw is empty, so it will be made equal to the current test_draw')
                score_test_draw = test_draw
                print('score_test_draw : ', score_test_draw)
                
            print('SCORE : ', score)
            print('TOTAL_HIGHEST_SCORE : ', total_highest_score)
            print('')

            if int(score) == int(total_highest_score):
                print('test_draw : ', test_draw)
                print('score_test_draw : ', score_test_draw)
                go_to_else = False
                if score == 9:
                    if test_draw[8] > score_test_draw[8]:
                            winner.clear()
                            
                            winner.append(players[player]['name'])
                            score_test_draw = test_draw
                    elif test_draw[8] < score_test_draw[8]:
                        break
                    else:
                        winner.append(players[player]['name'])
                    
                if score == 7:
                    if test_draw[6] > score_test_draw[6]:
                            winner.clear()
                            
                            winner.append(players[player]['name'])
                            score_test_draw = test_draw
                    elif test_draw[6] < score_test_draw[6]:
                        break
                    else:
                        biggest_pair_test_draw = False
                        biggest_pair_score_test_draw = False
                        try:
                           a = test_draw[2]
                           if test_draw[2] > test_draw[1]:
                               biggest_pair_test_draw = True
                        except:
                            pass
                        try:
                            a = score_test_draw[2]
                            if score_test_draw[2] > score_test_draw[1]:
                                biggest_pair_score_test_draw = True
                        except:
                            pass
                        if biggest_pair_test_draw == True:
                            pair_test = test_draw[2]
                        else:
                            pair_test = test_draw[1]
                        if biggest_pair_score_test_draw == True:
                            pair_score = score_test_draw[2]
                        else:
                            pair_score = score_test_draw[1]
                        if pair_test > pair_score:
                            winner.clear()
                            
                            winner.append(players[player]['name'])
                            score_test_draw = test_draw
                        elif pair_test < pair_score:
                            break
                        else:
                            winner.append(players[player]['name']) #draw
                            
                if score == 5:
                    if test_draw[4] > score_test_draw[4]:
                            winner.clear()
                            
                            winner.append(players[player]['name'])
                            score_test_draw = test_draw
                    elif test_draw[4] < score_test_draw[4]:
                        break
                    else:
                        winner.append(players[player]['name'])
                        
                if score == 3:
                    if test_draw[2] > test_draw[1]:
                        biggest_test_draw = test_draw[2]
                        smaller_test_draw = test_draw[1]
                    else:
                        biggest_test_draw = test_draw[1]
                        smaller_test_draw = test_draw[2]
                    if score_test_draw[2] > score_test_draw[1]:
                        biggest_score_test_draw = score_test_draw[2]
                        smaller_score_test_draw = score_test_draw[1]
                    else:
                        biggest_score_test_draw = score_test_draw[1]
                        smaller_score_test_draw = score_test_draw[2]

                    if biggest_test_draw > biggest_score_test_draw:
                            winner.clear()
                            
                            winner.append(players[player]['name'])
                            score_test_draw = test_draw
                    elif biggest_test_draw < biggest_score_test_draw:
                        break
                    else:
                        if smaller_test_draw > smaller_score_test_draw:
                            winner.clear()
                            
                            winner.append(players[player]['name'])
                            score_test_draw = test_draw
                        elif smaller_test_draw < smaller_score_test_draw:
                            break
                        else:
                            go_to_else = True
                else:
                    go_to_else = True
                    

                if go_to_else == True:
                    t = [test_draw[0]]
                    t[:]=t[0]
                    s = [score_test_draw[0]]
                    s[:]=s[0]
                    r = 0
                    t = [x for x in t if x not in [1]]
                    s = [x for x in s if x not in [1]]
                    print('TTTTTt : ', t)
                    print('SSSSS : ', s)
                    if len(t) != len(s):
                        print('error y43et5')
                        exit()
                    else:
                        while r <= int(len(t)-1):
                            if t[r] > s[r]:
                                winner.clear()
                                winner.append(players[player]['name'])
                                score_test_draw = test_draw
                            if t[r] < s[r]:
                                break
                            if r == len(score_test_draw[0])-1:
                                winner.append(players[player]['name'])
                            r += 1                    

            elif score > total_highest_score:
                total_highest_score = score
                winner.clear()
                winner.append(players[player]['name'])
                score_test_draw = test_draw

    print()
    print('the total_highest_score is : ', total_highest_score)

    return winner



def do_it_all(players, table, out_the_game, table_stable):
    score_test_draw = ([0, 0, 0, 0, 0, 0, 0, 0], None, None, None, None, None, None, None, None)
    print('')
    print('############## SHOW DOWN ##############')
    print('')
    final_winner = check_cards(players, table, out_the_game, score_test_draw)
    print('THE FINAL WINNER : ', final_winner)
    print('')
    print('TABLE : ', table_stable)
    print('the following are out the game: ', out_the_game)
    for player in players:
        if player in out_the_game:
            pass
        else:
            print(players[player]['name'], "'s hand is : ", players[player]['hand'])
    return final_winner



#do_it_all(players, table, out_the_game)

##table = ['2C', '2H', '12S', '12H', '12C']
##players = {
##    'player0' : {'name':'player0', 'hand':['3S', '3H'], 'score':0, 'test_draw':(None, None, None, None, None, None, None, None, None)},
##    'player1' : {'name':'player1', 'hand':['9H', '6H'], 'score':0, 'test_draw':(None, None, None, None, None, None, None, None, None)},
##    'player2' : {'name':'player2', 'hand':['13S', '4C'], 'score':0, 'test_draw':(None, None, None, None, None, None, None, None, None)}}
##
##
##
#print('The final winner is : ', check_cards(table))

##for a in range(3):
##    num = random.randint(1, 10)
##    print(num)
####pyautogui.alert(text='test of text', title='test', button='OK')
####pyautogui.confirm(text='test of text', title='title', buttons=['OK', 'Cancel'])
##pyautogui.password(text='text', title='title', default='', mask='*')
##for a in range(3):
##    num = random.randint(1, 10)
##    print(num)




            ##empate em 9: ganha a carta mais alta da sequência.
            ##
            ##
            ##empate em 7: Em caso de empate: ganha o pot o full house com o trio mais alto.
            ##Nos jogos com cartas comunitárias em que os jogadores têm os mesmos trios, ganha o full house do par com o valor mais alto.
            ##
            ##
            ##empate em 5: Em caso de empate: ganha a carta mais alta da sequência. 
            ##

            ##empate em 3: Em caso de empate: ganha o par mais alto. Se os jogadores tiverem o mesmo par mais alto, ganha o segundo par mais alto.
            ##Se ambos os jogadores tiverem dois pares idênticos, ganha a carta lateral mais alta.

            ##empate em 8: Em caso de empate: ganha o four of a kind mais alto.\
            ##Nos jogos com cartas comunitárias em que os jogadores têm o mesmo four of a kind, a quinta carta lateral mais alta ('kicker') ganha.
            ##
            ##empate em 6: Em caso de empate: ganha o jogador com a carta mais alta do ranking.
            ##Se for necessário, serão utilizadas a segunda, a terceira, a quarta e a quinta carta mais alta para determinar o vencedor.
            ##Se as cinco cartas tiverem todas o mesmo ranking, o pote é dividido. O naipe nunca é utilizado para alcançar um desempate no poker.
            ##
            ##empate em 4: Em caso de empate: ganha o trio mais alto. Nos jogos com cartas comunitárias em que os jogadores têm o mesmo trio,
            ##a carta lateral mais alta ou, se for preciso, a segunda carta mais alta, decidem o vencedor.            
            ##
            ##empate em 2: Em caso de empate: ganha o par mais alto. Se os jogadores tiverem o mesmo par, ganha a carta lateral mais alta e,
            ##se for preciso, podem ser usadas a segunda e terceira cartas laterais mais altas para desempatar.
            ##
            ##empate em 1: Em caso de empate: ganha a carta mais alta, e caso seja necessário, serão utilizadas a segunda,
            ##a terceira, a quarta e a quinta carta mais alta para desempatar.

