# main.py

from flask import Flask, render_template, Response
from camera import VideoCamera
import time

app = Flask(__name__)

@app.route('/')
def index():
	t1 = time.time()
	return render_template('index.html', t1 = t1)
#end def

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
	#end while
#end def

@app.route('/video_timer')
def video_timer():
	def generate():
		while True:
			yield time.time()
	#end def
	return Response(generate(), mimetype='text/plain')
#end def

@app.route('/video_feed')
def video_feed():
	return Response(gen(VideoCamera()),f
			mimetype='multipart/x-mixed-replace; boundary=frame')
#end def

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug = True)