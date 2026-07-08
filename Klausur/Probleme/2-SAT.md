---
typ: Problem
bereich: Komplexitätstheorie / Logik
klasse: P
aliases:
  - 2SAT
  - 2-SAT
  - 2-CNF-SAT
tags:
  - reduktion
  - komplexitaet
  - logik
  - reachability
---

# 2-SAT

## Kurzidee

**2-SAT** ist die Erfüllbarkeit von Formeln in 2-CNF, also einer Konjunktion von Klauseln mit jeweils höchstens zwei Literalen.

Beispiel:

$$
(x \lor y) \land (\neg x \lor z) \land (\neg y \lor \neg z)
$$

## Rolle im Reduktionsgraphen

[[2-SAT]] wird auf [[REACHABILITY]] reduziert. Dadurch wird gezeigt, dass 2-SAT effizient lösbar ist.

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[REACHABILITY]] | Polynomialzeit-Reduktion | Die Formel wird in einen Implikationsgraphen übersetzt. |

## Konstruktionsidee

Jede Klausel

$$
(a \lor b)
$$

wird als zwei Implikationen gelesen:

$$
\neg a \Rightarrow b
$$

und

$$
\neg b \Rightarrow a
$$

Aus diesen Implikationen entsteht ein gerichteter Graph über Literalen.

Eine 2-SAT-Formel ist unerfüllbar, wenn es eine Variable $x$ gibt, sodass $x$ und $\neg x$ gegenseitig erreichbar sind.

## Klausurmerksatz

2-SAT ist im Gegensatz zu 3-SAT effizient lösbar. Der zentrale Trick ist der Implikationsgraph.

## Quelle / Zitat

- Folien_11
- „Es gibt eine Polynomialzeit-Reduktion von dem 2-SAT-Problem auf das REACHABILITY-Problem.“

## Verwandte Notizen

- [[REACHABILITY]]
- [[SAT]]
- [[3-SAT]]
