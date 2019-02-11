#! python3
# AutoAdd something is a macro that is used to add  repeated character(s) to the copied text by each line


# This is an example of creating a numbered list leaving the first line unformatted

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    if i == 0:
        lines[i] = lines[i]
    else:
        lines[i] = str(i)+ '......' + str(lines[i])

text = '\n'.join(lines)

pyperclip.copy(text)
