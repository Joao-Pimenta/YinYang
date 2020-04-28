import random, pygame, os, sys, time, collections, math
from decimal import *
global player_played, table, table_stable, pot, pay, round_n, value, did_not_pay_their_debt, paid_their_debt, all_in, out_the_game
os.chdir('/home/joao/Ying Yang/Code')
from CardCheker import do_it_all
os.chdir('/home/joao/Ying Yang/Images')
pygame.init()
screen = pygame.display.set_mode((612, 476))
background = pygame.image.load('table.png')
pygame.display.set_caption('Ying Yang')
icon = pygame.image.load('chip.png')
pygame.display.set_icon(icon)
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

N_Players = 6
standard = 'question.png'
Big = 0.04
Small = 0.02
winner = '?'
player_played = []

global images
players_inalterado = ['p0', 'p1', 'p2', 'p3', 'p4', 'p5']
positions = ['0', '1', '2', '3', '4', '5']

positions_coordinates = [(182, 6), (430, 6), (532, 206), (430, 336), (182, 336), (14, 206)]
keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
deck = ['2D', '2H', '2C', '2S', '3D', '3H', '3C', '3S', '4D', '4H', '4C', '4S', '5D', '5H', '5C', '5S', '6D', '6H', '6C', '6S', '7D', '7H', '7C', '7S', '8D', '8H', '8C', '8S', '9D', '9H', '9C', '9S', '10D', '10H', '10C', '10S', '11D', '11H', '11C', '11S', '12D', '12H', '12C', '12S', '13D', '13H', '13C', '13S', '14D', '14H', '14C', '14S']

global players
players = {
    'p0' : {'name':'p0', 'money':1000, 'position':'-1', 'hand':[], 'debt':0, 'score':0, 'image':'1.png', 'paid':0, 'action':'0', 'status':'no play', 'gained':0},
    'p1' : {'name':'p1', 'money':1000, 'position':'-1', 'hand':[], 'debt':0, 'score':0, 'image':'2.png', 'paid':0, 'action':'0', 'status':'no play', 'gained':0},
    'p2' : {'name':'p2', 'money':1000, 'position':'-1', 'hand':[], 'debt':0, 'score':0, 'image':'3.png', 'paid':0, 'action':'0', 'status':'no play', 'gained':0},
    'p3' : {'name':'p3', 'money':1000, 'position':'-1', 'hand':[], 'debt':0, 'score':0, 'image':'4.png', 'paid':0, 'action':'0', 'status':'no play', 'gained':0},
    'p4' : {'name':'p4', 'money':1000, 'position':'-1', 'hand':[], 'debt':0, 'score':0, 'image':'5.png', 'paid':0, 'action':'0', 'status':'no play', 'gained':0},
    'p5' : {'name':'p5', 'money':1000, 'position':'-1', 'hand':[], 'debt':0, 'score':0, 'image':'6.png', 'paid':0, 'action':'0', 'status':'no play', 'gained':0}}

