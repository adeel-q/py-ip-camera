from camera import VideoCamera

def gen(camera):
	while True:
		frame = camera.get_frame()
		print(frame)
		#yield (b'--frame\r\n'
		#	b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
	#end while
#end def

if __name__ == '__main__':
	cam = VideoCamera();
	gen(cam)