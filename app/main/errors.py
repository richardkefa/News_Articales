from flask import render_template
from . import main

@main.errorhandler(404)
def four_ow_four(error):
  '''
  function to render the 404 error page
  '''
  return render_template('fourowfour.html'),404
