from flask import Flask, request, render_template, make_response
from dummy_data import dummy_data
from pathlib import Path
from bambu_status import BambuStatusSchema, BambuStatus

app = Flask(__name__)
api_key = Path('/run/secrets/api_key').read_text().strip()
schema = BambuStatusSchema()
bambu_status = schema.load(dummy_data)


@app.route('/bambu_status', methods=["GET"])
def status_json():
    resp = make_response(schema.dump(bambu_status))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/bambu_status', methods=["PUT"])
def update_status():
    global bambu_status

    if request.headers.get('X-Api-Key') != api_key:
        return "Unauthorized", 401

    data = request.json
    try:
        bambu_status = schema.load(data)
    except ValidationError:
        return "Bad Request", 400
    return "No content", 204
