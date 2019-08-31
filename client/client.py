import cv2
import zmq
import base64
import numpy as np

context = zmq.Context()
footage_socket = context.socket(zmq.SUB)
footage_socket.bind('tcp://*:5555')
footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))

while True:
    try:
        frame = footage_socket.recv_string()
        img = base64.b64decode(frame)
        npimg = np.fromstring(img, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)
        print(source.shape) #if image width is 400, it is verified that our resized image has received
        #cv2.imshow("Stream", source) #incase we have a display and we wanna see the feed
        #cv2.waitKey(1)

    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        break
