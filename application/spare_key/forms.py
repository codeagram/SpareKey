from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import Required
from .functions import get_recepients


branches = ["1GOB", "2MLR", "3POL", "4CBE", "5TPR", "6ERD", "7DG", "8KRR"]
recepients = get_recepients()


class AddSpareKey(FlaskForm):

    branches_tuple = list()
    recepients = [("Collections")]
    for branch in branches:
        branches_tuple.append((branch, branch))

    branch = SelectField("Branch", choices=branches_tuple)
    loan_no = StringField("Loan No", validators=[Required()])
    name = StringField("Name",validators=[Required()])
    recepient = SelectField("Recepient", choices=recepients)
    remarks = StringField("Remarks")
    submit = SubmitField("Submit")


class ReassignSpareKey(FlaskForm):

    recepient = SelectField(choices=recepients)


class AddFieldOfficer(FlaskForm):

    name = StringField("Name", validators=[Required()])


class ChangeDefaultDays(FlaskForm):

    days = IntegerField("Default Days")
