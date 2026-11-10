Day 66 – Advanced – Building Your Own API with RESTful Routing

📚 Today's Concepts

RESTful APIs

HTTP Methods and Status Codes

RESTful Routing

JSON Responses

CRUD Operations

🛠️ What I Built

Built a RESTful API for managing cafe information.

Implemented endpoints to retrieve, add, update, and delete cafe records.

Added the ability to update an individual cafe's coffee price.

Practiced returning JSON responses and appropriate HTTP status codes.

💡 What I Learned

REST and APIs

REST stands for Representational State Transfer.

REST is an architectural style for designing APIs.

REST uses HTTP to allow applications to communicate with servers.

SOAP, GraphQL, and Falcor are alternative API technologies or approaches, although they aren't all architectural styles equivalent to REST.

An API must follow certain architectural constraints to be considered RESTful.

HTTP Methods

GET: Retrieve information from a server.

POST: Create a new resource.

PUT: Replace an entire existing resource.

PATCH: Partially update an existing resource.

DELETE: Remove a resource.

RESTful Routing

Use consistent URL patterns and endpoints.

Use HTTP methods to communicate the intended action.

Identify individual resources using unique IDs.

Keep URLs focused on resources rather than actions.

JSON and Flask

jsonify() converts Python data into a JSON HTTP response.

request.args.get() retrieves parameters from the URL query string.

request.get_json() retrieves JSON data from the request body.

HTTP status codes communicate the result of an API request.

⚠️ Things to Remember

jsonify() is used to return JSON responses.

request.args.get("parameter") retrieves URL query parameters.

request.get_json() retrieves JSON request-body data.

A SQLAlchemy model represents a database table; an instance represents an individual record.

Updating an object's attribute and committing the session saves changes.

Check whether a database record exists before attempting to update or delete it.

Use appropriate HTTP status codes:

200: Successful request.

201: Resource created.

400: Bad request.

404: Resource not found.

500: Internal server error.

🚀 Key Takeaways

REST provides a consistent way for applications to communicate.

HTTP methods determine what action should be performed on a resource.

PUT replaces a resource, while PATCH makes a partial update.

I learned how to retrieve and modify individual database records through API endpoints.

Understanding APIs will allow me to connect my Python applications to other services and eventually build services other applications can use.