def draw():
    screen.blit(background, (0, 0))
    global players
    print('draw --4')
    for player in players:
        if players[player]['position'] == '-1':
            pass
        else:
            pX, pY = positions_coordinates[int(players[player]['position'])]
            screen.blit(pygame.image.load(players[player]['image']), (pX, pY))
            font = pygame.font.Font(None, 20)
            font2 = pygame.font.Font(None, 17)
            cards_font = pygame.font.Font(None, 30)
            m = str(Context(prec=2, rounding=ROUND_DOWN).create_decimal(players[player]['money']))
            d = str(Context(prec=2, rounding=ROUND_DOWN).create_decimal(players[player]['debt']))
            p = str(Context(prec=2, rounding=ROUND_DOWN).create_decimal(players[player]['paid']))
            g = str(Context(prec=2, rounding=ROUND_DOWN).create_decimal(players[player]['gained']))
            text = str('N/'+str(players[player]['name'])+'| M/'+m+'| D/'+d+'| P/'+p)
            textsurface = font.render(text, False, (0, 0, 0))
            handsurface = font.render(str(str(players[player]['hand']) + ', ' + str(players[player]['action'])), False, (0, 0, 0))
            position_and_status = font.render(str(str(players[player]['position']) + ', ' + str(players[player]['status']) + ', gained: ' + g), False, (0, 0, 0))
            cards = cards_font.render(str(table), False, (0, 0, 0))
            played_games = font2.render(str('Played ' + str(games_played) + ' games'), False, (0, 0, 0))
            out = font2.render(str('Out the game :' + str(out_the_game)), False, (0, 0, 0))
            allin = font2.render(str('All in :' + str(all_in)), False, (0, 0, 0))
            wi = font2.render(str('Winner :' + str(winner)), False, (0, 0, 0))
            progress_bar = font2.render(str('Round: ' + str(round_n) + ', Have played: ' + str(player_played)), False, (0, 0, 0))
            
            if players[player]['position'] != '5':
                pX = pX - 30
            if players[player]['position'] == '2':
                pX = pX - 70
            pY = pY+80
            screen.blit(textsurface,(pX, pY))
            pY = pY+20
            screen.blit(handsurface,(pX, pY))
            pY = pY+20
            screen.blit(position_and_status,(pX, pY))
    screen.blit(cards, (176, 178))
    screen.blit(played_games, (5, 5))
    screen.blit(out, (5, 20))
    screen.blit(allin, (5, 35))
    screen.blit(wi, (5, 50))
    screen.blit(progress_bar, (5, 65))
    if infinite_money == True:
        inf = font2.render('Infinite Money Activated', False, (0, 0, 0))
        screen.blit(inf, (5, 80))
    pygame.display.update()


#########################################


def prep(round_n):
    print('prep --6')
    global pot, less_money, positions, deck
    positions = ['0', '1', '2', '3', '4', '5']
    for player in players:
        while True:
            pos = random.choice(positions)
            if players[player]['position']=='0': less_money = -(Small); players[player]['paid'] = Small; pot = float(pot) + float(Small)
            elif players[player]['position']=='1': less_money = -(Big); players[player]['paid'] = Big; pot = float(pot) + float(Big)
            else: less_money = 0; players[player]['paid'] = 0

            players[player]['position'] = random.choice(positions)
            
            ha1 = random.choice(deck)
            while True:
                ha2 = random.choice(deck)
                if ha1 != ha2:
                    break
            players[player]['hand'].clear()
            players[player]['hand'].append(ha1)
            players[player]['hand'].append(ha2)
            if players[player]['name'] not in played:
                played.append(players[player]['name'])
            choosing = random.randint(0, 1)
            if choosing == 1:
                table_disposition[int(players[player]['position'])] = players[player]['name']
                positions.remove(players[player]['position'])
                deck.remove(ha1)
                deck.remove(ha2)
                break #1 is accept, 0 is refuse
    draw()
    print('this is the table order : ', table_disposition)
    #print('#1 the deck is: ', deck)

