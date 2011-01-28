from Cheetah.Template import Template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
import os


class MainHandler(webapp.RequestHandler):
  def get(self):
    path = os.path.join(os.path.dirname(__file__), 'templates/cheetahtest.tmpl')
    user = users.get_current_user()
    if not user:
      user = "Anonymous"
    template_values = {'user': user}
    tmpl = Template(file=path, searchList=(template_values,))
    self.response.out.write(tmpl)


app = webapp.WSGIApplication([
  ('/', MainHandler),
], debug=True)


def main():
  util.run_wsgi_app(app)


if __name__ == '__main__':
  main()
