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
- Aggregates all logs into logs/provisioning.log (created automatically).
- Supports Ubuntu and any Linux distribution that uses the APT package manager.

Project Structure:
configs/ - Machine configuration files (JSON)
scripts/ - Automation and provisioning scripts
src/ - Core modules (validation, models, utilities)
logs/ - Generated logs and execution results
infra_simulator.py - Main automation entry point

Prerequisites:
- Python 3.10+ and `pip install -r requirements.txt`
- Target machines should use an APT-based Linux distribution (Ubuntu/Debian). Running the controller from Windows is fine, but provisioning assumes APT.

How to Use:
1. Install dependencies: `pip install -r requirements.txt`.
2. Run the main automation script: `python infra_simulator.py`.
3. Follow the prompts to enter machine fields; the script validates and writes configs/instances.json.
4. Review progress and errors in logs/provisioning.log (auto-created).

Notes:
- Requires an APT-based Linux system (Ubuntu or similar).
- Run with appropriate permissions (sudo when needed).