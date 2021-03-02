from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import Gamestop, Game
from app.main.forms import GamestopForm, GameForm
from app import app, db

main = Blueprint('main', __name__)

# Create your routes here.
@main.route("/")
def homepage():
    all_gamestops = Gamestop.query.all()
    return render_template("home.html", all_gamestops=all_gamestops)

@main.route('/new_gamestop', methods=['GET', 'POST'])
@login_required
def new_gamestop():
    form = GamestopForm()
    if form.validate_on_submit():
        new_gamestop = Gamestop(title=form.title.data, address=form.address.data, user=current_user)
        db.session.add(new_gamestop)
        db.session.commit()
        flash("New Gamestop was created.")
        print("gamestop created.")
        return redirect(url_for("main.homepage"))
    return render_template("new_gamestop.html", form=form)

@main.route('/new_game', methods=['GET', 'POST'])
@login_required
def new_game():
    form = GameForm()
    if form.validate_on_submit():
        print(form.gamestop.data)
        new_game = Game(name=form.name.data, photo_url=form.photo_url.data, gamestop=form.gamestop.data)
        db.session.add(new_game)
        db.session.commit()
        flash("New game was created.")
        print("game created.")
        return redirect(url_for("main.game_detail", game_id=new_game.id))
    return render_template("new_game.html", form=form)


@main.route("/gamestop/<gamestop_id>", methods=["GET", "POST"])
def gamestop_detail(gamestop_id):
    gamestop = Gamestop.query.get(gamestop_id)
    form = GamestopForm(obj=gamestop)
    if form.validate_on_submit():
        gamestop.title = form.title.data
        gamestop.address = form.address.data
        # gamestop.user = current_user
        db.session.commit()
        flash(f"{gamestop.title} was updated successfully.")
        return redirect(url_for("main.gamestop_detail", gamestop_id=gamestop.id))

    return render_template("gamestop_detail.html", gamestop=gamestop, form=form)

@main.route("/game/<game_id>", methods=["GET", "POST"])
@login_required
def game_detail(game_id):
    game = Game.query.get(game_id)
    form = GameForm(obj=game)
    if form.validate_on_submit():
        game.name = form.name.data
        game.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{game.name} was updated successfully.")
        return redirect(url_for("main.game_detail", game_id=game.id))
    return render_template("game_detail.html", game=game, form=form)
