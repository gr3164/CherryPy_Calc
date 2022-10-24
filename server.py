import os
import cherrypy
import datetime

css_handler = cherrypy.tools.staticdir.handler(section="/", dir='path/to/css')
cherrypy.tree.mount(css_handler, '/css')


def Calculation(num1,num2,operator):
    if (operator == "+"):
        return num1+num2
    if (operator == "-"):
        return num1-num2
    if (operator == "*"):
        return num1*num2
    if (operator == "/"):
        return num1/num2
    if (operator == "%"):
        return num1%num2

def Time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time
def Date():
    date1 = datetime.date.today()
    return date1

class Calculator:
   
    def index(self):
        m1 = str(Time())
        m2 = str(Date())
        fx = open("index.html", encoding='utf-8').read().format(Time=m1, Date=m2)
        return fx
    index.exposed = True

    def Post_Calc(self,num1,num2,select1):
        return str(Calculation(int(num1),int(num2),select1))
    Post_Calc.exposed = True

conf={"/css": {"tools.staticdir.on": True,
               "tools.staticdir.dir": os.path.abspath("./css"),},
       '/joey_css.css':
                    { 'tools.staticfile.on':True,
                      'tools.staticfile.filename': os.path.abspath("./css/style.css"),
                    },
        "/img": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": os.path.abspath("./img"),}   
               }

cherrypy.quickstart(Calculator(),config=conf)