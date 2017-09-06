from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

chelseafc = {
	'Goalkeepers': {
				13:'Thiabut Courtois'
				},
	'Defenders': {
				3:'Marcos Alonso',
				28:'Cesar Azpilicueta',
				24:'Gary Cahill',
				30:'David Luiz',
				},
	'Midfielders': {
				7:'N`golo Kante',
				10:'Eden Hazard',
				4:'Cesc Fabregas',
				11:'Pedro Rodriguez',
				22:'Willian'
				},
	'Strikers': {
				9:'Alvaro Morata',
				19:'Diego Costa',
				23:'Michy Batshuayi'
				}
}

parser = reqparse.RequestParser()
parser.add_argument('num')
parser.add_argument('pos')
parser.add_argument('name')

def errorMessage(kit_number):
	if kit_number not in chelseafc:
		abort(404, message="Whoops, {} doesn't exist!".format(kit_number))


class Player(Resource):
    	def get(self, position, kit_number):
        	return {kit_number:chelseafc[position][kit_number]}

        def put(self, position, kit_number):
        	chelseafc[position][kit_number] = request.form['data']
        	return {kit_number:chelseafc[position][kit_number]}

        def delete(self, position, kit_number):
        	temp = chelseafc[position][kit_number]
        	del chelseafc[position][kit_number]
        	return 'Deleted ' + temp

class Position(Resource):
	def get(self, position):
		return chelseafc[position]

class Squad(Resource):
	def get(self):
		return chelseafc

	def post(self):
		args = parser.parse_args()
		if (int(args['num']) > 100):
			return "Can't make a players number so high!", 404
		else:
			chelseafc[args['pos']][args['num']] = args['name']
			return {args['num']:args['name']}, 200


api.add_resource(Squad, '/chelseafc')
api.add_resource(Position, '/chelseafc/<string:position>')
api.add_resource(Player, '/chelseafc/<string:position>/<string:kit_number>')

if __name__ == '__main__':
    app.run(debug=True)
