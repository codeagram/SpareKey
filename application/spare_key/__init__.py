from flask import Blueprint


SpareKey = Blueprint("SpareKey",__name__,
                    template_folder="templates",
                    static_folder="static")


from . import views
