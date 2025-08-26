from flask import Flask, render_template, url_for
from database import load_workout_from_db, init_db  # Import the function to load workouts from the database

init_db() # yeh function initializes the database and creates the table if it doesn't exist and also create .db file but not db folder
print("Database initialized ✅")

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page ("/")
@app.route("/")
def home():
    works = load_workout_from_db()  # Load jobs from the database using the function imported from database.py
    # return render_template(Home.html)
    return render_template("Home.html", works=works, company_name='Impulse')
    # some website allows access to dynamic data using API
    # Json is simply JavaScript objects

@app.route("/admin")  # URL error isliye aya admin ko register karna padega agar urlfor ka jinja tag use kar rha ho
def admin():           # Function name
    return render_template("Admin.html")



# Run the application if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)