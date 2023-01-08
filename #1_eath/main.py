from arts import slides
from time import sleep

# Make slide animation
for slide in slides:
    print('\033[H')  # clear terminal
    print('\u001b[32m', slide) #set text color
    sleep(0.2)

print('\u001b[0m')
