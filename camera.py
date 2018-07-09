# camera.py

import cv2

class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)
		#self.video = cv2.VideoCapture('video.mp4')
		
	#end def
	
	def __del__(self):
		self.video.release()
	#end def
	
	def get_frame(self):
		success, image = self.video.read()
		#encode raw image to jpeg
		ret, jpeg = cv2.imencode('.jpg', image)
		return jpeg.tobytes()
	#end def