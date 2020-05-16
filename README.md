# Studienarbeit: Mars Science Laboratory Curiosity Rover

![alt text](Images/mars_rover.jpg "Mars Rover")

Repository contains the documentation paper as well as Python source code written to make the Rover rove. :rocket:

### Meilensteine

| #    | Meilenstein | Termin | Status |
| ---- | --- | --- | --- |
| M01  | Basis-Installation und Konfiguration Raspberry Pi | 20.10.2019 | DONE |
| Mx01 | Entwurf in BrickLink Studio | 27.10.2019 | DONE |
| M02  | Steuerung Rover über Sprachkommandos | 03.11.2019 | DONE |
| M03  | Basis-Installation und Konfiguration Pixy-Kamera | 10.11.2019 | DONE |
| M04  | Erkennung von Wasserobjekten und Sprachausgabe | 24.11.2019 | DONE |
| M05  | Sechsrädriges Antriebssystem für unebenes Gelände | 01.12.2019 | DONE |
| M06  | Dokumentation mit BrickLink Studio (Version 2.0.10) | 08.12.2019 | DONE |

#### Definitions of Done
- DOD-M01: 
  - Raspberry-Pi-Installation (hier: Raspbian for Robots von Dexter Ind.)
  - BrickPi-Hardware-Aufbau inklusive Gehäuse zur Verbindung mit LEGO-Rover
  - prototypische Aktuatorsteuerung über Python-Script (Anschluss Batterie-Pack, Nutzung der BrickPi3-Library)
- DOD-M02:
  - Einbindung einer Spracherkennungs-Bibliothek
  - Erkennung der englischen Kommandos "Start", "Stop", "Move Left", "Move Right"
  - Ausführung bestimmter Funktionen nach Erkennung der o. g. Kommandos -> vorerst Dummys mit Konsolenausgabe
- DOD-M03:
  - Installation der Pixy-Cam in einer erhöhten und um 22,5° nach vorn geneigten Position
  - Aufnahme eines Video-Streams
  - Zugriff auf Stream via Python-Script
- DOD-M04:
  - Pixy-Kamera erkennt blaue 1x1-LEGO-Blöcke nach erfolgreichem Training bei mindestens 24 FPS
  - Sprachausgabe des Beispielsatzes "Yes, Master.", der als Antwort auf zuvor implementierte Sprachkommandos entgegnet wird, mittels pyttsx3 (Python-TTS-Bibliothek) und espeak (Unix-TTS-Engine)

#### Backlog
- Sicherstellung der "Unumkippbarkeit" des Rovers -> BrickLink-Modell überarbeiten
![alt text](Images/20200429_Mars_Rover_V5_front.png "Mars Rover Curiosity")
- Greifarm und -steuerung nachträglich ergänzen
- passendes Mikrofon besorgen
- neuen Lautsprecher (höhere Lautstärke)

### Ausstehende Erstattungen für privat ausgelegte Elemente
- USB-Soundkarte Sabrent (EUR 5,94)
- diverse Teile von BricksWorld XXL (EUR 3,74)
- Teile von 20th Century Bricks (EUR 4,13)
- Teile (u. a. Felgen) von Limpensbricks (EUR 78,86)
- Solarmodul von Conrad (EUR 9,99)
