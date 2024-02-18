import os
dir = os.path.dirname(os.path.abspath(__file__))
import json

class Certificates:
    def __init__(self):
        adminUser = "test, lia7624, evermell, omegaxis_"
        adminChannel = "general, test, 🔏alimentacion-bot"
        self.createRule("hello", adminUser, adminChannel)
        self.createRule("help", adminUser, adminChannel)
        self.createRule("addAssist", adminUser, adminChannel)
        self.createRule("updAssist:id", adminUser, adminChannel)
        self.createRule("delAssist:id", adminUser, adminChannel)
        self.createRule("listAssist", adminUser, adminChannel)
        self.createRule("listAssist:id", adminUser, adminChannel)
        self.createRule("listAssist:member", adminUser, adminChannel)

    def createRule(self, command, user, channel):
        command = command.replace(":", "_")
        filepath = f"{dir}/Commands/{command}/"
        rule = 1
        dictrule = {
            "user" : [item.strip() for item in user.split(',')],
            "channel" : [item.strip() for item in channel.split(',')]
        }
        if os.path.exists(filepath):
            files = os.listdir(filepath)
            dictexist = None
            exist = False
            for file in files:
                if str(rule) == file.replace(".json",""):
                    rule+=1
                with (open(f'{dir}/Commands/{command}/{file}', "r")
                      as file_json):
                    dictexist = json.load(file_json)
                if dictexist == dictrule:
                    exist = file
            if not exist:
                with (open(f'{dir}/Commands/{command}/{rule}.json', "w")
                      as file_json):
                    json.dump(dictrule, file_json,
                              ensure_ascii=False, indent=4)
                print(f"-> Created rule in '{command}/{rule}.json'!")
            else:
                print(f"-> Rule already exist in '{command}/{file}'...")
        else:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with (open(f'{dir}/Commands/{command}/{rule}.json', "w")
                  as file_json):
                json.dump(dictrule, file_json, ensure_ascii=False, indent=4)
            print(f"-> Created rule in '{command}/{rule}.json'!")