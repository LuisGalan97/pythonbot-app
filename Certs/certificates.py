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
        if os.path.exists(filepath):
            archivos = os.listdir(filepath)
            print(archivos)
        else:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with (open(f'{dir}/Commands/{command}/{rule}.json', "w") 
                  as file_json):
                json.dumps({
                    "user" : [item.strip() for item in user.split(',')],
                    "channel" : [item.strip() for item in channel.split(',')]
                }, file_json, ensure_ascii=False, indent=4)
            print(f"-> Created rule '/{command}/{rule}.json'!")

        '''
        
        if not os.path.exists(filepath):
            
            
        else: 
            print(f"-> Rule '/{command}/{rule}.json' already exist...")
        '''