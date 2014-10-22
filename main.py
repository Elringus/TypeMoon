import webapp2
import jinja2
import os
from webapp2 import WSGIApplication, Route


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self, *args, **kwargs):
        template = JINJA_ENVIRONMENT.get_template('templates/main.html')
        self.response.write(template.render())


routes = [
    Route(r'/<:.*>', handler=MainHandler)
]

app = WSGIApplication(routes, debug=False)

