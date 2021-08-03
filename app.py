import os

import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import sqlalchemy as db
import pandas as pd
from datetime import datetime
from decouple import config

# themes available at https://www.bootstrapcdn.com/bootswatch/
BS = "https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lux/bootstrap.min.css"
app = dash.Dash(__name__, external_stylesheets=[BS])
app.title = "Overwatch Team Stats"

url = config("URL")
table_name = "overwatch_team_stats"

# for a quick tutorial check out https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91
engine = db.create_engine(url)
connection = engine.connect()
metadata = db.MetaData()
data = db.Table(table_name, metadata, autoload_with=engine)

df = pd.read_sql_table(table_name, url)
df.sort_values(by=["id"], ascending=False, inplace=True)
df["timestamp"] = df["timestamp"].dt.strftime("%a %d.%m.%Y %H:%M")

app.layout = dbc.Container(
    [
        html.H1("Overwatch Team Stats"),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5("Stack"),
                        dbc.Select(
                            id="stack",
                            options=[
                                {"label": "2", "value": 2},
                                {"label": "3", "value": 3},
                                {"label": "4", "value": 4},
                            ],
                        ),
                    ],
                    width="auto",
                ),
                dbc.Col(
                    [
                        html.H5("Comp. mode"),
                        dbc.Select(
                            id="competitive_mode",
                            options=[
                                {"label": "Open", "value": "Open"},
                                {"label": "Role", "value": "Role"},
                            ],
                        ),
                    ],
                    width="auto",
                ),
                dbc.Col(
                    [
                        html.H5("Game mode"),
                        dbc.Select(
                            id="game_mode",
                            options=[
                                {"label": "Assault", "value": "Assault"},
                                {"label": "Control", "value": "Control"},
                                {"label": "Escort", "value": "Escort"},
                                {"label": "Hybrid", "value": "Hybrid"},
                            ],
                        ),
                    ],
                    width="auto",
                ),
                dbc.Col(
                    [
                        html.H5("Map"),
                        dbc.Select(
                            id="map",
                            options=[
                                {"label": "Blizzard World", "value": "Blizzard World"},
                                {"label": "Busan", "value": "Busan"},
                                {"label": "Dorado", "value": "Dorado"},
                                {"label": "Eichenwalde", "value": "Eichenwalde"},
                                {"label": "Hanamura", "value": "Hanamura"},
                                {"label": "Havana", "value": "Havana"},
                                {"label": "Hollywood", "value": "Hollywood"},
                                {"label": "Ilios", "value": "Ilios"},
                                {"label": "Junkertown", "value": "Junkertown"},
                                {"label": "Kings Row", "value": "Kings Row"},
                                {"label": "Lijiang Tower", "value": "Lijiang Tower"},
                                {"label": "Nepal", "value": "Nepal"},
                                {"label": "Numbani", "value": "Numbani"},
                                {"label": "Oasis", "value": "Oasis"},
                                {"label": "Rialto", "value": "Rialto"},
                                {"label": "Route 66", "value": "Route 66"},
                                {"label": "Temple of Anubis", "value": "Temple of Anubis"},
                                {"label": "Volskaya Industries", "value": "Volskaya Industries"},
                                {"label": "Watchpoint Gibraltar", "value": "Watchpoint Gibraltar"},
                            ],
                        ),
                    ],
                    width="auto",
                ),
                dbc.Col(
                    [
                        html.H5("Result"),
                        dbc.Select(
                            id="result",
                            options=[
                                {"label": "Won", "value": "Won"},
                                {"label": "Lost", "value": "Lost"},
                                {"label": "Draw", "value": "Draw"},
                            ],
                        ),
                    ],
                    width="auto",
                ),
                dbc.Col(
                    [
                        html.H5("Score"),
                        dbc.Input(
                            id="score",
                            type="number",
                            min=0,
                            max=10,
                            value=0,
                        ),
                    ],
                    width="auto",
                ),
                dbc.Col(
                    [
                        html.H5("Score enemy"),
                        dbc.Input(
                            id="score_enemy",
                            type="number",
                            min=0,
                            max=10,
                            value=0,
                        ),
                    ],
                    width="auto",
                ),
                dbc.Col(
                    [
                        html.H5("First"),
                        dbc.Select(
                            id="first",
                            options=[
                                {"label": "Attack", "value": "Attack"},
                                {"label": "Defend", "value": "Defend"},
                                {"label": "First won", "value": "First won"},
                                {"label": "First lost", "value": "First lost"},
                            ],
                        ),
                    ],
                    width="auto",
                ),
                dbc.Col(
                    [
                        html.H5("Sargmonster"),
                        dbc.Select(
                            id="sargmonster",
                            options=[
                                {"label": "Tank", "value": "Tank"},
                                {"label": "DPS", "value": "DPS"},
                                {"label": "Healer", "value": "Healer"},
                                {"label": "NA", "value": "NA"},
                            ],
                        ),
                    ],
                    width="auto",
                ),
                dbc.Col(
                    [
                        html.H5("SeviCoder777"),
                        dbc.Select(
                            id="sevicoder777",
                            options=[
                                {"label": "Tank", "value": "Tank"},
                                {"label": "DPS", "value": "DPS"},
                                {"label": "Healer", "value": "Healer"},
                                {"label": "NA", "value": "NA"},
                            ],
                        ),
                    ],
                    width="auto",
                ),
                dbc.Col(
                    [
                        html.H5("aegi97"),
                        dbc.Select(
                            id="aegi97",
                            options=[
                                {"label": "Tank", "value": "Tank"},
                                {"label": "DPS", "value": "DPS"},
                                {"label": "Healer", "value": "Healer"},
                                {"label": "NA", "value": "NA"},
                            ],
                        ),
                    ],
                    width="auto",
                ),
                dbc.Col(
                    [
                        html.H5("BSide"),
                        dbc.Select(
                            id="bside",
                            options=[
                                {"label": "Tank", "value": "Tank"},
                                {"label": "DPS", "value": "DPS"},
                                {"label": "Healer", "value": "Healer"},
                                {"label": "NA", "value": "NA"},
                            ],
                        ),
                    ],
                    width="auto",
                ),
                dbc.Col(
                    [
                        html.H5("Season"),
                        dbc.Input(
                            id="season",
                            type="number",
                            min=0,
                            max=100,
                            value=29,
                        ),
                    ],
                    width="auto",
                ),
            ],
        ),
        html.Div(style={"height": "30px"}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5("Auth token"),
                        dbc.Input(
                            id="auth_token_input",
                        ),
                    ],
                    width="auto",
                ),
                dbc.Col(
                    [
                        dbc.Button(
                            "Insert record",
                            id="insert_record_button",
                            color="primary",
                            className="mr-1"
                        ),
                    ],
                    width="auto",
                ),
                dbc.Col(
                    [
                        html.Div(
                            id="insert_record_feedback",
                            children=[],
                        ),
                    ],
                    width="auto",
                ),
            ],
        ),
        html.Div(style={"height": "30px"}),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            id="table",
                            children=[dbc.Table.from_dataframe(df.head(8), striped=True, bordered=True, responsive = True)],
                        ),
                    ],
                ),
            ],
        ),
    ],
    fluid=True,
)


