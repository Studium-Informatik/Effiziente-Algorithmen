---
typ: Problem
bereich: Komplexitätstheorie / Logik
klasse: P-vollständig / auswertungsnah
aliases:
  - Model Checking
  - MODEL-CHECKING
  - Modellprüfung
tags:
  - reduktion
  - komplexitaet
  - logik
  - circuit-eval
---

# MODEL-CHECKING

## Kurzidee

**MODEL-CHECKING** fragt, ob eine Struktur bzw. Interpretation eine logische Formel erfüllt.

Allgemein:

$$
\mathcal{A} \models \varphi?
$$

In den Folien wird es als Problem betrachtet, das auf [[CIRCUIT-EVAL]] reduziert werden kann.

## Rolle im Reduktionsgraphen

[[MODEL-CHECKING]] ist Ausgangsproblem einer Polynomialzeit-Reduktion auf [[CIRCUIT-EVAL]].

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[CIRCUIT-EVAL]] | Polynomialzeit-Reduktion | Die logische Formel wird als Schaltkreisstruktur ausgewertet. |

## Konstruktionsidee

Eine aussagenlogische oder logisch strukturierte Formel wird in einen logischen Schaltkreis übersetzt.

- Variablen bzw. atomare Aussagen werden zu Eingängen.
- Junktoren wie $\land$, $\lor$, $\neg$ werden zu Gattern.
- Die Auswertung der Formel entspricht der Auswertung des Schaltkreises.

## Logische Entsprechung

$$
(\mathcal{A},\varphi) \in MODEL\text{-}CHECKING \Longleftrightarrow C_{\varphi,\mathcal{A}} \in CIRCUIT\text{-}EVAL
$$

## Klausurmerksatz

Model-Checking kann als Schaltkreisauswertung verstanden werden: Formelstruktur wird zu Schaltkreisstruktur.

## Quelle / Zitat

- Folien_09
- „Reduktion von MODEL-CHECKING auf CIRCUIT-EVAL, was in Polynomialzeit funktioniert!“

## Verwandte Notizen

- [[CIRCUIT-EVAL]]
- [[SAT]]
- [[VALIDITY]]
