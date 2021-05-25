#OOps Google Helper's code for 2nd ques.

#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
# Add a print() to indicate the server which the new coonection_id is connected to. 
# id(server) is used here to reprensent different servers.
        print(f"connection_id:{connection_id} is connected through server_id: {id(server)}")
        # Add the connection to the dictionary with the selected server
        # Add the connection to the server
        self.connections[connection_id] = server
        server.add_connection(connection_id)
# Call ensure_availabilty() to check balance
        self.ensure_availability()

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer
#       Check if connection_id is in self.connections 
        if connection_id in self.connections.keys():
            self.connections[connection_id].close_connection(connection_id)
            del self.connections[connection_id]

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        amount_load = sum(server.load() for server in self.servers)
        amount_servers = len(self.servers)
#       return value based on the condition
        return 0 if amount_servers == 0 else amount_load/amount_servers

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
            print("LoadBalance Alert")
            self.servers.append(Server())

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#