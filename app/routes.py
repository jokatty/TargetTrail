from flask import Blueprint, request, redirect, render_template,jsonify
from sqlalchemy.orm import sessionmaker
from .models import Goal, init_db

bp = Blueprint('main', __name__)

engine = init_db()
Session = sessionmaker(bind=engine)
session = Session()

@bp.route('/')
def index():
    return "Hello, World!"

@bp.route('/goals')
def goals():
    goals = session.query(Goal).all()
    goal_list = [{'goal': goal.goal, 'duration': goal.duration} for goal in goals]
    return render_template('goals.html', goals=goal_list)

@bp.route('/new_goal', methods=['GET', 'POST'])
def new_goal():
    if request.method == 'POST':
        goal = request.form['goal']
        duration = request.form['duration']
        duration_unit = request.form['duration_unit']
        if duration_unit == 'hours':
            duration = int(duration) * 60
        duration = int(duration)
        new_goal = Goal(goal=goal, duration=duration)
        session.add(new_goal)
        session.commit()
        return redirect('/')
    return render_template('new_goal.html')
