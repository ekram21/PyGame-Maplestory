'''
Author: Selezar
15/1/17
Maplestory fighter game in the style of Mortal Combat
'''

import pygame
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

#Sprite background
    bg = Background(0,0)

#Set game FPS
    FPS = 30

#Prepare Game Objects
    clock = pygame.time.Clock()
    hand = Hand()

#walls
    wall_sprite_group = pygame.sprite.Group()
    my_wall1 = Collision_Line(200,830,2,20)
    my_wall2 = Collision_Line(900,830,2,20)
    my_wall3 = Collision_Line(1330,770,2,20)

    wall_sprite_group.add(my_wall1)
    wall_sprite_group.add(my_wall2)
    wall_sprite_group.add(my_wall3)

#platforms
    platform_sprite_group = pygame.sprite.OrderedUpdates()
    platform_ghost_line_sprite_group = pygame.sprite.OrderedUpdates()

    base_platform = Collision_Line(0, 865, 4000, 2)
    my_platform1 = Collision_Line(910, 800, 400, 2)
    my_platform2 = Collision_Line(1340, 750, 400, 2)
    
    base_platform_ghost = Collision_Line(0, 845, 4000, 2)
    my_platform1_ghost = Collision_Line(910,780,400,2)
    my_platform2_ghost = Collision_Line(1340, 730, 400, 2)

    platform_sprite_group.add(base_platform)
    platform_sprite_group.add(my_platform1)
    platform_sprite_group.add(my_platform2)

    platform_ghost_line_sprite_group.add(base_platform_ghost)
    platform_ghost_line_sprite_group.add(my_platform1_ghost)
    platform_ghost_line_sprite_group.add(my_platform2_ghost)

#player declarations
    Player = MapleChar(600, 825, 'Selezar')
    oichi = Oichi()

#Adding to super group which will handle drawing

    allsprites = pygame.sprite.LayeredUpdates((bg, Player, hand, oichi, wall_sprite_group, platform_sprite_group, platform_ghost_line_sprite_group))

    
