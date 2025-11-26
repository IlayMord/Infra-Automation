import os
import json
from pydantic import ValidationError
from src.logging_config import logger
from src.machine import Machine
from scripts.Nginx_installation import run_nginx_installer

#Collect machine data (inputs) from the user.
def collect_machine_data():

    machines = []

    while True:
        machine_fields = ['Name','OS','CPU','RAM','DiskSize']
        machine_dict = {}

        for field in machine_fields:
            data = input(f"Enter {field}:")
            machine_dict[field] = data

        machines.append(machine_dict)
        logger.info(f"collected data!")

        more = input("Add another machine? [yes/no]: ").strip().lower()
        if more not in ("yes","y"):
            break

    return machines


#Save validated machine data to JSON file.
def change_to_json(machines_list):
    base = os.path.dirname(__file__)
    path = os.path.join(base, "..","configs","instances.json")

    #Create a dir if it dosnt exsist.
    os.makedirs(os.path.dirname(path), exist_ok=True)

    #Save machine data to JSON.
    with open(path,"w") as file:
        json.dump(machines_list ,file, indent= 4)
        logger.info(f'Configuratuion saved to: {path}')

def main():
    raw_machines = collect_machine_data()
    validated_machines = []
    
    try:
        #Validate and create machine object.
        for machine_data in raw_machines:
            machine = Machine(**machine_data)
            
            #Log machine creation.
            logger.info(f"Machine created: {machine.model_dump()}")

            validated_machines.append(machine.change_to_dict())

        #Save the machine data to JSON format.
        change_to_json(validated_machines)

        #Run the insstaltion.
        run_nginx_installer()
        
    except (ValidationError, ValueError) as e:
        logger.error(f"Validation error: {e}")
        exit()
    
    except PermissionError as e:
        logger.error(f"Permission error: {e}")
        exit()

    except FileNotFoundError as e:
        logger.error(f"File not found {e}")
        exit()

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        exit()

#Run main program.
main()