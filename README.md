# Sikker kommunikasjon og sertifikathåndtering i byggautomasjon med Tailscale og OPC UA

Dette er et skole prosjekt som viser hvordan man kan etablere sikker og pålitelig kommunikasjon mellom en WAGO CC100 PLS og Ignition SCADA ved hjelp av [Tailscale](https://tailscale.com/) og OPC UA.

---

## Innhold

- `Avsluttende prosjekt.docx` – Prosjektrapport som dokumenterer fremgang, tekniske valg og evaluering
- `Vedlegg 1 - KI-deklarasjon`
- `Vedlegg 2 - Timeliste`
- `Vedlegg 3 - Forstudierapport`
- `Vedlegg 4 - Presentasjon`
- `Vedlegg 5 - Møter`
- `Vedlegg 6 - GanttDiagram`
- `Vedlegg 7 - pdf`
- `Vedlegg 8 - bilder`
- `Vedlegg 9 - codesysprogram`
- `Vedlegg 10 - UaExpert`
- `Vedlegg 11 - Skript`
	- `InstallTailscale.sh` – Bash-skript for installasjon og oppsett av Tailscale på WAGO CC100
	- `update_tailscale_certificates.sh` – Automatisk uthenting og installasjon av TLS-sertifikater fra Tailscale
	- `Sluttbrukerveiledning_OPCUA_Tailscale.docx` – Brukerveiledning for installasjon, drift og vedlikehold
- `Vedlegg 12 - Sluttbrukerveiledning`
- `Vedlegg 13 - E-post`




---

## Forutsetninger

- WAGO PLS med Linux-basert operativsystem (eks. CC100)
- SSH-tilgang til PLS
- Tailscale-konto (gratis fungerer fint)
- Ignition SCADA installert (gratis fungerer fint) og konfigurert med OPC UA
- UaExpert (valgfritt) for testing av sertifikatoppkobling

---

## Kom i gang

### 1. Installer Tailscale på PLS
```bash
chmod +x InstallTailscale.sh
./InstallTailscale.sh
```

### 2. Logg inn på Tailscale
Etter installasjon får du en `tailscale up`-kommando med URL for autentisering. Følg denne for å registrere enheten.

### 3. Konfigurer HTTPS-sertifikater
```bash
chmod +x update_tailscale_certificates.sh
./update_tailscale_certificates.sh
```
Dette skriptet bruker `tailscale cert` til å hente gyldige sertifikater og konfigurere webserveren (lighttpd).

---

## OPC UA-sertifikater

Sertifikathåndtering gjøres manuelt i denne løsningen:

1. Generer sertifikat i Codesys
2. Del sertifikater mellom SCADA og PLS
3. Aktiver `Sign & Encrypt` i Ignition og UaExpert
4. Verifiser at kommunikasjonen er kryptert

---

## Drift og overvåking

- Overvåk tilkoblingsstatus i Tailscale sitt adminpanel
- Bruk `tailscale status` på PLS
- Sertifikatene oppdateres ved å kjøre `update_tailscale_certificates.sh` periodisk (f.eks. via cron)

---

## Dokumentasjon

Se `Sluttbrukerveiledning_OPCUA_Tailscale.docx` for full instruksjon og `Avsluttende prosjekt.docx` for bakgrunn og vurdering.

---

## Forfatter

**Espen Klippenberg Bø**  
Student ved [TISIP fagskole](https://tisip.no/public/)  
[LinkedIn-profil](https://www.linkedin.com/in/espen-bo/)

---

## Lisens

Dette prosjektet er åpent og fritt å bruke for læring og demonstrasjon. For bruk i produksjon, anbefales det å teste grundig og tilpasse etter lokale behov.
