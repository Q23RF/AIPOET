from flask import Flask, render_template, redirect, request, send_from_directory
from random import randint
from poet import write
from mail import send
from post import write_on_img, send_line

app = Flask(__name__)
urls = ["https://genshin.hoyoverse.com/zh-tw/?gad_source=1&gclid=Cj0KCQjw-5y1BhC-ARIsAAM_oKkTSAn4TSQ50pyw2CICHlzWVETleLrG869aLrKdAspZmqZJVxzRIYgaAhBdEALw_wcB",
        "https://youtu.be/dQw4w9WgXcQ?si=yQi6RYOGE7kEJB2h"]
@app.route('/', methods=["POST", "GET"])
def main():
    if request.method == "POST":
        if int(request.form["id"])==1:	#寫詩
            n = int(request.form["n"])
            style = int(request.form["style"])
            if n <= 0:
                return redirect(urls[randint(0,1)])
            re = write(n, style)
            return render_template('main.html', poem=re)
        else:	#下載
            p = request.form["poem"]
            plist = p[2:-2].split("', '")
            ptext=""
            for line in plist:
                line = line.replace("\\n", "\n")
                ptext += line
            if int(request.form["id"])==3:	#要影印
                send_line(ptext)
            re = write_on_img(plist).save("data/pc.png")
            return send_from_directory('data', "pc.png", as_attachment=True)

    return render_template('main.html', poem='')


@app.route('/feedback', methods=["POST", "GET"])
def feedback():
    if request.method == "POST":
        fb = request.form["fb"]
        send_line("FEEDBACK: "+fb)
    return render_template('feedback.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(host='127.0.0.1', port=8080, debug=False)
