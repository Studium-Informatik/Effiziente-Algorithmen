---
typ: Problem
bereich: Komplexitätstheorie
klasse: NP-vollständig
aliases:
  - SAT
  - Satisfiability
  - Erfüllbarkeitsproblem
tags:
  - reduktion
  - komplexitaet
  - np
  - np-vollstaendig
  - sat
---

# SAT

## Kurzidee

**SAT** fragt, ob eine aussagenlogische Formel erfüllbar ist.

Formal:

$$
SAT = \{ \varphi \mid \varphi \text{ ist erfüllbar} \}
$$

Eine Formel ist erfüllbar, wenn es eine Belegung ihrer Variablen gibt, unter der die Formel wahr wird.

## Rolle im Reduktionsgraphen

[[SAT]] ist der zentrale Knotenpunkt der NP-Reduktionen. Es ist Zielproblem für allgemeine NP-Probleme und mehrere konkrete Modellierungsprobleme, aber auch Ausgangsproblem für die Reduktion auf [[3-SAT]].

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[Beliebiges Problem P in NP]] | Cook-Levin / Polynomialzeit | Berechnungen in NP werden als boolesche Formel codiert. |
| [[3-COLORABILITY]] | Polynomialzeit-Reduktion | Farben von Knoten werden durch boolesche Variablen codiert. |
| [[HOMOMORPHISMUS]] | Polynomialzeit-Reduktion | Mögliche Abbildungen zwischen Graphknoten werden als Variablen codiert. |

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[3-SAT]] | Polynomialzeit-Reduktion | Eine beliebige Formel wird in eine erfüllungsäquivalente 3-CNF-Formel übersetzt. |

## Wichtige Reduktionskette

$$
[[Beliebiges Problem P in NP]] \le_p [[SAT]] \le_p [[3-SAT]] \le_p [[INDEPENDENT SET]]
$$

## Klausurmerksatz

SAT ist das Standardziel, um NP-Härte zu zeigen. Sobald ein Problem auf SAT reduziert wird, kann man es mit SAT-Methoden modellieren. Sobald SAT auf ein Problem reduziert wird, ist dieses Zielproblem mindestens so schwer wie SAT.

## Quelle / Zitat

- Folien_10, Folien_11
- „Um zu zeigen, dass SAT NP-hart ist, müssen wir für jedes Problem P in NP zeigen, dass es eine Polynomialzeit-Reduktion von P auf SAT gibt.“
- „Wir müssen von SAT auf 3-SAT reduzieren [...] in eine erfüllungs-äquivalente Formel $\psi$ in 3-CNF übersetzt werden.“
- „Reduktion: 3-COLORABILITY auf SAT“.
- „Reduktion von Homomorphismus auf SAT [...] sodass $\phi$ erfüllbar $\Leftrightarrow$ es gibt Homomorphismus from G1 to G2.“

## Verwandte Notizen

- [[Beliebiges Problem P in NP]]
- [[3-SAT]]
- [[3-COLORABILITY]]
- [[HOMOMORPHISMUS]]
- [[VALIDITY]]
- [[co-SAT]]
