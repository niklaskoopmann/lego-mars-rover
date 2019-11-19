
# Studienarbeit: Mars Science Laboratory Curiosity Rover

![alt text](Images/mars_rover.jpg "Mars Rover")

Repository contains LaTeX sources of the paper as well as Python source code written to make the Rover rove. :rocket:

### Meilensteine

| # | Meilenstein | Termin | Status |
| --- | --- | --- | --- |
| M01 | Basis-Installation und Konfiguration Raspberry Pi | 20.10.2019 | DONE |
| Mx01 | Entwurf in BrickLink Studio | 27.10.2019 | DONE |
| M02 | Steuerung Rover über Sprachkommandos | 03.11.2019 | DONE |
| M03 | Basis-Installation und Konfiguration Pixy-Kamera | 10.11.2019 | DONE |
| M04 | Erkennung von Wasserobjekten und Sprachausgabe | 24.11.2019 | 33 % |
| M05 | Sechsrädriges Antriebssystem für unebenes Gelände | 01.12.2019 | TODO |
| M06 | Dokumentation mit BrickLink Studio (Version 2.0.10) | 08.12.2019 | TODO |

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
![alt text](Images/Mars_Rover_Updated.png "Mars Rover Curiosity")
- Greifarm und -steuerung 
- ggf. abweichen vom BrickPi zu MotoPi (https://www.reichelt.de/raspberry-pi-shield-motopi-motorsteuerung-rpi-shd-motopi-p202551.html)
- passendes Mikrofon finden und ggf. bestellen
- Räder des Rovers bestellen
- PixyCam mithilfe von blauen 1x1-LEGO-Blöcken (-> "Wasserobjekte") trainieren, sobald diese eintreffen

### Benötigte Teile (unverbindlich)
- 6x Rad-Reifen-Kombi 23799/23800 (zu bestellen)
- 6x Radadapter 92909 (zu bestellen)
- 5x EV3-Motor Medium (Hr. Benseler)
- 12x Liftarm Double Bent 32009
- ca. 56x Pin Connector 75535

### Erstattung für privat ausgelegte Anschaffungen
- USB-Soundkarte Sabrent (EUR 5,94)
