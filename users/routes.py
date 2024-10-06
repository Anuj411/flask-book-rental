from flask import Blueprint, redirect, render_template, request, url_for
from .forms import UserRegistrationForm
from . import users
from .models import user
from extensions import db


@users.route("/")
def user_list():
    users = user.query.all()
    return render_template("users/user_list.html", users=users)


@users.route("create/", methods=["GET", "POST"])
def user_create():
    form = UserRegistrationForm()
    if request.method == "GET":
        return render_template("users/user_form.html", form=form)
    else:
        if form.validate_on_submit():
            email = form.email.data
            full_name = form.full_name.data
            password = form.password.data
            
            try:
                user_obj = user(
                    full_name=full_name,
                    email=email,
                    password=password,
                )

                db.session.add(user_obj)
                db.session.commit()
                
            except Exception as e:
                db.session.rollback()
                print(f"Error: {e}")
        else:
            print(f"==>> form: {form.errors}")
            return render_template("users/user_form.html", form=form)

        return redirect(url_for("users.user_list"))


@users.route("update/<int:user_id>", methods=["GET", "POST"])
def user_update(user_id):
    user_obj = user.query.get_or_404(user_id)
    form = UserRegistrationForm(obj = user_obj)

    if request.method == "GET":
        return render_template("users/user_form.html", form=form, user=user_obj)
    else:
        if form.validate_on_submit():
            form.populate_obj(user_obj)
            
            try:
                db.session.commit()
                return redirect(url_for("users.user_list"))
                
            except Exception as e:
                db.session.rollback()
                print(f"Error: {e}")
        else:
            print(f"==>> form: {form.errors}")
            return render_template("users/user_form.html", form=form, user=user_obj)

    return render_template("users/user_form.html", form=form, user=user_obj)