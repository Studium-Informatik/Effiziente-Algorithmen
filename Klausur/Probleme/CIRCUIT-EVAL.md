---
typ: Problem
bereich: Komplexitätstheorie / Schaltkreise
klasse: P-vollständig
aliases:
  - Circuit Eval
  - CIRCUIT-EVAL
  - Schaltkreisauswertung
tags:
  - reduktion
  - komplexitaet
  - schaltkreise
  - model-checking
---

# CIRCUIT-EVAL

## Kurzidee

**CIRCUIT-EVAL** fragt, welchen Wert ein boolescher Schaltkreis bei gegebener Eingabe ausgibt.

Gegeben sind typischerweise:

- ein boolescher Schaltkreis $C$,
- Eingabewerte für die Eingänge,
- die Frage, ob der Ausgang $1$ ist.

## Rolle im Reduktionsgraphen

[[CIRCUIT-EVAL]] ist Zielproblem der Reduktion von [[MODEL-CHECKING]].

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[MODEL-CHECKING]] | Polynomialzeit-Reduktion | Die Formel wird in einen Schaltkreis übersetzt. |

## Konstruktionsidee

Eine logische Formel kann als Schaltkreis gelesen werden:

| Logik | Schaltkreis |
|---|---|
| $\land$ | AND-Gatter |
| $\lor$ | OR-Gatter |
| $\neg$ | NOT-Gatter |
| atomare Aussage | Eingang |

Die Frage, ob die Formel wahr ist, wird zur Frage, ob der Schaltkreis den Wert $1$ ausgibt.

## Klausurmerksatz

CIRCUIT-EVAL ist das natürliche Zielproblem, wenn die Auswertung einer logischen Formel als Schaltkreis dargestellt wird.

## Quelle / Zitat

- Folien_09
- „Reduktion von MODEL-CHECKING auf CIRCUIT-EVAL, was in Polynomialzeit funktioniert!“

## Verwandte Notizen

- [[MODEL-CHECKING]]
- [[SAT]]
- [[VALIDITY]]
