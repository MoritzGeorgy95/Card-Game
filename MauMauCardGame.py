"First official 2021 project"

import random
import pygame
import time

pygame.init()

"""All we need for the game setup using pygame (colors, fonts, our images and game window)"""

#game window
win= pygame.display.set_mode((1200, 800))

#game_caption
pygame.display.set_caption("Moritz Mau-Mau")

#game music
pygame.mixer.init()
pygame.mixer.music.load("game-soundtrack Kopie.mp3")
pygame.mixer.music.play(-1)

#colors, fonts, text rectangular
white= (255,255,255)
yellow= (204, 204, 0)
black= (0,0,0)
brown= (250, 235, 215)
font = pygame.font.Font('freesansbold.ttf', 24)
font_player_description= pygame.font.Font('freesansbold.ttf', 24)
font_button_text= pygame.font.Font('freesansbold.ttf', 12)
font_winner_button_text= pygame.font.Font('freesansbold.ttf', 24)

question_text = font.render('Do you want to start the game?', True, white)


option1_text= font.render("YES", True, yellow)
option2_text= font.render("EXIT", True, yellow)

option1_Rect = option1_text.get_rect()
option2_Rect= option2_text.get_rect()

player1_text= font_player_description.render("Player 1", True, black)
player2_text= font_player_description.render("Player 2", True, black)

button_text= font_button_text.render("Draw Card?", True, black)
button_text_Rect= button_text.get_rect()

cant_play_text= font_button_text.render("Fold", True, black)
cant_play_text_Rect= cant_play_text.get_rect()

make_wish_text= font_button_text.render("Make wish", True, black)
make_wish_text_Rect= make_wish_text.get_rect()

#images

    #1 menuscreen
menu_screen_background= pygame.image.load("Menuscreen.jpg")
Dame= pygame.image.load("Dame.jpg")
King= pygame.image.load("King.jpg")
Ass= pygame.image.load("Ass.jpg")

    #2 actual game

game_background= pygame.image.load("Hintergrund.jpg")




#game mechanics and functionality

class Card:
    cards=[]
    def __init__(self, image, type, number):
        self.image=image
        self.cards.append(self)
        self.type= type
        self.number= number
        #self.player


#create all cards

herzass = Card(pygame.image.load("images/AH.jpg"), "herz", 14)
herzkoenig= Card(pygame.image.load("images/KH.jpg"), "herz", 13)
herzdame = Card(pygame.image.load("images/QH.jpg"), "herz", 12)
herzbube = Card(pygame.image.load("images/JH.jpg"), "herz", 11)
herzzehn = Card(pygame.image.load("images/10H.jpg"), "herz", 10)
herzneun= Card(pygame.image.load("images/9H.jpg"), "herz", 9)
herzacht = Card(pygame.image.load("images/8H.jpg"), "herz", 8)
herzsieben = Card(pygame.image.load("images/7H.jpg"), "herz", 7)

pikass = Card(pygame.image.load("images/AS.jpg"), "pik", 14)
pikkoenig= Card(pygame.image.load("images/KS.jpg"), "pik", 13)
pikdame = Card(pygame.image.load("images/QS.jpg"), "pik", 12)
pikbube = Card(pygame.image.load("images/JS.jpg"), "pik", 11)
pikzehn = Card(pygame.image.load("images/10S.jpg"), "pik", 10)
pikneun= Card(pygame.image.load("images/9S.jpg"), "pik", 9)
pikacht = Card(pygame.image.load("images/8S.jpg"), "pik", 8)
piksieben = Card(pygame.image.load("images/7S.jpg"), "pik", 7)

karoass = Card(pygame.image.load("images/AD.jpg"), "karo", 14)
karokoenig= Card(pygame.image.load("images/KD.jpg"), "karo", 13)
karodame = Card(pygame.image.load("images/QD.jpg"), "karo", 12)
karobube = Card(pygame.image.load("images/JD.jpg"), "karo", 11)
karozehn = Card(pygame.image.load("images/10D.jpg"), "karo", 10)
karoneun= Card(pygame.image.load("images/9D.jpg"), "karo", 9)
karoacht = Card(pygame.image.load("images/8D.jpg"), "karo", 8)
karosieben= Card(pygame.image.load("images/7D.jpg"), "karo", 7)

