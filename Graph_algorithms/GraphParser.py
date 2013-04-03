import xml.etree.ElementTree as etree
from Vertex import Vertex
import json
import types

class GraphParser:
    def __init__(self,Filename=None):
        if Filename==None:
            raise Exception("No filename provided")
            return
        graphinxml=etree.parse(Filename)
        self.graphroot=graphinxml.getroot()

    def getNodes(self):
        """
        Here is a issue I need to solve later:
        The node must all have tag value or all not.
        I would later made that optional.
        For know, keep it simple!
        """
        nodeList = []
        for child in self.graphroot.findall("node"):
            value = None
            try:
                value = child.attrib["value"]
            except KeyError:
                pass
            nodeList.append(Vertex(child.attrib["key"],value))
        return nodeList
    
    def isProp(self,prop,default=True):
        try:
            simple = eval(self.graphroot.find(prop).text)
            if type(simple) != types.BooleanType:
                raise Exception("Information is not provided correctly!")
            else:
                return simple
        except AttributeError:
            return default

        
    def isSimple(self):
        return self.isProp("simple")
    
    def isDirectional(self):
        return self.isProp("directional",default=False)

    def _lookup(self,key):
        if Vertex(key) in self.getNodes():
            return self.getNodes()[self.getNodes().index(Vertex(key))]
        else:
            return Vertex(key)

    def getAdjacencyList(self):
        """
        This is not finished for now
        """
        adjacencyList = {}
        for vertex in self.graphroot.findall("node"):
            nodes = [v.attrib["node"] for v in vertex.findall("edge")]
            adjacencyList[self._lookup(vertex.attrib["key"])] = map(self._lookup,nodes)
        return adjacencyList

if __name__=="__main__":
    Parser = GraphParser("graph.xml")
    print Parser.getNodes()
    Parser.getAdjacencyList()
    print Parser.isSimple()
    print Parser.isDirectional()
