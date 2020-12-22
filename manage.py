#!/usr/bin/python3


import sys
import subprocess
import json


CONFIG_PATH = "./config.json"


def main():

    if len(sys.argv) != 2:
        print("Provide exactly one parameter")
        sys.exit(1)

    cfg = read_config()

    command = sys.argv[1]
    
    if command == "deploy":
        for deployment in cfg["deployments"]:
            subprocess.call(
                "rsync -av ./webroot/ {0}@{1}:{2}".format(
                    deployment["username"],
                    deployment["host"],
                    deployment["webroot"]
                ), 
                shell=True
            )
    else:
        print("Unknown command")

def read_config():
    with open(CONFIG_PATH, "r") as f:
        content = f.read()
    return json.loads(content)

if __name__ == "__main__":
    main()


# vim: tabstop=4 softtabstop=4 shiftwidth=4 expandtab

