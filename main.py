import webapp2

form="""
<form action="/verification" method="post">
    Name: <input type="text" name="name" value=%(name)s ><br>
    Password: <input type="text" name="password" value=%(password)s ><br>
    Verify Password: <input type="text" name="verify" value=%(verify)s ><br>
    Email(Optional): <input type="text" name="email" value=%(email)s ><br>
    <input type="submit" value="Submit">
</form>
"""

class VerificationHandler(webapp2.RequestHandler):

    def write_form(self, inputString=""):
        self.response.write(form % {"inputString": inputString})

    def doEscape(self, s):
        return s

    def get(self):
        self.response.headers['Content-Type'] = 'html'
        self.response.write(form)

    def post(self):
        inputString = self.request.get("text")

        self.response.write(form)

app = webapp2.WSGIApplication([
    ('/verification',VerificationHandler),
], debug=True)