from flask import Flask, render_template, url_for, request, jsonify,  flash, redirect
from database import load_workout_from_db, init_db, load_workouts_from_db, add_membershipTodb,insert_trial_membership, create_tables, load_all_trainers  # Import the function to load workouts from the database
import os

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

@app.route("/api/fitnessPrograms")
def list_fitness_programs():
    works = load_workout_from_db()
    return jsonify(works)

@app.route("/admin")  # URL error isliye aya admin ko register karna padega agar urlfor ka jinja tag use kar rha ho
def admin():           # Function name
    return render_template("Admin.html")

# <id> isme value home ke loop mei applyChartCard.html se ayi hai work in works ke through value work['id'] 
@app.route("/exercisePage/<id>") # yeh apply karne ke baad wala page hai jisme us particular exercise ka info hai phir button click karne ke baad form aata hai 
def showExcercise(id):
    worked = load_workouts_from_db(id) # workout and workouts different hai
    if not worked:
        return "Not Found", 404
    else:
        return render_template("exercisePage.html", company_name='Impulse', worked=worked)

@app.route("/api/exercisePage/<id>")
def list_fitness_json(id):
    worked = load_workouts_from_db(id)
    return jsonify(worked)

@app.route("/applicationForm/<id>")
def loadApplicationPage(id):
    load = load_workouts_from_db(id)
    if not load:
        return "Form not found", 404
    else:
        return render_template("exerciseApplicationForm.html",work=load)

@app.route("/exercisePage/<mem_id>/submit_membership", methods=["POST"]) # id jagah kux aur naam dedo mem_id mei value work['id'] se pass hogi variable ka kaam kar rha hai jo bhi <id> hai inme kahi na kahi se value pass ho rhi hai
def feed_membership(mem_id):
    data = request.form # request.args bhi data leta hai but data url mei visible hota hai yeh data ko browser requests directly url ko post karta hai aur data access hota request.form se
    # work = load_workouts_from_db(mem_id)
    # print(dict(request.form))
    add_membershipTodb(mem_id, data) # yha se data load hoga database mei
    # return "Membership added successfully ✅"
    # data = request.args   # yeh output Flask console me aana chahiye
    # return jsonify(data
    return render_template("formSubmitted.html", application=data) # help in displying submitted data on this html page

@app.route("/membershipDetails")
def load_navMembership():
    return render_template("navMembership.html")


app.secret_key = os.getenv("SECRET_KEY", "fallback_key") # yeh flash ke liye banani padti hai security ke liye
@app.route("/trial", methods=["GET", "POST"])
def trial_form():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        plan_id = request.form["plan_id"]
        preferred_date = request.form["preferred_date"]

        insert_trial_membership(name, email, phone, plan_id, preferred_date)
        flash("Trial class booked successfully!", "success")
        return render_template("trialBooked.html")   # redirect nahi, direct render
    
    return render_template("trial_form.html")

@app.route("/trainerCard")
def trainer_card():
    load = load_all_trainers()
    return render_template("trainerInfo.html", info=load)

create_tables()

# Run the application if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)