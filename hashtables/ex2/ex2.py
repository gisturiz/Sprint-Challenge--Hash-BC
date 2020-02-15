#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [] * length

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    if hash_table_retrieve(hashtable, "NONE"):
        route.append(hash_table_retrieve(hashtable, "NONE"))
    
    for i in range(0, length - 2):
        route.append(hash_table_retrieve(hashtable, route[-1:][0]))
    
    # if hash_table_retrieve(hashtable, "NONE"):
    #     route.append(hash_table_retrieve(hashtable, "NONE"))

    # for i in range(0, length - 2):
    #     route.append(hash_table_retrieve(hashtable, route[-1:][0]))

    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

result = reconstruct_trip(tickets, 3)
print(result)
