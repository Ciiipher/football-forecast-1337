from framework.request_handler import  FFRequestHandler

class Home(FFRequestHandler):
    def get(self):

        self.render('home/home.html')