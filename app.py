from dash import Dash, dcc, html 
import dash_bootstrap_components as dbc 

import pandas as pd 

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Card([
      dbc.CardBody([
         html.H1("Hello from Dash! In a new environment"),
         html.Hr(),
         html.P("I created and evnironment for this fashboard")
         
    ])
  ],
  className='mt-3'
  )
])

  

if __name__ == '__main__':
    app.run_server(debug=True)


    
    