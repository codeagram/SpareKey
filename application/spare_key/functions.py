from application import db
from application.spare_key.models import SpareKeyDB, FieldOfficers


class SpareKeyCRUD:


    def __init__(self):

        pass

    def add_key(self, branch, loan_no, name, recepient, remarks):

        key = SpareKeyDB(branch=branch,
                        loan_no=loan_no,
                        name=name,
                        recepient=recepient,
                        remarks=remarks)
        print("Added")

        db.session.add(key)
        db.session.commit()

        db.session.close()

    def get_all_keys(self):

        all_keys = SpareKeyDB.query.all()

        db.session.close()

        return all_keys


def get_recepients():

    recepients = FieldOfficers.name.query.all()

    db.cession.close()

    return recepients


def get_recepients_tuple(recepients):

    recepients_tuple = list()

    for name in recepients:
        recepients_tuple.append((name, name))

    return recepients_tuple
