import pathlib

pth = pathlib.Path('./')

for f in pth.iterdir():
    print(f)



with open('sydney.JPG','rb') as infile, open('sydney2.JPG', 'wb') as outfile:
    outfile.write(infile.read())