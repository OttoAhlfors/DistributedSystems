import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:3000')

# Take user input for topic and text
print("Enter topic:")

topic = input()
print("Enter text:")
text = input()

print("Add note,", s.makeNote(topic, text))

print("Give topic to find")
topic = input()

print("Note found,", s.getNote(topic))