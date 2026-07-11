from flask import Flask, request, Response, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = "supersecret"      #to lock session -> Encrypts and secures session data.

#homepage -> login page
@app.route ("/", methods=["GET", "POST"])
def login():

   valid_users = {
        'admin': '123',
        'olive': 'pass',
        'adam': 'pass123',
        'ahn': 'pass456'
   }
   
   if request.method == "POST":        #request.method -> Tells whether the request is GET, POST
      Username = request.form.get("Username")      #Retrieves a value from a submitted HTML form.
      Password = request.form.get("Password")

      if Username in valid_users and Password == valid_users[Username]:       #dictionary[value] -> returns key-value
         session["user"] = Username       #store data in session (ie, saves the username in the session) -> session["user"] = "Olive".
         return redirect(url_for("welcome"))
      else:
         return Response("<h2 style='color:red;text-align:center;'>Invalid Credentials. Try Again.</h2>",mimetype="text/html")       #Tells the browser whether response is text/HTML


   return '''
         <!DOCTYPE html>
         <html>
            <head>
               <title>Email Scheduler Login</title>
            </head>

            <body style="background: #f4f6f9; font-family:Arial;">
                  
               <center>
               <h1 style="color:#0d6efd;">Email Scheduler</h1>
               <p>Please login to continue.</p>
               <hr style="width: 40%;">

               <form method="POST">
               <label>Username : </label>
               <input type="text" name="Username" placeholder="Enter your username" style="width: 300px; padding: 10px; border-radius: 6px; margin-top: 5px;"><br>
               <label>Password : </label>
               <input type="password" name="Password" placeholder="Enter your password" style="width: 300px; padding: 10px; border-radius: 6px; margin-top: 5px;"><br>

               <input type="submit" value="Login">
               </form>

               </center>
            </body>
         </html>
'''

#welcome page + email form -> after login
@app.route("/welcome")
def welcome():
   
   if "user" in session:
      return f'''
            <!DOCTYPE html>
            <html>
               <head>
                  <title>Email Scheduler Login</title>
               </head>

               <body style="background: #f4f6f9; font-family:Arial;">   

                  <center>
                  <h1 style="color:#0d6efd;">Email Scheduler Dashboard</h1>                
                  <h2>Welcome, {session["user"]}!</h2>
                  <hr style="width: 70%;">

                  <form action="/schedule-email" method="POST">
                     <label>Recipient Email: </label>
                     <input type="email" name="recipient" placeholder="Enter recipient email" style="width: 500px; padding: 10px; border-radius: 6px;"><br><br>
                     <label>Subject: </label>
                     <input type="text" name="subject" placeholder="Enter subject" style="width: 500px; padding: 10px; border-radius: 6px;"><br><br>
                     <label>Message: </label>
                     <textarea name="message" rows="6" placeholder="Type your email here..." style="width: 500px; padding: 10px; border-radius: 6px;"></textarea><br><br>
                     <label>Date: </label>
                     <input type="date" name="date" style="padding: 8px; margin-left: 10px;"><br><br>
                     <label>Time: </label>
                     <input type="time" name="time" style="padding: 8px; margin-left: 10px;"><br><br>

                     <button type="submit" style="padding: 14px 35px; background: #0d6efd; color: white; font-size: 16px;
                                                   border: none; border-radius: 6px; cursor: pointer;">Schedule Email</button><br>
                  </form>

                  <a href="{url_for("logout")}" style="color: red; font-size: 18px; text-decoration: none;">Logout</a>
   '''
   return redirect(url_for("login"))

#flask receiving the form -> sending data to FastAPI
@app.route("/schedule-email", methods=["POST"])
def schedule():

   data = {
        "recipient": request.form["recipient"],
        "subject": request.form["subject"],
        "message": request.form["message"],
        "date": request.form["date"],
        "time": request.form["time"]
    }
   response = requests.post(
      "http://127.0.0.1:8000/schedule",
      json=data
   )

   if response.status_code == 200:
      return "Email Scheduled Successfully!"
   else:
      return "Something went wrong."

#returning values in table at route "/allemails"
@app.route("/allemails")
def callallemails():

   response = requests.get("http://127.0.0.1:8000/allemails")
   
   if response.status_code != 200:
      return "Could not fetch emails from FastAPI."
   
   emails = response.json()

   html = """
      <h2>All Emails</h2>
      <table border="1">
      <tr>
         <th>ID</th>
         <th>Recipient</th>
         <th>Subject</th>
         <th>Message</th>
         <th>Date</th>
         <th>Time</th>
         <th>Status</th>
      </tr>
   """

   for email in emails:
      html += f"""
         <tr>
            <td>{email[0]}</td>
            <td>{email[1]}</td>
            <td>{email[2]}</td>
            <td>{email[3]}</td>
            <td>{email[4]}</td>
            <td>{email[5]}</td>
            <td>{email[6]}</td>
         </tr>
      """

   html += "</table>"

   return html


#returning values in table at route "/sent"
@app.route("/sent")
def callsent_emails():

   response = requests.get("http://127.0.0.1:8000/sent")
   
   if response.status_code != 200:
      return "Could not fetch emails from FastAPI."
   
   emails = response.json()

   html = """
      <h2>Sent Emails</h2>
      <table border="1">
      <tr>
         <th>ID</th>
         <th>Recipient</th>
         <th>Subject</th>
         <th>Message</th>
         <th>Date</th>
         <th>Time</th>
         <th>Status</th>
      </tr>
   """

   for email in emails:
      html += f"""
         <tr>
            <td>{email[0]}</td>
            <td>{email[1]}</td>
            <td>{email[2]}</td>
            <td>{email[3]}</td>
            <td>{email[4]}</td>
            <td>{email[5]}</td>
            <td>{email[6]}</td>
         </tr>
      """

   html += "</table>"

   return html

#returning values in table at route "/scheduled"
@app.route("/scheduled")
def callpendingemails():

   response = requests.get("http://127.0.0.1:8000/scheduled")
   
   if response.status_code != 200:
      return "Could not fetch emails from FastAPI."
   
   emails = response.json()

   html = """
      <h2>Scheduled Emails (Pending)</h2>
      <table border="1">
      <tr>
         <th>ID</th>
         <th>Recipient</th>
         <th>Subject</th>
         <th>Message</th>
         <th>Date</th>
         <th>Time</th>
         <th>Status</th>
      </tr>
   """

   for email in emails:
      html += f"""
         <tr>
            <td>{email[0]}</td>
            <td>{email[1]}</td>
            <td>{email[2]}</td>
            <td>{email[3]}</td>
            <td>{email[4]}</td>
            <td>{email[5]}</td>
            <td>{email[6]}</td>
         </tr>
      """

   html += "</table>"

   return html


#logout route -> here removing user-key from session -> session.pop("user")
@app.route("/logout")
def logout():
   session.pop("user", None)        #example, session["user"] = "Olive" ->  Removes the user from the session (logs them out).
   return redirect(url_for("login"))


if __name__ == "__main__":
   app.run(debug = True)