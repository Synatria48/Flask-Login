from flask import Flask, render_template, request, session, url_for, redirect

main = Flask(__name__)
main.config["SECRET_KEY"] = "iniSecretKey2021"
main.jinja_env.filters["zip"] = zip

@main.route("/")
def halaman_utama():
    if "user" not in session:
        return redirect(url_for('halaman_login'))
    else:
        return render_template("index.html")

@main.route("/login", methods = ["POST", "GET"])
def halaman_login():
    if "user" in session:
        return redirect(url_for('sukses'))
    else :
        if request.method == 'POST':
            user = request.form['user']
            password = request.form['pass']
            if user == 'admin@gmail.com' and password == 'admin':
                session['user'] = user
                return redirect(url_for('sukses'))
            else:
                return redirect(url_for('halaman_login'))
        return render_template("login.html")

@main.route("/logout")
def halaman_logout():
    if "user" not in session:
        return redirect(url_for('halaman_login'))
    else:
        session.pop("user")
        return redirect(url_for('halaman_login'))

@main.route("/sukses")
def sukses():
    if "user" in session:
        data = "Anda berhasil Login, silahkan klik tombol menu lainnya"
        return render_template("sukses.html", data=data)
    else:
        return redirect(url_for('halaman_login'))

@main.route("/about")
def halaman_about():
    if "user" not in session:
        return redirect(url_for('halaman_login'))
    else:
        return render_template("about.html")

@main.route("/contact")
def halaman_contact():
    data_contact  = {
        "no" : [1,2,3],
        "jenis" : ["Telp", "LinkedIn", "Email"],
        "kontak" : [629695028666, "synatria subekti", "synatria.subekti@gmail.com"]
    }
    if "user" not in session:
        return redirect(url_for('halaman_login'))
    else:
        return render_template("contact.html", data=data_contact)

if __name__ == "__main__":
    main.run(debug=True, port=9000)
