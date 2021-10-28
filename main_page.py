'''
Importing packages and dependencies
DASH - application framework for the dashboard
pandas - data handeling and cleaning
numpy - data handeling and cleaning
mysql.connect - connector to data base
'''
import DASH
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import mysql.connector

connection = mysql.connector.connect(user = 'user',
                                     password = 'password',
                                     host = '127.0.0.1,
                                     database = 'database')

# Initializing the app framework
app = dash.Dash(__name__)




# Runs app on local server 
if __name__ == '__main__':
  app.server_run(debug=True)
