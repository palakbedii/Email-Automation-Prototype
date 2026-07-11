login page <br>
accept username & password <br>
login data stored in session<br>
login successful -> redict to wwelcome page<br>
feature logout<br><br>


User visits "/"<br>
        ↓<br>
Login page appears<br>
        ↓<br>
User enters username & password<br>
        ↓<br>
POST request sent<br>
        ↓<br>
request.form.get()<br>
        ↓<br>
username == admin?<br>
password == 123?<br>
    ↓ Yes<t>                 ↓ No<br>
Store session["user"]<t>      Response("Invalid Credentials")<br>
        ↓<br>
redirect(url_for("welcome"))<br>
        ↓<br>
/welcome<br>
        ↓<br>
"user" in session ?<br>
    ↓ Yes<t>              ↓ No<br>
Welcome admin!<t>      redirect("/")<br>
        ↓<br>
Logout clicked<br>
        ↓<br>
session.pop("user")<br>
        ↓
redirect("/")
