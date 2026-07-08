---
typ: Problem
bereich: Berechenbarkeit / Unentscheidbarkeit
klasse: unentscheidbar
aliases:
  - H
  - Halteproblem
tags:
  - reduktion
  - berechenbarkeit
  - unentscheidbarkeit
---

# Halteproblem $H$

## Kurzidee

Das **Halteproblem** fragt, ob eine gegebene Maschine auf einer gegebenen Eingabe hält.

Typische formale Darstellung:

$$
H = \{ \langle i,x\rangle \mid \varphi_i(x) \downarrow \}
$$

Dabei ist $i$ ein Maschinenindex und $x$ eine Eingabe.

## Rolle im Reduktionsgraphen

Das Halteproblem ist der zentrale Knoten der Unentscheidbarkeitsreduktionen. Es dient als Brücke, um weitere Probleme als unentscheidbar oder nicht aufzählbar nachzuweisen.

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[Selbstanwendungsproblem S]] | funktionale Reduktion | $i$ wird auf $\langle i,i\rangle$ abgebildet. |

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[Maschinenausgabe 5 X]] | funktionale Reduktion | Die Maschine wird so verändert, dass sie beim Halten Ausgabe $5$ erzeugt. |
| [[Nullfunktion-Problem]] | funktionale Reduktion | Es wird ein Index konstruiert, dessen Funktion genau im relevanten Fall konstant $0$ ist. |

## Wichtige Reduktionskette

$$
[[Selbstanwendungsproblem S]] \leq [[Halteproblem H]] \leq [[Maschinenausgabe 5 X]]
$$

und zusätzlich:

$$
[[Halteproblem H]] \leq [[Nullfunktion-Problem]]
$$

## Klausurmerksatz

Um die Unentscheidbarkeit eines neuen Problems zu zeigen, reduziert man häufig das Halteproblem darauf. Wenn das Zielproblem entscheidbar wäre, wäre dadurch auch das Halteproblem entscheidbar. Das ist ein Widerspruch.

## Quelle / Zitat

- Folien_07, Folien_08
- „Wir zeigen Unentscheidbarkeit von $X = \{m' \mid u(m') = 5\}$ Reduktion R vom Halteproblem H“.
- „Beispiel: Reduktion von H, $\{j \in \mathbb{N} \mid \phi_j = const_0^1\}$ nicht aufzählbar. Zeige $H \le \{j \in \mathbb{N} \mid \phi_j = const_0^1\}$“.

## Verwandte Notizen

- [[Selbstanwendungsproblem S]]
- [[Maschinenausgabe 5 X]]
- [[Nullfunktion-Problem]]
