import os
import numpy
import re
# python2
adjmat = list()
map = dict()

def main():
    edgelist = "level_1_edges/part-00000"
    # edgelist = raw_input("Enter path for edges file: ")
    if not os.path.isfile(edgelist):
        print("Invalid file! Exitting")
        exit(0)

    nodesU = []
    max = 0
    print("+--- Starting")
    e = open(edgelist, 'rU')
    lines = e.read().splitlines()
    for line in lines:
        line = line[5:-1]
        line = line.split(',')
        line[0] = int(line[0])
        line[1] = int(line[1])

        if line[0] > max:
            max = line[0]
        elif line[1] > max:
            max = line[1]
        
        # if line[0] not in nodesU:
        nodesU += [line[0]]
        # if line[1] not in nodesU:
        nodesU+= [line[1]]
        # print(line)
        adjmat.append(line)

    nodesU = list(set(nodesU))
    sorted = nodesU
    sorted.sort()
    map = dict()
    # l.keys()[l.values().index(9)]
    for i  in xrange(0, len(sorted)):
        # print sorted[i], ">", i
        map[sorted[i]] = i
        
    # print adjmat
    print "max", max, "len", len(nodesU)
    matrix = [[0] * len(map) for i in xrange(0, len(map))]
    print "\n\n\n", max
    for each in adjmat:
        print each[0], "<--", each[2], "-->", each[1]
        map0 = map[each[0]]
        map1 = map[each[1]]
        print map0, map1
        matrix[map0][map1] = each[2] # set edge weight in adj. matrix
        matrix[map1][map0] = each[2] 

    print "matrix done"
    out = ""
    for each in sorted:
        for other in nodesU:
            out += str(matrix[map[each]][map[other]]) + "   "
        out += "\n"

    print "Final out"
    # print out
    x_matrix = open("X.txt", "w")
    x_matrix.write(out)
    x_matrix.close()


    # def gen_labels():

    vertices = "level_1_vertices/part-00000"
    # vertices = raw_input("Enter path for vertices file: ")
    if not os.path.isfile(vertices):
        print("Invalid file! Exitting")
        exit(0)

    nodes = []
    max = 0
    print("+--- Starting")
    e = open(vertices, 'rU')
    lines = e.read().splitlines()
    for line in lines:
        commas = [m.start() for m in re.finditer(r",",line)]

        # (104216,{community:104196,communitySigmaTot:2010,internalWeight:4,nodeWeight:1})
        node = int(line[1:commas[0]])
        centre = int(line[commas[0] + 12 : commas[1]])
        print node, ">", centre

        if node not in nodes:
            nodes += [node]
        if node > max:
            max = node



    community = [0] * (max+1)
    init = 0 
    notin = 0
    print "starting community marking"
    print nodesU
    for line in lines:
        commas = [m.start() for m in re.finditer(r",",line)]

        # (104216,{community:104196,communitySigmaTot:2010,internalWeight:4,nodeWeight:1})
        node = int(line[1:commas[0]])
        centre = int(line[commas[0] + 12 : commas[1]])
        if node in nodesU:
            init += 1
            print "\t", node, ": in X"
            community[node] = map[centre]
        else:
            notin += 1
            print "\t\t\t", node,": not in X"
            pass

    print "starting output writing", init, "in", notin, "notin"
    out = ""
    for each in community:
        if each !=0:
            out += str(each) + "\n"

    print "Final out"
    # print out
    labels = open("labels.txt", "w")
    labels.write(out)
    labels.close()


if __name__ == '__main__':
    main()
