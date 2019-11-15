from flask import Flask, render_template, request
import time
import sys
import json
# encoding=utf8

from pykondo import *
from twisted.python import log
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.wsgi import WSGIResource
from autobahn.twisted.websocket import WebSocketServerFactory, \
    WebSocketServerProtocol
app = Flask(__name__)
from autobahn.twisted.resource import WebSocketResource, WSGIRootResource


class EchoServerProtocol(WebSocketServerProtocol):
	# web socket icin twisted tabanlı autobahn framework u kullandık.  web socket daha hızlı olacağı icin
	#javascriptte gonder fonksiyonu calistiginda fonksiyon onMessage
    def onMessage(self, payload, isBinary):
	
        message = payload.decode('utf8')
        message = json.loads(message)
	
	#print message["servo_id"]
	#print message["frame"]
	#servo_id = message["servo_id"]
	#print 2
	#frame = message["frame"]
	#realKondo.setServoPos(servo_id, frame)
	
	for i in range(4):
	    realKondo.hareketEt(str(message["pos"+str(i+1)]))
	    print message["pos"+str(i+1)]
	    
	
	self.sendMessage(payload, isBinary)
	

@app.route('/', methods=['POST', 'GET'])
def hello_world():
	#sayfa ilk istendiğinde ve tanımlı hareketler calismasi istendiğinde sunucuya bir istek gönderilir.
	#bu istek bu fonksiyonu calistirir.
    BATARYA = "Robot calisir durumda degil"
    
    if request.method == "POST":
        try:
            komut = request.json['komut']
            hareket_adi = request.json['hareket_adi']
            # print komut + hareket_adi
            if komut == "hareket":
                realKondo.playMotion(motions[hareket_adi])
        except Exception as e:
            print (e.message)
    elif request.method == "GET":
        try:
            BATARYA = realKondo.readBatteryLevel()
        except Exception as e:
            pass
    
    return render_template('tasarimsaacma.html', {"batarya": BATARYA)


@app.route('/basic')
def kondo_socket_page():
    return render_template('deneme.html')


class DummyKondo(object):
    def __init__(self):
        print("DummyCondo olusturuldu")

    def readBatteryLevel(self):
        return ("Batarya Leveli Super")

    def playMotion(self, motion_id):
        time.sleep(60)
        print ("Playing Kondo Motion %", motion_id)

    def close(self):
        print ("DummyKondo yorgun....kapandi.......")

class RealKondo(object):
    def __init__(self):
        self.max_wait = 50 * 1000000

        self.ki = KondoInstance()

        ret = kondo_init(self.ki)

        print(self.ki.error)
    def setServoPos(self, id, frame):
	kondo_set_servo_pos(self.ki, int(id), int(frame))

    def readBatteryLevel(self):
        print("reading battery level")

        level=0

        ret = kondo_read_analog(self.ki,level, 0)

        if ret < 0:
	    #print type(ret), len(ret)
	    #print ret
	    #print ret[1]
            sys.exit(self.ki.error)

        return ret[1]

    def playMotion(self, motion_id):
        print ("Playing Kondo Motion %", motion_id)

        ret = kondo_play_motion(self.ki, motion_id, self.max_wait)

        if ret < 0:

            sys.exit(self.ki.error)
    def hareketEt(self, pos):
	ret = kondo_hareket(self.ki, pos)
        if ret < 0:
            sys.exit(self.ki.error)

    def close(self):
        ret = kondo_close(self.ki)

        if ret < 0:

            sys.exit(self.ki.error)
if __name__ == '__main__':
    motions = {
        "Greeting": 0,
        "Home Position": 1,
        "Wave": 2,
        "HipHipHipHurray": 3,
        "Chagrined": 4,
        "Headstand": 5,
        "Clap": 6,
        "10 Claps": 7,
        "Rythm claps": 8,
        "Push-ups": 9,
        "One legged bend": 10,
        "Bunny hop A": 11,
        "Bunny hop B": 12,
        "Stand-up stomach": 13,
        "Stand-up back": 14,
        "Safewalk forward": 15,
        "Safewalk backward": 16,
        "Safewalk left": 17,
        "Safewalk right": 18,
        "Quickturn left": 19,
        "Quickturn right": 20,
        "Regular walk forward": 21,
        "Regular walk back": 22,
        "Regular walk left": 23,
        "Regular walk right": 24,
        "Kick ball fwd left": 25,
        "Kick ball fwd right": 26,
        "Kick ball side left": 27,
        "Kick ball side right": 28,
        "Kick ball backwd left": 29,
        "Kick ball backwd right": 30
    }

    try:
        # batarya leveli(fake) denemek icin raise Exception yorumdan al..
        #raise Except
        dummyKondo = DummyKondo()
	
	
    except Exception as e:
        e.message
    realKondo = RealKondo()
    #realKondo.hareketEt("2B 10 3D F3 3F 00 00 14 4C 1D 4C 1D 4C 1D 4C 1D 4C 1D 4C 1D 4C 1D 4C 1D 4C 1D 4C 1D 4C 1D 4C 1D 4C 1D 4C 1D 4C 1D 4C 1D 4C 1D B7")
    
    log.startLogging(sys.stdout)  # create a Twisted Web resource for our WebSocket server
    wsFactory = WebSocketServerFactory(u"ws://0.0.0.0:8080")#127.0.0.1
    wsFactory.protocol = EchoServerProtocol
    wsResource = WebSocketResource(wsFactory)

    # create a Twisted Web WSGI resource for our Flask server
    wsgiResource = WSGIResource(reactor, reactor.getThreadPool(), app)

    # create a root resource serving everything via WSGI/Flask, but
    # the path "/ws" served by our WebSocket stuff
    rootResource = WSGIRootResource(wsgiResource, {b'ws': wsResource})

    # create a Twisted Web Site and run everything
    site = Site(rootResource)

    reactor.listenTCP(8080, site)
    reactor.run()



