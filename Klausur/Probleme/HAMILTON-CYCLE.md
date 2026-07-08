---
typ: Problem
bereich: Komplexitätstheorie / Graphen
klasse: NP-vollständig
aliases:
  - Hamilton Cycle
  - Hamiltonkreis
  - HC
tags:
  - reduktion
  - komplexitaet
  - graphen
  - np-vollstaendig
  - hamilton
---

# HAMILTON-CYCLE

## Kurzidee

**HAMILTON-CYCLE** fragt, ob ein Graph einen Zyklus enthält, der jeden Knoten genau einmal besucht und zum Startknoten zurückkehrt.

## Rolle im Reduktionsgraphen

[[HAMILTON-CYCLE]] ist eng verwandt mit [[HAMILTON-PATH]] und dient als Standardausgangspunkt für Reduktionen auf Tourenprobleme wie [[TSP(E)]].

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[TSP(E)]] | Polynomialzeit-Reduktion | Kanten des Graphen erhalten kleine Kosten, Nichtkanten große Kosten; eine kurze Tour entspricht einem Hamiltonkreis. |

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[HAMILTON-PATH]] | Polynomialzeit-Reduktion | Ein Hamiltonpfad wird durch Zusatzkonstruktion zu einem Hamiltonkreis geschlossen. |
| [[3-SAT]] | typische Reduktion in Vorlesungen | Erfüllende Belegungen werden durch durchlaufbare Gadget-Strukturen kodiert. |

## Konstruktionsidee

Für die Reduktion auf TSP wird aus einem Graphen ein vollständiger gewichteter Graph konstruiert. Originalkanten bekommen Gewicht `1`, Nichtkanten Gewicht `2`. Eine Tour der Länge höchstens `n` existiert genau dann, wenn der ursprüngliche Graph einen Hamiltonkreis besitzt.

## Klausurmerksatz

Hamilton-Cycle ist die „Rundreise ohne Wiederholung“ und reduziert direkt auf die Entscheidungsvariante von TSP.

## Quelle / Zitat

- Vorlesungsfolien / Übung: Hamilton-Cycle und TSP
- Hinweis: konkrete Foliennummer ergänzen.

## Verwandte Notizen

- [[HAMILTON-PATH]]
- [[TSP(E)]]
- [[3-SAT]]
