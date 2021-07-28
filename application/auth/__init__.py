from flask import Blueprint


AuthBP = Blueprint("AuthBP", __name__,
                    template_folder="templates",
                    static_folder="static")


from . import routes
