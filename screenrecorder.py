import cv2
import numpy as np
from PIL import ImageGrab

def screenRecord():
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1920, 1080))

    while True:
        # Capture the screen
        img = ImageGrab.grab()
        frame = np.array(img)

        # Convert the color from RGB to BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Write the frame to the video file
        out.write(frame)

        # Display the recording screen
        cv2.imshow("Screen Recorder", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release everything if job is done
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    screenRecord()