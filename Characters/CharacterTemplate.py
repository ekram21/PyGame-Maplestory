'''
Author: Selezar
MapleChar character animation and main class

TODO: FIX OFFSETS ON PHANTOM BLOW 
'''

import pygame
from HelperFunctions import *
import random


class MapleChar(pygame.sprite.Sprite):
    '''
    MapleChars character model and all animations and logic
    '''

    def __init__(self, Start_X, Start_Y, name):

    #All beginning inits
        self.name = name

        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_sprite_image('stand1_0.png', 'MapleSprites', self.name, 'blink', 'frame 0')

        self.Base_X_Poistion = Start_X
        self.Base_Y_position = Start_Y

        self.Current_X_position = Start_X
        self.Current_Y_position = Start_Y

        self.Distance_Above_Ground = abs(self.Current_Y_position-self.Base_Y_position)

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = self.Current_X_position, self.Current_Y_position

        self.Current_Animation = 'Idle'

        self.Current_Faced_Side = 'Left'

        self.Jump_Bool = False

        #Button pressed booleans
        self.Is_Jump_Button_Pressed_Bool = False
        self.Is_Right_Button_Pressed_Bool = False
        self.Is_Left_Button_Pressed_Bool = False

        self.count = 1

        self.JumpCount = None
        self.steps_above_ground = None

        self.jump_sound = load_sound('jump.wav' , 'Jump')
        self.sword_sound = load_sound('sword.wav', 'UpperAttack')

        self.Bool_Check_If_Under_base = self.Base_Y_position-self.Current_Y_position

    #Blink cache

        '''blinking stuff'''
        self.Blink_list = []
        FileName = 'stand1_0.png'
        self.Blink_list.append(load_sprite_image(FileName, 'MapleSprites', self.name, 'blink', 'frame 1'))
        self.Blink_list.append(load_sprite_image(FileName, 'MapleSprites', self.name, 'blink', 'frame 2'))

    #Jump cache

        '''jumping cache'''
        self.jump_cache_list = []
        FileName = 'jump_0.png'
        for i in range(0,16):
            self.jump_cache_list.append(load_sprite_image(FileName, 'MapleSprites', self.name, 'blink', 'frame 0'))

    #INDEPENDANT FPS
        '''independant fps stuff'''
        self.Checking_List_Idle = [] #everytime the image is read this will be filled up with it ,needed for independant fps scaler of animations
        self.Idle_Scalar = 5           #repeat each image frae by the int set here

        self.Checking_List_Walk = []
        self.Walk_Scalar = 2

        self.Checking_List_UpperStab1 = []
        self.UpperStab1_Scaler = 8

        self.Checking_List_UpperStab2 = []
        self.UpperStab2_Scaler = 8

        self.Checking_List_Alert = []
        self.Alert_Scalar = 7

        self.Checking_List_SpinAttack = []
        self.SpinAttack_Scaler = 5

    #Specific count stuff
        '''specific counts for specific animations'''
        self.AlertCount = 0

    #Jump gravity and strength stuff
        '''jump gravity stuff'''
        self.Jump_Gravity = 14          #the gravity
        self.JumpFactor = 10            #How high the jump is
        self.Jump_x_translation = 9    #how much left and right the jump moves the character

        self.e = 0
        self.k = (self.Jump_Gravity/2)+1

        self.a = (self.Jump_Gravity/2)
        self.b = self.Jump_Gravity+1

        

    def update(self):
        '''call the frames of each chosen animation one after another here'''
        
        if self.Current_Animation=='Idle':

            self.Jump_Bool = False

            self.Checking_List_Idle.append(self.count)

            FileName =  'stand1_' + str(self.count) + '.png'
            self.image, self.rect = load_sprite_image(FileName, 'MapleSprites', self.name, 'blink', 'frame 0')

            #Flip the image depending on which side char is facing
            if self.Current_Faced_Side=='Right':
                self.image = pygame.transform.flip(self.image, 1, 0)

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()
            self.rect.topleft = self.Current_X_position, self.Current_Y_position

            if len(self.Checking_List_Idle)==self.Idle_Scalar:
                '''independant fps setter'''
                self.count+=1
                self.Checking_List_Idle = []
            else:
                self.count+=0

            if self.count==5:
                self.count=1
                if random.randint(1,11)==10:
                    '''this will randomly make the character blink once with probability of 1/11'''
                    self.count=0
                    self.Current_Animation = 'StandingBlink'

        elif self.Current_Animation=='StandingBlink':

            self.Jump_Bool = False

            self.Checking_List_Idle.append(self.count)

            self.image, self.rect = self.Blink_list[self.count]

            #Flip the image depending on which side char is facing
            if self.Current_Faced_Side=='Right':
                self.image = pygame.transform.flip(self.image, 1, 0)

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()
            self.rect.topleft = self.Current_X_position, self.Current_Y_position

            if len(self.Checking_List_Idle)==self.Idle_Scalar:
                '''independant fps setter'''
                self.count+=1
                self.Checking_List_Idle = []
            else:
                self.count+=0

            if self.count==2:
                self.count=1
                self.Current_Animation='Idle'

        elif self.Current_Animation=='Walk_Right':

            if self.count==4:
                self.count = 0

            self.Jump_Bool = False

            self.Checking_List_Walk.append(self.count)

            self.Current_X_position+=12 
            FileName = 'walk1_' + str(self.count) + '.png'
            self.image, self.rect = load_sprite_image(FileName, 'MapleSprites', self.name, 'blink', 'frame 0')

            #Need to flip the left walking images
            self.image = pygame.transform.flip(self.image, 1, 0)

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()

            if self.Current_X_position<1650:
                '''checking to see that the character is on the far right'''
                self.rect = self.Current_X_position, self.Current_Y_position
            else:
                self.Current_X_position = 1650
                self.rect = self.Current_X_position, self.Current_Y_position

            if len(self.Checking_List_Walk)==self.Walk_Scalar:
                self.count+=1
                self.Checking_List_Walk = []
            else:
                self.count+=0

            self.Current_Faced_Side = 'Right'

            if self.count==4:
                self.count=0

        elif self.Current_Animation=='Walk_Left':

            if self.count==4:
                self.count = 0

            self.Jump_Bool = False

            self.Checking_List_Walk.append(self.count)

            self.Current_X_position+=-12 
            FileName = 'walk1_' + str(self.count) + '.png'
            self.image, self.rect = load_sprite_image(FileName, 'MapleSprites', self.name, 'blink', 'frame 0')

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()

            if self.Current_X_position>-70:
                '''checking to see that the character is on the far left'''
                self.rect = self.Current_X_position, self.Current_Y_position
            else:
                self.Current_X_position = -70
                self.rect = self.Current_X_position, self.Current_Y_position

            if len(self.Checking_List_Walk)==self.Walk_Scalar:
                self.count+=1
                self.Checking_List_Walk = []
            else:
                self.count+=0

            self.Current_Faced_Side = 'Left'

            if self.count==4:
                self.count=0

        elif self.Current_Animation=='Crouch':

            self.Jump_Bool = False

            self.Current_Y_position = self.Base_Y_position
            self.Current_Y_position+=26

            FileName =  'prone_' + str(self.count) + '.png'
            self.image, self.rect = load_sprite_image(FileName, 'MapleSprites', self.name, 'blink', 'frame 0')

            if self.Current_Faced_Side=='Right':
                '''x must be offset by a bit'''
                self.image = pygame.transform.flip(self.image, 1, 0)

                self.Current_X_position+=7

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()
                self.rect.topleft = self.Current_X_position, self.Current_Y_position

                self.Current_X_position+=-7

            elif self.Current_Faced_Side=='Left':
                '''x must be offset by a bit'''
                self.Current_X_position+=-20

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()
                self.rect.topleft = self.Current_X_position, self.Current_Y_position

                self.Current_X_position+=20

        elif self.Current_Animation=='UpperStab1':

            self.Jump_Bool = False

            self.Checking_List_UpperStab1.append(self.count)

            '''fixing y offset'''
            self.Current_Y_position = self.Base_Y_position

            if (self.count%2 == 0):
                self.Current_Y_position+=6

            FileName =  'stabO1_' + str(self.count) + '.png'
            self.image, self.rect = load_sprite_image(FileName, 'MapleSprites', self.name, 'blink', 'frame 0')

            if self.Current_Faced_Side=='Right':
                self.image = pygame.transform.flip(self.image, 1, 0)
                self.rect.topleft = self.Current_X_position, self.Current_Y_position
            else:
                self.Current_X_position+=-6
                self.rect.topleft = self.Current_X_position, self.Current_Y_position
                self.Current_X_position+=6
            

            if len(self.Checking_List_UpperStab1)==self.UpperStab1_Scaler:
                self.count+=1
                self.Checking_List_UpperStab1 = []
            else:
                self.count+=0

            if self.count==2:
                self.count=0
                self.Current_Animation = 'UpperStab2'
                #self.sword_sound.play()

        elif self.Current_Animation=='UpperStab2':

            self.Jump_Bool = False

            self.Checking_List_UpperStab2.append(self.count)

            '''fixing y offset'''
            self.Current_Y_position = self.Base_Y_position

            if (self.count%2 == 0):
                self.Current_Y_position+=6

            FileName =  'stabO2_' + str(self.count) + '.png'
            self.image, self.rect = load_sprite_image(FileName, 'MapleSprites', self.name, 'blink', 'frame 0')

            if self.Current_Faced_Side=='Right':
                self.image = pygame.transform.flip(self.image, 1, 0)
                self.rect.topleft = self.Current_X_position, self.Current_Y_position
            else:
                self.Current_X_position+=-6
                self.rect.topleft = self.Current_X_position, self.Current_Y_position
                self.Current_X_position+=6

            if len(self.Checking_List_UpperStab2)==self.UpperStab2_Scaler:
                self.count+=1
                self.Checking_List_UpperStab2 = []
            else:
                self.count+=0

            if self.count==2:
                self.count=0
                self.Current_Animation = 'UpperStab1'
                #self.sword_sound.play()

        elif self.Current_Animation=='SpinAttack':

            self.Jump_Bool = False

            self.Checking_List_SpinAttack.append(self.count)

            '''fixing y offset'''
            self.Current_Y_position = self.Base_Y_position
            self.Current_Y_position+=3

            FileName =  'swingO3_' + str(self.count) + '.png'
            self.image, self.rect = load_sprite_image(FileName, 'MapleSprites', self.name, 'blink', 'frame 0')

            if self.Current_Faced_Side=='Right':
                self.image = pygame.transform.flip(self.image, 1, 0)
                self.rect.topleft = self.Current_X_position, self.Current_Y_position
            else:
                self.Current_X_position+=-26
                self.Current_Y_position+=1
                self.rect.topleft = self.Current_X_position, self.Current_Y_position
                self.Current_X_position+=26
                self.Current_Y_position+=-1

            if len(self.Checking_List_SpinAttack)==self.SpinAttack_Scaler:
                self.count+=1
                self.Checking_List_SpinAttack = []
            else:
                self.count+=0

            if self.count==3:
                self.count=0

        elif self.Current_Animation=='JumpStraightUp':

            self.Jump_Bool = True

            if self.count>self.e and self.count<self.k:
                self.Current_Y_position+=-self.JumpFactor

            elif self.count>self.a and self.count<self.b:
                self.Current_Y_position+=self.JumpFactor

            self.image, self.rect = self.jump_cache_list[1]

            if self.Current_Faced_Side=='Right':

                self.image = pygame.transform.flip(self.image, 1, 0)

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()
                self.rect.topleft = self.Current_X_position, self.Current_Y_position

                self.count+=1

                self.JumpCount = self.count

                if self.count>self.Jump_Gravity:
                    self.count=1
                    self.Reset_Y_Position_To_Base()
                    self.jump_sound.play()

            elif self.Current_Faced_Side=='Left':

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()
                self.rect.topleft = self.Current_X_position, self.Current_Y_position

                self.count+=1

                self.JumpCount = self.count

                if self.count>self.Jump_Gravity:
                    self.count=1
                    self.Reset_Y_Position_To_Base()
                    self.jump_sound.play()
                    
        elif self.Current_Animation=='PrematureJumpEnding':
            '''
            this section is to animate when the sprite does not jump or carry out full animation
            so it needs to still be animated falling down the number of steps it jumped up. At 
            the end this function will call the idle animation     
            '''
            #find out how many steps the sprite was pushed above ground
            if self.Jump_Bool==True:
                if self.JumpCount>self.e and self.JumpCount<self.k:
                    self.steps_above_ground = self.JumpCount-1
                elif self.JumpCount>self.a and self.JumpCount<self.b:
                    self.steps_above_ground = self.b-self.JumpCount
            
            if self.steps_above_ground!=0 and self.steps_above_ground!=None:

                self.Jump_Bool=False

                self.Current_Y_position+=self.JumpFactor

                self.image, self.rect = self.jump_cache_list[1]

                #Flip the image depending on which side char is facing
                if self.Current_Faced_Side=='Right':
                    self.image = pygame.transform.flip(self.image, 1, 0)

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()
                self.rect.topleft = self.Current_X_position, self.Current_Y_position


            self.Distance_Above_Ground = abs(self.Current_Y_position-self.Base_Y_position)
            print ('Distance above ground: '+str(self.Distance_Above_Ground))
            self.steps_above_ground = self.Distance_Above_Ground/self.JumpFactor

            self.Bool_Check_If_Under_base = self.Base_Y_position-self.Current_Y_position

            try:
                if round(self.steps_above_ground)==0 or self.Bool_Check_If_Under_base<0:
                    self.Reset_Y_Position_To_Base()
                    self.Current_Animation = 'Idle'
            except:
                pass
                self.Reset_Y_Position_To_Base()
                self.Current_Animation = 'Idle'
            
        elif self.Current_Animation=='JumpLeft':

            self.Jump_Bool = True

            if self.count>self.e and self.count<self.k:
                self.Current_Y_position+=-self.JumpFactor
                self.Current_X_position+=-self.Jump_x_translation

            elif self.count>self.a and self.count<self.b:
                self.Current_Y_position+=self.JumpFactor
                self.Current_X_position+=-self.Jump_x_translation

            self.image, self.rect = self.jump_cache_list[1]

            if self.Current_Faced_Side=='Right':

                self.image = pygame.transform.flip(self.image, 1, 0)

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()

                if self.Current_X_position>-70:
                    '''these will stop the character from jumping off of 70 pixels left'''
                    self.rect = self.Current_X_position, self.Current_Y_position
                else:
                    self.Current_X_position = -70
                    self.rect = self.Current_X_position, self.Current_Y_position

                self.count+=1

                self.JumpCount = self.count

                if self.count>self.Jump_Gravity:
                    self.count=1
                    self.Reset_Y_Position_To_Base()
                    self.jump_sound.play()

            elif self.Current_Faced_Side=='Left':

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()

                if self.Current_X_position>-70:         
                    '''these will stop the character from jumping off of 70 pixels left'''
                    self.rect = self.Current_X_position, self.Current_Y_position
                else:
                    self.Current_X_position = -70
                    self.rect = self.Current_X_position, self.Current_Y_position

                self.count+=1

                self.JumpCount = self.count

                if self.count>self.Jump_Gravity:
                    self.count=1
                    self.Reset_Y_Position_To_Base()
                    print ('reset to base on jump left func')
                    self.jump_sound.play()

        elif self.Current_Animation=='PrematureJumpEndingLeft':
            '''
            this section is to animate when the sprite does not jump or carry out full animation
            so it needs to still be animated falling down the number of stteps it jumped up. At 
            the end this function will call the idle animation     
            '''
            #find out how many steps the sprite was pushed above ground

            if self.Jump_Bool==True:

                if self.JumpCount>0 and self.JumpCount<9:
                    self.steps_above_ground = self.JumpCount-1
                elif self.JumpCount>8 and self.JumpCount<17:
                    self.steps_above_ground = self.b-self.JumpCount

            if self.steps_above_ground!=0 and self.steps_above_ground!=None:

                self.Jump_Bool=False

                self.Current_Y_position+=self.JumpFactor
                self.Current_X_position+=-self.Jump_x_translation

                self.image, self.rect = self.jump_cache_list[1]

                #Flip the image depending on which side char is facing
                if self.Current_Faced_Side=='Right':
                    self.image = pygame.transform.flip(self.image, 1, 0)

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()
                self.rect.topleft = self.Current_X_position, self.Current_Y_position

                self.Distance_Above_Ground = abs(self.Current_Y_position-self.Base_Y_position)
                print ('Distance above ground: '+str(self.Distance_Above_Ground))
                self.steps_above_ground = self.Distance_Above_Ground/self.JumpFactor

                self.Bool_Check_If_Under_base = self.Base_Y_position-self.Current_Y_position


            try:
                if round(self.steps_above_ground)==0 or self.Bool_Check_If_Under_base<0:

                    self.Reset_Y_Position_To_Base()

                    if self.Is_Left_Button_Pressed_Bool:
                        self.Current_Animation = 'Walk_Left'
                    else:
                        self.Current_Animation = 'Idle'
            except:
                pass
                self.Reset_Y_Position_To_Base()

                if self.Is_Left_Button_Pressed_Bool:
                    self.Current_Animation = 'Walk_Left'
                else:
                    self.Current_Animation = 'Idle' 

        elif self.Current_Animation=='JumpRight':

            self.Jump_Bool = True

            if self.count>self.e and self.count<self.k:
                self.Current_Y_position+=-self.JumpFactor
                self.Current_X_position+=self.Jump_x_translation

            elif self.count>self.a and self.count<self.b:
                self.Current_Y_position+=self.JumpFactor
                self.Current_X_position+=self.Jump_x_translation

            self.image, self.rect = self.jump_cache_list[1]

            if self.Current_Faced_Side=='Right':

                self.image = pygame.transform.flip(self.image, 1, 0)

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()

                if self.Current_X_position<1650:
                    '''making sure character desnt jump off screen to the right'''
                    self.rect = self.Current_X_position, self.Current_Y_position
                else:
                    self.Current_X_position = 1650
                    self.rect = self.Current_X_position, self.Current_Y_position

                self.count+=1

                self.JumpCount = self.count

                if self.count>self.Jump_Gravity:
                    self.count=1
                    self.Reset_Y_Position_To_Base()
                    self.jump_sound.play()

            elif self.Current_Faced_Side=='Left':

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()

                if self.Current_X_position<1650:
                    '''making sure character desnt jump off screen to the right'''
                    self.rect = self.Current_X_position, self.Current_Y_position
                else:
                    self.Current_X_position = 1650
                    self.rect = self.Current_X_position, self.Current_Y_position

                self.count+=1

                self.JumpCount = self.count

                if self.count>self.Jump_Gravity:
                    self.count=1
                    self.Reset_Y_Position_To_Base()
                    self.jump_sound.play()

        elif self.Current_Animation=='PrematureJumpEndingRight':
            '''
            this section is to animate when the sprite does not jump or carry out full animation
            so it needs to still be animated falling down the number of stteps it jumped up. At 
            the end this function will call the idle animation     
            '''
            #find out how many steps the sprite was pushed above ground
            if self.Jump_Bool==True:
                if self.JumpCount>self.e and self.JumpCount<self.k:
                    self.steps_above_ground = self.JumpCount-1
                elif self.JumpCount>self.a and self.JumpCount<self.b:
                    self.steps_above_ground = self.b-self.JumpCount
            
            if self.steps_above_ground!=0 and self.steps_above_ground!=None:

                self.Jump_Bool=False

                self.Current_Y_position+=self.JumpFactor
                self.Current_X_position+=self.Jump_x_translation

                self.image, self.rect = self.jump_cache_list[1]

                #Flip the image depending on which side char is facing
                if self.Current_Faced_Side=='Right':
                    self.image = pygame.transform.flip(self.image, 1, 0)

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()
                self.rect.topleft = self.Current_X_position, self.Current_Y_position

                self.Distance_Above_Ground = abs(self.Current_Y_position-self.Base_Y_position)
                print ('Distance above ground: '+str(self.Distance_Above_Ground))
                self.steps_above_ground = self.Distance_Above_Ground/self.JumpFactor

                self.Bool_Check_If_Under_base = self.Base_Y_position-self.Current_Y_position

            try:
                if round(self.steps_above_ground)==0 or self.Bool_Check_If_Under_base<0:

                    self.Reset_Y_Position_To_Base()

                    if self.Is_Right_Button_Pressed_Bool:
                        self.Current_Animation = 'Walk_Right'
                    else:
                        self.Current_Animation = 'Idle'
            except:
                pass
                self.Reset_Y_Position_To_Base()

                if self.Is_Right_Button_Pressed_Bool:
                    self.Current_Animation = 'Walk_Right'
                else:
                    self.Current_Animation = 'Idle'

        elif self.Current_Animation=='Alert':

            self.Jump_Bool = False

            self.Checking_List_Alert.append(self.count)

            FileName =  'alert_' + str(self.count) + '.png'
            self.image, self.rect = load_sprite_image(FileName, 'MapleSprites', self.name, 'blink', 'frame 0')

            #Flip the image depending on which side char is facing
            if self.Current_Faced_Side=='Right':
                self.image = pygame.transform.flip(self.image, 1, 0)

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()
            self.rect.topleft = self.Current_X_position, self.Current_Y_position

            if len(self.Checking_List_Alert)==self.Alert_Scalar:
                '''independant fps setter'''
                self.count+=1
                self.Checking_List_Alert = []
            else:
                self.count+=0

            if self.count==5:
                self.AlertCount+=1
                self.count=0
                '''we want to repeat this sequence of animation 3 times then go to idle state'''
                if self.AlertCount==3:
                    self.AlertCount = 0
                    self.Current_Animation = 'Idle'
                else:
                    self.Current_Animation = 'Alert'



    def Update_Animation(self, anim):
        '''this function can ba called from outide to change the current animation sequence'''

        self.count = 0
        self.Current_Animation = anim

    def Update_Animation_without_resetting_Count(self, anim):
        '''similar to update_animation but does not reset count. used for animations like walking'''

        self.Current_Animation = anim

    def Reset_Y_Position_To_Base(self):
        '''this function when called will reset the y position of the character to base 730'''

        self.Current_Y_position = self.Base_Y_position

    def Is_The_Character_On_Floor(self):
        '''returns a true or false depending on wether the character is touching the floor or not'''
        self.Distance_Above_Ground = abs(self.Current_Y_position-self.Base_Y_position)

        if self.Distance_Above_Ground==0:
            return True
        else:
            return False

    def Is_Jump_Button_Pressed(self, w):
        '''boolean function which can be called from outside to tell the class wether the jump button is pressed or not'''

        if w=='T':
            self.Is_Jump_Button_Pressed_Bool = True
        elif w=='F':
            self.Is_Jump_Button_Pressed_Bool = False

    def Is_Left_Button_Pressed(self, w):
        '''boolean function which can be called from outside to tell the class wether the left button is pressed or not'''
        if w=='T':
            self.Is_Left_Button_Pressed_Bool = True
        elif w=='F':
            self.Is_Left_Button_Pressed_Bool = False

    def Is_Right_Button_Pressed(self, w):
        '''boolean function which can be called from outside to tell the class wether the right button is pressed or not'''
        if w=='T':
            self.Is_Right_Button_Pressed_Bool = True
        elif w=='F':
            self.Is_Right_Button_Pressed_Bool = False

    def Fetch_Current_Character_Position(self):
        '''returns the current x and y co ordinate of the character'''

        return self.Current_X_position,self.Current_Y_position

    def Fetch_Current_Facing_Side(self):
        '''returns the side the character is facing now'''

        return self.Current_Faced_Side

    def Fetch_State_of_Jump_Button(self):
        '''returns bool whether the jump button is pressed or not'''
        return self.Is_Jump_Button_Pressed

class SelezarPotrait(pygame.sprite.Sprite):
    """generates a potrait of Selezar"""

    def __init__(self, Start_X, Start_Y):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_image('SelezarPotrait2.png', 'Idle')
        #self.image.set_colorkey((163,130,251))
        self.image.set_colorkey((63,72,204))
        scale = 0.7
        w,h = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(w*scale), int(h*scale)))

        self.Current_X_position = Start_X
        self.Current_Y_position = Start_Y

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.rect.topleft = self.Current_X_position, self.Current_Y_position

    def update(self):

        return None

class SelezarLogo(pygame.sprite.Sprite):
    """generates a logo text of Selezar"""

    def __init__(self, Start_X, Start_Y):
        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_image('SelezarLogo.png', 'Idle')
        self.image.set_colorkey((0,0,0))

        self.Current_X_position = Start_X
        self.Current_Y_position = Start_Y

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

        self.rect.topleft = self.Current_X_position, self.Current_Y_position

    def update(self):

        return None