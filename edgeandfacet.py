import ansa
from ansa import base
from ansa import constants

#==============================================================================
# Getting references to entities

n = base.CreateEntity(constants.ABAQUS, "NODE")
nn = base.Entity(constants.ABAQUS, n._id, "NODE")

if n == nn:
        print("OK: Objects are equal")
else:
        print("ERROR")

#==============================================================================


nodes = []
n_coords = [ (0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0),
             (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1) ]
for i in range(8):
        vals = {}
        for j, v in enumerate(('X1', 'X2', 'X3')):
                vals[v] = n_coords[i][j]
        n = base.CreateEntity(constants.NASTRAN, "GRID", vals)
        nodes.append(n)

vals = {}
for i, n in enumerate(('G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8' )):
        vals[n] = nodes[i]._id
vals['PID'] = 1
vals['type'] = 'CHEXA'

solid = base.CreateEntity(constants.NASTRAN, "SOLID", vals)
facet = base.Entity(constants.NASTRAN, solid._id, 'SOLID', facet=1)
print(facet.ansa_type(constants.NASTRAN))

edge = base.Entity(constants.NASTRAN, solid._id, 'SOLID', edge_index=1)


#==============================================================================

#printing internal representations of entities
n = base.CreateEntity(constants.ABAQUS, "NODE")
s = str(n)
print(s)
# prints like: Entity: 0x000000001F3BF920: type: 1101(1101,N_GRID) id:-2

#sorting entities by id
l = []
n = base.CreateEntity(constants.ABAQUS, "NODE")
l.append(n)
n = base.CreateEntity(constants.ABAQUS, "NODE")
l.append(n)
ll = sorted(l, key=lambda e: e._id)
#checking for defunct objects
# shell: a Shell with nodes 1, 2, 3, 4
l = []
l.append(shell)
n = base.Entity(constants.ABAQUS, 1, "NODE")

# the following call with delete the shell
base.DeleteEntity(n, force=True)

#now the object in l[0]  has been deleted.
shell = l[0]
if not shell.is_usable():
        print("This object is not usable")

#inheriting from entity
class myAnsaObject(base.Entity):
        def __init__(self, deck, id, type):
                super().__init__(deck, id, type)


def do_stuff():
        n = myAnsaObject(constants.ABAQUS, 1, "NODE")

def main():
        shell = base.Entity(constants.ABAQUS, 'SHELL', 1)
        vals = shell.get_entity_values(constants.ABAQUS, ('G1', 'G2', 'G3', 'G4'))

        print(vals)

        node = base.Entity(constants.ABAQUS, 'NODE', 1)
        shell.set_entity_values(constants.ABAQUS, {'G1':node})
        vals = shell.get_entity_values(constants.ABAQUS, ('G1',))

        print(vals)

def main():
        node = base.CreateEntity(constants.ABAQUS, 'NODE')
        node.position = (-12.0193, 0., 8.)
        print(node.position)

        node2 = base.CreateEntity(constants.ABAQUS, 'NODE')
        node2.position = node.position
        print(node2.position)

def main():
        ent = base.GetEntity(ansa.constants.ABAQUS, 'SOLID', 16583)

        list = {'G21': 8, 'G3': 146564655656}
        debug_mode = constants.REPORT_ALL
        ret, debug_report = ent.set_entity_values(constants.ABAQUS, list, debug = debug_mode)

        if not ret:
                pprintt.pprint('No errors or warnings found!')
        else:
                pprint.pprint(debug_report)

a = [0,1,2,3,4]
b = [0,2,6]
list(set(a) & set(b))   # 使用  "&"  运算求a与b的交集，输出：[0, 2]
list(set(a) | set(b))   # 使用  "|"  运算求a与b的并集，输出：[0, 1, 2, 3, 4, 6]
list(set(b) - set(a))   # 使用  "-"  运算求a与b的差(补)集： 求b中有而a中没有的元素，输出：[6]
list(set(a) - set(b))   # 使用  "-"  运算求a与b的差(补)集： 求a中有而b中没有的元素，输出：[1, 3, 4]
list(set(a) ^ set(b))   # 使用  "^"  运算求a与b的对称差集，输出：[1, 3, 4, 6]
