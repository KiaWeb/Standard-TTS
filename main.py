import load
from flask import Flask, render_template, request, Response
from markupsafe import escape

app = Flask(__name__)
n = None
na = "Kia TTS"
y = "We're innovating."
v = "1.0"
patch = n

@app.route("/")
def i():
	if not patch:
		return render_template("index.html",v=v,na=na)
	else:
		return Response(patch,status=503,mimetype='text/plain')
	
@app.route("/post",methods=["POST","GET"])
def p():
	if not patch:
		tts = load.TextToSpeech()
		pr = request.form
		return render_template("sound.html",na=na,mp3=tts.get_pronunciation(pr['t']),t=pr['t'],escape=escape)
	else:
		return Response(patch,status=503,mimetype='text/plain')
	
@app.route("/tts",methods=["POST"])
def a():
	if not patch:
		tts = load.TextToSpeech()
		pr = request.json
		return Response("{'file':"+"http://localhost:5000/"+tts.get_pronunciation(pr['text'])+"}",status=200,mimetype='application/json')
	else:
		return Response(patch,status=503,mimetype='application/json')
	
	
app.run(host="127.0.0.1",port=5000)