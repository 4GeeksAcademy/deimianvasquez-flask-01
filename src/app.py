from flask import Flask, jsonify, request


# Simulación de database
humans = [
    {
        "id":1,
        "name":"Deimian",
        "last_name": "Vásquez"   
    },
    {
        "id":2,
        "name":"Elio",
        "last_name": "Colmenares"   
    },
    {
        "id":3,
        "name":"Ricardo",
        "last_name": "Arias"   
    }
]


app = Flask(__name__)

@app.route("/health-check")
def healt_check():
    return "ok "


# endpoint return all humans
@app.route("/person", methods=["GET"])
def get_all_human():
    try:
        # consulta a la base de datos
        return jsonify(humans)
    except Exception as error:
       return {
           "message": "Tenemos un error en nuestra plataforma, si continua cominuquese a soporte"
       }, 500


@app.route("/person/<int:theid>", methods=["GET"]) 
def get_one_person(theid):
    try:
        result = list(filter(lambda item: item["id"] == theid, humans))
        if result:
            return jsonify(result[0]), 200
        else:
            return jsonify({"message":"user not found"}), 404
        
    except Exception as error:
        print(error)
        return {
           "message": "Tenemos un error en nuestra plataforma, si continua cominuquese a soporte"
       }, 500
    

@app.route("/person", methods=["POST"])
def add_new_human():
    body = request.json
    try:
        # manera de validar que existen
        # if body.get("name") is None:
        #     return jsonify({"message":"Se debe enviar un name"}), 400
        # if body.get("last_name") is None:
        #     return jsonify({"message":"Se debe enviar un last_name"}), 400
        

        # Forma 2
        # required_fields = {"name", "last_name"}
        # missing_fields = required_fields - set(body.keys())

        # if missing_fields:
        #     return jsonify({"message": f"Missing required fields: {', '.join(missing_fields)}"}), 400


        # Forma 3
        if body.get("name") is None or body.get("last_name") is None:
            return jsonify({"message":"Missin required fields: name, last_name"}), 400
       

        # body.update({"id":len(humans)+1})
        body["id"] =len(humans)+1
        humans.append(body)


        return jsonify("Se agrego exitosamente"), 201
    except Exception as error:
        return {
           "message": "Tenemos un error en nuestra plataforma, si continua cominuquese a soporte"
       }, 500


@app.route("/person/<int:theid>", methods=["PUT"])
def update_human(theid):
    body = request.json

    try:
        if body.get("name") is None:
            return jsonify({"message":"Se debe enviar un name"}), 400
        if body.get("last_name") is None:
            return jsonify({"message":"Se debe enviar un last_name"}), 400

        new_human = list(filter(lambda item: item["id"] == theid, humans))

        if new_human:
            new_human = new_human[0]
            new_human["name"] = body["name"]
            new_human["last_name"] = body["last_name"]
            return jsonify(new_human), 200
        else:
            return jsonify({"message":"user not found"}), 404
    except Exception as error:
        return {
           "message": "Tenemos un error en nuestra plataforma, si continua cominuquese a soporte"
        }, 500


@app.route("/person/<int:theid>", methods=["DELETE"])
def delete_one_human(theid):
    try:
        result = list(filter(lambda item: item["id"] == theid, humans))

        if result:
            new_human = list(filter(lambda item: item["id"] != theid, humans))
            humans = new_human
            return jsonify([]), 201
        else:
            return jsonify({"message":"user not found"}), 404
            
        
    except Exception as error:
        return {
           "message": "Tenemos un error en nuestra plataforma, si continua cominuquese a soporte"
        }, 500





if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3001", debug=True)


"""
    Created --> POST
    Read(request)--> GET
    Update  --> PUT
    Delete  --> Eliminar
"""    






