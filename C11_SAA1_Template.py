# Import "pygame" module 
import pygame
# Import "time" module
import time
# Initialize "pygame"
pygame.init() 

# Create a screen of size (400, 300)
screen = pygame.display.set_mode((400,300))
# Set the "screen" title as "Counter" 
pygame.display.set_caption("Counter")

# RGB color combinations
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
YELLOW = (255,255,0)

carryOn = True
while carryOn:
       # Initiate a 'for' loop with range 1 to 20

            # Fill the screen with "DARKBLUE" color

            
            # Display the text "Counter:" at loaction (140, 100)



            
            # Display the value of "i" variable of 'for' loop below the text "Counter:" at loaction (180,130)



            
            # Check if user has clicked on close botton on the game window when the counter is running. 
            # If 'True' close the window.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    carryOn = False
                    pygame.quit()

            # Update the contents of display

            # Wait for 1 seconds before displaying next counter value

                    
# Close the window on the occurence of "pygame.QUIT".        
pygame.quit()