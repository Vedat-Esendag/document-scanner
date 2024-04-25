import cv2

def main():
    # Initialize the camera capture object with the default camera
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    # Continuously capture frames from the webcam
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Display the frame in a window
        cv2.imshow('Camera', frame)

        # Press 'q' to exit the loop
        c = cv2.waitKey(1)
        if c == ord('q'):
            break

    # Release the video capture object and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