kreuzass = Card(pygame.image.load("images/AC.jpg"), "kreuz", 14)
kreuzkoenig= Card(pygame.image.load("images/KC.jpg"), "kreuz", 13)
kreuzdame = Card(pygame.image.load("images/QC.jpg"), "kreuz", 12)
kreuzbube = Card(pygame.image.load("images/JC.jpg"), "kreuz", 11)
kreuzzehn = Card(pygame.image.load("images/10C.jpg"), "kreuz", 10)
kreuzneun= Card(pygame.image.load("images/9C.jpg"), "kreuz", 9)
kreuzacht = Card(pygame.image.load("images/8C.jpg"), "kreuz", 8)
kreuzsieben = Card(pygame.image.load("images/7C.jpg"), "kreuz", 7)

#create deck

deck= Card.cards

def shuffle_deck():
    for i in range(0, len(deck)):
        rep = random.randint(0, 31)
        deck[i], deck[rep] = deck[rep], deck[i]

    return deck


deck = shuffle_deck()
deck = shuffle_deck()



#get_hand

def get_cards(numCards=5):
    hand = []
    for i in range(numCards):
        hand.append(deck[0])
        deck.remove(deck[0])


    return hand


Player1_hand= get_cards(5)
Player2_hand= get_cards(5)


#create slots on which cards are drawn

class Slots:
    slots_list=[]
    def __init__(self, x, y, card=None):
        self.x= x
        self.y= y
        self.width= 66
        self.height= 100
        self.slots_list.append(self)
        self.card= card

    def click(self, pos):
        x1=pos[0]
        x2=pos[1]
        if x1 >= self.x and x1 <= self.x + self.width and x2 >= self.y and x2 <= self.y + self.height:
            
            return True

        else:
            return False

    def set_card(self, card):
        if self.card== None:
            self.card= card

#Player1
P1_slot_1= Slots(395, 660)
P1_slot_2= Slots(481, 660)
P1_slot_3= Slots(567, 660)
P1_slot_4= Slots(653, 660)
P1_slot_5= Slots(739, 660)

P1_slot_6= Slots(825, 660)
P1_slot_7= Slots(309, 660)
P1_slot_8= Slots(911, 660)
P1_slot_9= Slots(223, 660)
P1_slot_10= Slots(997, 660)
P1_slot_11=Slots(137, 660)

Player1_slots= Slots.slots_list[:11]
Player1_slots_coords= [(P1_slot_1.x, P1_slot_1.y), (P1_slot_2.x, P1_slot_2.y), (P1_slot_3.x, P1_slot_3.y), (P1_slot_4.x, P1_slot_4.y), (P1_slot_5.x, P1_slot_5.y), (P1_slot_6.x, P1_slot_6.y), (P1_slot_7.x, P1_slot_7.y), (P1_slot_8.x, P1_slot_8.y), (P1_slot_9.x, P1_slot_9.y), (P1_slot_10.x, P1_slot_10.y), (P1_slot_11.x, P1_slot_11.y)]


#Player2
P2_slot_1= Slots(395, 40)
P2_slot_2= Slots(481, 40)
P2_slot_3= Slots(567, 40)
P2_slot_4= Slots(653, 40)
P2_slot_5= Slots(739, 40)

P2_slot_6= Slots(825, 40)
P2_slot_7= Slots(309, 40)
P2_slot_8= Slots(911, 40)
P2_slot_9= Slots(223, 40)
P2_slot_10= Slots(997, 40)
P2_slot_11= Slots(137, 40)

Player2_slots= Slots.slots_list[11:]
Player2_slots_coords= [(P2_slot_1.x, P2_slot_1.y), (P2_slot_2.x, P2_slot_2.y), (P2_slot_3.x, P2_slot_3.y), (P2_slot_4.x, P2_slot_4.y), (P2_slot_5.x, P2_slot_5.y), (P2_slot_6.x, P2_slot_6.y), (P2_slot_7.x, P2_slot_7.y), (P2_slot_8.x, P2_slot_8.y), (P2_slot_9.x, P2_slot_9.y), (P2_slot_10.x, P2_slot_10.y), (P2_slot_11.x, P2_slot_11.y)]


