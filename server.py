from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from my_sql_select import select
from my_sql_python_insert import insert

def qwe(a):
    return a

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler, allow_none=True)

def myfunction(x, y):
    return x+y
server.register_function(myfunction) #registration obj func in server
server.register_function(select)
# Run the server's main loop
server.serve_forever()