filelist = ['file.1.xml', 'file.2.html', 'file.3.html']

for file in filelist:
    file = file.replace('.', '_', 1)
    print(file)