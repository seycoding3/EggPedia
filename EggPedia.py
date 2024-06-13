from flask import *
app = Flask("EggPedia")
@app.route('/',methods = ["POST","GET"])
def main():
    if request.method == "POST":
        ttle = request.form["query"]
        return redirect(f"https://m.youtube.com/results?sp=mAEA&search_query={ttle}")
    else:
        return f"<title>EggPedia</title><h2>Youtube Search</h2><form action='#' method='post'><input name='query'><button type='sumbit'>Search</button></form><a type='button' href='/google'>Google Search</a>"

@app.route("/google",methods=["POST","GET"])
def gs():
    if request.method == "POST":
        ttle = request.form["query"]
        if ttle == "Google Gravity":
            return redirect("https://mrdoob.com/projects/chromeexperiments/google-gravity/")
        else:
            return redirect(f"https://www.google.com/search?q={ttle}")
    else:
      return f"<title>EggPedia</title><h2>Google Search</h2><form action='#' method='post'><input name='query'><button type='sumbit'>Search</button></form><a href='/'>YouTube Search</a>"
app.run("localhost",port=2000,debug=False)