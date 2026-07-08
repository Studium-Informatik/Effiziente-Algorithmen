---
typ: Problem
bereich: Berechenbarkeit / Unentscheidbarkeit
klasse: unentscheidbar
aliases:
  - X
  - Maschinenausgabe 5
  - Ausgabe-5-Problem
tags:
  - reduktion
  - berechenbarkeit
  - unentscheidbarkeit
---

# Maschinenausgabe 5 $X$

## Kurzidee

Das Problem fragt, ob eine Maschine bei ihrer Ausführung die Ausgabe $5$ produziert.

In den Folien wird es etwa als Menge beschrieben:

$$
X = \{m' \mid u(m') = 5\}
$$

## Rolle im Reduktionsgraphen

[[Maschinenausgabe 5 X]] ist ein Zielproblem für eine Reduktion vom [[Halteproblem H]]. Dadurch kann seine Unentscheidbarkeit gezeigt werden.

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[Halteproblem H]] | funktionale Reduktion | Aus einer Maschine wird eine neue Maschine gebaut, die im Haltefall immer $5$ ausgibt. |

## Konstruktionsidee

Zu einer Instanz des Halteproblems wird eine neue Maschine $m'$ konstruiert:

1. Simuliere die ursprüngliche Maschine.
2. Falls die Simulation hält, schreibe bzw. gib $5$ aus.
3. Falls die Simulation nicht hält, entsteht auch keine Ausgabe $5$.

Damit gilt informell:

$$
\langle m,x\rangle \in H \Longleftrightarrow m' \in X
$$

## Klausurmerksatz

Das Ausgabeproblem ist unentscheidbar, weil eine Entscheidung darüber, ob $5$ ausgegeben wird, das [[Halteproblem H]] entscheiden würde.

## Quelle / Zitat

- Folien_07, Folien_08
- „Wir zeigen Unentscheidbarkeit von $X = \{m' \mid u(m') = 5\}$ Reduktion R vom Halteproblem H“.

## Verwandte Notizen

- [[Halteproblem H]]
- [[Nullfunktion-Problem]]
- [[Selbstanwendungsproblem S]]
