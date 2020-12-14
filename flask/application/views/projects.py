from flask import render_template
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

from application.instances.secrets import GITHUB_TOKEN

from application import app

@app.route("/projects")
def projects():
    result = queryGithub(
                 """
                 query getPublicRepos {
                   rateLimit {
                     cost
                     remaining
                     resetAt
                   }
                   user(login: "sheep5") {
                     repositories(first: 100, privacy: PUBLIC, orderBy: {field: CREATED_AT, direction: DESC}) {
                       totalCount
                       nodes {
                         name
                         description
                         url
                       }
                     }
                   }
                 }
                 """
             )
    projects = result["user"]["repositories"]["nodes"]
    return render_template("projects.html", projects=projects)

""" Queries the given query string to Github's API v4. """
def queryGithub(query):
    if type(query) != str:
        #TODO: error checking
        pass
    
    # Select transport with defined URL endpoint
    transport = RequestsHTTPTransport(
                    url="https://api.github.com/graphql",
                    use_json=True,
                    headers={
                        "Authorization": "token " + GITHUB_TOKEN
                    }
                )
    
    # Create GraphQL client using defined transport
    client = Client(
                 transport=transport,
                 fetch_schema_from_transport=True
             )
    
    # Provide GraphQL query
    gql_query = gql(query)
    
    # Execute query on transport
    return client.execute(gql_query)