import xml.etree.ElementTree as etree
from Vertex import Vertex

class GraphParser:
    def __init__(self,Filename=None):
        if Filename==None:
            raise Exception("Not filename provided")
            return
        graphinxml=etree.parse(Filename)
        self.graphroot=graphinxml.getroot()
        for child in self.graphroot:
            print child.tag+":"+str(child.attrib)
            print child[0].tag+":"+str(child[0].text)

    def getNode(self):
        try:
            nodeValueStrings=[valueString.attrib["value"] for valueString in self.graphroot]
        except :
            nodeValueStrings=None
        if nodeValueStrings:
            return [Vertex(child.attrib["key"],value=child.attrib["value"]) for child in self.graphroot]
        else:
            return [Vertex(child.attrib["key"]) for child in self.graphroot]
    
    def getAdjacencyList(self):
        pass   

if __name__=="__main__":
    Parser = GraphParser("graph.xml")
    print Parser.getNode()
