from . import SpareKeyBP
from flask import render_template, redirect
from .forms import AddSpareKey
from .functions import SpareKeyCRUD


@SpareKeyBP.route("/")
def index():

    return render_template("index.html")


@SpareKeyBP.route("/documentation", methods=["GET", "POST"])
def documentation():

    form = AddSpareKey()

    if form.validate_on_submit():
        print("Valid")
        add = SpareKeyCRUD()
        add.add_key(form.branch.data,
                    form.loan_no.data,
                    form.name.data,
                    form.recepient.data,
                    form.remarks.data)

        return redirect("documentation")

    return render_template("documentation.html", form=form)


@SpareKeyBP.route("/collections")
def collections():

    form = AddSpareKey()

    return render_template("collections.html", form=form)


@SpareKeyBP.route("/SpareKeyAdmin")
def spare_key_admin():

    return render_template("spare_key_admin.html")
