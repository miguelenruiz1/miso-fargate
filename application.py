from flask import jsonify
from app import create_app

application = create_app()
app = application  # alias

@application.route('/ping')
def ping():
    return jsonify(status='ok', message='pong'), 200

if __name__ == '__main__':
    # Sólo aquí, si quieres, inicializa la BD antes de servir
    # with application.app_context():
    #     from app import db
    #     db.create_all()
    application.run(host='0.0.0.0', port=5000)
