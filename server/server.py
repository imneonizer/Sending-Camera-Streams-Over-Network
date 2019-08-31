import base64
import cv2
import zmq
import imutils

context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
footage_socket.connect('tcp://192.168.0.108:5555') #ipaddress of client

camera = cv2.VideoCapture(0)  # init the camera

while True:
    try:
        grabbed, frame = camera.read()  # grab the current frame
        frame = imutils.resize(frame, width=400) #resizing for faster transmission
        encoded, buffer = cv2.imencode('.jpg', frame)
        jpg_as_text = base64.b64encode(buffer)
        footage_socket.send(jpg_as_text)

    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        break
