---
typ: Problem
bereich: Komplexitätstheorie / Logik
klasse: co-NP-vollständig
aliases:
  - coSAT
  - co-SAT
  - Unerfüllbarkeit
tags:
  - reduktion
  - komplexitaet
  - logik
  - validity
---

# co-SAT

## Kurzidee

**co-SAT** fragt, ob eine aussagenlogische Formel unerfüllbar ist.

Formal:

$$
co\text{-}SAT = \{\varphi \mid \varphi \text{ ist nicht erfüllbar}\}
$$

Das ist das Komplement von [[SAT]].

## Rolle im Reduktionsgraphen

[[co-SAT]] ist direkt mit [[VALIDITY]] verknüpft. Die Verbindung erfolgt durch Negation.

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[VALIDITY]] | Polynomialzeit-Reduktion | Eine Formel ist allgemeingültig genau dann, wenn ihre Negation unerfüllbar ist. |

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[VALIDITY]] | Polynomialzeit-Reduktion | Eine unerfüllbare Formel wird durch Negation zu einer allgemeingültigen Formel. |

## Zentrale Äquivalenz

$$
\varphi \in co\text{-}SAT \Longleftrightarrow \neg\varphi \in VALIDITY
$$

und:

$$
\varphi \in VALIDITY \Longleftrightarrow \neg\varphi \in co\text{-}SAT
$$

## Klausurmerksatz

co-SAT ist das Unerfüllbarkeitsproblem. Der Übergang zu VALIDITY erfolgt durch Negation.

## Quelle / Zitat

- Folien_10
- „VALIDITY kann in Polynomialzeit auf das co-SAT-Problem reduziert werden.“
- „co-SAT kann man auf das VALIDITY-Problem reduzieren.“

## Verwandte Notizen

- [[VALIDITY]]
- [[SAT]]
- [[3-SAT]]
