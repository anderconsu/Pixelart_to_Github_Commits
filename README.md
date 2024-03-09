# Pixelart to Github Commits

This script aims to convert the pixels of an image into a matrix of numbers, representing the number of commits.

It was designed to be used with the [Gitfiti proyect](https://github.com/gelstudios/gitfiti) , but you can change the output value by modifying the 'hex_dict' values with the desired hex for the intended return value.

The result is both printed and written to a txt file. You can copy it to the Gitfiti repository directory and import it by specifying the name in the Gitfiti script.

-   The pixel art **MUST** be created with the exact HEX values specified in the script. If not, adjust the 'hex_dict' accordingly.

-   The height for GitHub activity is 7px
