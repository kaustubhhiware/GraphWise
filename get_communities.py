import os
import re
import numpy
# python2

def main():

    vertices = "level_0_vertices/part-00000"
    # vertices = raw_input("Enter path for vertices file: ")
    if not os.path.isfile(vertices):
        print("Invalid file! Exitting")
        exit(0)

    nodes = []
    sorted = []
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

        if centre not in nodes:
            nodes += [node]
            print "Added centre", centre
        else:
            print "Redundant centre", centre
        if node > max:
            max = node

    print "Number of communities",len(nodes)
    # sorted = nodes
    # sorted.sort()
    # map = dict()
    # # l.keys()[l.values().index(9)]
    # for i  in xrange(0, len(sorted)):
    #     # print sorted[i], ">", i
    #     map[sorted[i]] = i

    # community = [0] * (max+1)
    # print "starting community marking"
    # for line in lines:
    #     commas = [m.start() for m in re.finditer(r",",line)]

    #     # (104216,{community:104196,communitySigmaTot:2010,internalWeight:4,nodeWeight:1})
    #     node = int(line[1:commas[0]])
    #     centre = int(line[commas[0] + 12 : commas[1]])
    #     community[node] = map[centre]

    # print "starting output writing"
    # out = ""
    # for each in community:
    #     if each !=0:
    #         out += str(each) + "\n"

    # print "Final out"
    # # print out
    # labels = open("labels.txt", "w")
    # labels.write(out)
    # labels.close()

if __name__ == '__main__':
    main()