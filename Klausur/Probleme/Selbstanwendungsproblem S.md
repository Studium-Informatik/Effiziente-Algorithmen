---
typ: Problem
bereich: Berechenbarkeit / Unentscheidbarkeit
klasse: unentscheidbar
aliases:
  - S
  - Selbstanwendungsproblem
tags:
  - reduktion
  - berechenbarkeit
  - unentscheidbarkeit
---

# Selbstanwendungsproblem $S$

## Kurzidee

Das **Selbstanwendungsproblem** fragt, ob eine Maschine bzw. ein Programm auf der eigenen Codierung hält.

Formal kann man es als Menge auffassen:

$$
S = \{ i \mid \varphi_i(i) \downarrow \}
$$

Dabei bedeutet $\varphi_i(i) \downarrow$, dass das Programm mit Index $i$ auf Eingabe $i$ hält.

## Rolle im Reduktionsgraphen

Das Selbstanwendungsproblem ist ein klassisches Ausgangsproblem in der Berechenbarkeitstheorie. Es wird verwendet, um das [[Halteproblem H]] mit einer sehr direkten Konstruktion zu verknüpfen.

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[Halteproblem H]] | funktionale Reduktion | Der Index $i$ wird auf das Paar $\langle i,i\rangle$ abgebildet. |

## Wichtige Reduktion

$$
S \leq H
$$

mit

$$
i \in S \Longleftrightarrow \langle i,i\rangle \in H
$$

Die Reduktionsfunktion ist:

$$
f(i) = \langle i,i\rangle
$$

## Klausurmerksatz

Wenn man für $S$ entscheiden könnte, ob eine Maschine auf sich selbst hält, dann könnte man damit auch entsprechende Fälle des [[Halteproblem H]] entscheiden. Die Reduktion zeigt, dass das Selbstanwendungsproblem eng mit dem Halteproblem verbunden ist.

## Quelle / Zitat

- GeminiChat, Folien_07, Folien_08
- „Wir können formal zeigen, dass sich $S$ auf $H$ reduzieren lässt ($S \le H$). Es gilt: $i \in S \Leftrightarrow \langle i, i \rangle \in H$“.

## Verwandte Notizen

- [[Halteproblem H]]
- [[Maschinenausgabe 5 X]]
- [[Nullfunktion-Problem]]
