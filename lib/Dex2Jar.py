import os

class Dex2Jar:
    D2J_PATH = "tools/dex2jar/dex2jar.sh"

    def __init__(self, input_filepath):
        self.input_filepath = input_filepath
        self.execute()

    def execute(self):
        os.system("rm -r .temp")
        os.system("mkdir -p .temp/res")
        os.system("cp .temp2/AndroidManifest.xml .temp")
        os.system("cp -r .temp2/res/. .temp/res")
        os.system("rm -r .temp2")
        os.system("mkdir .temp2")
        os.system("unzip "+self.input_filepath +" -d .temp2")
        for file in os.listdir(".temp2"):
            if file.endswith(".dex"):
                print(os.path.join(".temp2", file))
                os.system("./" + Dex2Jar.D2J_PATH + " "+os.path.join(".temp2", file) )
                os.system("cp "+os.path.join(".temp2", file.replace(".","_"))+"2jar.jar .temp")
                os.system("unzip "+os.path.join(".temp2", file.replace(".","_"))+"2jar.jar -d .temp")
        # os.system('''find .temp -type f -name "*.class" -exec tools/Jad/jad {} -d .temp \;''')
        os.system("tools/Jad/jad -o -r -sjava -dsrc .temp/**/*.class")
        # os.system("cd .temp;mkdir src;cd ..")
        os.system("cp -r src/. .temp/src")
        os.system("rm -r src")
        os.system("rm -r .temp2")
        # command = "./" + ApkTool.APKTOOL_PATH + " d " + self.input_filepath + " -f -o .temp"
        # print(os.system(command))