def fight(round_n):
    global player_played, pot, pay, value, did_not_pay_their_debt, paid_their_debt, all_in, out_the_game, players
    print('fight --8')
    
    for player in players:
        if players[player]['name'] in out_the_game or players[player]['name'] in all_in:
            if players[player]['name'] in out_the_game:
                players[player]['status'] = 'out'
            else:
                players[player]['status'] = 'all_in'
        else:
            players[player]['status'] = 'ready to play'
    draw()
    
    player_played = []
    try:
        played[:] = [x for x in out_the_game and x for x in all_in]
    except:
        try:
            played[:] = [x for x in all_in]
        except:
            played[:] = [x for x in out_the_game]
    paid_their_debt.clear()
    did_not_pay_their_debt = [x for x in players_inalterado if x not in out_the_game if x not in all_in if x not in paid_their_debt]
    forward = False
    start_position = -1
    pass_1_times = 0
    return_if_no_money = True
    while forward == False:
        for a in out_the_game:
            if a in player_played:
                player_played.remove(a)
        for a in all_in:
            if a in player_played:
                player_played.remove(a)
        
        start_position = start_position + 1
        if start_position == 6:
            start_position = -1
            
        if len(player_played) == int(N_Players - len(out_the_game) - len(all_in)) or int(len(out_the_game) + len(all_in)) == int(N_Players):
            break
        for player in players:
            if players[player]['name'] in all_in or players[player]['name'] in out_the_game:
                pass
            else:

                if players[player]['name'] in player_played:
                    print('player ', players[player]['name'], 'has played')
                    print('the player_played list is: ', player_played)
                    print('int(N_Players - len(out_the_game) - len(all_in)) = ', int(N_Players - len(out_the_game) - len(all_in)))
                    print('out_the_game : ', out_the_game)
                    print('all_in : ', all_in)
                else:
                    if round_n == 1:
                        if pass_1_times != 1:
                            pass_1_times += 1
                            start_position = 2
                            
                    if int(players[player]['position']) == start_position:
                        if players[player]['name'] in all_in or players[player]['name'] in out_the_game:
                            print('player ', players[player]['name'], 'is in all in or out of the game')

                        elif value == 0 and int(len(played)+len(out_the_game)+len(all_in)) == N_Players and len(did_not_pay_their_debt) == 0:
                            proceed = False
                            forward = True
                            print('FORWARD IS TRUE')
                            print(str(len(played)+len(out_the_game)+len(all_in)))
                            print('players that have played:', played)
                            print('out_the_game:', out_the_game)
                            print('all_in:', all_in)
                            print('did_not_pay_their_debt:', did_not_pay_their_debt)
                            print('SOMETHING WRONG')
                            break

                        else:
                            print('player ', players[player]['name'], 'is playing')
                            return_if_no_money = True
                            while return_if_no_money == True:
                                return_if_no_money = False

                                print('checkpoint 1')

                                try:
                                    did_not_pay_their_debt.remove(players[player]['name'])
                                except:
                                    pass
                                try:
                                    paid_their_debt.append(players[player]['name'])
                                except:
                                    pass
                                print('checkpoint 2')
                                
                                value = pay - players[player]['paid']
                                players[player]['paid'] = 0

                                print('checkpoint 3')

                                pX, pY = positions_coordinates[int(players[player]['position'])]
                                screen.blit(pygame.image.load('square.png'), (pX, pY))
                                pygame.display.update()

                                print('SQAURE')
                            

                                played.append(str(players[player]['name']))
                                still_in_game = int(len(players_inalterado)-len(all_in)-len(out_the_game))

                                choosing = random.choice(keys)
                                typed = keys[1:-1] # last element is fold and first is check
                                percentage = [0.02, 0.05, 0.1, 0.25, 0.45, 0.65, 0.85, 1]
                                if choosing == keys[-1]:
                                    if float(value) == float(0):
                                        choosing = keys[0] #if no pay, fold is interpreted has check
                                        players[player]['action'] = 'fold w/no pay is check '
                                    else:
                                        players[player]['action'] = 'fold'
                                        out_the_game.append(players[player]['name'])
                                        try:player_played.remove(players[player]['name'])
                                        except:pass
                                        try:did_not_pay_their_debt.remove(players[player]['name'])
                                        except:pass
                                        try: paid_their_debt.remove(players[player]['name'])
                                        except:pass     
                                else:
                                    if float(players[player]['money']) <= float(value):
                                        pot = float(pot + players[player]['money'])
                                        players[player]['money'] = 0
                                        players[player]['debt'] = float(value-players[player]['money'])
                                        if players[player]['name'] in paid_their_debt:paid_their_debt.remove(players[player]['name'])
                                        if players[player]['name'] in did_not_pay_their_debt: did_not_pay_their_debt.remove(players[player]['name'])
                                        if players[player]['name'] not in all_in: all_in.append(players[player]['name'])
                                        if players[player]['name'] in out_the_game: print('error 56y23qhjk46'), 
                                        try:player_played.remove(players[player]['name'])
                                        except:pass

                                    else:
                                        players[player]['money'] = float(players[player]['money'] - value)
                                        pot = float(pot) + float(value)
                                        players[player]['paid'] = value
                                        
                                    if choosing in keys[0]:
                                        players[player]['action'] = 'check'
                                    
                                    else:
        ##                                have_to_play_less[:] = paid_their_debt[:]
        ##                                less_pay = pay
                                        #nao tenho a certeza se isto esta completamente correto

                                        awa = typed.index(choosing)
                                        print('awa : ', awa)
                                        computation = players[player]['money']*percentage[awa]

                                        pay = float(round(computation, 2))
                                        pot = float(pot) + float(pay)
                                        players[player]['money'] = float(players[player]['money']) - float(pay)

                                        players[player]['action'] = str('raise '+str(percentage[awa])+'%'+' to '+str(pay))

                                        player_played.clear()
                                        print('because ', players[player]['name'], ' placed a bet, only him must be in the player_played list:')
                                        print(player_played)
                                        #played[:] = [players[player]['name']]
                                        did_not_pay_their_debt = [x for x in players_inalterado if x not in out_the_game if x not in all_in if x not in paid_their_debt]
                                        
                                    if players[player]['money'] == 0:
                                        if players[player]['name'] in paid_their_debt:paid_their_debt.remove(players[player]['name'])
                                        elif players[player]['name'] in did_not_pay_their_debt: did_not_pay_their_debt.remove(players[player]['name'])
                                        elif players[player]['name'] not in all_in: all_in.append(players[player]['name'])
                                        elif players[player]['name'] in out_the_game: print('error 56y23qhjk46'), 
                                        try:player_played.remove(players[player]['name'])
                                        except:pass
                            player_played.append(players[player]['name'])
                            players[player]['status'] = 'played'
                            print(players[player]['name'], ' had the action: ', players[player]['action'])
                            draw()
    draw()

