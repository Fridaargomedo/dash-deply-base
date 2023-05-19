from dash import Dash, dcc, html 
import dash_bootstrap_components as dbc 
import pandas as pd 
import plotly.express as px 

df = pd.read_csv("exams.csv)

app = Dash(
    external_stylesheets=[dbc.themes.LUX]
)

app.layout = dbc.Container([
    dbc.Card([
      dbc.CardBody([
         html.H1("Ejemplo de radio button"),
         html.Hr(),
         html.P("Un ejemplo de uso de radio button")
         dash_table.DataTable(df.to_dict("records"), page_size=10),
         dbc.Form([
             dbc.Row([
                 dbc.Label("Exam", html_for="radio exams", width=1),
                 dbc.RadioItems(
                     id="radio exams",
                     options = [
         
    ])
  ],
  className='mt-3'
  )
])

  

if __name__ == '__main__':
    app.run_server(debug=True)


    
    
