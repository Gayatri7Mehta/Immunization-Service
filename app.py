from flask import Flask, render_template

app = Flask(__name__)

# This is a temporary in-memory database for demonstration purposes.
# In a production application, you should use a proper database system.
child_data = []

@app.route('/')
def home():
    return "welcome to child immunization service"

@app.route('/register', methods=['GET', 'POST'])
def register():

    return render_template('registration.html')

@app.route('/schedule')
def schedule():
    # Display the child's schedule based on the data in child_data
    return render_template('vaccination_schedule.html')

if __name__ == '__main__':
    app.run(debug=True)
