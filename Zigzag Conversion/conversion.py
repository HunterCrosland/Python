def convert(s: str, numRows: int) -> str:

    if len(s) < numRows or numRows == 1:
        return s

    top_increment = (numRows-1)*2
    returnstr = str()

    for i in range(numRows):
        increment = top_increment - i*(2)
        complement = 0
        needsComplement = True

        if increment != 0 and increment != top_increment:
            complement = top_increment - increment
        else:
            increment = top_increment
            needsComplement = False


        indexer = i
        returnstr += s[indexer] 

        while len(returnstr) < len(s):

            try:
                indexer += increment
                returnstr += s[indexer]

                if needsComplement:
                    indexer += complement
                    returnstr += s[indexer]

            except:
                break


    return returnstr
