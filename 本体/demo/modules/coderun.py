import re

#runclass
class coderun:
    def runcode(self,input):

        try:
            classname = re.findall("(.*?):.*~.*;",input)
            classdef = re.findall(".*:(.*?)~.*;",input)
            classv = str(re.findall(".*:.*~(.*?);",input))

            exec("from modules import " + classname[0])

            exec(classname[0] + "." + classdef[0] + '(' + classv + ')')

        except IsADirectoryError:
            print("error")



