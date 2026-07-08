---
typ: Problem
bereich: Komplexitätstheorie / Optimierung
klasse: NP-vollständig
aliases:
  - TSP
  - TSP-Entscheidungsproblem
  - Travelling-Salesperson-Problem
  - Traveling-Salesman-Problem
tags:
  - reduktion
  - komplexitaet
  - optimierung
  - graphen
  - np-vollstaendig
  - tsp
---

# TSP(E)

## Kurzidee

**TSP(E)** bezeichnet hier die Entscheidungsvariante des Travelling-Salesperson-Problems: Gibt es eine Rundtour durch alle Städte mit Gesamtkosten höchstens `B`?

## Rolle im Reduktionsgraphen

[[TSP(E)]] ist ein klassisches NP-vollständiges Entscheidungsproblem und erhält NP-Schwere typischerweise über eine Reduktion von [[HAMILTON-CYCLE]].

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[SAT]] | theoretische Cook-Levin-Reduktion | Da TSP(E) in NP liegt, kann es prinzipiell auf SAT reduziert werden. |

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[HAMILTON-CYCLE]] | Polynomialzeit-Reduktion | Hamiltonkreise werden als Touren mit Kosten höchstens `n` kodiert. |

## Konstruktionsidee

Aus einem Graphen `G` mit `n` Knoten wird ein vollständiger gewichteter Graph gebaut. Für ursprüngliche Kanten setzt man Kosten `1`, für Nichtkanten Kosten `2`. Dann existiert eine Tour mit Kosten höchstens `n` genau dann, wenn `G` einen Hamiltonkreis besitzt.

## Klausurmerksatz

TSP als Entscheidungsproblem ist NP-vollständig; die Optimierungsvariante fragt nach der kürzesten Tour.

## Quelle / Zitat

- Vorlesungsfolien / Übung: Hamilton-Cycle zu TSP
- Hinweis: konkrete Foliennummer ergänzen.

## Verwandte Notizen

- [[HAMILTON-CYCLE]]
- [[HAMILTON-PATH]]
- [[SAT]]
