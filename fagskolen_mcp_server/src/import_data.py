import pandas as pd 
import json 
import mysql.connector
import os

parent_folder_path = os.path.dirname(os.path.dirname(__file__))

with open(os.path.join(parent_folder_path, "studie.json"), 'r', encoding="utf-8") as file:
    studie = json.load(file)

with open(os.path.join(parent_folder_path, 'alle_emner_enriched.json'), 'r', encoding="utf-8") as file:
    emner = json.load(file)

def get_connection() -> mysql.connector.MySQLConnection :
    config_path = os.path.join(parent_folder_path, "database", "config.cnf")
    return mysql.connector.connect(
        option_files=config_path,
        option_groups="client",
    )

def insert_emner(emner) -> None:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        for emne in emner:
            query = "INSERT IGNORE INTO emner (emnenavn, " \
                                        "emneurl, " \
                                    "emnekode, " \
                                    "studieprogram, " \
                                    "studiepoeng, " \
                                    "sted, " \
                                    "nivaa, " \
                                    "ansvarlig, " \
                                    "kunnskap, " \
                                    "ferdigheter, " \
                                    "kompetanse, " \
                                    "studieurl) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            
            emnenavn = emne.get("emne_name", None)
            emneurl = emne.get("emne_link", None)
            emnekode = emne.get('emnekode', None)
            studie = emne.get("from_study", None)
            studiepoeng = emne.get("studiepoeng", None)
            studiested = emne.get('studiested', None)
            nivaa = emne.get("studienivå", None)
            ansvarlig = emne.get("emneansvarlig", None)
            kunnskap = emne.get("læringsutbytte_kunnskap", None)
            ferdigheter = emne.get("læringsutbytte_ferdigheter", None)
            kompetanse = emne.get("læringsutbytte_generell_kompetanse", None)
            studieurl = emne.get("study_url", None)


            arguments = (emnenavn,
                        emneurl,
                        emnekode,
                        studie,
                        studiepoeng,
                        studiested,
                        nivaa,
                        ansvarlig,
                        kunnskap,
                        ferdigheter,
                        kompetanse,
                        studieurl)
            cursor.execute(query, arguments)
        print(cursor.fetchall())
        conn.commit()
    finally:
        conn.close()

def insert_studier(studier) -> None:
    conn = get_connection()
    try:
        cursor = conn.cursor()
        for studie in studier :
            query = "INSERT IGNORE INTO studier (studienavn," \
                                            "program_url, "\
                                            "nivaa, "\
                                            "poeng," \
                                            "beskrivelse, "\
                                            "spraak, "\
                                            "hvorfor, "\
                                            "hva, "\
                                            "studieform , "\
                                            "oppmotte, "\
                                            "politiattest, "\
                                            "muligheter) "\
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            
            studienavn = studie.get('title',None)
            program_url = studie.get('link',None)
            nivaa = studie.get('nivå',None)
            poeng = studie.get('studiepoeng',None)
            beskrivelse = studie.get('beskrivelse',None)
            spraak = studie.get('undervisningsspråk',None)
            hvorfor = studie.get('hvorfor velge studiet',None)
            hva = studie.get('hva lærer du',None)
            studieform = studie.get('undervisning og samlinger',None)
            oppmotte = studie.get('obligatorisk oppmøte',None)
            politiattest = studie.get('politiattest',None)
            muligheter  = studie.get('karrieremuligheter',None)

            argumenter = (studienavn,
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
                        muligheter)

            cursor.execute(query, argumenter)
        print(cursor.fetchall())
        conn.commit()
    finally:
        conn.close()

insert_studier(studie)
insert_emner(emner)