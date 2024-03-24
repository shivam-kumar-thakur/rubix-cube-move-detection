import cv2
import mediapipe as mp
import time

width = 640
height = 480

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

def webCam():
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)
    ptime = 0
    ctime = 0

    prev_hand_landmarks = None
    current_hand_landmarks = {}

    while True:
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    current_hand_landmarks[id] = [lm.x, lm.y, lm.z]

                if prev_hand_landmarks:
                    """ we want to Compare current hand landmarks with previous landmarks.
                     Here, we'll detect significant changes in finger top points
                     and determine if the hand is moving up, down, or clockwise """

                    # Compare finger top points, excluding the thumb
                    prev_finger_points = [prev_hand_landmarks[i] for i in range(1, 5)]
                    curr_finger_points = [current_hand_landmarks[i] for i in range(1, 5)]

                    # Checking for a significant change in the y-coordinate of finger top points
                    for prev_pt, curr_pt in zip(prev_finger_points, curr_finger_points):
                        if abs(curr_pt[1] - prev_pt[1]) > 0.05:
                            if curr_pt[1] > prev_pt[1]:
                                print("Moving Down")
                            else:
                                print("Moving Up")

                            # Checking for a significant change in the x-coordinate of finger top points
                            if curr_pt[0] > prev_pt[0]:
                                print("Moving Right")
                            else:
                                print("Moving Left")

                prev_hand_landmarks = current_hand_landmarks.copy()

                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

        ctime = time.time()
        fps = 1 / (ctime - ptime)
        ptime = ctime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
        cv2.imshow("image", img)
        key = cv2.waitKey(1)  # 1ms
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

webCam()
