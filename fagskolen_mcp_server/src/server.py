import json
from mcp.server.fastmcp import FastMCP

from student_repo import fetch_studieformer, fetch_studiesteder, fetch_studier
from db_config import DATABASE_TYPE

# Initialize FastMCP server
server = FastMCP("fagskolen_mcp_server")

@server.prompt(
    title="Developer Info Prompt",
    description="Prompt to get information about the developer of this server",
)

# TOOL 1: Static developer information
@server.tool(
    name="get_developer_info",
    title="Get Developer Info",
    description="Get information about the developer of this server"
)

async def get_developer_info() -> str:
    """
    Returns static contact information about the developer.
    This is just example data - no database needed.
    """
    developer_info = {
        "name": "Wilhelm",
        "role": "Software Developer",
        "contact": "wilhelmer@afk.no"
    }
    return json.dumps(developer_info, ensure_ascii=False)


# TOOL 2: Get study formats from database
@server.tool(
    name="get_studieformer",
    title="Get Studieformer",
    description="List study modes (studieformer) for fagskolen programs from the database"
)
async def get_studieformer() -> str:
    """
    Fetches all study formats from the configured database.
    Currently using: {DATABASE_TYPE}
    Examples: 'Samlingsbasert', 'Nettbasert med samlinger', 'Modulbasert', 'Deltid'
    """
    studieformer = fetch_studieformer()
    return json.dumps(studieformer, ensure_ascii=False)


# TOOL 3: Get study locations from database  
@server.tool(
    name="get_studiesteder",
    title="Get Studiesteder",
    description="List all study locations (studiesteder) from the database"
)
async def get_studiesteder() -> str:
    """
    Fetches all study locations from the configured database.
    Currently using: {DATABASE_TYPE}
    Examples: 'Fredrikstad', 'Kjeller', 'Drammen', 'Kongsberg', 'Gauldal'
    """
    studiesteder = fetch_studiesteder()
    return json.dumps(studiesteder, ensure_ascii=False)


# TOOL 4: Get study programs from database
@server.tool(
    name="get_studier",
    title="Get Studier",
    description="List all study programs with their categories from the database"
)
async def get_studier() -> str:
    """
    Fetches all study programs with their categories from the configured database.
    Currently using: {DATABASE_TYPE}
    Examples: Programs like 'Observasjons- og vurderingskompetanse' in category 'Helse'
    """
    studieprogram = fetch_studier()
    return json.dumps(studieprogram, ensure_ascii=False)
