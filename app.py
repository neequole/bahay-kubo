from flask import Flask
from flask_graphql import GraphQLView

from schema import schema

app = Flask(__name__)
app.config.update(
    ENV='development',
    DEBUG=True,
)

# Add the /graphql endpoint for GraphiQL interface
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)


@app.route('/')
def hello():
    return 'Sorry, Netong\'s Bahay Kubo main gate is closed. ' \
           'Please use <a href="/graphql">GraphiQL</a> gate instead!'


if __name__ == "__main__":
    app.run()
