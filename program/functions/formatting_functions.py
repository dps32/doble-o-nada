def titleCentred(title_ascii,width=136):
    title_centred = ""
    for i in range(title_ascii.count("\n")):
        if i == 0:
            ini = 0
            fin = title_ascii.find("\n")
        else:
            ini = fin + 1
            fin = title_ascii.find("\n",ini)
        title_centred += title_ascii[ini:fin].center(width) + "\n"
    return title_centred