def main(games_played):
    global winner, infinite_money, played, deck, table_disposition, value, pot, round_n, pay, score, out_the_game, table, table_stable, all_in, analized,did_not_pay_their_debt, paid_their_debt, have_to_play_less

    reps = 0

    infinite_money = True
    for player in players:
        players[player]['money'] = random.randint(1, 5)

    deck = ['2D', '2H', '2C', '2S', '3D', '3H', '3C', '3S', '4D', '4H', '4C', '4S', '5D', '5H', '5C', '5S', '6D', '6H', '6C', '6S', '7D', '7H', '7C', '7S', '8D', '8H', '8C', '8S', '9D', '9H', '9C', '9S', '10D', '10H', '10C', '10S', '11D', '11H', '11C', '11S', '12D', '12H', '12C', '12S', '13D', '13H', '13C', '13S', '14D', '14H', '14C', '14S']    
    table_disposition = ['0', '0', '0', '0', '0', '0']
    value = 0
    pot = 0
    round_n = 0
    pay = 0
    score = 0
    played = []
    out_the_game = []
    table = []
    table_stable = []
    all_in = []
    analized = []
    did_not_pay_their_debt = []
    paid_their_debt = []
    have_to_play_less = []
    print('main() --12')
    num = 0
    while True:
        if round_n == 0: prep(round_n)
        elif round_n == 1: num = 3
        else: num = 1; pay = 0
        
        for a in range(num):
            card = random.choice(deck)
            table.append(card)
            deck.remove(card)
            #print('#2 the deck is: ', deck)

        table_stable[:] = table[:]
        return_list = []
            
        #checked
            
        if round_n == 1 or round_n == 2:
            print('is in Fight in the round: ', round_n)
            fight(round_n)
        elif round_n == 3:
            print('this is the table that is going for the other function : ', table)
            print('this are the players that are out of the game: ', out_the_game)
            print('this are the players in all in : ', all_in)
            for player in players:
                n = players[player]['name']
                h = players[player]['hand']
                print('player ', n, ' has the hand: ', h)
                if players[player]['name'] not in out_the_game:
                    players[player]['status'] = 'waiting show down'
            draw()
            winner = list(do_it_all(players, table, out_the_game, table_stable))
            try: #to compensate an error from 'no winner' and then devision by zero, it repeats the operation one more time
                toadd = float(pot/len(winner))
                print('winner : ', winner)
                print('toadd : ', toadd)
                for a in winner:
                    print('a : ', a)
                    players[a]['gained'] += toadd
                draw()
                reps = 0
                break
            except:
                reps = 0
                round_n -= 1
                reps = reps + 1
        else:
            if round_n != 0:
                print('EEEEEEEEEEEERRRRRRRRRRRRRRRROOOOOOOOOOOOOOOOORRRRRRRRRRRRR')
                break
        round_n += 1

        #quit if x is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

if __name__ == '__main__':
    games_played = 0
    while True:
        main(games_played)
        games_played = games_played + 1
        print()
        print()
        print('PLAYED ', games_played, ' GAMES')
        print()
        print()
    

################### confirmas estas duas coisas: que comeca na posicao 2 e que, depois da 1 vez que o jogo passa pelas posicoes 0 e 1
###################, esses jogadores deixam de ter privilegio, mas se continuar a ronda 1
