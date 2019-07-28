import os

class ApkTool:
    APKTOOL_PATH = "tools/apktool/apktool.jar"

    def __init__(self, input_filepath , output_directory):
        self.input_filepath = input_filepath
        self.output_directory = output_directory
        self.execute()

    def execute(self):
        command = "java -jar " + ApkTool.APKTOOL_PATH + " d " + self.input_filepath + " -f -o .temp2" 
        print(os.system(command))
