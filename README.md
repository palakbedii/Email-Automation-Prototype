login page
accept username & password
login data stored in session
login successful -> redict to wwelcome page
feature logout


User visits "/"
        ↓
Login page appears
        ↓
User enters username & password
        ↓
POST request sent
        ↓
request.form.get()
        ↓
username == admin?
password == 123?
    ↓ Yes                 ↓ No
Store session["user"]      Response("Invalid Credentials")
        ↓
redirect(url_for("welcome"))
        ↓
/welcome
        ↓
"user" in session ?
    ↓ Yes              ↓ No
Welcome admin!      redirect("/")
        ↓
Logout clicked
        ↓
session.pop("user")
        ↓
redirect("/")
