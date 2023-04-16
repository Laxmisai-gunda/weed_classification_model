import cv2
from predict import predict

cam = cv2.VideoCapture(0)

while True:
    status, frame = cam.read()

    if not status:
        print('Failed To open camera')

    else:

        cv2.imwrite('current.png', frame)

        label = predict('current.png')
        print(label)
        cv2.putText(frame, label, (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        cv2.imshow('Live', frame)

        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
    
