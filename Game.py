'''
Author: Selezar
15/1/17
Maplestory fighter game in the style of Mortal Combat
'''

import os, pygame
from pygame.locals import *
from HelperFunctions import *
from Characters.Selezar import *
from MousePointer import *
from Characters.PriestQB import *
from Characters.Keiji import *
from Characters.Oichi import *
from Characters.CharacterTemplate import *
from HealthBar import *
from DemonPowerUp import *
from Rasengan import *
from TimeCountdown import *
from Jobs.DualBlade import *
from Background import *


def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""

#Initialize Everything
    screen_width = 1700
    screen_height = 900
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Maple Combat')
    pygame.mouse.set_visible(0)

    pygame.key.set_repeat(10,10)

    print (pygame.key.get_repeat())

#Background variables
    # bg_Start_x = 0
    # bg_Start_Y = 0

#Create The Background
    # bg_image,bg_rect = load_image("b5.jpg", 'Backgrounds')
    # bg_rect.topleft = bg_Start_x, bg_Start_Y

#Display The Background
    # screen.fill((0,0,0))
    # screen.blit(bg_image, bg_rect)
    # pygame.display.flip()

#Sprite background
    bg = Background(0,0)



#Set game FPS
    FPS = 30

#Prepare Game Objects
    clock = pygame.time.Clock()
    jump_sound = load_sound('jump.wav' , 'Jump')
    #bgm = load_sound('Battle.wav', 'Backgrounds')
    #sword_sound = load_sound('sword.wav', 'UpperAttack')
    Running_sound = load_sound('Running.wav', 'Walk')
    Woman_Breath_sound = load_sound('WomanBreath.wav', 'Oichi')

    hand = Hand()

    #selezar = Selezar(1100,730)


    selezar = MapleChar(600, 785, 'Selezar')
    selezarP = SelezarPotrait(1440, 130)
    selezarlogo = SelezarLogo(1000,83)

    oichi = Oichi()
    oichiP = OichiPotrait(115,130)
    oichilogo = OichiLogo(515,86)
    
    right_hp_bar = Hp_Bar_Right(1000,100)
    left_hp_bar = Hp_Bar_Left(100,97)

    tleft = Time_Countdown_Left(816,130, FPS)
    tright = Time_Countdown_Right(850, 130, FPS)

    allsprites = pygame.sprite.LayeredUpdates((bg, selezar, hand, oichi,))
    #allsprites.add(selezarP)
    #allsprites.add(selezarlogo)
    #allsprites.add(right_hp_bar)
    #allsprites.add(oichiP)
    #allsprites.add(oichilogo)
    #allsprites.add(left_hp_bar)
    #allsprites.add(tleft)
    #allsprites.add(tright)

    
