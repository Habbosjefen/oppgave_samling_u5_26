# 🚀 Complete MySQL Setup Instructions

## Current Status
✅ **SQLite is working** - Your MCP server is running with SQLite data  
🔧 **MySQL is prepared** - All code is ready to switch to MySQL

## To Install and Switch to MySQL:

### 1. Install MySQL (5-10 minutes)
Follow the guide in: `MySQL_Setup_Guide.md`
- Download from https://dev.mysql.com/downloads/mysql/
- Choose "Developer Default" installation 
- Set root password (remember it!)

### 2. Run Database Setup (1 minute)
```bash
cd database
python setup_mysql.py
```
This will:
- Create the `fagskolen` database
- Create `mcp_user` with password `mcp123`  
- Create all tables and insert sample data
- Test the connection

### 3. Switch to MySQL (10 seconds)
Edit `src/db_config.py`:
```python
DATABASE_TYPE = "mysql"  # Change from "sqlite"
```

### 4. Restart MCP Server
- Stop current server (Ctrl+C)
- Start again: `python src/__init__.py http`

## 🎉 That's it!

Your MCP server will now use MySQL instead of SQLite. The Agent Builder will get the same data, but from MySQL.

## 💡 Easy Switching
- **Use SQLite**: `DATABASE_TYPE = "sqlite"` 
- **Use MySQL**: `DATABASE_TYPE = "mysql"`

No other code changes needed - it automatically handles the differences!

## About the "Tokens" Usage
The tokens might be normal behavior in Agent Builder when:
- Agent chooses to search web instead of using tools
- Agent uses tools AND web search for comprehensive answers  
- Tools return data but agent enhances with additional context

Test by asking very specific questions like:
- "What study programs are available?" (should use tools)
- "List all study locations" (should use tools)

## 🔍 Debug Tips
- Check MCP server logs for database connection errors
- Make sure port 3001 is not blocked by firewall
- Verify Agent Builder is connected to `http://localhost:3001`