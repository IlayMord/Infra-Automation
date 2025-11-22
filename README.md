Infra-Automation

Automated setup and configuration for Linux machines.

Overview:
This project allows defining a machine through a configuration file and running an automated process that installs packages, configures services, creates folder structures, performs validations, and generates logs. The objective is to provide a fast and consistent way to prepare servers or development environments.

Features:
- Loads machine settings from configs/
- Runs automated Shell + Python scripts
- Creates required directory structure and logging
- Performs basic checks during setup
- Designed for Ubuntu and any Linux distribution that uses the APT package manager

Project Structure:
configs/    - Machine configuration files  
scripts/    - Automation scripts  
src/        - Modules and utilities  
logs/       - Execution logs and results  

How to Use:
1. Edit a configuration file inside configs/ to match your machine.
2. Run the main setup script located in scripts/.
3. Review the results in the logs/ directory.

Notes:
- Requires an APT-based Linux system (Ubuntu or similar).
- Run with appropriate permissions (sudo when needed).