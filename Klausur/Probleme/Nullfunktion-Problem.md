---
typ: Problem
bereich: Berechenbarkeit / Unentscheidbarkeit
klasse: nicht aufzählbar / unentscheidbar
aliases:
  - Nullfunktion
  - konstante Nullfunktion
  - const_0^1
tags:
  - reduktion
  - berechenbarkeit
  - unentscheidbarkeit
---

# Nullfunktion-Problem

## Kurzidee

Das Problem fragt, ob die von einem Index $j$ berechnete Funktion genau die konstante Nullfunktion ist.

In den Folien erscheint die Menge:

$$
\{j \in \mathbb{N} \mid \phi_j = const_0^1\}
$$

Dabei ist $const_0^1$ die einstellige konstante Nullfunktion.

## Rolle im Reduktionsgraphen

Das Nullfunktion-Problem ist ein Zielproblem für eine Reduktion vom [[Halteproblem H]]. Es dient als Beispiel dafür, dass auch scheinbar einfache semantische Eigenschaften von Programmen nicht entscheidbar bzw. nicht aufzählbar sein können.

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[Halteproblem H]] | funktionale Reduktion | Konstruiere einen Index $j$, dessen berechnete Funktion genau im relevanten Fall konstant $0$ ist. |

## Konstruktionsidee

Aus einer Halteproblem-Instanz wird ein neuer Programmindex erzeugt. Dieses neue Programm wird so gebaut, dass seine berechnete Funktion die konstante Nullfunktion ist, genau dann wenn die gewünschte Bedingung aus der Halteproblem-Instanz erfüllt ist.

Typische Beweisform:

$$
\langle m,x\rangle \in H \Longleftrightarrow j \in \{j \mid \phi_j = const_0^1\}
$$

Je nach Folienkonvention kann die Richtung über das Komplement bzw. Nicht-Halten formuliert sein. Entscheidend ist die berechenbare Transformation der Instanz.

## Klausurmerksatz

Das Nullfunktion-Problem ist ein semantisches Programmproblem. Solche Probleme sind typisch für Reduktionen vom Halteproblem.

## Quelle / Zitat

- Folien_08
- „Beispiel: Reduktion von H, $\{j \in \mathbb{N} \mid \phi_j = const_0^1\}$ nicht aufzählbar. Zeige $H \le \{j \in \mathbb{N} \mid \phi_j = const_0^1\}$“.

## Verwandte Notizen

- [[Halteproblem H]]
- [[Maschinenausgabe 5 X]]
- [[Selbstanwendungsproblem S]]
