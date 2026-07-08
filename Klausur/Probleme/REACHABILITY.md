---
typ: Problem
bereich: Komplexitätstheorie / Graphen
klasse: P
aliases:
  - Reachability
  - Erreichbarkeit
  - Graph-Erreichbarkeit
tags:
  - reduktion
  - komplexitaet
  - graphen
  - 2-sat
---

# REACHABILITY

## Kurzidee

**REACHABILITY** fragt, ob in einem gerichteten Graphen ein Knoten $t$ von einem Startknoten $s$ aus erreichbar ist.

Formal:

$$
\text{Gibt es einen gerichteten Pfad von } s \text{ nach } t?
$$

## Rolle im Reduktionsgraphen

[[REACHABILITY]] ist Zielproblem der Reduktion von [[2-SAT]]. Die Erreichbarkeit im Implikationsgraphen entscheidet, ob Widersprüche zwischen Literalen entstehen.

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[2-SAT]] | Polynomialzeit-Reduktion | Erfüllbarkeit wird über Erreichbarkeit im Implikationsgraphen geprüft. |

## Zusammenhang mit 2-SAT

Aus einer 2-SAT-Formel entsteht ein Implikationsgraph. Für jede Variable $x$ betrachtet man die Literale $x$ und $\neg x$.

Die Formel ist unerfüllbar, wenn für ein $x$ gilt:

$$
x \leadsto \neg x
$$

und

$$
\neg x \leadsto x
$$

also wenn beide Literale in derselben stark zusammenhängenden Komponente liegen.

## Klausurmerksatz

Reachability ist der graphentheoretische Kern hinter dem effizienten Algorithmus für 2-SAT.

## Quelle / Zitat

- Folien_11
- „Es gibt eine Polynomialzeit-Reduktion von dem 2-SAT-Problem auf das REACHABILITY-Problem.“

## Verwandte Notizen

- [[2-SAT]]
- [[SAT]]
- [[3-SAT]]
