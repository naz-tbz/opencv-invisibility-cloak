import cv2
import numpy as np

def apply_invisible_cloak(frame, background):

    # Step 1: Convert current frame from BGR to HSV color space
    # HSV makes color detection easier than BGR
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Step 2: Define GREEN color range
    # Lower green range
    lower_green1 = np.array([35, 40, 40])
    upper_green1 = np.array([70, 255, 255])

    # Second green range (slightly different shades)
    lower_green2 = np.array([70, 40, 40])
    upper_green2 = np.array([90, 255, 255])

    # Create masks using both ranges
    mask1 = cv2.inRange(hsv, lower_green1, upper_green1)
    mask2 = cv2.inRange(hsv, lower_green2, upper_green2)

    # Step 3: Combine both masks
    mask = mask1 + mask2

    # Step 4: Clean the mask using morphologyEx
    # cv2.morphologyEx() performs advanced image transformations.
    # MORPH_OPEN removes small unwanted noise from the mask.
    # MORPH_DILATE expands white regions to cover cloak better.

    kernel = np.ones((3, 3), np.uint8)

    # Remove noise
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)

    # Expand mask area slightly
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=1)

    # Step 5: Inverse mask (everything except green area)
    inverse_mask = cv2.bitwise_not(mask)

    # Step 6: Extract cloak area from background
    # Wherever green cloth exists, take pixels from saved background
    cloak_area = cv2.bitwise_and(background, background, mask=mask)

    # Step 7: Extract non-cloak area from current frame
    current_area = cv2.bitwise_and(frame, frame, mask=inverse_mask)

    # Step 8: Combine both images
    # Green cloth area replaced by background
    final_output = cv2.add(cloak_area, current_area)

    return final_output


# Start webcam
cap = cv2.VideoCapture(0)

print("Press 'b' to capture background")
print("Wear green cloth/object for invisibility effect")
print("Press 'q' to quit")


# Capture background image
while True:
    ret, background = cap.read()

    if not ret:
        break

    cv2.imshow("Capture Background - Press B", background)

    # Save background when user presses b
    if cv2.waitKey(1) & 0xFF == ord('b'):
        break


# Main loop
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Apply invisibility effect
    output = apply_invisible_cloak(frame, background)

    cv2.imshow("Invisible Cloak Effect", output)

    # Quit program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Release camera and close windows
cap.release()
cv2.destroyAllWindows()