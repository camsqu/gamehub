from flask import Flask, url_for, render_template

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/pg1")
def render_page1():
    return render_template('page1.html')


@app.route("/pg2")
def render_page2():
    return render_template('page2.html')


if __name__=="__main__":
    app.run(debug=False, port=54321)
