---
typ: Problem
bereich: Komplexitätstheorie
klasse: NP-vollständig
aliases:
  - 3SAT
  - 3-SAT
  - 3-CNF-SAT
tags:
  - reduktion
  - komplexitaet
  - np
  - np-vollstaendig
  - sat
---

# 3-SAT

## Kurzidee

**3-SAT** ist die Variante von [[SAT]], bei der die Formel in konjunktiver Normalform vorliegt und jede Klausel genau drei Literale besitzt.

Beispiel:

$$
(x_1 \lor \neg x_2 \lor x_3) \land (\neg x_1 \lor x_4 \lor x_5)
$$

## Rolle im Reduktionsgraphen

[[3-SAT]] ist ein klassisches Zwischenproblem für NP-Härtebeweise. Es ist spezieller als [[SAT]], aber immer noch NP-vollständig.

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[SAT]] | Polynomialzeit-Reduktion | Eine allgemeine Formel wird in erfüllungsäquivalente 3-CNF transformiert. |

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[INDEPENDENT SET]] | Polynomialzeit-Reduktion | Für jede Klausel wird ein Dreieck im Graphen erzeugt; Konflikte werden durch Kanten dargestellt. |

## Konstruktionsidee: SAT zu 3-SAT

Eine beliebige Formel wird mithilfe von Umformungen und Hilfsvariablen in eine Formel $\psi$ in 3-CNF übersetzt.

Wichtig ist nicht syntaktische Gleichheit, sondern Erfüllungsäquivalenz:

$$
\varphi \in SAT \Longleftrightarrow \psi \in 3\text{-}SAT
$$

## Konstruktionsidee: 3-SAT zu Independent Set

Für jede Klausel entsteht ein Dreieck mit den drei Literalen als Knoten. Zusätzlich werden Kanten zwischen komplementären Literalen verschiedener Klauseln eingefügt.

Eine erfüllende Belegung entspricht dann einer unabhängigen Menge, die aus jeder Klausel genau ein wahres Literal auswählt.

## Klausurmerksatz

3-SAT ist oft der praktische Startpunkt, um NP-Härte für Graphprobleme zu zeigen.

## Quelle / Zitat

- Folien_10, Folien_11
- „Wir müssen von SAT auf 3-SAT reduzieren [...] in eine erfüllungs-äquivalente Formel $\psi$ in 3-CNF übersetzt werden.“
- „Es gibt eine Polynomialzeit-Reduktion von 3-SAT auf INDEPENDENT SET.“

## Verwandte Notizen

- [[SAT]]
- [[INDEPENDENT SET]]
- [[Beliebiges Problem P in NP]]
