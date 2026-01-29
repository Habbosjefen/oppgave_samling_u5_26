## How to Connect Your MCP Server to AI Toolkit Agent Builder

This guide shows you how to connect your running MCP server to the AI Toolkit Agent Builder so you can ask questions and get responses from your database.

### Prerequisites
- Your MCP server should be running properly
- AI Toolkit extension should be installed in VS Code

### Step 1: Start Your MCP Server
1. Open a PowerShell terminal in VS Code
2. Navigate to your project folder
3. Run: `python src\__init__.py http`
4. Wait for: **"Uvicorn running on http://127.0.0.1:3001"**
5. ✅ Keep this terminal running - don't close it!

### Step 2: Handle Port Conflicts (if needed)
If you get an error like "error while attempting to bind on address", port 3001 is already in use:

1. Find what's using port 3001:
   ```
   netstat -ano | findstr :3001
   ```
2. Kill the blocking process (replace XXXX with the PID number):
   ```
   taskkill /PID XXXX /F
   ```
3. Start your server again: `python src\__init__.py http`

### Step 3: Open AI Toolkit Agent Builder
1. **Click the AI Toolkit icon** in VS Code sidebar (looks like a robot/AI icon)
2. **Look for "Agent Builder"** or **"Prompt Builder"** button
3. **Alternative:** Press `Ctrl+Shift+P` and search for:
   - `AI Toolkit: Open Agent Builder`
   - `AI Toolkit: Open Prompt Builder`

### Step 4: Connect Your MCP Server
1. **In Agent Builder interface, look for:**
   - "My Resources" section
   - "MCP Server" subsection
   - Your server: **`local-server-fagskolen_mcp_server`**

2. **Connect the server:**
   - Click on your `local-server-fagskolen_mcp_server` 
   - It should connect to `http://localhost:3001/mcp`
   - Wait for successful connection

3. **Verify connection:**
   - Look for "Edit tool list" - you should see your tools:
     - get_developer_info
     - get_studieformer
     - get_studiesteder  
     - get_studieprogram

### Step 5: Test Your Connected Agent
Ask questions that will use your database tools:

**Example questions:**
- "What study programs are available in the database?"
- "List all study locations (studiesteder)"
- "What study formats (studieformer) do you have?"
- "Tell me about the available study programs and their categories"

### Expected Results
✅ **Working correctly:** Agent calls your MCP tools and responds with data from your SQLite database

❌ **Not working:** Agent searches the web instead of using your tools

### Troubleshooting
- **Connection failed:** Make sure your MCP server is still running (check the terminal)
- **No tools visible:** Restart both the server and Agent Builder
- **Web search instead of tools:** Check if the MCP server connection is active in Agent Builder
- **Port errors:** Kill existing processes using port 3001 (see Step 2)

### Important Notes
- **Keep the server running** throughout your Agent Builder session
- **Don't use VS Code debug panel** - use manual PowerShell terminals
- **Your database has sample data** about fagskolen study programs, locations, and formats

### Quick Commands Reference
```bash
# Start server
python src\__init__.py http

# Check port usage
netstat -ano | findstr :3001

# Kill blocking process (replace XXXX with PID)
taskkill /PID XXXX /F
```

---

**Success!** Your Agent Builder can now answer questions using your local database instead of searching the web! 🎉