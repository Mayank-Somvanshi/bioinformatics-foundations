# command = ""
# while command != "quit":  # != means does not
#    command = input(">")
#   print("ECHO", command)
# since our code will only quit when we type quit so we use another code which would quit even if any quit

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
