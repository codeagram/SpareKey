from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import InputRequired


branches = ["1GOB", "2MLR", "3POL", "4CBE", "5TPR", "6ERD", "7DG", "8KRR"]


class AddSpareKey(FlaskForm):

    branches_tuple = list()
    recepients = [("Collections")]
    for branch in branches:
        branches_tuple.append((branch, branch))

    branch = SelectField("Branch", choices=branches_tuple)
    loan_no = StringField("Loan No", validators=[InputRequired()])
    name = StringField("Name",validators=[InputRequired()])
    recepient = SelectField("Recepient", choices=recepients)
    remarks = StringField("Remarks")
    submit = SubmitField("Submit")