#Gameslot

class Gameslot:
    def __init__(self, x, y, card):
        self.x= x
        self.y= y
        self.card=card

    def remove_card(self):
        deck.remove(self.card)



gameslot= Gameslot(567, 350, random.choice(deck))


gameslot.remove_card()


#draw all the cards

def draw_hand(hand, coords):

    win.blit(game_background, (0, 0))

    for i in range(len(hand)):
        win.blit(hand[i].image, coords[i])


    #win.blit(gameslot.card.image, (gameslot.x, gameslot.y))


# draw_card_button

class Button:
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y= y
        self.height= height
        self.width= width
        self.color= color

    def click(self, pos):
        x1 = pos[0]
        x2 = pos[1]
        if x1 >= self.x and x1 <= self.x + self.width and x2 >= self.y and x2 <= self.y + self.height:

            return True

        else:
            return False

    def draw(self, text=None, coords=None):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        win.blit(text, coords)

Draw_Button= Button(60, 367, 66, 100, brown)

Cannot_Play_Button=Button(60, 367 + 86, 66, 100, brown)

Winner_Button= Button(300, 300, 200, 600, brown)

Make_Wish_Button= Button(1040, 367, 66, 100, brown)


#assign images to slots

def assign_images_to_slots(hand, slots):

    for i in range(len(hand)):
        slots[i].card = hand[i]

    for slot in slots[len(hand): ]:
        slot.card= None

#special card 7 function

def seven(number_of_sevens, hand):
    for i in range(number_of_sevens):
        hand.append(deck[0])
        deck.remove(deck[0])
        hand.append(deck[0])
        deck.remove(deck[0])


def reset_variables():
    pass

"""Menu Screen
Draw a menu screen onto the surface
that has clickable options"""


menu_screen= True

while menu_screen:

    win.blit(menu_screen_background, (0,0))
    win.blit(Dame, (120, 100))
    win.blit(King, (900, 100))
    win.blit(Ass, (515, 110))
    win.blit(question_text, (417, 500))
    win.blit(option1_text, (578, 580))
    win.blit(option2_text, (572, 660))
    pygame.display.update()


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
           pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos= pygame.mouse.get_pos()
            if pos[0] >= 578 and pos[0] <= 578 + option1_Rect[2] and pos[1] >= 580 and pos[1]<= 580 + option1_Rect[3]:
                menu_screen = False

            if pos[0] >= 572 and pos[0] <= 572 + option2_Rect[2] and pos[1] >= 660 and pos[1] <= 660 + option2_Rect[3]:
                pygame.quit()



"""Main game loop, this is where we play"""


run= True

player1_turn= True
player2_turn= False
seven_count= 0

#all that happens when bube
mandatory_mode= None
make_wish_mode= False

#cards already drawn
player2_cards_drawn= 0
player1_cards_drawn= 0

