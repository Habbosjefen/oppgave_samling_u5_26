### Main.ipynb
1. Hoved koden for web-scraping verktøy
2. Henter informasjon om alle studier og emner

### Main copy.ipynb
1. Kopi av hovedkoden før endringer på struktur (cleanup)

### lenker.json
1. Første filen som blir laget for å lagre informasjon om alle studier + studieurl

### studie.json
1. Fil over alle studier
2. Inneholder ønsket oppsett på informasjon som blir hentet ut av web scraper

### alle_emner.json
1. Oversikt over alle emner som hentes fra web scraper
2. Inneholder nødvendig informasjon for videre kode i main skal hente ut ønsket informasjon

### alle_emner_enriched.json
1. Oversikt over alle emner fra alle studiene
2. Inneholder ønsket oppsett på data

### alle_emner_enriched_mangler.json
1. Oversikt over emner som manuelt blir hentet grunnet feil henting av url av web scraper
2. Hensikt er å samle all informasjonen på ett sted før de manuelt copy-pastes over i "alle_emner_enriched.json" der det er feil/mangler