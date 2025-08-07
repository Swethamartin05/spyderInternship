installed_versions=["2.3","2.5","2.1","2.5","2.5","2.0"]
current_version="2.5"
computer_number=1
for version in installed_versions:
    if(version<current_version):
        print("Computer",computer_number,":Please update from version",version,"to",current_version)
    computer_number=computer_number+1
