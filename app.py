from flask import Flask, render_template, url_for

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page ("/")
@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/admin")  # URL error isliye aya admin ko register karna padega agar urlfor ka jinja tag use kar rha ho
def admin():           # Function name
    return render_template("Admin.html")

# Run the application if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)