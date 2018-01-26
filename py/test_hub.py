import sys, json

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return lines[0]

def main():
    #get our data as an array from read_in()
    lines = read_in()

    query = str(lines)

    if query == "":

        data = {'name': "Please enter a search term!"}

    elif query == "Marco":

        data = {'result': 'Polo'}

    else:

        data = {'result': 'Blah Blah Blah!'}

    sys.stdout.write(json.dumps(data))
    print (json.dumps(data))

if __name__ == '__main__':
    main()
