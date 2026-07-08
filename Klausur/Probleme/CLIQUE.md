---
typ: Problem
bereich: Komplexitätstheorie / Graphen
klasse: NP-vollständig
aliases:
  - Clique
  - k-Clique
  - Cliquenproblem
tags:
  - reduktion
  - komplexitaet
  - graphen
  - np-vollstaendig
  - komplementgraph
---

# CLIQUE

## Kurzidee

**CLIQUE** fragt, ob ein Graph eine Menge von mindestens `k` paarweise benachbarten Knoten enthält.

Eine solche Knotenmenge heißt Clique.

## Rolle im Reduktionsgraphen

[[CLIQUE]] ist eng äquivalent zu [[INDEPENDENT SET]] über den Komplementgraphen. Dadurch kann NP-Vollständigkeit unmittelbar zwischen beiden Problemen übertragen werden.

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[INDEPENDENT SET]] | Polynomialzeit-Reduktion | Eine k-Clique in `G` ist ein unabhängiges Set der Größe `k` im Komplementgraphen. |
| [[VERTEX COVER]] | über [[INDEPENDENT SET]] | Unabhängige Mengen entsprechen Komplementen von Vertex Covers. |

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[INDEPENDENT SET]] | Polynomialzeit-Reduktion | Ein unabhängiges Set in `G` ist eine Clique im Komplementgraphen. |
| [[3-SAT]] | typische Reduktion über [[INDEPENDENT SET]] | Klausel-Literal-Auswahlen werden als kompatible Cliquen modelliert. |

## Konstruktionsidee

Man bildet den Komplementgraphen `Ḡ`: Zwei Knoten sind in `Ḡ` genau dann verbunden, wenn sie in `G` nicht verbunden sind. Dann entspricht jede unabhängige Menge in `G` einer Clique in `Ḡ`.

## Klausurmerksatz

Clique in `G` ist Independent Set im Komplementgraphen `Ḡ`.

## Quelle / Zitat

- Vorlesungsfolien / Übung: Graphprobleme und Komplementgraph
- Hinweis: konkrete Foliennummer ergänzen.

## Verwandte Notizen

- [[INDEPENDENT SET]]
- [[VERTEX COVER]]
- [[3-SAT]]
