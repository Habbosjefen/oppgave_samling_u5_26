## Complete Step-by-Step Setup Guide: MCP Server with AI Toolkit

This guide covers everything from initial setup to having a working MCP server connected to AI Toolkit Agent Builder.

---

## Phase 1: Initial Setup and Understanding
Activate venv:
.venv\Scripts\Activate.ps1

### Step 1: Understand Your Project Structure
Your MCP server project contains:
- **src/server.py** - MCP tools (API endpoints)
- **src/student_repo.py** - Database functions  
- **src/db.py** - SQLite database connection
- **database/** - MySQL setup files (not used in this setup)
- **.aitk/mcp.json** - MCP server configuration

### Step 2: Choose Database Type
We use **SQLite** for simplicity instead of MySQL:
- ✅ SQLite: Local file database, no external server needed
- ❌ MySQL: Requires separate MySQL server setup

---

## Phase 2: Fix Database Connection

### Step 3: Fix student_repo.py for SQLite
**Problem:** Original code used MySQL syntax `cursor(dictionary=True)`  
**Solution:** Updated to work with SQLite

```python
# In src/student_repo.py - Fixed version
def fetch_studieformer() -> list[dict]:
    conn = get_connection()
    try:
        cursor = conn.cursor()  # Remove dictionary=True for SQLite
        cursor.execute("SELECT navn FROM studieformer ORDER BY navn")
        rows = cursor.fetchall()
        cursor.close()
        return [{"navn": row[0]} for row in rows]  # Convert to dict format
    finally:
        conn.close()
```

### Step 4: Setup SQLite Database with Sample Data
```bash
python src/db.py
```
This creates `database/fagskolen.db` with tables and sample data.

---

## Phase 3: Add Database Testing Functions

### Step 5: Add New Database Functions
Added to **src/student_repo.py**:
- `fetch_studiesteder()` - Get study locations
- `fetch_studieprogram()` - Get study programs with categories

### Step 6: Add New MCP Tools  
Added to **src/server.py**:
- `get_studiesteder` - Lists study locations
- `get_studieprogram` - Lists study programs
- Removed `get_weather` (was mock data)

**Final tools:**
1. `get_developer_info` - Static developer info
2. `get_studieformer` - Study formats from database
3. `get_studiesteder` - Study locations from database  
4. `get_studieprogram` - Study programs from database

---

## Phase 4: Install Dependencies and Inspector

### Step 7: Install Required Packages
```bash
pip install --force-reinstall pydantic-settings fastmcp
```

### Step 8: Install MCP Inspector (Optional)
```bash
git clone https://github.com/modelcontextprotocol/inspector.git
cd inspector
npm install
```

---

## Phase 5: Fix VS Code Debug Issues

### Step 9: Avoid Debug Panel Problems
**Problem:** VS Code debug panel causes import conflicts  
**Solution:** Use manual PowerShell terminals instead

**❌ Don't use:** "Run MCP Server (HTTP)" from debug panel  
**✅ Do use:** `python src\__init__.py http` in regular terminal

---

## Phase 6: Start and Test MCP Server

### Step 10: Start MCP Server (Manual Method)
```bash
# In PowerShell terminal
python src\__init__.py http
```
**Expected output:** `INFO: Uvicorn running on http://127.0.0.1:3001`

### Step 11: Test with MCP Inspector (Optional)
```bash
# In second terminal
cd inspector
npm start
```
- Browser opens to http://localhost:5173
- Click "Connect" → Use URL: http://localhost:3001/mcp
- Test all 4 tools

---

## Phase 7: Connect to AI Toolkit Agent Builder

### Step 12: Handle Port Conflicts
If you get port binding errors:
```bash
# Find what's using port 3001
netstat -ano | findstr :3001

# Kill the blocking process (replace XXXX with PID)
taskkill /PID XXXX /F

# Restart your server
python src\__init__.py http
```

### Step 13: Open AI Toolkit Agent Builder
1. Click **AI Toolkit icon** in VS Code sidebar
2. Look for **"Agent Builder"** or **"Prompt Builder"** button
3. Alternative: `Ctrl+Shift+P` → `AI Toolkit: Open Agent Builder`

### Step 14: Connect Your MCP Server
1. In Agent Builder, find **"My Resources"** → **"MCP Server"**
2. Look for: **`local-server-fagskolen_mcp_server`**
3. Connect it (should connect to http://localhost:3001/mcp)
4. Verify: "Edit tool list" should show your 4 tools

---

## Phase 8: Test the Complete Setup

### Step 15: Test Agent with Database Questions
Ask questions that use your database:

**Test questions:**
- "What study programs are available in the database?"
- "List all study locations (studiesteder)"  
- "What study formats (studieformer) do you have?"
- "Tell me about study programs and their categories"

**✅ Success:** Agent responds with data from your SQLite database  
**❌ Problem:** Agent searches web instead of using your tools

---

## Quick Reference Commands

### Start Server
```bash
python src\__init__.py http
```

### Fix Port Issues
```bash
netstat -ano | findstr :3001
taskkill /PID XXXX /F
```

### Initialize Database  
```bash
python src/db.py
```

### Start Inspector
```bash
cd inspector
npm start
```

---

## Configuration Files Created/Modified

### 1. src/student_repo.py  
Added 2 new database functions with proper SQLite syntax

### 2. src/server.py
Added 2 new MCP tools, removed weather tool, added documentation

### 3. How to Start Your MCP Server.md
Manual startup instructions (no debug panel)

### 4. How to Connect Agent Builder to MCP Server.md  
AI Toolkit connection guide

---

## What You Can Do Now

✅ **MCP Server** running with 4 database tools  
✅ **SQLite Database** with fagskolen study data  
✅ **MCP Inspector** for direct tool testing  
✅ **AI Toolkit Agent Builder** for conversational testing  
✅ **Database queries** instead of web search  

## Common Issues and Solutions

| Problem | Solution |
|---------|----------|
| Port 3001 in use | Kill blocking process, restart server |
| Import errors with debug panel | Use manual PowerShell terminals |
| Agent searches web | Check MCP server connection in Agent Builder |
| Tools not visible | Restart server and Agent Builder |
| SQLite errors | Run `python src/db.py` to reinitialize |

---

**🎉 You now have a complete MCP server setup that connects your AI agent to your local database!**