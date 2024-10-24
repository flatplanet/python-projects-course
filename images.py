# pip install Pillow
from PIL import Image

# Function to resize the image
def resize_image(input_path, output_path, new_width):
    # Error handling for opening the image with PIL
    try:
        # Open The Image
        # img = Image.open(input_path)
        with Image.open(input_path) as img:
            # Get the original dimensions
            # print(img.size)
            # img.size == (960, 720)
            width,height = img.size
            # Print out our dimensions
            print(f"Original Size: {width} x {height}")

            # Calculate the new height to maintain the aspect ratio
            aspect_ratio = height / width 

            # Aspen.jpg width=960 height=720
            # Aspen aspect ratio = .75
            # Resized width = 480 resized height = 360

            # get the new height
            new_height = int(new_width * aspect_ratio)

            # Resize the image
            resized_image = img.resize((new_width, new_height))

            # Save the new image
            resized_image.save(output_path)

            # Output the results to the user
            print(f"Image resied and saved as {output_path}. New Size: {new_width} x {new_height}")




    except IOError:
        print("Error: Unable to open or save the image. Please check the file paths.")


# Main Function
def image_resizer():
    # c:/python-projects/aspen.jpg
    input_path = input("Enter the path of the image to resize: ")
    output_path = input("Enter the output path for the resized image: ")
    new_width = int(input("Enter the new width for the resized image: "))

    # Resize the image
    resize_image(input_path, output_path, new_width)








# Call the main function
image_resizer()
