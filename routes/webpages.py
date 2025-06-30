from flask import Blueprint, render_template, request, redirect, request, flash, url_for
from db_schema import db, Meal, Ingredient, Meal_Ingredient
import math

# Flag this file as a routes file for main.py
webpage_blueprint = Blueprint('webpage', __name__)


@webpage_blueprint.route('/configure', methods = ['GET', 'POST'])
def configure():
    pass