from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "nothing to see here"

@app.route('/')
def home():
    return render_template("home.html")

@app.route ('/result', methods =['POST'])
def result():
    print(request.form)
    your_name = request.form['your_name']
    dojo_location = request.form['dojo_location']
    favorite_language = request.form['favorite_language']
    comment_optional = request.form ['comment_optional']
    session["your_name"] = request.form.get("your_name")
    print(f"Name: {{your_name}}")
    print(f"Dojo Location: dojo_location")
    print(f"favorite_language")
    print(f"comment")

    return render_template('result.html', your_name = your_name, dojo_location = dojo_location, favorite_language = favorite_language, comment_optional = comment_optional)


if __name__ == "__main__":
    app.run(debug=True)