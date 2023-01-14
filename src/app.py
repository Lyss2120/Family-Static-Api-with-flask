"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():
# this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    if members:
    # status_code 200 si se agregó con éxito, 400 si no lo hace porque el cliente (solicitud) falla, 500 si el servidor encuentra un error
        return jsonify(members), 200
    else:
        return jsonify({"msg":"There have been some errors in your request"}),400


@app.route('/member/<int:member_id>', methods=['GET', 'DELETE'])
def get_delete_member(member_id):
    member = jackson_family.get_member(member_id)#es jacksonfamily en vez de familystructure porque arriba lo cambia
    if request.method == 'GET':
            return jsonify(member), 200
    else:
            jackson_family.delete_member(member_id)
            return jsonify({
                "done": True
            }), 200


@app.route('/member', methods=['POST'])
def add_new_member():
# https://3000-breathecode-exercisefam-xzrzq0f5ywx.ws-us80.gitpod.io/
    member = request.get_json()
    if member["first_name"] !="" and member["age"] !="" and len(member["lucky_numbers"]) > 0:
        jackson_family.add_member({
            "id": member["id"] if "id" in member else None,
            "first_name": member["first_name"],
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
        })
        return {}, 200
    else:
        return jsonify({"msg":"There have been some errors in your request"}), 400


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
