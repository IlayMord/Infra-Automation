import subprocess
import os
import sys
import logging

#Path to log file.
log_file = os.path.join(os.path.dirname(__file__),"..","logs","installation.log")

#Check if logs directory exists.
os.makedirs(os.path.dirname(log_file), exist_ok=True)


#Configure logging.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    fh = logging.FileHandler(log_file)
    fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(fh)

def run_nginx_installer():

    #Build the full path to the Bash script.
    script_path = os.path.join(os.path.dirname(__file__),"setup_nginx.sh")

    #Check if script file exists.
    if not os.path.isfile(script_path):
        logger.error("Installer script does not exist.")
        sys.exit(1)

    try:
        #Running the Bash script using subprocess.
        subprocess.run(["bash",script_path],check=True,text=True)

    #The script work but returned a failed exit code.
    except subprocess.CalledProcessError as e:
        logger.error(f"ERROR: Script failed with exit code {e.returncode}")
        sys.exit(1)

    #The file dosnt exsist.
    except FileNotFoundError:
        logger.error("ERROR: Bash script not found.")
        sys.exit(1)

    #Any unexpted error.
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)

