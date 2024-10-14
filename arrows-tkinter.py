from tkinter import *




# Build out a simple app gui
root = Tk()
root.title("Arrows!")
root.geometry("300x100")

def key_pressed(event):
	key = event.keysym
	if key == "Up":
		my_label.config(text="Up!")
	elif key == "Down":
		my_label.config(text="Down...")
	elif key == "Left":
		my_label.config(text="<-- Left")
	elif key == "Right":
		my_label.config(text="Right -->")
	elif key == 'q':
		root.destroy()



# Label
my_label = Label(root, text="Press arrow keys. Press 'q' to exit...")
my_label.pack(pady=20)


# Focus the window 
root.focus_set()

# Bind the keyboard
root.bind('<KeyPress>', key_pressed)


root.mainloop()