"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Survey(Controller):
    def __init__(self, action):
        super(Survey, self).__init__(action)
 
   
    def index(self):
        if 'submit' not in session:
            session['submit'] = 0
        if 'name' not in session:
            session['name'] = ''
        if 'dojo_location' not in session:
            session['dojo_location'] = ''       
        if 'Favorite_Language' not in session:
            session['Favorite_Language'] = ''

        if 'comments' not in session:
            session['comments'] = ''
     
        return self.load_view('index.html')

    def process(self):
        session['name'] = request.form['name']
        session['dojo_location'] = request.form['dojo_location']
        session['Favorite_Language'] = request.form['Favorite_Language']
        session['comments'] = request.form['comments']
        session['submit'] += 1
        return redirect('/result')

    def result(self):
        return self.load_view('result.html')