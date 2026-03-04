import pyautogui
import keyboard
import time
import tkinter as tk
from tkinter import simpledialog




def ask_copy_count():
    root = tk.Tk()
    root.withdraw()


    root.attributes("-topmost", True)
    root.update()
    root.deiconify()
    root.lift()
    root.focus_force()


    answer = simpledialog.askinteger(
        "Duplicate Block",
        "How many times would you like this copied and pasted?",
        parent=root,
        minvalue=1,
        maxvalue=100
    )


    root.attributes("-topmost", False)
    root.destroy()
    return answer




def On_hotkey():
    time.sleep(0.2)


    copies = ask_copy_count()
    if copies is None:
        return


    pyautogui.keyUp("shift")
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("alt")


    time.sleep(1)


    # Expand selection downward
    while True:
        pyautogui.keyDown("shift")
        pyautogui.press("down")
        pyautogui.keyUp("shift")


        time.sleep(0.05)


        # Copy to check if blank (but DO NOT re-copy cleaned text later)
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.1)


        # Get plain text just to detect blank line
        import pyperclip
        text = pyperclip.paste()
        lines = text.splitlines()


        if len(lines) > 0 and lines[-1].strip() == "":
            break


    # Now copy the FULL rich selection once
    pyautogui.hotkey("ctrl", "c")


    # Move cursor below block
    pyautogui.press("down")


    # Paste with formatting preserved
    for _ in range(copies):
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")




keyboard.add_hotkey("f8", On_hotkey)
keyboard.wait("esc")
