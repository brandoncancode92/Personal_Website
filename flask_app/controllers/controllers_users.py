from flask_app import app
from flask import render_template

# Get Routes
# Route for rendering the Home Page.
@app.get('/')
def index():
    return render_template('homepage.html')

# Route for rendering the Game Vault page.
@app.get('/game_vault')
def view_game_vault():
    return render_template('game_vault.html')

# Route for rendering the view Heroes and Villains page.
@app.get('/heroes_and_villains')
def view_heroes_and_villains():
    return render_template('heroes_and_villains.html')

# Route for rendering the clock page.
@app.get('/clock')
def clock():
    return render_template('clock.html')

# Route for rendering the calculator page.
@app.get('/calculator')
def calculator():
    return render_template('calculator.html')