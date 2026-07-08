---
typ: Problem
bereich: Komplexitätstheorie / Logik
klasse: NP-vollständig
aliases:
  - NAE-SAT
  - Not-All-Equal-SAT
  - NAE-3-SAT
tags:
  - reduktion
  - komplexitaet
  - logik
  - sat
  - np-vollstaendig
---

# NAESAT

## Kurzidee

**NAESAT** fragt, ob eine aussagenlogische Formel so erfüllbar ist, dass in jeder Klausel nicht alle Literale denselben Wahrheitswert haben.

Bei 3-Klauseln bedeutet das: In jeder Klausel muss mindestens ein Literal wahr und mindestens ein Literal falsch sein.

## Rolle im Reduktionsgraphen

[[NAESAT]] ist ein typisches Zwischenproblem in Reduktionen ausgehend von [[3-SAT]]. Es ist eng mit Varianten wie [[1-IN-3-SAT]] verwandt.

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[1-IN-3-SAT]] | typische Reduktion in Vorlesungen | NAE-Bedingungen werden durch Gadgets in Genau-eins-Bedingungen übersetzt. |
| [[SAT]] | Spezialfall / Kodierung | Jede NAE-Klausel kann durch normale aussagenlogische Bedingungen beschrieben werden. |

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[3-SAT]] | Polynomialzeit-Reduktion | Klauseln werden durch Hilfsvariablen so ersetzt, dass die Not-All-Equal-Bedingung die Erfüllbarkeit simuliert. |

## Konstruktionsidee

Man ergänzt Klausel-Gadgets und gegebenenfalls eine ausgezeichnete Wahrheitsvariable. Dadurch wird aus der Forderung „mindestens ein Literal ist wahr“ eine NAE-Bedingung, bei der nicht alle Literale gleich sein dürfen.

## Klausurmerksatz

NAESAT ist eine NP-vollständige SAT-Variante, bei der jede Klausel sowohl einen wahren als auch einen falschen Eintrag braucht.

## Quelle / Zitat

- Vorlesungsfolien / Übung: Varianten von 3-SAT
- Hinweis: konkrete Foliennummer ergänzen.

## Verwandte Notizen

- [[SAT]]
- [[3-SAT]]
- [[1-IN-3-SAT]]
- [[k-SAT]]