#Main Loop
    Left_Key_Bool = False
    Right_Key_Bool = False
    Jump_Left_History_Bool = False #This will be true if the last event was a jump left keydown
    Jump_Right_History_Bool = False #This will be true if the last event was a jump right keydown
    going = True
    
    #bgm.play()
    while going:

        Current_Side_Character_Is_Facing = Player.Fetch_Current_Facing_Side()
        Current_Player_Positions = Player.Fetch_Current_Character_Position()

        clock.tick(FPS)
        Floor_Bool = Player.Is_The_Character_On_Floor()

        #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False 

            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                going = False

        #------------Player KEYBOARD EVENTS-------------------#

        #-----------Navigation------------------------------#
            elif event.type==KEYDOWN and event.key==K_DOWN and Floor_Bool==True:
                Jump_Left_History_Bool = False
                Jump_Right_History_Bool = False
                Player.Update_Animation('Crouch')
            elif event.type==KEYUP and event.key==K_DOWN:
                Player.Reset_Y_Position_To_Base()
                Player.Update_Animation('Idle')


            elif event.type==KEYDOWN and event.key==K_LEFT and Floor_Bool==True:
                '''GOING LEFT'''
                
                Player.Is_Left_Button_Pressed('T')
                Jump_Left_History_Bool = False
                Jump_Right_History_Bool = False
                Left_Key_Bool = True

                Player.Update_Animation_without_resetting_Count('Walk_Left')


            elif event.type==KEYUP and event.key==K_LEFT:
                
                Player.Is_Left_Button_Pressed('F')
                Left_Key_Bool = False

                #bg.Update_Animation('Idle')

                jbool = Player.Fetch_State_of_Jump_Button()

                if jbool==True:
                    '''this is so that when the person lets go of direction buttons mid air the char is smoothly let down'''
                    Player.Update_Animation('PrematureJumpEndingLeft')
                elif jbool==False and Left_Key_Bool==False and Floor_Bool==True:
                    '''when direction button is stopped being pressed character will stand in idle'''
                    Player.Update_Animation('Idle')




            elif event.type==KEYDOWN and event.key==K_RIGHT and Floor_Bool==True:
                '''GOING RIGHT'''
                #print ('GOING RIGHT')

              #  pygame.key.set_repeat(1,1)

               # print (pygame.key.get_repeat())
                
                Player.Is_Right_Button_Pressed('T')
                Jump_Right_History_Bool = False
                Jump_Left_History_Bool = False
                Right_Key_Bool = True
                Player.Update_Animation_without_resetting_Count('Walk_Right')

                '''animate map going left if character is at right most edge'''
                if Current_Player_Positions[0]>(screen_width-60):
                    bg.Update_Animation('Move_Left')
                    oichi.Change_Current_X_Position(-12)


            elif event.type==KEYUP and event.key==K_RIGHT:

                Player.Is_Right_Button_Pressed('F')
                Right_Key_Bool = False
                jbool = Player.Fetch_State_of_Jump_Button()

                bg.Update_Animation('Idle')

                if jbool==True:
                    '''this is so that when the person lets go of direction buttons mid air the char is smoothly let down'''
                    Player.Update_Animation('PrematureJumpEndingRight')
                elif jbool==False and Right_Key_Bool==False and Floor_Bool==True:
                    '''when direction button is stopped being pressed character will stand in idle'''
                    Player.Update_Animation('Idle')

        #-----------Attack Section--------------------------#

            elif event.type==KEYDOWN and event.key==K_z and Floor_Bool==True:

                '''blade fury'''
                #sword_sound.play()
                Jump_Right_History_Bool = False
                Jump_Left_History_Bool = False
                Player.Update_Animation('SpinAttack')
                Cur_POS = Player.Fetch_Current_Character_Position()
                bfury = BladeFury(Cur_POS[0], Cur_POS[1])
                allsprites.add(bfury)

            elif event.type==KEYUP and event.key==K_z:

                #sword_sound.fadeout(5)
                allsprites.remove(bfury)
                Player.Reset_Y_Position_To_Base()
                Player.Update_Animation('Alert')

            elif event.type==KEYDOWN and event.key==K_LSHIFT and Floor_Bool==True:

                '''phantom blow'''
                #sword_sound.play()
                Jump_Right_History_Bool = False
                Jump_Left_History_Bool = False
                Player.Update_Animation('SpinAttack')
                Cur_POS = Player.Fetch_Current_Character_Position()
                pblow = PhantomBlow(Cur_POS[0], Cur_POS[1], Current_Side_Character_Is_Facing)
                allsprites.add(pblow)

            elif event.type==KEYUP and event.key==K_LSHIFT:

                #sword_sound.fadeout(5)
                allsprites.remove(pblow)
                Player.Reset_Y_Position_To_Base()
                Player.Update_Animation('Alert')

            elif event.type==KEYDOWN and event.key==K_b and Floor_Bool==True:

                '''spin attack'''
                #sword_sound.play()
                Jump_Right_History_Bool = False
                Jump_Left_History_Bool = False
                Player.Update_Animation('SpinAttack')

            elif event.type==KEYUP and event.key==K_b:

                Player.Reset_Y_Position_To_Base()
                Player.Update_Animation('Alert')

        #-----------JUMP SECTION----------------------------#

            elif event.type==KEYDOWN and event.key==K_x and Left_Key_Bool==False and Right_Key_Bool==False and Floor_Bool==True:
                print ('jump straight up')
                Jump_Left_History_Bool = False
                Jump_Right_History_Bool = False
                Player.Update_Animation_without_resetting_Count('JumpStraightUp')
                #jump_sound.play()
            elif event.type==KEYUP and event.key==K_x and Jump_Left_History_Bool==False and Jump_Right_History_Bool==False:
                Player.Update_Animation('PrematureJumpEnding')

            elif event.type==KEYDOWN and event.key==K_x and Left_Key_Bool==True and Floor_Bool==True:
                print ('jump left')
                Player.Is_Jump_Button_Pressed('T')
                Player.Update_Animation_without_resetting_Count('JumpLeft')
                Jump_Left_History_Bool = True
                #jump_sound.play()
            elif event.type==KEYUP and event.key==K_x and Jump_Left_History_Bool==True:
                Player.Is_Jump_Button_Pressed('F')
                Player.Update_Animation('PrematureJumpEndingLeft')

            elif event.type==KEYDOWN and event.key==K_x and Right_Key_Bool==True and Floor_Bool==True:
                print ('jump right')
                Player.Is_Jump_Button_Pressed('T')
                Player.Update_Animation_without_resetting_Count('JumpRight')
                Jump_Right_History_Bool = True
                #jump_sound.play()
            elif event.type==KEYUP and event.key==K_x and Jump_Right_History_Bool==True:
                Player.Is_Jump_Button_Pressed('F')
                Player.Update_Animation('PrematureJumpEndingRight')



        #------------Oichi-----------------------------------#
            elif event.type==KEYDOWN and event.key==K_p:
                oichi.Update_Facing_Side('Left')
                oichi.Update_Animation('Walk')
            elif event.type==KEYUP and event.key==K_p:
                oichi.Update_Animation('Idle')

            elif event.type==KEYDOWN and event.key==K_i:
                oichi.Update_Facing_Side('Right')
                oichi.Update_Animation('Walk')
            elif event.type==KEYUP and event.key==K_i:
                oichi.Update_Animation('Idle')

            elif event.type==KEYDOWN and event.key==K_9:
                oichi.Update_Animation('JumpStraightUp')
            elif event.type==KEYUP and event.key==K_9:
                oichi.Update_Animation('Walk')

        allsprites.remove(Player)
        Player.update(wall_sprite_group, platform_sprite_group, platform_ghost_line_sprite_group)
        allsprites.update()
        allsprites.add(Player)
        allsprites.move_to_back(Player)
        allsprites.move_to_back(bg)

        #Draw Everything

        allsprites.draw(screen)
        pygame.display.flip()

    pygame.quit()




if __name__ == '__main__':
    main()
