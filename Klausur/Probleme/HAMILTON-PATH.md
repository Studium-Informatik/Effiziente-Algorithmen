---
typ: Problem
bereich: Komplexitätstheorie / Graphen
klasse: NP-vollständig
aliases:
  - Hamilton Path
  - Hamiltonpfad
  - HP
tags:
  - reduktion
  - komplexitaet
  - graphen
  - np-vollstaendig
  - hamilton
---

# HAMILTON-PATH

## Kurzidee

**HAMILTON-PATH** fragt, ob ein Graph einen Pfad enthält, der jeden Knoten genau einmal besucht.

## Rolle im Reduktionsgraphen

[[HAMILTON-PATH]] ist ein klassisches NP-vollständiges Graphproblem und wird häufig auf [[HAMILTON-CYCLE]] reduziert, indem Pfadenden durch zusätzliche Konstruktionen zu einem Zyklus geschlossen werden.

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[HAMILTON-CYCLE]] | Polynomialzeit-Reduktion | Durch Zusatzknoten oder markierte Endpunkte wird ein Hamiltonpfad in einen Hamiltonkreis übersetzt. |

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[3-SAT]] | typische Reduktion in Vorlesungen | Variablen- und Klausel-Gadgets erzwingen einen Pfad, der genau einer erfüllenden Belegung entspricht. |

## Konstruktionsidee

Eine typische Reduktion fügt einen neuen Knoten hinzu, der mit möglichen Start- und Endknoten verbunden wird. Ein Hamiltonpfad im ursprünglichen Graphen lässt sich dann zu einem Hamiltonkreis im erweiterten Graphen schließen.

## Klausurmerksatz

Hamiltonpfad: jeden Knoten genau einmal besuchen; Hamiltonkreis: zusätzlich zum Start zurückkehren.

## Quelle / Zitat

- Vorlesungsfolien / Übung: Hamiltonsche Wege und Kreise
- Hinweis: konkrete Foliennummer ergänzen.

## Verwandte Notizen

- [[HAMILTON-CYCLE]]
- [[TSP(E)]]
- [[3-SAT]]
