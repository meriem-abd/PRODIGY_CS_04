# PRODIGY_CS_04
<h1>key logger</h1>
<h2>warning:</h2>
This script is intended for educational purposes only. Misuse of keyloggers for unauthorized monitoring or data collection is illegal and unethical. Ensure you have proper authorization before using this script on any system.
<h2>overview:</h2>
This Python script implements a simple keylogger using the keyboard library. The keylogger monitors and records key presses into a specified file. It continuously logs keystrokes until the 'Esc' key is pressed, at which point it stops logging and terminates.

<h2>features:</h2>
<p><strong>Keystroke Logging:</strong>Captures each key pressed by the user</p>

<p><strong>custom file path:</strong>Allows the user to specify a file path to save the logged keystrokes.</p>

<p><strong>graceful exit:</strong>Stops logging when the 'Esc' key is pressed</p>

<h2>process:</h2>
<p><strong>pressed(key) Function:</strong>This function is called every time a key is pressed. It writes the key information to the specified file.</p>

<p><strong>File Path Input:</strong>The script prompts the user to enter the path where the logged keystrokes will be saved.</p>

<p><strong>Callback Registration:</strong>The keyboard.on_press method registers the pressed function to be called on every key press.</p>

<p><strong>Script Execution:</strong>The script prints a message indicating that the keylogger is running and waits for the 'Esc' key to stop.</p>
