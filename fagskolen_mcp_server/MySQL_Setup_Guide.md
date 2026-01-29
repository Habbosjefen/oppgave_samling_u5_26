# MySQL Setup Guide for Windows

## Step 1: Download and Install MySQL

1. **Download MySQL**: Go to https://dev.mysql.com/downloads/mysql/
   - Choose "Windows (x86, 64-bit), MSI Installer"
   - Download the larger "mysql-installer-community" file (about 400MB+)

2. **Run the Installer**:
   - Choose "Developer Default" setup type
   - This installs MySQL Server, MySQL Workbench, and other tools

3. **During Installation**:
   - **Root Password**: Set a simple password like `root123` (remember this!)
   - **Authentication**: Choose "Use Legacy Authentication Method" for compatibility
   - **Windows Service**: Keep "Start the MySQL Server at System Startup" checked

## Step 2: Verify Installation

Open Command Prompt and test:
```bash
mysql -u root -p
```
Enter your password when prompted.

## Step 3: Create Database and User

In MySQL command line:
```sql
CREATE DATABASE fagskolen;
CREATE USER 'mcp_user'@'localhost' IDENTIFIED BY 'mcp123';
GRANT ALL PRIVILEGES ON fagskolen.* TO 'mcp_user'@'localhost';
FLUSH PRIVILEGES;
USE fagskolen;
```

## Step 4: Run Database Setup Scripts

We'll run the SQL scripts to create tables and insert data.

## Alternative: Use MySQL Workbench
- Open MySQL Workbench (installed with MySQL)
- Connect to localhost with root user
- Run the SQL scripts through the GUI

---

**Next**: After MySQL is installed, we'll update your Python code to use the new database!