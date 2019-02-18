# Developed by M.Bucknell Optimal Consultng Ltd
#	
# Meade LX200 Classic Virtual Handset - GUI with Init & full handset control
# Interface from a FTDI USB serial port set to 5v with Tx & Rx inverted (use the FTDI tools to configure this
#
# Set the SPORT value to your FTDI serial port and then run, you should see the hex data being printed, comment out if you don't want to see the data
# press initalise button to send the init string "FFFFFFFFFF*" this will allow the base to accept handset control or serial port control


import serial

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import  QTimer
SPORT='/dev/ttyUSB0'


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_LX200ClassicHandset(object):
    def setupUi(self, LX200ClassicHandset):
        LX200ClassicHandset.setObjectName(_fromUtf8("LX200ClassicHandset"))
        LX200ClassicHandset.resize(350, 558)
        self.Handset = QtGui.QWidget()
        self.Handset.setObjectName(_fromUtf8("Handset"))
        self.BENTER = QtGui.QPushButton(self.Handset)
        self.BENTER.setGeometry(QtCore.QRect(30, 90, 91, 41))
        self.BENTER.setObjectName(_fromUtf8("BENTER"))
        self.L8 = QtGui.QRadioButton(self.Handset)
        self.L8.setGeometry(QtCore.QRect(20, 280, 51, 22))
        self.L8.setObjectName(_fromUtf8("L8"))
        self.BMODE = QtGui.QPushButton(self.Handset)
        self.BMODE.setGeometry(QtCore.QRect(130, 90, 91, 41))
        self.BMODE.setObjectName(_fromUtf8("BMODE"))
        self.BGOTO = QtGui.QPushButton(self.Handset)
        self.BGOTO.setGeometry(QtCore.QRect(230, 90, 91, 41))
        self.BGOTO.setObjectName(_fromUtf8("BGOTO"))
        self.BN = QtGui.QPushButton(self.Handset)
        self.BN.setGeometry(QtCore.QRect(130, 140, 91, 41))
        self.BN.setObjectName(_fromUtf8("BN"))
        self.BE = QtGui.QPushButton(self.Handset)
        self.BE.setGeometry(QtCore.QRect(230, 160, 91, 41))
        self.BE.setObjectName(_fromUtf8("BE"))
        self.BW = QtGui.QPushButton(self.Handset)
        self.BW.setGeometry(QtCore.QRect(30, 160, 91, 41))
        self.BW.setObjectName(_fromUtf8("BE_2"))
        self.BS = QtGui.QPushButton(self.Handset)
        self.BS.setGeometry(QtCore.QRect(130, 190, 91, 41))
        self.BS.setObjectName(_fromUtf8("BS"))
        self.B7 = QtGui.QPushButton(self.Handset)
        self.B7.setGeometry(QtCore.QRect(80, 270, 51, 41))
        self.B7.setObjectName(_fromUtf8("B7"))
        self.label = QtGui.QLabel(self.Handset)
        self.label.setGeometry(QtCore.QRect(80, 250, 51, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.Handset)
        self.label_2.setGeometry(QtCore.QRect(150, 250, 51, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.B8 = QtGui.QPushButton(self.Handset)
        self.B8.setGeometry(QtCore.QRect(150, 270, 51, 41))
        self.B8.setObjectName(_fromUtf8("B8"))
        self.label_3 = QtGui.QLabel(self.Handset)
        self.label_3.setGeometry(QtCore.QRect(220, 250, 51, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.B9 = QtGui.QPushButton(self.Handset)
        self.B9.setGeometry(QtCore.QRect(220, 270, 51, 41))
        self.B9.setObjectName(_fromUtf8("B9"))
        self.label_4 = QtGui.QLabel(self.Handset)
        self.label_4.setGeometry(QtCore.QRect(220, 320, 51, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.B5 = QtGui.QPushButton(self.Handset)
        self.B5.setGeometry(QtCore.QRect(150, 340, 51, 41))
        self.B5.setObjectName(_fromUtf8("B5"))
        self.label_5 = QtGui.QLabel(self.Handset)
        self.label_5.setGeometry(QtCore.QRect(150, 320, 51, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.B6 = QtGui.QPushButton(self.Handset)
        self.B6.setGeometry(QtCore.QRect(220, 340, 51, 41))
        self.B6.setObjectName(_fromUtf8("B6"))
        self.label_6 = QtGui.QLabel(self.Handset)
        self.label_6.setGeometry(QtCore.QRect(80, 320, 51, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.B4 = QtGui.QPushButton(self.Handset)
        self.B4.setGeometry(QtCore.QRect(80, 340, 51, 41))
        self.B4.setObjectName(_fromUtf8("B10"))
        self.label_7 = QtGui.QLabel(self.Handset)
        self.label_7.setGeometry(QtCore.QRect(220, 390, 51, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.B2 = QtGui.QPushButton(self.Handset)
        self.B2.setGeometry(QtCore.QRect(150, 410, 51, 41))
        self.B2.setObjectName(_fromUtf8("B2"))
        self.label_8 = QtGui.QLabel(self.Handset)
        self.label_8.setGeometry(QtCore.QRect(150, 390, 51, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.B3 = QtGui.QPushButton(self.Handset)
        self.B3.setGeometry(QtCore.QRect(220, 410, 51, 41))
        self.B3.setObjectName(_fromUtf8("B3"))
        self.label_9 = QtGui.QLabel(self.Handset)
        self.label_9.setGeometry(QtCore.QRect(80, 390, 51, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.B1 = QtGui.QPushButton(self.Handset)
        self.B1.setGeometry(QtCore.QRect(80, 410, 51, 41))
        self.B1.setObjectName(_fromUtf8("B1"))
        self.label_10 = QtGui.QLabel(self.Handset)
        self.label_10.setGeometry(QtCore.QRect(220, 460, 51, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.BUP = QtGui.QPushButton(self.Handset)
        self.BUP.setGeometry(QtCore.QRect(150, 480, 51, 41))
        self.BUP.setObjectName(_fromUtf8("BUP"))
        self.label_11 = QtGui.QLabel(self.Handset)
        self.label_11.setGeometry(QtCore.QRect(150, 460, 51, 20))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.BDOWN = QtGui.QPushButton(self.Handset)
        self.BDOWN.setGeometry(QtCore.QRect(220, 480, 51, 41))
        self.BDOWN.setObjectName(_fromUtf8("BDOWN"))
        self.label_12 = QtGui.QLabel(self.Handset)
        self.label_12.setGeometry(QtCore.QRect(80, 460, 51, 20))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.B0 = QtGui.QPushButton(self.Handset)
        self.B0.setGeometry(QtCore.QRect(80, 480, 51, 41))
        self.B0.setObjectName(_fromUtf8("B0"))
        self.L4 = QtGui.QRadioButton(self.Handset)
        self.L4.setGeometry(QtCore.QRect(20, 350, 51, 22))    
        self.L4.setObjectName(_fromUtf8("L4"))
        self.L2 = QtGui.QRadioButton(self.Handset)
        self.L2.setGeometry(QtCore.QRect(20, 420, 51, 22))
        self.L2.setObjectName(_fromUtf8("L2"))
        self.L1 = QtGui.QRadioButton(self.Handset)
        self.L1.setGeometry(QtCore.QRect(20, 490, 51, 22))
        self.L1.setObjectName(_fromUtf8("L1"))
        self.LALT = QtGui.QRadioButton(self.Handset)
        self.LALT.setGeometry(QtCore.QRect(240, 220, 117, 22))
        self.LALT.setObjectName(_fromUtf8("LALT"))
        self.DISPLAY = QtGui.QTextBrowser(self.Handset)
        self.DISPLAY.setGeometry(QtCore.QRect(30, 30, 291, 21))        
        self.DISPLAY.setObjectName(_fromUtf8("DISPLAY"))
        self.DISPLAY_2 = QtGui.QTextBrowser(self.Handset)
        self.DISPLAY_2.setGeometry(QtCore.QRect(30, 50, 291, 21))
        self.DISPLAY_2.setObjectName(_fromUtf8("DISPLAY_2"))
        self.SERIALPORT = QtGui.QLineEdit(self.Handset)
        self.SERIALPORT.setGeometry(QtCore.QRect(90, 0, 151, 27))
        self.SERIALPORT.setObjectName(_fromUtf8("SERIALPORT"))
        self.BINIT = QtGui.QPushButton(self.Handset)
        self.BINIT.setGeometry(QtCore.QRect(250, 0, 71, 27))
        self.BINIT.setObjectName(_fromUtf8("BINIT"))
        self.BOPEN = QtGui.QPushButton(self.Handset)
        self.BOPEN.setGeometry(QtCore.QRect(30, 0, 51, 27))
        self.BOPEN.setObjectName(_fromUtf8("BOPEN"))
        LX200ClassicHandset.setWidget(self.Handset)
	self.BENTER.pressed.connect(on_ENTER_pressed)
	self.BENTER.released.connect(on_ENTER_released)
	self.BMODE.pressed.connect(on_MODE_pressed)
	self.BMODE.released.connect(on_MODE_released)
	self.BGOTO.pressed.connect(on_GOTO_pressed)
	self.BGOTO.released.connect(on_GOTO_released)
	self.BN.pressed.connect(on_N_pressed)
	self.BN.released.connect(on_N_released)
	self.BW.pressed.connect(on_W_pressed)
	self.BW.released.connect(on_W_released)
	self.BE.pressed.connect(on_E_pressed)
	self.BE.released.connect(on_E_released)
	self.BS.pressed.connect(on_S_pressed)
	self.BS.released.connect(on_S_released)
	self.B7.pressed.connect(on_7_pressed)
	self.B7.released.connect(on_7_released)
	self.B8.pressed.connect(on_8_pressed)
	self.B8.released.connect(on_8_released)
	self.B9.pressed.connect(on_9_pressed)
	self.B9.released.connect(on_9_released)
	self.B4.pressed.connect(on_4_pressed)
	self.B4.released.connect(on_4_released)
	self.B5.pressed.connect(on_5_pressed)
	self.B5.released.connect(on_5_released)
	self.B6.pressed.connect(on_6_pressed)
	self.B6.released.connect(on_6_released)
	self.B1.pressed.connect(on_1_pressed)
	self.B1.released.connect(on_1_released)
	self.B2.pressed.connect(on_2_pressed)
	self.B2.released.connect(on_2_released)
	self.B3.pressed.connect(on_3_pressed)
	self.B3.released.connect(on_3_released)
	self.B0.pressed.connect(on_0_pressed)
	self.B0.released.connect(on_0_released)
	self.BUP.pressed.connect(on_PREV_pressed)
	self.BUP.released.connect(on_PREV_released)
	self.BDOWN.pressed.connect(on_NEXT_pressed)
	self.BDOWN.released.connect(on_NEXT_released)
	#self.BOPEN.pressed.connect(on_OPEN_pressed)
	self.BINIT.pressed.connect(on_INIT_pressed)
	
        self.retranslateUi(LX200ClassicHandset)
        QtCore.QMetaObject.connectSlotsByName(LX200ClassicHandset)

    def retranslateUi(self, LX200ClassicHandset):
        LX200ClassicHandset.setWindowTitle(_translate("LX200ClassicHandset", "LX200 Classic Virtual Handset", None))
        self.BENTER.setText(_translate("LX200ClassicHandset", "ENTER", None))
        self.L8.setText(_translate("LX200ClassicHandset", "x8", None))
        self.BMODE.setText(_translate("LX200ClassicHandset", "MODE", None))
        self.BGOTO.setText(_translate("LX200ClassicHandset", "GOTO", None))
        self.BN.setText(_translate("LX200ClassicHandset", "N", None))
        self.BE.setText(_translate("LX200ClassicHandset", "E", None))
        self.BW.setText(_translate("LX200ClassicHandset", "E", None))
        self.BS.setText(_translate("LX200ClassicHandset", "S", None))
        self.B7.setText(_translate("LX200ClassicHandset", "7", None))
        self.label.setText(_translate("LX200ClassicHandset", "SLEW", None))
        self.label_2.setText(_translate("LX200ClassicHandset", "RET", None))
        self.B8.setText(_translate("LX200ClassicHandset", "8", None))
        self.label_3.setText(_translate("LX200ClassicHandset", "M", None))
        self.B9.setText(_translate("LX200ClassicHandset", "9", None))
        self.label_4.setText(_translate("LX200ClassicHandset", "STAR", None))
        self.B5.setText(_translate("LX200ClassicHandset", "5", None))
        self.label_5.setText(_translate("LX200ClassicHandset", "FOCUS", None))
        self.B6.setText(_translate("LX200ClassicHandset", "6", None))
        self.label_6.setText(_translate("LX200ClassicHandset", "FIND", None))
        self.B4.setText(_translate("LX200ClassicHandset", "4", None))
        self.label_7.setText(_translate("LX200ClassicHandset", "CNGC", None))
        self.B2.setText(_translate("LX200ClassicHandset", "2", None))
        self.label_8.setText(_translate("LX200ClassicHandset", "MAP", None))
        self.B3.setText(_translate("LX200ClassicHandset", "3", None))
        self.label_9.setText(_translate("LX200ClassicHandset", "CNTR", None))
        self.B1.setText(_translate("LX200ClassicHandset", "1", None))
        self.label_10.setText(_translate("LX200ClassicHandset", "NEXT", None))
        self.BUP.setText(_translate("LX200ClassicHandset", "U", None))
        self.label_11.setText(_translate("LX200ClassicHandset", "PREV", None))
        self.BDOWN.setText(_translate("LX200ClassicHandset", "D", None))
        self.label_12.setText(_translate("LX200ClassicHandset", "GUIDE", None))
        self.B0.setText(_translate("LX200ClassicHandset", "0", None))
        self.L4.setText(_translate("LX200ClassicHandset", "x4", None))
        self.L2.setText(_translate("LX200ClassicHandset", "x2", None))
        self.L1.setText(_translate("LX200ClassicHandset", "x1", None))
        self.LALT.setText(_translate("LX200ClassicHandset", "ALT", None))
        self.SERIALPORT.setText(_translate("LX200ClassicHandset", "/dev/ttyUSB01", None))
        self.BINIT.setText(_translate("LX200ClassicHandset", "Initalise", None))
        #self.BOPEN.setText(_translate("LX200ClassicHandset", "Open", None))

def on_ENTER_pressed():
	ser.write(chr(0x0d))
def on_ENTER_released():
	ser.write(chr(0x8d))
def on_MODE_pressed():
	ser.write(chr(0x4d))
def on_MODE_released():
	ser.write(chr(0xcd))
def on_GOTO_pressed():
	ser.write(chr(0x47))
def on_GOTO_released():
	ser.write(chr(0xc7))
def on_N_pressed():
	ser.write(chr(0x4e))
def on_N_released():
	ser.write(chr(0xce))
def on_W_pressed():
	ser.write(chr(0x57))
def on_W_released():
	ser.write(chr(0xd7))
def on_E_pressed():
	ser.write(chr(0x45))
def on_E_released():
	ser.write(chr(0xc5))
def on_S_pressed():
	ser.write(chr(0x53))
def on_S_released():
	ser.write(chr(0xd3))
def on_7_pressed():
	ser.write(chr(0x37))
def on_7_released():
	ser.write(chr(0xb7))
def on_8_pressed():
	ser.write(chr(0x38))
def on_8_released():
	ser.write(chr(0xb8))
def on_9_pressed():
	ser.write(chr(0x39))
def on_9_released():
	ser.write(chr(0xb9))
def on_4_pressed():
	ser.write(chr(0x34))
def on_4_released():
	ser.write(chr(0xb4))
def on_5_pressed():
	ser.write(chr(0x35))
def on_5_released():
	ser.write(chr(0xb5))
def on_6_pressed():
	ser.write(chr(0x36))
def on_6_released():
	ser.write(chr(0xb6))
def on_1_pressed():
	ser.write(chr(0x31))
def on_1_released():
	ser.write(chr(0xb1))
def on_2_pressed():
	ser.write(chr(0x32))
def on_2_released():
	ser.write(chr(0xb2))
def on_3_pressed():
	ser.write(chr(0x33))
def on_3_released():
	ser.write(chr(0xb3))
def on_0_pressed():
	ser.write(chr(0x30))
def on_0_released():
	ser.write(chr(0xb0))
def on_PREV_pressed():
	ser.write(chr(0x2e))
def on_PREV_released():
	ser.write(chr(0xae))
def on_NEXT_pressed():
	ser.write(chr(0x44))
def on_NEXT_released():
	ser.write(chr(0xc4))
def on_INIT_pressed():
	ser.write(chr(0xFF))
	ser.write(chr(0xFF))
	ser.write(chr(0xFF))
	ser.write(chr(0xFF))
	ser.write(chr(0xFF))
	ser.write(chr(0x2a))

def on_OPEN_pressed():
	ser.write("open")	

def serial_read():
	ui.SERIALPORT.setText(SPORT)
	if ser.in_waiting > 0:
		line=ser.readline()
		# check to see if the line has 1B (starting char) in it
		LINETERM=line.find(chr(0x1b))
		LINESTART=0
		LINEEND=1
		#print len(line)
		print line.encode('hex')

		if LINETERM == -1:
			DISPLAYLINE[2]=DISPLAYLINE[2]+line
		else:
			while LINEEND != len(line):
				LINEEND = line.find(chr(0x1b),LINESTART+1)
				if LINEEND == -1:
					# this is a null, but it messes up the searching, so we end a line with it
					LINEEND = line.find(chr(0x00),LINESTART+1)
				if LINEEND == -1:
					LINEEND = len(line)
				LINEDISPLAYNO = line[LINESTART+1:LINESTART+2]
				if LINEDISPLAYNO == '1':
					if len(line[LINESTART+2:LINEEND])<=1:
						# this is a marker line 
						DISPLAYLINE[1]=line[LINESTART+2:LINEEND] + DISPLAYLINE[1][1:]
					else:
						DISPLAYLINE[1]=line[LINESTART+2:LINEEND]
				elif LINEDISPLAYNO == '2':
                                        if len(line[LINESTART+2:LINEEND])<=1:
                                                # this is a marker line
                                                DISPLAYLINE[2]=line[LINESTART+2:LINEEND] + DISPLAYLINE[2][1:]
                                        else:
                                                DISPLAYLINE[2]=line[LINESTART+2:LINEEND]
				elif LINEDISPLAYNO == 'C':
					DISPLAYLINE[1]=line[LINESTART+2:LINEEND]
					DISPLAYLINE[2]=""
				elif LINEDISPLAYNO == 'D':
					if line[LINESTART+2:LINESTART+3]==chr(0x01):
						print "ALT LED ON"
						ui.LALT.setAutoExclusive(False)
						ui.LALT.setChecked(True)
						ui.LALT.setAutoExclusive(True)
					else:
						ui.LALT.setAutoExclusive(False)
                                                ui.LALT.setChecked(False)
						ui.LALT.setAutoExclusive(True)
						print "ALT LED OFF"
				elif LINEDISPLAYNO == 'L':
					if line[LINESTART+2:LINESTART+3]==chr(0x08):
						print "Speed x8 LED ON"
						ui.L8.setChecked(True)
					elif line[LINESTART+2:LINESTART+3]==chr(0x04):
						print "Speed x4 LED ON"
						ui.L4.setChecked(True)
					elif line[LINESTART+2:LINESTART+3]==chr(0x02):
						print "Speed x2 LED ON"
						ui.L2.setChecked(True)
					elif line[LINESTART+2:LINESTART+3]==chr(0x01):
						print "Speed x1 LED ON"
						ui.L1.setChecked(True)
				#print LINESTART,LINEEND
				LINESTART=LINEEND
		ui.DISPLAY.setText(DISPLAYLINE[1])
		ui.DISPLAY_2.setText(DISPLAYLINE[2])


try:
	ser = serial.Serial(SPORT, 9600, timeout=0.01)
	ser.isOpen()
except:
	print "Failed to connect"
	#exit()


if __name__ == "__main__":
    DISPLAYLINE = ["line0","line1","line2"]
    import sys
    app = QtGui.QApplication(sys.argv)
    LX200ClassicHandset = QtGui.QDockWidget()
    ui = Ui_LX200ClassicHandset()
    ui.setupUi(LX200ClassicHandset)
    LX200ClassicHandset.show()
    #sys.exit(app.exec_())
    timer=QTimer()
    timer.timeout.connect(serial_read)
    timer.start(150)
    app.exec_()

