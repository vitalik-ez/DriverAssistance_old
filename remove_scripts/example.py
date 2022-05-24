# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import sys
import qimage2ndarray

class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self, width = 640, height = 480, fps = 25):
        super().__init__()

        self.video_size = QtCore.QSize(width, height)
        self.camera_capture = cv2.VideoCapture(0)

        self.frame_timer = QtCore.QTimer()
        self.fps = fps

        self.setup_camera(self.fps)

        # Setup UI
        #self = QtWidgets.QMainWindow()
        self.setupUi()



    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(720, 691)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 701, 671))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.VideoContainer = QtWidgets.QWidget(self.widget)
        self.VideoContainer.setObjectName("VideoContainer")
        self.videoStream = QtWidgets.QLabel(self.VideoContainer)
        self.videoStream.setGeometry(QtCore.QRect(0, 0, 701, 591))
        self.videoStream.setText("")
        self.videoStream.setObjectName("videoStream")
        self.verticalLayout.addWidget(self.VideoContainer)
        self.ControlContainer = QtWidgets.QWidget(self.widget)
        self.ControlContainer.setMaximumSize(QtCore.QSize(16777215, 100))
        self.ControlContainer.setObjectName("ControlContainer")
        self.widget1 = QtWidgets.QWidget(self.ControlContainer)
        self.widget1.setGeometry(QtCore.QRect(0, 20, 701, 81))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")


        self.startButton = QtWidgets.QPushButton(self.widget1)
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 0, 0, 1, 1)


        self.switchcamerabutton = QtWidgets.QPushButton(self.widget1)
        self.switchcamerabutton.setObjectName("switchcamerabutton")
        self.gridLayout.addWidget(self.switchcamerabutton, 0, 1, 1, 1)

        
        self.pauseButton = QtWidgets.QPushButton(self.widget1)
        self.pauseButton.setObjectName("pauseButton")
        self.gridLayout.addWidget(self.pauseButton, 0, 2, 1, 1)

        self.quitButton = QtWidgets.QPushButton(self.widget1)
        self.quitButton.setObjectName("quitButton")
        self.quitButton.clicked.connect(self.close_app)

        self.gridLayout.addWidget(self.quitButton, 1, 0, 1, 3)
        self.verticalLayout.addWidget(self.ControlContainer)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.switchcamerabutton.setText(_translate("MainWindow", "Switch camera"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))


    def setup_camera(self, fps):
        self.camera_capture.set(3, self.video_size.width())
        self.camera_capture.set(4, self.video_size.height())
        self.frame_timer.timeout.connect(self.display_video_stream)
        self.frame_timer.start(int(1000 // fps))


    def display_video_stream(self):
        ret, frame = self.camera_capture.read()
        if not ret:
            print("Error reading frame from camera")
            return False
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        image = qimage2ndarray.array2qimage(frame)
        self.videoStream.setPixmap(QtGui.QPixmap.fromImage(image))



    def close_app(self):
        self.close()

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    
    ui = Ui_MainWindow()
    
    ui.show()
    sys.exit(app.exec_())