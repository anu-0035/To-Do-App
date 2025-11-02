from flask import Blueprint, render_template, flash, url_for, redirect, request, session

auth_bp = Blueprint('auth', __name__)

USER_CREDENTIALS = {
    'username': "admin",
    'password': "pass"
}

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
            session["user"] = username
            flash("Login successful", "success")
            return redirect(url_for("tasks.view_task"))  # ✅ redirect after successful login
        else:
            flash("Invalid username or password", "danger")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logout Successfully", "info")
    return redirect(url_for("auth.login"))
