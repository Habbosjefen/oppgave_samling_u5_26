import sqlite3
import os


def get_connection() -> sqlite3.Connection:
    """Get SQLite database connection for workshop/development"""
    base_dir = os.path.dirname(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, "database", "fagskolen.db")
    
    # Create database directory if it doesn't exist
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    # Enable foreign keys
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def setup_database():
    """Create tables and seed data for SQLite"""
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        # Create tables (SQLite syntax)
        cursor.executescript("""
        -- SQLite version of the database schema
        CREATE TABLE IF NOT EXISTS studiesteder (
          studiested_id INTEGER PRIMARY KEY AUTOINCREMENT,
          navn TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS studieformer (
          studieform_id INTEGER PRIMARY KEY AUTOINCREMENT,
          navn TEXT NOT NULL UNIQUE
        );

        CREATE TABLE IF NOT EXISTS studieprogram (
          studieprogram_id INTEGER PRIMARY KEY AUTOINCREMENT,
          navn TEXT NOT NULL UNIQUE,
          kategori TEXT NOT NULL DEFAULT 'Helse',
          program_url TEXT,
          kort_beskrivelse TEXT
        );

        CREATE TABLE IF NOT EXISTS studietilbud (
          studietilbud_id INTEGER PRIMARY KEY AUTOINCREMENT,
          studieprogram_id INTEGER NOT NULL,
          studiested_id INTEGER NOT NULL,
          studieform_id INTEGER NOT NULL,
          varighet_verdi INTEGER NOT NULL CHECK (varighet_verdi > 0),
          varighet_enhet TEXT NOT NULL CHECK (varighet_enhet IN ('uker','måneder','år')),
          studiepoeng_min REAL NOT NULL CHECK (studiepoeng_min >= 0),
          studiepoeng_max REAL NOT NULL CHECK (studiepoeng_max >= studiepoeng_min),
          apent_for_opptak INTEGER NOT NULL DEFAULT 1,
          merknad TEXT,
          FOREIGN KEY (studieprogram_id) REFERENCES studieprogram(studieprogram_id) ON DELETE CASCADE,
          FOREIGN KEY (studiested_id) REFERENCES studiesteder(studiested_id),
          FOREIGN KEY (studieform_id) REFERENCES studieformer(studieform_id),
          UNIQUE (studieprogram_id, studiested_id, studieform_id, varighet_verdi, varighet_enhet, studiepoeng_min, studiepoeng_max)
        );

        CREATE TABLE IF NOT EXISTS emner (
          emne_id INTEGER PRIMARY KEY AUTOINCREMENT,
          studieprogram_id INTEGER NOT NULL,
          emnenavn TEXT NOT NULL,
          emnekode TEXT,
          studiepoeng REAL,
          rekkefolge INTEGER,
          kort_beskrivelse TEXT,
          FOREIGN KEY (studieprogram_id) REFERENCES studieprogram(studieprogram_id) ON DELETE CASCADE
        );

        CREATE TABLE IF NOT EXISTS studieplaner (
          studieplan_id INTEGER PRIMARY KEY AUTOINCREMENT,
          studieprogram_id INTEGER NOT NULL,
          plan_url TEXT NOT NULL,
          gyldig_fra DATE,
          merknad TEXT,
          FOREIGN KEY (studieprogram_id) REFERENCES studieprogram(studieprogram_id) ON DELETE CASCADE
        );
        """)
        
        # Insert seed data
        cursor.executescript("""
        -- Seed data for SQLite
        INSERT OR IGNORE INTO studiesteder (navn) VALUES
          ('Fredrikstad'),
          ('Kjeller'),
          ('Drammen'),
          ('Kongsberg'),
          ('Gauldal');

        INSERT OR IGNORE INTO studieformer (navn) VALUES
          ('Samlingsbasert'),
          ('Nettbasert med samlinger'),
          ('Modulbasert'),
          ('Deltid');

        INSERT OR IGNORE INTO studieprogram (navn, kategori, program_url, kort_beskrivelse) VALUES
          ('Observasjons- og vurderingskompetanse i helsetjenesten', 'Helse',
           'https://fagskolen-viken.no/studier/helse/observasjons-og-vurderingskompetanse-i-helsetjenesten',
           'Videreutdanning med fokus på systematisk observasjon, vurdering og dokumentasjon av helsetilstand.'),
          ('Optometri for medhjelpere', 'Helse',
           'https://fagskolen-viken.no/studier/helse/optometri-medhjelpere',
           'Videreutdanning for medhjelpere innen optometri/optisk virksomhet.'),
          ('Praktisk veiledning', 'Helse',
           'https://fagskolen-viken.no/studier/helse/praktisk-veiledning',
           'Videreutdanning som styrker kompetanse i veiledning, kommunikasjon og etisk refleksjon i helsetjenesten.'),
          ('Psykisk helsearbeid og rusarbeid', 'Helse',
           'https://fagskolen-viken.no/studier/helse/psykisk-helsearbeid-og-rusarbeid',
           'Utdanning rettet mot arbeid med psykisk helse og rus, med nettundervisning kombinert med fysiske samlinger.');
        """)
        
        conn.commit()
        print("✅ SQLite database setup complete!")
        
    except Exception as e:
        conn.rollback()
        print(f"❌ Error setting up database: {e}")
        raise
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    setup_database()