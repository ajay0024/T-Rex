import pyautogui
import time

distance = 200
while pyautogui.locateCenterOnScreen('t-rex.png', grayscale=True) is None:
    time.sleep(0.25)
    print("Waiting for T-Rex Game Screen")
tx, ty = pyautogui.locateCenterOnScreen('t-rex.png', grayscale=True)
print(tx, ty)
start_time = time.time()
playing = True
while playing:
    mx = 120
    black_found = False
    if not pyautogui.pixelMatchesColor(tx + mx, ty, (247, 247, 247), tolerance=10):
        black_found = True
    time_spent = time.time() - start_time
    mx = mx + int(time_spent * 2)
    if black_found:
        print(tx + mx, ty)
        print(time_spent)
        pyautogui.press("up")
