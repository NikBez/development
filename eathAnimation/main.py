from time import sleep

from arts import slides

# Make slide animation
for slide in slides:
    print('\033[H')  # clear terminal
    print('\u001b[32m', slide)  # set text color and animate slide
    sleep(0.2)

print('\u001b[0m')  # return default text color
