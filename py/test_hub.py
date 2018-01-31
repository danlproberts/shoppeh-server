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
    data = 'placeholder'

    with open('../test.txt', 'w') as filelog:
        filelog.write(query)
        filelog.write(str(type(query)))

    if query == "":

        data = "Please enter a search term!"

    elif query == "Marco":

        data = 'Polo'

    else:

        data = 'Blah Blah Blah!'

    with open('../test.txt', 'a') as filelog:
        filelog.write(data)
        filelog.write(str(type(data)))

    sys.stdout.write(json.dumps(data))
    print (json.dumps(data))

if __name__ == '__main__':
    main()
