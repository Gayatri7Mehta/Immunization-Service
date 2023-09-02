from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This is a temporary in-memory database for demonstration purposes.
# In a production application, you should use a proper database system.
child_data = []

@app.route('/')
def home():
    return "Welcome to the Child Immunization Service"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Process the submitted form data
        child_name = request.form.get('child_name')
        age = request.form.get('age')
        # Add the child's data to the temporary database
        child_data.append({'child_name': child_name, 'age': age})
        # Implement scheduling logic here based on age
        # For demonstration, just redirect to the scheduling page
        return redirect(url_for('schedule'))
    return render_template('registration.html')

@app.route('/schedule')
def schedule():
    # Display the child's schedule based on the data in child_data
    return render_template('vaccination_schedule.html', child_data=child_data)

if __name__ == '__main__':
    app.run(debug=True)
