#!/usr/bin/env python
from flask import Flask
from flask_graphql import GraphQLView
import graphene
import requests
from graphene.types import json
app = Flask(__name__)
class Query(graphene.ObjectType):
	hello = graphene.String()
	name = graphene.String()
	position = json.JSONString()
	def resolve_hello(self, args, context, info):
		return "World!"

	def resolve_name(self, args, context, info):
		return "Mike"

	def resolve_position(self, args, context, info):
		r = requests.get('http://api.axfrcheck.com/api/domain/openssl.org')
		return r.json()

schema = graphene.Schema(query=Query)
result = schema.execute('{position}')
print result, result.data['position']

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
app.run()