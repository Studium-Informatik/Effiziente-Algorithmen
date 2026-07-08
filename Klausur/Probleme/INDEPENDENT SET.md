---
typ: Problem
bereich: Komplexitätstheorie / Graphen
klasse: NP-vollständig
aliases:
  - Independent Set
  - Unabhängige Menge
tags:
  - reduktion
  - komplexitaet
  - graphen
  - np-vollstaendig
---

# INDEPENDENT SET

## Kurzidee

Beim Problem **INDEPENDENT SET** fragt man, ob ein Graph eine unabhängige Menge einer bestimmten Größe besitzt.

Eine unabhängige Menge ist eine Knotenauswahl, in der keine zwei ausgewählten Knoten durch eine Kante verbunden sind.

Formal:

$$
\text{Gibt es } S \subseteq V \text{ mit } |S| \ge k \text{ und } \forall u,v \in S: \{u,v\} \notin E?
$$

## Rolle im Reduktionsgraphen

[[INDEPENDENT SET]] ist Zielproblem der Reduktion von [[3-SAT]]. Damit wird gezeigt, dass ein konkretes Graphproblem NP-hart ist.

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[3-SAT]] | Polynomialzeit-Reduktion | Klauseln werden zu Dreiecken, komplementäre Literale werden durch Konfliktkanten verbunden. |

## Konstruktionsidee

Zu jeder 3-SAT-Klausel wird ein Dreieck erzeugt. Die drei Knoten entsprechen den drei Literalen.

Zusätzlich werden Kanten zwischen Knoten eingefügt, deren Literale sich widersprechen, also z. B. $x$ und $\neg x$.

Eine unabhängige Menge der Größe „Anzahl der Klauseln“ wählt genau ein Literal pro Klausel aus, ohne Widersprüche zu erzeugen.

## Logische Entsprechung

$$
\varphi \in 3\text{-}SAT \Longleftrightarrow (G,k) \in INDEPENDENT\ SET
$$

## Klausurmerksatz

Bei der Reduktion von 3-SAT auf Independent Set stehen Dreiecke für Klauseln und Konfliktkanten für widersprüchliche Literale.

## Quelle / Zitat

- Folien_10
- „Es gibt eine Polynomialzeit-Reduktion von 3-SAT auf INDEPENDENT SET.“

## Verwandte Notizen

- [[3-SAT]]
- [[SAT]]
- [[3-COLORABILITY]]
