#OOPs Assignment Google Helper's Code and explaination.

#Begin Portion 1#
class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
#       Check if the connection_id is in the dict, in case that the connection_id /
#       is deleted twice or more which will cause an erro.
        if connection_id in self.connections.keys():
            del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for connect_nums in self.connections.values():
            total += connect_nums
#       I can use sum() instead of this loop
#       total = sum(self.connections.values())
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
#End Portion 1#