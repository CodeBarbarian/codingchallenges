def GenerateBanner(Username, Delimiter):
    # One is enough, trust me
    Delimiter = Delimiter[0]

    UsernameLength = len(Username)

    TOP     = ''
    BOTTOM  = ''

    for i in range (UsernameLength + 4):
        TOP     += Delimiter
        BOTTOM  += Delimiter

    print TOP
    print str(Delimiter) + ' ' + str(Username) + ' ' + str(Delimiter)
    print BOTTOM

GenerateBanner("CodeBarbarian", "-")
