from flask import Blueprint, render_template

from displate.displate import Displate

playground = Blueprint('playground', __name__)


@playground.route('/')
def hello():
    displates = (
        Displate("yellow", "yellow.jpg"),
        Displate("vivi", "vivi.jpg"),
        Displate("bw", "bw.jpg"),
        # Displate("lovecraft", "lovecraft.jpg"),
        # Displate("lovecraft", "lovecraft.jpg"),
        # Displate("lovecraft", "lovecraft.jpg"),
        # Displate("lovecraft", "lovecraft.jpg"),
        # Displate("lovecraft", "lovecraft.jpg"),
        # Displate("lovecraft", "lovecraft.jpg"),
        # Displate("lovecraft", "lovecraft.jpg"),
        # Displate("lovecraft", "lovecraft.jpg"),
    )

    return render_template('index.html', displates=displates)
