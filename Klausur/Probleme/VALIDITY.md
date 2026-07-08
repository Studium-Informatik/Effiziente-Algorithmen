---
typ: Problem
bereich: Komplexitätstheorie / Logik
klasse: co-NP-vollständig
aliases:
  - Validity
  - Allgemeingültigkeit
  - Tautologieproblem
tags:
  - reduktion
  - komplexitaet
  - logik
  - co-sat
---

# VALIDITY

## Kurzidee

**VALIDITY** fragt, ob eine aussagenlogische Formel unter jeder Belegung wahr ist.

Formal:

$$
VALIDITY = \{\varphi \mid \varphi \text{ ist allgemeingültig}\}
$$

Das heißt:

$$
\forall \alpha: \alpha \models \varphi
$$

## Rolle im Reduktionsgraphen

[[VALIDITY]] ist über Negation eng mit [[co-SAT]] verbunden. In den Folien wird die Reduktion in beide Richtungen genannt.

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[co-SAT]] | Polynomialzeit-Reduktion | Eine unerfüllbare Formel entspricht einer allgemeingültigen Negation. |

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[co-SAT]] | Polynomialzeit-Reduktion | Eine Formel ist allgemeingültig genau dann, wenn ihre Negation unerfüllbar ist. |

## Zentrale Äquivalenz

$$
\varphi \in VALIDITY \Longleftrightarrow \neg \varphi \in co\text{-}SAT
$$

Umgekehrt gilt:

$$
\varphi \in co\text{-}SAT \Longleftrightarrow \neg \varphi \in VALIDITY
$$

## Klausurmerksatz

VALIDITY und co-SAT sind über Negation direkt ineinander überführbar.

## Quelle / Zitat

- Folien_10
- „VALIDITY kann in Polynomialzeit auf das co-SAT-Problem reduziert werden.“
- „VALIDITY kann direkt auf co-SAT reduziert werden.“
- „co-SAT kann man auf das VALIDITY-Problem reduzieren.“

## Verwandte Notizen

- [[co-SAT]]
- [[SAT]]
- [[3-SAT]]
