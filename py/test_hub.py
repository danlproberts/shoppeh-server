import sys, json

#Read data from stdin
def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return lines[0]

def main():
    #get our data as an array from read_in()
    #lines = read_in()

    query = str(sys.argv[1])
    data = 'placeholder'


    if query == "":

        data = "Please enter a search term!"

    elif query == "marco":

        data = 'Polo'

    else:

        data = 'Blah Blah Blah!'

    with open('test.txt', 'a') as filelog:
        filelog.write(data)
        filelog.write('\n' + str(sys.argv))

    print (json.dumps(data))

with open('test.txt', 'w') as filelog:
    filelog.write(__name__)

if __name__ == '__main__':
    main()
