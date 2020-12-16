""" Static typing-related imports """
from typing import Dict

""" Flask-related imports """
from flask import render_template
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

""" nate.dev-related imports """
from application.instances.secrets import GITHUB_USERNAME, GITHUB_TOKEN
from application import app

@app.route("/projects")
def projects() -> None:
    # Store query results from GitHub
    result : Dict = queryGithub(
                        f"""
                        query getPublicRepos {{
                          rateLimit {{
                            cost
                            remaining
                            resetAt
                          }}
                          user(login: "{GITHUB_USERNAME}") {{
                            repositories(
                              first: 100,
                              privacy: PUBLIC,
                              orderBy: {{
                                field: CREATED_AT,
                                direction: DESC
                              }}
                            ) {{
                              totalCount
                              nodes {{
                                name
                                description
                                url
                              }}
                            }}
                          }}
                        }}
                        """
                 )
    
    
    try:
        # Check if the query result is malformed
        projects : Dict = result["user"]["repositories"]["nodes"]
        return render_template("projects.html", projects=projects)
    except (AttributeError, KeyError):
        # code to show user an error
        pass


""" Queries the given query string to Github's API v4. """
def queryGithub(query : str) -> Dict:
    # Select transport with defined URL endpoint
    transport : RequestsHTTPTransport = RequestsHTTPTransport(
                                            url="https://api.github.com/graphql",
                                            use_json=True,
                                            headers={
                                                "Authorization": f"token {GITHUB_TOKEN}"
                                            }
                                        )
    
    # Create GraphQL client using defined transport
    client : Client = Client(
                          transport=transport,
                          fetch_schema_from_transport=True
                      )
    
    # Provide GraphQL query
    gql_query : gql = gql(query)
    
    # Execute query on transport
    return client.execute(gql_query)
