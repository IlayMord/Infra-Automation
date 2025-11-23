**Infra-Automation**

Automated setup and configuration for Linux machines.

Overview:
This project allows defining one or more machines through configuration files and executing an automated process that installs packages, configures services, validates inputs, creates required folder structures, and generates detailed logs.
The goal is to deliver a consistent and efficient way to prepare servers or development environments with minimal manual work.

Features:
- Loads one or multiple machine configurations from the configs/ directory.
- Executes automated provisioning using both Shell and Python scripts.
- Creates required directories and log files if they do not exist.
- Performs validation on machine parameters before provisioning.
- Generates clear, timestamped logs for troubleshooting.
- Supports Ubuntu and any Linux distribution that uses the APT package manager.

Project Structure:
configs/ - Machine configuration files (JSON)
scripts/ - Automation and provisioning scripts
src/ - Core modules (validation, models, utilities)
logs/ - Generated logs and execution results
infra_simulator.py - Main automation entry point

How to Use:
1. Create or update a machine configuration file inside configs/.
2. Run the main automation script (infra_simulator.py).
3. The system will validate the configuration, run provisioning scripts, and save results.
4. Review all logs and outputs inside the logs/ directory.

Notes:
- Requires an APT-based Linux system (Ubuntu or similar).
- Run with appropriate permissions (sudo when needed).