import pandas as pd
from flask import Flask,jsonify

data=pd.read_excel("pokedex.xlsx")

app=Flask(__name__)

@app.route("/")
def introduccion():
    respuesta={
        "mensaje":"esta es una api de pokedex, perrita :3"
    }
    return jsonify(respuesta)

@app.route("/nombre/<nombre>")
def pokemon_por_nombre(nombre):
    d=data[data["Nombre"]==nombre].iloc[0]
    r={"Numero":int(d["Numero"]),"Nombre":d["Nombre"]}
    return jsonify(r)

@app.route("/id/<id>")
def pokemon_por_numero(id):
    print(data)
    d=data[data["Numero"]==int(id)].iloc[0]
    print(d)
    r={"Numero":int(d["Numero"]),"Nombre":d["Nombre"]}
    return jsonify(r)


if __name__=="__main__":
    app.run()