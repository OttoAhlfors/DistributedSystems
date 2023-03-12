# Lähteet:
# https://www.geeksforgeeks.org/create-xml-documents-using-python/

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from datetime import datetime
from xml.dom import minidom
import xml.etree.ElementTree as ET

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


class Notes:
    def __init__(self, topic, text, date):
        self.topic = topic
        self.text = text
        self.date = date

with SimpleXMLRPCServer(('localhost', 3000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    @server.register_function
    def makeNote(topic, text):
        date = datetime.now()
        Note = Notes(topic, text, date)

        tree = ET.parse('Notes.xml')
        root = tree.getroot()

        for note in root.iter("Note"):
            if note.attrib["Topic"] == topic:
                modText = note.find("Text")
                modText.text = text
                modDate = note.find("Date")
                modDate.text = str(date)

                string_xml = ET.tostring(root)

                with open("Notes.xml", "wb") as file:
                    file.write(string_xml)
                
                return "Note modified"
            
        newNote = ET.SubElement(root, "Note")
        newNote.attrib["Topic"] = topic

        textForNewNote = ET.SubElement(newNote, "Text")
        textForNewNote.text = text
        dateForTheNewNote = ET.SubElement(newNote, "Date")
        dateForTheNewNote.text = str(date)

        string_xml = ET.tostring(root)

        with open("Notes.xml", "wb") as file:
            file.write(string_xml)

        return "Note added"
   
    @server.register_function
    def getNote(topic):

        tree = ET.parse('Notes.xml')
        root = tree.getroot()

        for note in root.iter("Note"):
            if note.attrib["Topic"] == topic:
                text = note.find("Text")
                date = note.find("Date")

                Note = Notes(note.attrib["Topic"], text.text, date.text)
                return Note
            else: 
                return "No note found"


    server.serve_forever()