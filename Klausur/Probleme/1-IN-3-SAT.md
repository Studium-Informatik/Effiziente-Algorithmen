---
typ: Problem
bereich: Komplexitätstheorie / Logik
klasse: NP-vollständig
aliases:
  - ONE-IN-THREE-SAT
  - Exact-1-in-3-SAT
  - Genau-eins-in-drei-SAT
tags:
  - reduktion
  - komplexitaet
  - logik
  - sat
  - np-vollstaendig
---

# 1-IN-3-SAT

## Kurzidee

**1-IN-3-SAT** fragt, ob eine Formel aus 3-Literal-Klauseln so belegbar ist, dass in jeder Klausel **genau ein** Literal wahr ist.

## Rolle im Reduktionsgraphen

[[1-IN-3-SAT]] ist eine besonders restriktive SAT-Variante. Trotz der starken Einschränkung bleibt das Problem NP-vollständig und wird häufig als Zwischenproblem für Gadget-Reduktionen verwendet.

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[SAT]] | Spezialfall / Kodierung | Die Genau-eins-Bedingung lässt sich als aussagenlogische Formel ausdrücken. |
| [[3-SAT]] | Polynomialzeit-Kodierung | Jede Genau-eins-Klausel kann durch mehrere 3-CNF-Klauseln beschrieben werden. |

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[3-SAT]] | typische Polynomialzeit-Reduktion | 3-SAT-Klauseln werden durch Gadgets ersetzt, die genau eine wahre Wahl erzwingen. |
| [[NAESAT]] | typische Reduktion in Vorlesungen | Not-All-Equal-Bedingungen werden durch Genau-eins-Gadgets simuliert. |

## Konstruktionsidee

Für jede ursprüngliche Klausel werden Hilfsvariablen eingeführt. Die neuen Klauseln erzwingen, dass eine zulässige Belegung genau eine der relevanten Optionen auswählt und damit die ursprüngliche Klausel erfüllt.

## Klausurmerksatz

1-IN-3-SAT bleibt NP-vollständig, obwohl jede Klausel exakt eine wahre Variable verlangt.

## Quelle / Zitat

- Vorlesungsfolien / Übung: SAT-Gadgets und NP-Vollständigkeit
- Hinweis: konkrete Foliennummer ergänzen.

## Verwandte Notizen

- [[SAT]]
- [[3-SAT]]
- [[NAESAT]]
- [[k-SAT]]
