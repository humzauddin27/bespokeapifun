from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

chelseafc = {
	'Goalkeepers': {
				'13':'Thiabut Courtois'
				},
	'Defenders': {
				'3':'Marcos Alonso',
				'28':'Cesar Azpilicueta',
				'24':'Gary Cahill',
				'30':'David Luiz',
				},
	'Midfielders': {
				'7':'N`golo Kante',
				'10':'Eden Hazard',
				'4':'Cesc Fabregas',
				'11':'Pedro Rodriguez',
				'22':'Willian'
				},
	'Strikers': {
				'9':'Alvaro Morata',
				'19':'Diego Costa',
				'23':'Michy Batshuayi'
				}
}

def errorMessage(kit_number):
	if kit_number not in chelseafc:
		abort(404, message="Whoops, {} doesn't exist!".format(kit_number))


class player(Resource):
    	def get(self, kit_number):
    		errorMessage(kit_number)
        	return {kit_number: chelseafc[kit_number]}

        def put(self, kit_number):
        	chelseafc[kit_number] = request.form['data']
        	return {kit_number: chelseafc[kit_number]}

        ##def post(self, id):

        ##def delete(self, id):

class squadList(Resource):
	def get(self):
		return chelseafc

	#def post


api.add_resource(squadList, '/chelseafc')
api.add_resource(player, '/chelseafc/<string:kit_number>')

if __name__ == '__main__':
    app.run(debug=True)
