from sys import argv

def main():
    mdFile = getFile()
    
    line = mdFile.readline()
    line.strip()
    print(line),
    mdFile.close()

def getFile():
    """http://stackoverflow.com/questions/7033987/python-get-files-from-command-line"""

    if len(argv) > 2:
        raise ValueError("No more than 1 file may be parsed at a time.")
    elif len(argv) == 1:
        raise ValueError("You must provide a file to parse.")

    filename = argv[-1]

    try:
        f = open(filename, 'r')
    except IOError:
        raise ValueError("File " + filename + " could not be opened")

    return f

if __name__ == "__main__":
    main()

