import argparse
from lib.ApkTool import ApkTool
from lib.Dex2Jar import Dex2Jar


def main():
    parser = argparse.ArgumentParser()
    welcome = "cli interface to test data related security issues in android"
    parser = argparse.ArgumentParser(description=welcome)
    parser.add_argument('--apk', '-apk', required=True, help='Location of the apk file')
    parser.parse_args()
    args = parser.parse_args()
    apkLoc = args.apk
    ApkTool(apkLoc,"/anidiot")
    Dex2Jar(apkLoc)
    print(apkLoc)


if __name__ == "__main__":
    main()
