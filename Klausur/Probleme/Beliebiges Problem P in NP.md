---
typ: Metaproblem
bereich: Komplexitätstheorie
gruppe: NP
aliases:
  - P in NP
  - beliebiges NP-Problem
  - Problem in NP
tags:
  - reduktion
  - komplexitaet
  - np
  - cook-levin
---

# Beliebiges Problem $P \in NP$

## Kurzidee

Ein Problem $P$ liegt in **NP**, wenn es für Ja-Instanzen ein Zertifikat gibt, das in Polynomialzeit überprüft werden kann.

Äquivalent kann man sagen: Eine nichtdeterministische Turingmaschine entscheidet $P$ in Polynomialzeit.

## Rolle im Reduktionsgraphen

Dieser Knoten steht für den allgemeinen Startpunkt des Satzes von Cook-Levin:

$$
\forall P \in NP: P \le_p SAT
$$

Damit wird [[SAT]] als NP-hart nachgewiesen.

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[SAT]] | Cook-Levin / Polynomialzeit | Die Berechnung einer nichtdeterministischen Maschine wird als erfüllbare Formel codiert. |

## Konstruktionsidee

Für ein beliebiges Problem $P \in NP$ gibt es eine polynomiell zeitbeschränkte Verifikation oder Maschinenberechnung. Diese Berechnung wird als aussagenlogische Formel beschrieben.

Die Formel ist erfüllbar genau dann, wenn es ein gültiges Zertifikat bzw. eine akzeptierende Berechnung gibt.

$$
x \in P \Longleftrightarrow f(x) \in SAT
$$

## Klausurmerksatz

Cook-Levin ist die Grundreduktion der NP-Vollständigkeit: Jedes Problem in NP lässt sich in Polynomialzeit auf [[SAT]] reduzieren.

## Quelle / Zitat

- Folien_11
- „Um zu zeigen, dass SAT NP-hart ist, müssen wir für jedes Problem P in NP zeigen, dass es eine Polynomialzeit-Reduktion von P auf SAT gibt.“

## Verwandte Notizen

- [[SAT]]
- [[3-SAT]]
- [[INDEPENDENT SET]]