@app.callback(
    Output(component_id="insert_record_feedback", component_property="children"),
    Output(component_id="table", component_property="children"),
    Input(component_id="insert_record_button", component_property="n_clicks"),
    State(component_id="stack", component_property="value"),
    State(component_id="competitive_mode", component_property="value"),
    State(component_id="game_mode", component_property="value"),
    State(component_id="map", component_property="value"),
    State(component_id="result", component_property="value"),
    State(component_id="score", component_property="value"),
    State(component_id="score_enemy", component_property="value"),
    State(component_id="first", component_property="value"),
    State(component_id="sargmonster", component_property="value"),
    State(component_id="sevicoder777", component_property="value"),
    State(component_id="aegi97", component_property="value"),
    State(component_id="bside", component_property="value"),
    State(component_id="season", component_property="value"),
    State(component_id="auth_token_input", component_property="value"),
)
def insert_record_into_db(n_clicks, selected_stack, selected_competitive_mode, selected_game_mode, selected_map,
                          selected_result, inputted_score, inputted_score_enemy, selected_first, selected_sargmonster,
                          selected_sevicoder777, selected_aegi97, selected_bside, inputted_season, inputted_auth_token):
    
    if dash.callback_context.triggered[0]["prop_id"] == "insert_record_button.n_clicks":

        if inputted_auth_token == config("AUTH_TOKEN"):
        
            query = db.insert(data).values(
                timestamp=datetime.now(),
                stack=selected_stack,
                competitive_mode=selected_competitive_mode,
                game_mode=selected_game_mode,
                map=selected_map,
                result=selected_result,
                score=inputted_score,
                score_enemy=inputted_score_enemy,
                first=selected_first,
                sargmonster=selected_sargmonster,
                sevicoder777=selected_sevicoder777,
                aegi97=selected_aegi97,
                bside=selected_bside,
                season=inputted_season
            )
            ResultProxy = connection.execute(query)

            df = pd.read_sql_table(table_name, url)
            df.sort_values(by=["id"], ascending=False, inplace=True)
            df["timestamp"] = df["timestamp"].dt.strftime("%a %d.%m.%Y %H:%M")

            return "Record inserted successfully!", dbc.Table.from_dataframe(df.head(8), striped=True, bordered=True, responsive = True)

        else:
            return "Wrong auth token!", dash.no_update

    return dash.no_update, dash.no_update


if __name__ == "__main__":
    app.run_server(debug=True)