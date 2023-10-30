import mss
import pyautogui

def capture_screenshot():
    with mss.mss() as sct:
        screenshot = sct.shot(output="screenshot.png")
    return screenshot

def find_first_red_pixel(image_path):
    import cv2
    import numpy as np

    image = cv2.imread(image_path)
    red_pixel = np.array([0, 0, 255])  # Red pixel in BGR format

    # Find the first red pixel
    red_pixel_coords = np.argwhere(np.all(image == red_pixel, axis=-1))
    if red_pixel_coords.size > 0:
        return tuple(red_pixel_coords[0])
    else:
        return None

def click_at_pixel(x, y):
    pyautogui.click(y, x)

if __name__ == "__main__":
    #clicking top left
    pyautogui.click(1,1)
    # Capture a screenshot
    screenshot_path = "screenshot.png"
    capture_screenshot()

    # Find the first red pixel
    red_pixel_coords = find_first_red_pixel(screenshot_path)

    if red_pixel_coords:
        x, y = red_pixel_coords
        print(f"Found a red pixel at coordinates (x={x}, y={y}). Clicking...")
        click_at_pixel(x, y)
    else:
        print("No red pixel found in the screenshot.")