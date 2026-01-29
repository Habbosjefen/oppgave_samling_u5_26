"""
Database setup script for MySQL
Run this after MySQL is installed to create the database and tables
"""

import mysql.connector
from mysql.connector import Error
import os
import configparser
import configparser

def setup_mysql_database():
    """
    Sets up the MySQL database with tables and data
    """
    print("🔧 Setting up MySQL database...")
    
    # First, connect to MySQL server (without specific database)
    try:
        # Connect as root to create database and user
        root_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=input("brainbob MySQL root password: ")
        )
        
        cursor = root_connection.cursor()
        
        # Create database
        print("📁 Creating database 'fagskolen'...")
        cursor.execute("CREATE DATABASE IF NOT EXISTS fagskolen DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_unicode_ci")
        
        # Create user for MCP server
        print("👤 Creating MCP user...")
        cursor.execute("CREATE USER IF NOT EXISTS 'brainbob'@'localhost' IDENTIFIED BY 'brainbob'")
        cursor.execute("GRANT ALL PRIVILEGES ON fagskolen.* TO 'brainbob'@'localhost'")
        cursor.execute("FLUSH PRIVILEGES")
        
        cursor.close()
        root_connection.close()
        print("✅ Database and user created successfully!")
        
    except Error as e:
        print(f"❌ Error creating database: {e}")
        return False
    
    # Now connect with the MCP user to create tables and insert data
    try:
        # Read and execute SQL files
        print("🏗️ Creating tables...")
        
        # Read table creation script
        with open('database/01_create_tables_mysql.sql', 'r', encoding='utf-8') as file:
            table_script = file.read()
        
        # Read data insertion script  
        with open('database/02_seed_data_mysql.sql', 'r', encoding='utf-8') as file:
            data_script = file.read()
        
        # Read database config or use defaults
        try:
            config = configparser.ConfigParser()
            config.read('database/config.cnf')
            db_user = config.get('client', 'user', fallback='mcp_user')
            db_password = config.get('client', 'password', fallback='mcp123')
        except:
            db_user = 'mcp_user'
            db_password = 'mcp123'
        
        # Connect with MCP user
        connection = mysql.connector.connect(
            host='localhost',
            database='fagskolen',
            user=db_user,
            password=db_password
        )
        
        cursor = connection.cursor()
        
        # Execute table creation (split by semicolon for multiple statements)
        for statement in table_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
        
        # Execute data insertion
        for statement in data_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
        
        connection.commit()
        cursor.close()
        connection.close()
        
        print("✅ Tables created and data inserted successfully!")
        return True
        
    except Error as e:
        print(f"❌ Error setting up tables: {e}")
        return False

def test_connection():
    """
    Test the database connection with the MCP user
    """
    print("🧪 Testing database connection...")
    
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='brainbob', 
            user='root',
            password='brainbob'
        )
        
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM studieprogram")
        count = cursor.fetchone()[0]
        
        cursor.close()
        connection.close()
        
        print(f"✅ Connection successful! Found {count} study programs in database.")
        return True
        
    except Error as e:
        print(f"❌ Connection failed: {e}")
        return False

if __name__ == "__main__":
    print("🚀 MySQL Database Setup for fagskolen MCP Server")
    print("=" * 50)
    
    if setup_mysql_database():
        test_connection()
        print("\n🎉 Database setup complete! You can now switch to MySQL in your MCP server.")
        print("\n📋 Next steps:")
        print("1. Update student_repo.py to use MySQL")
        print("2. Restart your MCP server")
        print("3. Test in Agent Builder")
    else:
        print("\n❌ Setup failed. Please check MySQL installation and try again.")