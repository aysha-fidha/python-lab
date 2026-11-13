with open("source.txt","r")as fin,open("dest.txt","w")as fout:
    for i,line in enumerate(fin,start=1):
        if i%2!=0:
            fout.write(line)