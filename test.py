import socket
import cv2
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
s.bind(('127.0.0.1', 11574))

print('Bind UDP on 11574...')

while True:
    # 接收数据:
    data, addr = s.recvfrom(400000)

    print('Received from %s:%s.' % addr)
    #解码
    nparr = np.frombuffer(data, np.uint8)

    #解码成图片numpy
    img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow('result',img_decode)
    reply = "get message!!!"
    s.sendto(reply.encode('utf-8'), addr)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #cv2.destroyAllWindows()

s.close()

cv2.destroyAllWindows()