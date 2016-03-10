def display_board( state ):
    print " "
    print "| %d  %d  %d |" % (state[0], state[3], state[6]) #here % is used as an assignment operator to print the states
    print "| %d  %d  %d |" % (state[1], state[4], state[7])
    print "| %d  %d  %d |" % (state[2], state[5], state[8])

def move_up( state ):
    new_state = state[:]
    index = new_state.index(0)
    if index in [0, 3, 6]:     #base condition to move up as toppest elements of matrix cannot move up further
             temp = new_state[index - 1]
             new_state[index - 1] = new_state[index]
             new_state[index] = temp
             display_board( state )
             return new_state
    else:
        return None

def move_down( state ):
    new_state = state[:]
    index = new_state.index( 0 )
    if index not in [2, 5, 8]: #base condition to move down as lowest elements of matrix cannot move down further
             temp = new_state[index + 1]
             new_state[index + 1] = new_state[index]
             new_state[index] = temp
             display_board( new_state )
             return new_state
    else:
        return None

def move_left( state ):
    new_state = state[:]
    index = new_state.index( 0 )
    if index not in [0, 1, 2]: #base condition to move left as leftmost elements of matrix cannot move left further
             temp = new_state[index - 3]
             new_state[index - 3] = new_state[index]
             new_state[index] = temp
             display_board( new_state )
             return new_state
    else:
        return None

def move_right( state ):
    new_state = state
    index = new_state.index(0)
    if index not in [6, 7, 8]: #base condition to move up as rightmost elements of matrix cannot move right further
             temp = new_state[index + 3]
             new_state[index + 3] = new_state[index]
             new_state[index] = temp
             display_board( new_state )
             return new_state
    else:
        return None

def create_node( state, parent, operator, depth, cost ):#a new node is created where state is the index where 0 is present
    return Node( state, parent, operator, depth, cost )

def expand_node( node, nodes ):
    expanded_nodes = []
    expanded_nodes.append( create_node( move_up( node.state ), node, "up", node.depth + 1, 0 ) )
    expanded_nodes.append( create_node( move_down( node.state ), node, "down", node.depth + 1, 0 ) )
    expanded_nodes.append( create_node( move_left( node.state ), node, "left", node.depth + 1, 0 ) )
    expanded_nodes.append( create_node( move_right( node.state), node, "right", node.depth + 1, 0 ) )
    expanded_nodes = [node for node in expanded_nodes if node.state != None]
    return expanded_nodes

def bfs( start, goal ):
    nodes = []
    nodes.append( create_node( start, None, None, 0, 0 ) )
    while True:
        if len( nodes ) == 0: return None
        node = nodes.pop(0)
        if node.state == goal:
            moves = []
            temp = node
            while True:
                moves.insert(0, temp.operator)
                if temp.depth == 1: break
                temp = temp.parent
            return moves
        nodes.extend( expand_node( node, nodes ) )

class Node:
    def __init__( self, state, parent, operator, depth, cost ):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost



# Main method
def main():
    start = [8, 0, 7, 1, 2, 6, 3, 4, 5]
    result = bfs( start,final )
    if result == None:
        print "No solution found"
    elif result == [None]:
        print "Start node was the goal!"
    else:
        print result
        print len(result), " moves"

final = [1, 8, 7, 2, 0, 6, 3, 4, 5]
main()