while run:

    if player1_turn:

        assign_images_to_slots(Player1_hand, Player1_slots)
        draw_hand(Player1_hand, Player1_slots_coords)
        win.blit(player1_text, (550, 610))
        win.blit(gameslot.card.image, (gameslot.x, gameslot.y))
        Draw_Button.draw(button_text, (Draw_Button.x + 16, Draw_Button.y + 27))
        Cannot_Play_Button.draw(cant_play_text, (Cannot_Play_Button.x + Cannot_Play_Button.width / 2 - cant_play_text_Rect[2] / 2, Cannot_Play_Button.y + Cannot_Play_Button.height / 2 - cant_play_text_Rect[3] / 2))




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type== pygame.MOUSEBUTTONDOWN:
                pos= pygame.mouse.get_pos()
                for slot in Player1_slots[:len(Player1_hand)]:

                    if slot.click(pos):


                        
                        if slot.card.type == gameslot.card.type or slot.card.number == gameslot.card.number:
                            if slot.card.number == 7:
                                seven_count+= 1
                                if not any(card.number == 7 for card in Player2_hand):
                                    seven(seven_count, Player2_hand)
                                    seven_count= 0
                                    Player1_hand.remove(slot.card)
                                    gameslot.card = slot.card
                                    player1_cards_drawn = 0
                                    player1_turn = False
                                    player2_turn = True
                                    break
                                else:
                                    Player1_hand.remove(slot.card)
                                    gameslot.card = slot.card
                                    player1_cards_drawn = 0
                                    player1_turn = False
                                    player2_turn = True
                                    break


                            elif slot.card.number == 8 or slot.card.number == 14:
                                Player1_hand.remove(slot.card)
                                gameslot.card = slot.card
                                break


                            else:
                                Player1_hand.remove(slot.card)
                                gameslot.card = slot.card
                                player1_cards_drawn = 0
                                player1_turn = False
                                player2_turn = True
                                break



                if Draw_Button.click(pos) and player1_cards_drawn < 1:
                    player1_cards_drawn += 1
                    Player1_hand.append(deck[0])
                    deck.remove(deck[0])


                if Cannot_Play_Button.click(pos):

                    player1_cards_drawn= 0
                    player2_turn= True
                    player1_turn= False




    if player2_turn:
        assign_images_to_slots(Player2_hand, Player2_slots)
        draw_hand(Player2_hand, Player2_slots_coords)
        win.blit(player2_text, (550, 190))
        win.blit(gameslot.card.image, (gameslot.x, gameslot.y))
        Draw_Button.draw(button_text, (Draw_Button.x + 16, Draw_Button.y + 27))
        Cannot_Play_Button.draw(cant_play_text, (Cannot_Play_Button.x + Cannot_Play_Button.width / 2 - cant_play_text_Rect[2] / 2, Cannot_Play_Button.y + Cannot_Play_Button.height / 2 - cant_play_text_Rect[3] / 2))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type== pygame.MOUSEBUTTONDOWN and player2_turn:

                pos = pygame.mouse.get_pos()
                for slot in Player2_slots[:len(Player2_hand)]:

                    if slot.click(pos):

                        if slot.card.type == gameslot.card.type or slot.card.number == gameslot.card.number:
                            if slot.card.number == 7:
                                seven_count += 1
                                if not any(card.number == 7 for card in Player1_hand):
                                    seven(seven_count, Player1_hand)
                                    seven_count = 0
                                    Player2_hand.remove(slot.card)
                                    gameslot.card = slot.card
                                    player2_cards_drawn=0
                                    player1_turn = True
                                    player2_turn = False
                                    break

                                else:
                                    Player2_hand.remove(slot.card)
                                    gameslot.card = slot.card
                                    player2_cards_drawn = 0
                                    player1_turn = True
                                    player2_turn = False
                                    break

                            elif slot.card.number == 8 or slot.card.number == 14:
                                Player2_hand.remove(slot.card)
                                gameslot.card = slot.card
                                break

                            else:
                                Player2_hand.remove(slot.card)
                                gameslot.card = slot.card
                                player2_cards_drawn = 0
                                player1_turn = True
                                player2_turn = False
                                break





                if Draw_Button.click(pos) and player2_cards_drawn < 1:
                    player2_cards_drawn += 1

                    Player2_hand.append(deck[0])
                    deck.remove(deck[0])

                if Cannot_Play_Button.click(pos):
                    player2_cards_drawn = 0
                    player2_turn= False
                    player1_turn= True



    if len(Player2_hand) == 0 or len(Player1_hand) == 0:
        player2_turn= False
        player1_turn= False

        if len(Player2_hand) == 0:
            winner_button_text= font_winner_button_text.render("Player 2 is the winner!", True, black)
            win.blit(game_background, (0,0))
            Winner_Button.draw(winner_button_text, (Winner_Button.x + 160, Winner_Button.y + 94))
            pygame.display.update()

        if len(Player1_hand) == 0:
            winner_button_text = font_winner_button_text.render("Player 1 is the winner!", True, black)
            win.blit(game_background, (0, 0))
            Winner_Button.draw(winner_button_text, (Winner_Button.x + 160, Winner_Button.y + 94))
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False

    if len(deck) == 0:
        deck= Card.cards
        deck= shuffle_deck()
        deck= shuffle_deck()
        for card in Player1_hand:
            deck.remove(card)

        for card in Player2_hand:
            deck.remove(card)

    pygame.display.update()

pygame.quit()





