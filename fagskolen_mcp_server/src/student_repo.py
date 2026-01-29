from db_mysql import get_connection


def fetch_studieformer() -> list[dict]:
    """
    Get all study formats from the database.
    Returns: List of study formats like 'Samlingsbasert', 'Nettbasert med samlinger', etc.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT navn FROM studieformer ORDER BY navn")
        rows = cursor.fetchall()
        
        cursor.close()
        print("Study formats fetched:", rows)
        return rows
    finally:
        conn.close()


def fetch_studiesteder() -> list[dict]:
    """
    Get all study locations from the database.
    Returns: List of locations like 'Fredrikstad', 'Kjeller', 'Drammen', etc.
    """
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        #cursor.execute("SELECT navn FROM studiesteder ORDER BY navn")
        cursor.execute("SELECT DISTINCT sted FROM emner ORDER BY sted")
        rows = cursor.fetchall()
        
        cursor.close()
        print("Study locations fetched:", rows)
        return rows
    finally:
        conn.close()


def fetch_studieprogram() -> list[dict]:
    """
    Get all study programs with their categories from the database.
    Returns: List of programs with their names and categories (like 'Helse')
    """
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT navn, kategori FROM studieprogram ORDER BY navn")
        rows = cursor.fetchall()
        cursor.close()
        print("Study programs fetched:", rows)
        return rows
    finally:
        conn.close()


def fetch_studier() -> list[dict]:
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT 
                studienavn,
                program_url,
                nivaa,
                poeng,
                beskrivelse,
                spraak,
                hvorfor,
                hva,
                studieform,
                oppmotte,
                politiattest,
                muligheter
            FROM studier
            ORDER BY studienavn
        """)
        rows = cursor.fetchall()
        cursor.close()
        print("Rows fetched:", rows)
        return rows
    finally:
        conn.close()


def fetch_emner() -> list[dict]:
    conn = get_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT
                emnekode,
                emneurl,
                emnenavn,
                studieprogram,
                studiepoeng,
                nivaa,
                sted,
                ansvarlig,
                kunnskap,
                ferdigheter,
                kompetanse,
                studieurl,
                kort_beskrivelse
            FROM emner
            ORDER BY emnenavn
        """)
        rows = cursor.fetchall()
        cursor.close()
        print("Rows fetched:", rows)
        return rows
    finally:
        conn.close()
