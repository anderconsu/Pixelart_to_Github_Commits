from PIL import Image

#* The hex values of github commits
# commit_21 = "rgb(56, 211, 83)", '38d353'
# commit_18 = "rgb(37, 166, 64)", "25a640"
# commit_15 = "rgb(37, 166, 65)", "25a641"
# commit_12 = "rgb(0, 109, 50)", "006d32"
# commit_3 = "rgb(14, 68, 42)", "0e442a"

hex_dict = {
    "38d353": 5,
    "25a640": 4,
    "25a641": 3,
    "006d32": 2,
    "0e442a": 1,
}


def hex_to_value(hex_color):
    """
    Converts a hexadecimal color code to its corresponding value from hex_dict.

    Args: 
        hex_color (str): The hexadecimal color code to convert.

    Returns:
        int: The corresponding value of the hexadecimal color code. Returns 0 if the color code is not found in the dictionary.
    """
    # Convert hex color to lowercase to ensure consistency
    hex_color = hex_color.lower()

    # Get the corresponding value from the dictionary, default to 0 if not found
    return hex_dict.get(hex_color, 0)



def image_to_matrix_list(image_path: str, dictionary: dict) -> list:
    """
    Convert an image to a matrix.

    Args:
        image_path (str): The path to the image file.

    Returns:
        list: A list of lists representing the matrix list of the image pixels, based on the dictionary values.
    """
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to RGB
    img = img.convert('RGB')

    # Get the width and height of the image
    width, height = img.size

    # Initialize an empty list to store rows
    rows = []

    # Iterate through each row of pixels
    for y in range(height):
        # Get the pixels in the current row
        row_values = [dictionary(''.join(format(c, '02x') for c in img.getpixel((x, y)))) for x in range(width)]
        
        # Append the row to the list of rows
        rows.append(row_values)

    return rows

if __name__ == "__main__":
    
    try:
        # Replace 'your_image_path.jpg' with the actual path to your image
        image_path = './pixel_art.png'
        tempInput = input("Enter the path to the image: (default: pixel_art.png)\n")
        if tempInput != "":
            image_path = tempInput

        # Get the binary list representation of the image
        binary_list = image_to_matrix_list(image_path, hex_to_value)
        
        name = input("Enter the name of the art:\n")
        if name == "":
            name = "pixel_art"

        # Print the result  
        print(f':{name}')      
        for index, row in enumerate(binary_list):
            if index == 0:
                print(f'[{row},')
            elif index == len(binary_list) - 1:
                print(f'{row}]')
            else:
                print(f'{row},')

        # Write the result to a text file
        with open(f'{name}.txt', 'w') as file:
            file.write(f':{name}\n')
            for index, row in enumerate(binary_list):
                if index == 0:
                    file.write(f'[{row},\n')
                elif index == len(binary_list) - 1:
                    file.write(f'{row}]\n')
                else:
                    file.write(f'{row},\n')
                
    except Exception as e:
        print(f"An error occurred: {e}")