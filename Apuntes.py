import graphviz 
import tempfile

f = graphviz.Digraph('finite_state_machine')
f.attr(rankdir='LR')

f.attr('node', shape='doublecircle')
f.node('final')

f.attr('node', shape='plaintext')
f.edge('', 'Q0', label='Inicio')

f.attr('node', shape='circle')
f.node('Q0')
f.node('Inicio')
f.edge('Q0', 'Q2', label='1')
f.edge('Q0', 'Q1', label='0')
f.edge('Q2', 'Q0', label='1')
f.edge('Q1', 'Q0', label='0')
f.edge('Q1', 'Q3', label='1')
f.edge('Q3', 'Q1', label='1')
f.edge('Q2', 'Q3', label='0')
f.edge('Q3', 'Q2', label='0')
f.view(tempfile.mktemp())