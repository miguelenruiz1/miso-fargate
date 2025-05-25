from app import create_app, db
from flask import jsonify, abort

application = create_app()
app = application  # Add alias for compatibility

@application.before_first_request
def init_app_db():
    db.create_all()

@application.route("/<string:id>")
def heroe(id):
    item = data.get(id)
    if item is None:
        return jsonify({"error": f"Heroe '{id}' no encontrado"}), 404
    return jsonify(item)

if __name__ == '__main__':
    #with application.app_context():
    #    db.create_all()
    application.run(host='0.0.0.0', port=5000)