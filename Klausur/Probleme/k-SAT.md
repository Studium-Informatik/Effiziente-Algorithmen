---
typ: Problem
bereich: Komplexitätstheorie / Logik
klasse: P für k <= 2, NP-vollständig für k >= 3
aliases:
  - kSAT
  - k-CNF-SAT
  - k-KNF-SAT
tags:
  - reduktion
  - komplexitaet
  - logik
  - sat
  - np-vollstaendig
---

# k-SAT

## Kurzidee

**k-SAT** ist die Erfüllbarkeit aussagenlogischer Formeln in k-CNF, also einer Konjunktion von Klauseln mit höchstens oder genau k Literalen pro Klausel.

## Rolle im Reduktionsgraphen

[[k-SAT]] verallgemeinert [[3-SAT]]. Für festes `k >= 3` ist k-SAT NP-vollständig, während [[2-SAT]] effizient lösbar ist.

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[SAT]] | Spezialfall | Jede k-CNF-Formel ist insbesondere eine aussagenlogische Formel. |
| [[3-SAT]] | Polynomialzeit-Reduktion für festes k >= 3 | Lange Klauseln werden durch Hilfsvariablen in 3-Klauseln zerlegt. |

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[3-SAT]] | Spezialfall | 3-SAT ist k-SAT für `k = 3`. |
| [[SAT]] | Normalform-Reduktion | Allgemeine Formeln werden zunächst in eine geeignete CNF-Form gebracht. |

## Konstruktionsidee

Für Klauseln mit mehr als drei Literalen werden neue Hilfsvariablen eingeführt. Eine lange Klausel wird durch eine Kette von 3-Klauseln ersetzt, sodass die neue Formel genau dann erfüllbar ist, wenn die ursprüngliche Formel erfüllbar war.

## Klausurmerksatz

k-SAT ist ab `k = 3` NP-vollständig; der Sonderfall 2-SAT liegt in P.

## Quelle / Zitat

- Vorlesungsfolien / Übung: SAT, 3-SAT und Normalformen
- Hinweis: konkrete Foliennummer ergänzen.

## Verwandte Notizen

- [[SAT]]
- [[2-SAT]]
- [[3-SAT]]
- [[NAESAT]]
