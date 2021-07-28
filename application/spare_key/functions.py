from application import db
from application.spare_key.models import SpareKeyDB


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

        pass
