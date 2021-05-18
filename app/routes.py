from app.forms import MiastoForm
from flask import render_template, url_for,flash, redirect
from app import app

@app.route('/')
def home():
   return "hello world!"