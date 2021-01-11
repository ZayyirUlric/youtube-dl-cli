import youtube_dl # In the case of an import error, please run: pip install youtube_dl ~OR~ python -m pip install youtube_dl

def requestInput():
    link = input("Please enter a valid YouTube URL: \n> ")
    return link

def welcome():
    print("Input `help` for a list of commands." + '\n')

def ytHelp():
    print('''
    read: \t Reads links from links.txt file.
    exit: \t Closes the program.
    todo: \t To do list, also shows changelog if available.
    help: \t Brings up the available commands.
    pick: \t Prints available formats for selection.
    ''')

def toDo():
    print('''
    TODO: \n
    \t - Add playlist download support.
    \t - Probably switch to using cases/dict.
    \t - Better input string parsing.
    \n
    CHANGELOG: \n
    \t - Added picking formats for individual downloads.
    \t - Changed input design a bit.
    ''')

def isWorst():
    isWorst = str(input("Force worst video encoding? (Y/n) \n> "))
    if (isWorst == "y" or isWorst == "Y" or isWorst == "yes" or isWorst =="Yes"):
        return True
    elif (isWorst == "n" or isWorst == "N" or isWorst == "no" or isWorst =="No"):
        return False
    else:
        print("Invalid input.")
        isWorst()

def pick():
    selectionLink = input("Please enter a YouTube video link to select from: \n> ")
    if (isWorst() == False):
        options = {
            'listformats': True
        }
        with youtube_dl.YoutubeDL(options) as ytdl:   
            try:
                ytdl.download([selectionLink])
            except:
                return 
        selectionFormat = str(int(input("Please input the integer representing the format: \n> ")))
        selectedFormatOptions = {
            'format': selectionFormat
        }
        with youtube_dl.YoutubeDL(selectedFormatOptions) as ytdl:   
            try:
                ytdl.download([selectionLink])
            except:
                return 
    else:
        options = {
            'format': 'worst'
        }
        with youtube_dl.YoutubeDL(options) as ytdl:   
            try:
                ytdl.download([selectionLink])
            except:
                return 

ytdl_opts = {}
welcome()
while 69 == 69:
    yt_link = requestInput()
    if (yt_link == "exit"):
        print("Closing.")
        exit()
    elif (yt_link == "help"):
        ytHelp()
    elif (yt_link == "todo"):
        toDo()
    elif (yt_link == "pick"):
        pick()
    elif (yt_link == "ytdlhelp"): #Used for debugging
        print(help(youtube_dl))
    elif (yt_link == "read"):
        temp_link_array = []
        try:
            f = open("links.txt","rt")
            for line in f:
                temp_link_array.append(line)
            i = 0
            if (len(temp_link_array) == 0):
                print("Links.txt file is empty.")
            else:
                while (i != len(temp_link_array)):
                    with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:   
                        try:
                            ytdl.download([temp_link_array[i]])
                            i+=1
                        except:
                            print("Iteration error." + '\n')
            f.close()
        except:
            print("File read error.")
            print("Generating new file")
            g = open("links.txt","w")
            g.close()
    else:
        print('\n')
        with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:   
            try:
                ytdl.download([yt_link])
                print('''
                \n
                ======================================
                
                 \t Done with download.
                
                ======================================
                \n
                ''')
            except:
                print("Input error." + '\n')
        
