from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "iniSecretKey2021"

@app.route("/homes")
def halamanhome():
    umur = 21
    hari = ['Senin','Selasa']
    hati = "Senang"
    return render_template("index.html", umur=umur, hari=hari, hati=hati)

@app.route("/about")
def halamanabout():
    return render_template("about.html")

@app.route("/contact")
def halamancontact():
    return render_template("contact.html")

@app.route("/parsing/<int:nilai>")
def parsingku(nilai):
    return "Nilainya adalah {}".format(nilai)

@app.route("/parsingargument")
def parsingargument():
    url = request.args.get("p")
    return "Nilai parsing adalah {}".format(url)

@app.route("/halaman/<int:nilai>")
def session_1(nilai):
    session["angka"] = nilai
    return "Anda berhasil set Sessions"

@app.route("/halaman/lihat")
def lihatsession():
    try:
        data = session["angka"]
        return "Anda memiliki session {}".format(data)
    except:
        return "Anda belum memiliki session"

@app.route("/halaman/destroy")
def hapussession():
    session.pop("angka")
    return "Anda telah menghapus session"

if __name__ == "__main__":
    app.run(debug=True)
