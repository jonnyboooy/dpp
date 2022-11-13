# PUBLISHER

import cv2
from paho.mqtt import client as mqtt
from datetime import datetime

class MQTT_Work():
    Brocker = "mqtt.eclipseprojects.io"
    client_name = "###Publisher###"
    client = mqtt.Client(client_name)
    client.connect(Brocker)
    topic_name = 'position'

    def Publish(self, output_str):
        self.client.publish(self.topic_name, output_str)

class GUI_Work():

    capture = cv2.VideoCapture(0)
    window_name = 'task_6'
    x = -100
    y = -100
    can_print = False
    date = ''
    data = ''

    def GetImage(self):
        ret, img = self.capture.read()
        return img

    def PrintImage(self, img):
        cv2.imshow(self.window_name, img)

    def show_clicked(self, event,x_num,y_num,flags,param):
        mq = MQTT_Work()

        if event == cv2.EVENT_LBUTTONDOWN:
            self.x = x_num
            self.y = y_num
            self.PrintDataAndDate()
            self.can_print = True
            message = gui.data
            mq.Publish(message)

    def DestroyWindows(self):
        self.capture.release()
        cv2.destroyAllWindows()

    def GetTime(self):
        dt_now = datetime.now()
        return dt_now

    def PrintDataAndDate(self):
        self.date = self.GetTime().strftime('%d-%m-%Y %H:%M:%S') + ':'
        self.data = f'x = {self.x}, y = {self.y}'

    def PrintRectangle(self, img):
        cv2.rectangle(img,(self.x-20,self.y-10),(self.x+20,self.y+10), (0,0,255), 2)

if __name__ == '__main__':

    gui = GUI_Work()

    key = -1

    while True:
        key = cv2.waitKey(5)

        if key == ord('q') or key == ord('Q'):
            break
        else:
            image1 = gui.GetImage()
            image2 = gui.GetImage()

            cv2.namedWindow(gui.window_name)

            c = cv2.setMouseCallback(gui.window_name, gui.show_clicked)

            if gui.can_print == True:
                gui.PrintRectangle(image1)

            if key == ord('c') or key == ord('C'):
                gui.PrintImage(image2)
                gui.can_print = False
            else:
                gui.PrintImage(image1)

    gui.DestroyWindows()