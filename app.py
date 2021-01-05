from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story
app= Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def prompt_form():
    prompts = story.prompts
    return render_template("prompt_form.html",prompts = prompts)

@app.route('/story')
def show_story():
    fin_story = story.generate(request.args)
    return render_template("story.html",fin_story = fin_story)
