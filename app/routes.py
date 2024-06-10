from flask import Blueprint
from sqlalchemy.orm import sessionmaker
from .models import Goal, init_db

bp = Blueprint('main', __name__)

engine = init_db()
Session = sessionmaker(bind=engine)
session = Session()

@bp.route('/')
def index():
    return "Hello, World!"