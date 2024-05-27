import os
from typing import final

url: final = r"E:\Download\TestScn.txt"
opt_url: final = r"E:\Download\OptTestScn.txt"

opt = str()

if os.path.isfile(url) == False:
    print("INVALID URL!")
    exit()
else:
    rf = open(url, 'r', encoding="utf-8")
    content = rf.read()
    rf.close()

    temp = content.split('\n')

    for i in temp:
        if len(i) != 0:
            spt = i.split(':')
            if len(spt) >= 2:
                opt += spt[1].lstrip() + '\n'
            else:
                opt += i + '\n'
    
    with open(opt_url, 'w', encoding='utf-8') as optfile:
        optfile.write(opt)

print("COMPLETED")