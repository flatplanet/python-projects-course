import turtle
import os


# Clear screen
os.system("clear")

# Create a turtle object
t = turtle.Turtle()
# Create a screen object
screen = turtle.Screen()


# Reset the screen
def reset_turtle():
	t.clear()
	t.penup()
	t.home()
	t.pendown()


# Draw a square
def draw_square(size):
	#reset_turtle()
	# For loop to do 4 lines
	for _ in range(4):
		t.forward(size)
		t.right(90)

# Draw a triangle
def draw_triangle(size):
	#reset_turtle()
	for _ in range(3):
		t.forward(size)
		t.left(120)

# Draw a circle
def draw_circle(radius):
	#reset_turtle()
	t.circle(radius)
	



# Main function
def draw_shape():
	while True:
		# Clear the screen
		os.system("clear")
		print("\nSelect a Shape to Draw:")
		print("1. Square")
		print("2. Circle")
		print("3. Triangle")
		print("4. Exit")

		# Prompt the user
		choice = input("Enter the number of your choice: ")

		# Choice logic
		if choice == "1":
			size = int(input("Enter the Size of the Square: "))
			draw_square(size)
		elif choice == "2":
			size = int(input("Enter the Radius of the Circle: "))
			draw_circle(size)

		elif choice == "3":
			size = int(input("Enter the Size of the Triangle: "))
			draw_triangle(size)

		elif choice == "4":
			print("Exiting the program. Later!")
			# close turle screen
			turtle.bye()
			break
			

		# Catch errors
		else:
			print("Invalid Choice, please try again...")







# Run the app
draw_shape()


# # Complete the drawing
#turtle.done()