#Main Loop
    Left_Key_Bool = False
    Right_Key_Bool = False
    Jump_Left_History_Bool = False #This will be true if the last event was a jump left keydown
    Jump_Right_History_Bool = False #This will be true if the last event was a jump right keydown
    going = True
    
    #bgm.play()
    while going:

        Current_Side_Character_Is_Facing = selezar.Fetch_Current_Facing_Side()
        Current_User_Positions = selezar.Fetch_Current_Character_Position()

        clock.tick(FPS)
        Floor_Bool = selezar.Is_The_Character_On_Floor()

        #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False 

            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                going = False

        #-----------------------------USER KEYBOARD EVENTS-------------------#

        #-----------Navigation------------------------------#
            elif event.type==KEYDOWN and event.key==K_DOWN and Floor_Bool==True:
                Jump_Left_History_Bool = False
                Jump_Right_History_Bool = False
                selezar.Update_Animation('Crouch')
            elif event.type==KEYUP and event.key==K_DOWN:
                selezar.Reset_Y_Position_To_Base()
                selezar.Update_Animation('Idle')




            elif event.type==KEYDOWN and event.key==K_LEFT and Floor_Bool==True:
                '''GOING LEFT'''

                #print ('GOING LEFT')
                #pygame.key.set_repeat(1,1)

                #print (pygame.key.get_repeat())
                
                selezar.Is_Left_Button_Pressed('T')
                Jump_Left_History_Bool = False
                Jump_Right_History_Bool = False
                Left_Key_Bool = True
                selezar.Update_Animation_without_resetting_Count('Walk_Left')

                '''animate map going left if character is at left most edge'''
                if Current_User_Positions[0]<5:
                    bg.Update_Animation('Move_Right')
                    oichi.Change_Current_X_Position(12)

            elif event.type==KEYUP and event.key==K_LEFT:
                
                selezar.Is_Left_Button_Pressed('F')
                Left_Key_Bool = False

                bg.Update_Animation('Idle')

                jbool = selezar.Fetch_State_of_Jump_Button()

                if jbool:
                    '''this is so that when the person lets go of direction buttons mid air the char is smoothly let down'''
                    selezar.Update_Animation('PrematureJumpEndingLeft')
                else:
                    selezar.Update_Animation('Idle')






            elif event.type==KEYDOWN and event.key==K_RIGHT and Floor_Bool==True:
                '''GOING RIGHT'''
                #print ('GOING RIGHT')

              #  pygame.key.set_repeat(1,1)

               # print (pygame.key.get_repeat())
                
                selezar.Is_Right_Button_Pressed('T')
                Jump_Right_History_Bool = False
                Jump_Left_History_Bool = False
                Right_Key_Bool = True
                selezar.Update_Animation_without_resetting_Count('Walk_Right')

                '''animate map going left if character is at right most edge'''
                if Current_User_Positions[0]>(screen_width-60):
                    bg.Update_Animation('Move_Left')
                    oichi.Change_Current_X_Position(-12)


            elif event.type==KEYUP and event.key==K_RIGHT:

                selezar.Is_Right_Button_Pressed('F')
                Right_Key_Bool = False
                jbool = selezar.Fetch_State_of_Jump_Button()

                bg.Update_Animation('Idle')

                if jbool:
                    '''this is so that when the person lets go of direction buttons mid air the char is smoothly let down'''
                    selezar.Update_Animation('PrematureJumpEndingRight')
                else:
                    selezar.Update_Animation('Idle')

        #-----------Attack Section--------------------------#

            elif event.type==KEYDOWN and event.key==K_z and Floor_Bool==True:

                '''blade fury'''
                #sword_sound.play()
                Jump_Right_History_Bool = False
                Jump_Left_History_Bool = False
                selezar.Update_Animation('SpinAttack')
                Cur_POS = selezar.Fetch_Current_Character_Position()
                bfury = BladeFury(Cur_POS[0], Cur_POS[1])
                allsprites.add(bfury)

            elif event.type==KEYUP and event.key==K_z:

                #sword_sound.fadeout(5)
                allsprites.remove(bfury)
                selezar.Reset_Y_Position_To_Base()
                selezar.Update_Animation('Alert')

            elif event.type==KEYDOWN and event.key==K_LSHIFT and Floor_Bool==True:

                '''phantom blow'''
                #sword_sound.play()
                Jump_Right_History_Bool = False
                Jump_Left_History_Bool = False
                selezar.Update_Animation('SpinAttack')
                Cur_POS = selezar.Fetch_Current_Character_Position()
                pblow = PhantomBlow(Cur_POS[0], Cur_POS[1], Current_Side_Character_Is_Facing)
                allsprites.add(pblow)

            elif event.type==KEYUP and event.key==K_LSHIFT:

                #sword_sound.fadeout(5)
                allsprites.remove(pblow)
                selezar.Reset_Y_Position_To_Base()
                selezar.Update_Animation('Alert')

            elif event.type==KEYDOWN and event.key==K_b and Floor_Bool==True:

                '''spin attack'''
                #sword_sound.play()
                Jump_Right_History_Bool = False
                Jump_Left_History_Bool = False
                selezar.Update_Animation('SpinAttack')

            elif event.type==KEYUP and event.key==K_b:

                selezar.Reset_Y_Position_To_Base()
                selezar.Update_Animation('Alert')
        #-----------JUMP SECTION----------------------------#

            elif event.type==KEYDOWN and event.key==K_x and Left_Key_Bool==False and Right_Key_Bool==False and Floor_Bool==True:
                print ('jump straight up')
                Jump_Left_History_Bool = False
                Jump_Right_History_Bool = False
                selezar.Update_Animation_without_resetting_Count('JumpStraightUp')
                jump_sound.play()
            elif event.type==KEYUP and event.key==K_x and Jump_Left_History_Bool==False and Jump_Right_History_Bool==False:
                selezar.Update_Animation('PrematureJumpEnding')

            elif event.type==KEYDOWN and event.key==K_x and Left_Key_Bool==True and Floor_Bool==True:
                print ('jump left')
                selezar.Is_Jump_Button_Pressed('T')
                selezar.Update_Animation_without_resetting_Count('JumpLeft')
                Jump_Left_History_Bool = True
                jump_sound.play()
            elif event.type==KEYUP and event.key==K_x and Jump_Left_History_Bool==True:
                selezar.Is_Jump_Button_Pressed('F')
                selezar.Update_Animation('PrematureJumpEndingLeft')

            elif event.type==KEYDOWN and event.key==K_x and Right_Key_Bool==True and Floor_Bool==True:
                print ('jump right')
                selezar.Is_Jump_Button_Pressed('T')
                selezar.Update_Animation_without_resetting_Count('JumpRight')
                Jump_Right_History_Bool = True
                jump_sound.play()
            elif event.type==KEYUP and event.key==K_x and Jump_Right_History_Bool==True:
                selezar.Is_Jump_Button_Pressed('F')
                selezar.Update_Animation('PrematureJumpEndingRight')







        #------------Oichi-----------------------------------#
            elif event.type==KEYDOWN and event.key==K_p:
                Running_sound.play()
                Woman_Breath_sound.play()
                oichi.Update_Facing_Side('Left')
                oichi.Update_Animation('Walk')
            elif event.type==KEYUP and event.key==K_p:
                Running_sound.fadeout(10)
                Woman_Breath_sound.fadeout(10)
                oichi.Update_Animation('Idle')

            elif event.type==KEYDOWN and event.key==K_i:
                Running_sound.play()
                Woman_Breath_sound.play()
                oichi.Update_Facing_Side('Right')
                oichi.Update_Animation('Walk')
            elif event.type==KEYUP and event.key==K_i:
                Running_sound.fadeout(10)
                Woman_Breath_sound.fadeout(10)
                oichi.Update_Animation('Idle')

            elif event.type==KEYDOWN and event.key==K_9:
                Woman_Breath_sound.play()
                oichi.Update_Animation('JumpStraightUp')
            elif event.type==KEYUP and event.key==K_9:
                Woman_Breath_sound.fadeout(10)
                oichi.Update_Animation('Walk')


        # if pygame.sprite.collide_rect(selezar, oichi)==1:
        #     print ('COLLIDED')
        # else:
        #     print ('Not collided')

        allsprites.update()

        #Draw Everything
        #screen.blit(bg_image, bg_rect)
        allsprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

#Game Over



if __name__ == '__main__':
    main()
