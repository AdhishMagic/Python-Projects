import cv2
import numpy as np
from PIL import ImageGrab

def screenRecord():
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1920, 1080))

    while True:
        img = ImageGrab.grab()
        frame = np.array(img)

        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        out.write(frame)

        cv2.imshow("Screen Recorder", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    screenRecord()