## How to Start Your MCP Server (Simple Manual Method)

Follow these steps to test your MCP Server. Avoid VS Code debug panel - use manual terminals instead.

### Step 0: Clean Start
1. Kill all running terminals (if any)
2. Close any debug panels that are running

### Step 1: Start the MCP Server (Manual Terminal - NO DEBUG PANEL)
1. Open a new PowerShell terminal in VS Code (Terminal → New Terminal)
2. Make sure you're in the project folder
3. Run: `python src\__init__.py http`
4. Wait for "Uvicorn running on http://127.0.0.1:3001" message
5. ✅ Leave this terminal running

### Step 2: Test with Inspector (Optional)
1. Open a second terminal in VS Code  
2. Run: `cd inspector`
3. Run: `npm start`
4. Browser should open to http://localhost:5173
5. Click "Connect" and use URL: http://localhost:3001/mcp

### Step 3: Test with Agent Builder
1. Keep server running (Step 1)
2. Press Ctrl+Shift+P → "AI Toolkit: Open Agent Builder"
3. Connect to your server or ask questions like:
   - "What study programs are available?"
   - "List study locations"

### Quick Commands
```bash
# Terminal 1: Start server (avoid debug panel!)
python src\__init__.py http

# Terminal 2 (optional): Start inspector  
cd inspector
npm start
```

### Important Notes
- **DON'T use VS Code debug panel** - it conflicts with the server
- **Use regular PowerShell terminals** instead
- Server should show "Uvicorn running" when working correctly

### What Each Tool Does
- **get_developer_info**: Shows developer contact information
- **get_studieformer**: Fetches study formats from SQLite database (Samlingsbasert, etc.)
- **get_studiesteder**: Fetches study locations from SQLite database (Fredrikstad, etc.)  
- **get_studieprogram**: Fetches study programs with categories from SQLite database