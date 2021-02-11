from flask import Flask, request, render_template
#----------------------------------------
# Hello Flask World
#
# Going through basic use of python's 
# flask framework.
#
# Usage:
#   $ flask run
#----------------------------------------
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def test(): 
    if request.method == "POST": 
        # Getting html user input
        first_name = request.form.get("fname") 
        last_name = request.form.get("lname")

        # Printing retrieved to terminal  
        print(first_name)
        print(last_name)

        # Building the return value string
        ret_val = "The name you entered is "
        ret_val += first_name
        ret_val += " "
        ret_val += last_name

        return ret_val 
    return render_template("form.html") 


if __name__ == '__main__':
    app.run()