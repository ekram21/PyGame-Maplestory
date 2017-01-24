'''
Selezar character animation and main class
'''

import pygame
from HelperFunctions import *


class Selezar(pygame.sprite.Sprite):
    '''
    Selezars character model and all animations and logic
    '''

    def __init__(self, Start_X, Start_Y):

        pygame.sprite.Sprite.__init__(self) #call Sprite intializer

        self.image, self.rect = load_image('1idleN.png', 'Idle')

        self.Base_X_Poistion = 1100
        self.Base_Y_position = 730

        self.Current_X_position = Start_X
        self.Current_Y_position = Start_Y

        self.Distance_Above_Ground = abs(self.Current_Y_position-self.Base_Y_position)

        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = self.Current_X_position, self.Current_Y_position

        self.Current_Animation = 'Idle'

        self.Current_Faced_Side = 'Left'

        self.Jump_Bo9ol = False

        #Button pressed booleans
        self.Is_Jump_Button_Pressed_Bool = False
        self.Is_Right_Button_Pressed_Bool = False
        self.Is_Left_Button_Pressed_Bool = False

        self.count = 2

        self.JumpCount = None
        self.steps_above_ground = None

        self.jump_sound = load_sound('jump.wav' , 'Jump')
        self.sword_sound = load_sound('sword.wav', 'UpperAttack')

        self.Bool_Check_If_Under_base = self.Base_Y_position-self.Current_Y_position

        '''independant fps stuff'''
        self.Checking_List_Idle = [] #everytime the image is read this will be filled up with it ,needed for independant fps scaler of animations
        self.Idle_Scalar = 5           #repeat each image frae by the int set here
        self.Walk_Scalar = 1



    def update(self):
        '''call the frames of each chosen animation one after another here'''
        
        if self.Current_Animation=='Idle':

            self.Jump_Bool = False

            self.Checking_List_Idle.append(self.count)

            FileName = str(self.count) + 'idleN.png'
            self.image, self.rect = load_image(FileName, 'Idle')

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

            if self.count==17:
                self.count=1

        elif self.Current_Animation=='Walk_Right':

            self.Jump_Bool = False

            self.Current_X_position+=20 
            FileName = str(self.count) + 'walkN.png'
            self.image, self.rect = load_image(FileName, 'Walk')

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

            self.count+=1

            self.Current_Faced_Side = 'Right'


            if self.count==9:
                self.count=1

        elif self.Current_Animation=='Walk_Left':

            self.Jump_Bool = False

            self.Current_X_position+=-20 
            FileName = str(self.count) + 'walkN.png'
            self.image, self.rect = load_image(FileName, 'Walk')

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()

            if self.Current_X_position>-70:
                '''checking to see that the character is on the far left'''
                self.rect = self.Current_X_position, self.Current_Y_position
            else:
                self.Current_X_position = -70
                self.rect = self.Current_X_position, self.Current_Y_position

            self.count+=1

            self.Current_Faced_Side = 'Left'

            if self.count==9:
                self.count=1

        elif self.Current_Animation=='Crouch':

            self.Jump_Bool = False

            FileName = str(self.count) + 'crouch.png'
            self.image, self.rect = load_image(FileName, 'Crouch')

            if self.Current_Faced_Side=='Right':
                self.image = pygame.transform.flip(self.image, 1, 0)

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()
            self.rect.topleft = self.Current_X_position, self.Current_Y_position

            self.count+=1

            if self.count==8:
                self.count=1

        elif self.Current_Animation=='UpperAttack':

            self.Jump_Bool = False

            FileName = str(self.count) + 'upperattack.png'
            self.image, self.rect = load_image(FileName, 'UpperAttack')

            if self.Current_Faced_Side=='Right':
                self.image = pygame.transform.flip(self.image, 1, 0)

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()
            self.rect.topleft = self.Current_X_position, self.Current_Y_position

            self.count+=1

            if self.count==13:
                self.count=1
                self.sword_sound.play()

        elif self.Current_Animation=='JumpStraightUp':

            self.Jump_Bool = True

            if self.count==1 or self.count==2 or self.count==3 or self.count==4 or self.count==5 or self.count==6:
                self.Current_Y_position+=-20

            elif self.count==7 or self.count==8 or self.count==9 or self.count==10 or self.count==11 or self.count==12:
                self.Current_Y_position+=20


            FileName = str(self.count) + 'jump.png'
            self.image, self.rect = load_image(FileName, 'Jump')

            if self.Current_Faced_Side=='Right':

                self.image = pygame.transform.flip(self.image, 1, 0)

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()
                self.rect.topleft = self.Current_X_position, self.Current_Y_position

                self.count+=1

                self.JumpCount = self.count

                if self.count>13:
                    self.count=1
                    self.Reset_Y_Position_To_Base()
                    self.jump_sound.play()

            elif self.Current_Faced_Side=='Left':

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()
                self.rect.topleft = self.Current_X_position, self.Current_Y_position

                self.count+=1

                self.JumpCount = self.count

                if self.count>12:
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
                if self.JumpCount>0 and self.JumpCount<7:
                    self.steps_above_ground = self.JumpCount-1
                elif self.JumpCount>6 and self.JumpCount<12:
                    self.steps_above_ground = 13-self.JumpCount
            
            if self.steps_above_ground!=0 and self.steps_above_ground!=None:

                self.Jump_Bool=False

                self.Current_Y_position+=20

                FileName = '1jump.png'
                self.image, self.rect = load_image(FileName, 'Jump')

                #Flip the image depending on which side char is facing
                if self.Current_Faced_Side=='Right':
                    self.image = pygame.transform.flip(self.image, 1, 0)

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()
                self.rect.topleft = self.Current_X_position, self.Current_Y_position


            self.Distance_Above_Ground = abs(self.Current_Y_position-self.Base_Y_position)
            print ('Distance above ground: '+str(self.Distance_Above_Ground))
            self.steps_above_ground = self.Distance_Above_Ground/20

            self.Bool_Check_If_Under_base = self.Base_Y_position-self.Current_Y_position

            if self.steps_above_ground==0 or self.Bool_Check_If_Under_base<0:
                self.Reset_Y_Position_To_Base()
                self.Current_Animation = 'Idle'

            
        elif self.Current_Animation=='JumpLeft':

            self.Jump_Bool = True

            if self.count==1 or self.count==2 or self.count==3 or self.count==4 or self.count==5 or self.count==6:
                self.Current_Y_position+=-20
                self.Current_X_position+=-10

            elif self.count==7 or self.count==8 or self.count==9 or self.count==10 or self.count==11 or self.count==12:
                self.Current_Y_position+=20
                self.Current_X_position+=-10


            FileName = str(self.count) + 'jump.png'
            self.image, self.rect = load_image(FileName, 'Jump')

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

                if self.count>12:
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

                if self.count>12:
                    self.count=1
                    self.Reset_Y_Position_To_Base()
                    self.jump_sound.play()

        elif self.Current_Animation=='PrematureJumpEndingLeft':
            '''
            this section is to animate when the sprite does not jump or carry out full animation
            so it needs to still be animated falling down the number of stteps it jumped up. At 
            the end this function will call the idle animation     
            '''
            #find out how many steps the sprite was pushed above ground
            if self.Jump_Bool==True:
                if self.JumpCount>0 and self.JumpCount<7:
                    self.steps_above_ground = self.JumpCount-1
                elif self.JumpCount>6 and self.JumpCount<12:
                    self.steps_above_ground = 13-self.JumpCount
            
            if self.steps_above_ground!=0 and self.steps_above_ground!=None:

                self.Jump_Bool=False

                self.Current_Y_position+=20
                self.Current_X_position+=-9

                FileName = '1jump.png'
                self.image, self.rect = load_image(FileName, 'Jump')

                #Flip the image depending on which side char is facing
                if self.Current_Faced_Side=='Right':
                    self.image = pygame.transform.flip(self.image, 1, 0)

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()
                self.rect.topleft = self.Current_X_position, self.Current_Y_position

                self.Distance_Above_Ground = abs(self.Current_Y_position-self.Base_Y_position)
                #print ('Distance above ground: '+str(self.Distance_Above_Ground))
                self.steps_above_ground = self.Distance_Above_Ground/20

                self.Bool_Check_If_Under_base = self.Base_Y_position-self.Current_Y_position

            if self.steps_above_ground==0 or self.Bool_Check_If_Under_base<0:

                self.Reset_Y_Position_To_Base()

                if self.Is_Left_Button_Pressed_Bool:
                    self.Current_Animation = 'Walk_Left'
                else:
                    #self.Reset_Y_Position_To_Base()
                    self.Current_Animation = 'Idle'

        elif self.Current_Animation=='JumpRight':

            self.Jump_Bool = True

            if self.count==1 or self.count==2 or self.count==3 or self.count==4 or self.count==5 or self.count==6:
                self.Current_Y_position+=-20
                self.Current_X_position+=10

            elif self.count==7 or self.count==8 or self.count==9 or self.count==10 or self.count==11 or self.count==12:
                self.Current_Y_position+=20
                self.Current_X_position+=10


            FileName = str(self.count) + 'jump.png'
            self.image, self.rect = load_image(FileName, 'Jump')

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

                if self.count>12:
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

                if self.count>12:
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
                if self.JumpCount>0 and self.JumpCount<7:
                    self.steps_above_ground = self.JumpCount-1
                elif self.JumpCount>6 and self.JumpCount<12:
                    self.steps_above_ground = 13-self.JumpCount
            
            if self.steps_above_ground!=0 and self.steps_above_ground!=None:

                self.Jump_Bool=False

                self.Current_Y_position+=20
                self.Current_X_position+=9

                FileName = '1jump.png'
                self.image, self.rect = load_image(FileName, 'Jump')

                #Flip the image depending on which side char is facing
                if self.Current_Faced_Side=='Right':
                    self.image = pygame.transform.flip(self.image, 1, 0)

                screen = pygame.display.get_surface()
                self.area = screen.get_rect()
                self.rect.topleft = self.Current_X_position, self.Current_Y_position

                self.Distance_Above_Ground = abs(self.Current_Y_position-self.Base_Y_position)
                print ('Distance above ground: '+str(self.Distance_Above_Ground))
                self.steps_above_ground = self.Distance_Above_Ground/20

                self.Bool_Check_If_Under_base = self.Base_Y_position-self.Current_Y_position

            if self.steps_above_ground==0 or self.Bool_Check_If_Under_base<0:

                self.Reset_Y_Position_To_Base()

                if self.Is_Right_Button_Pressed_Bool:
                    self.Current_Animation = 'Walk_Right'
                else:
                    #self.Reset_Y_Position_To_Base()
                    self.Current_Animation = 'Idle'

        elif self.Current_Animation=='RasenganStance':

            self.Jump_Bool = False

            FileName = str(self.count) + '.png'
            self.image, self.rect = load_image(FileName, 'RasenganStance')

            if self.Current_Faced_Side=='Right':
                self.image = pygame.transform.flip(self.image, 1, 0)

            screen = pygame.display.get_surface()
            self.area = screen.get_rect()
            self.rect.topleft = self.Current_X_position, self.Current_Y_position

            self.count+=1

            if self.count==4:
                self.count=1

    def Update_Animation(self, anim):
        '''this function can ba called from outide to change the current animation sequence'''

        self.count = 1
        self.Current_Animation = anim

    def Reset_Y_Position_To_Base(self):
        '''this function when called will reset the y position of the character to base 730'''

        self.Current_Y_position = 730

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
