---
typ: Problem
bereich: Komplexitätstheorie / Graphen
klasse: NP-vollständig
aliases:
  - Vertex Cover
  - Knotenüberdeckung
  - k-Vertex-Cover
tags:
  - reduktion
  - komplexitaet
  - graphen
  - np-vollstaendig
  - komplement
---

# VERTEX COVER

## Kurzidee

**VERTEX COVER** fragt, ob es in einem Graphen eine Menge von höchstens `k` Knoten gibt, die jede Kante berührt.

## Rolle im Reduktionsgraphen

[[VERTEX COVER]] ist komplementär zu [[INDEPENDENT SET]] bezüglich der gewählten Knotenmenge. In einem Graphen mit `n` Knoten gilt: Es gibt ein Independent Set der Größe `k` genau dann, wenn es ein Vertex Cover der Größe `n - k` gibt.

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[INDEPENDENT SET]] | Polynomialzeit-Reduktion | Das Komplement eines Vertex Covers ist eine unabhängige Menge. |
| [[CLIQUE]] | über [[INDEPENDENT SET]] | Independent Set entspricht Clique im Komplementgraphen. |

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[INDEPENDENT SET]] | Polynomialzeit-Reduktion | Aus Zielgröße `k` wird Covergröße `n - k`. |
| [[CLIQUE]] | über Komplementgraph | Cliquen werden zuerst als unabhängige Mengen interpretiert. |

## Konstruktionsidee

Für einen Graphen `G = (V, E)` und eine Zahl `k` setzt man `k' = |V| - k`. Eine Menge `S` ist genau dann unabhängig, wenn `V \ S` jede Kante abdeckt.

## Klausurmerksatz

Independent Set und Vertex Cover sind zwei Seiten derselben Knotenauswahl: `S` unabhängig genau dann, wenn `V \ S` ein Vertex Cover ist.

## Quelle / Zitat

- Vorlesungsfolien / Übung: Independent Set, Clique, Vertex Cover
- Hinweis: konkrete Foliennummer ergänzen.

## Verwandte Notizen

- [[INDEPENDENT SET]]
- [[CLIQUE]]
- [[3-SAT]]
