import webapp2
import re

form="""
<form action="/verification" method="post">
    Name: <input type="text" name="username" value="%(username)s">%(user_name_error)s<br>
    Password: <input type="password" name="password" value="%(password)s">%(pswd_error)s<br>
    Verify Password: <input type="password" name="verify" value="%(verify)s">%(verify_error)s<br>
    Email(Optional): <input type="text" name="email" value="%(email)s">%(email_error)s<br>
    <input type="submit" value="Submit">
</form>
"""

class VerificationHandler(webapp2.RequestHandler):

    def write_form(self, username="", password="", verify="", email="", user_name_error="", pswd_error="", verify_error="", email_error=""):
        self.response.write(form % {"username": username,
                                    "password":password,
                                    "verify":verify,
                                    "email":email,
                                    "user_name_error":user_name_error,
                                    "pswd_error":pswd_error,
                                    "verify_error":verify_error,
                                    "email_error":email_error})

    def get(self):
        self.write_form()

    def post(self):
        user_name = self.request.get('username')
        user_password = self.request.get('password')
        user_verification = self.request.get('verify')
        user_email = self.request.get('email')

        user_name_error = ""
        pswd_error = ""
        verify_error = ""
        email_error = ""

        if (self.validUserName(user_name) and self.validPassword(user_password) and self.validVerification(user_password, user_verification) and self.validEmail(user_email)):
            self.redirect("/welcome?username=" + user_name)

        else: 
            if(not self.validUserName(user_name)):
                user_name_error = "That's not a valid username."
            if(not self.validPassword(user_password)):
                pswd_error = "That wasn't a valid password."
                user_password = ""
                user_verification = ""
            if(self.validPassword(user_password) and not self.validVerification(user_password, user_verification)):
                verify_error = "Your passwords didn't match."
                user_password = ""
                user_verification = ""
            if(not self.validEmail(user_email)):
                email_error = "That's not a valid email."

            self.write_form(user_name,user_password,user_verification,user_email,user_name_error,pswd_error,verify_error,email_error)

    def validUserName(self, user_name):
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        return USER_RE.match(user_name)

    def validPassword(self, pswd):
        PSWD_RE = re.compile(r"^.{3,20}$")
        return PSWD_RE.match(pswd)

    def validVerification(self, first, second):
        return first == second

    def validEmail(self, email):
        if email == "":
            return True
        EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
        return EMAIL_RE.match(email)


class welcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        self.response.write("Welcome, " + username + "!")

app = webapp2.WSGIApplication([
    ('/verification',VerificationHandler),
    ('/welcome', welcomeHandler),
], debug=True)

