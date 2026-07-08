---
typ: Problem
bereich: Komplexitätstheorie / Graphen
klasse: NP-vollständig
aliases:
  - 3-Colorability
  - 3-Färbbarkeit
  - Graph-3-Färbbarkeit
tags:
  - reduktion
  - komplexitaet
  - graphen
  - sat
---

# 3-COLORABILITY

## Kurzidee

**3-COLORABILITY** fragt, ob die Knoten eines Graphen mit drei Farben gefärbt werden können, sodass benachbarte Knoten verschiedene Farben haben.

Formal:

$$
\exists c: V \to \{1,2,3\} \text{ mit } \forall \{u,v\}\in E: c(u) \ne c(v)
$$

## Rolle im Reduktionsgraphen

[[3-COLORABILITY]] wird auf [[SAT]] reduziert. Dadurch wird gezeigt, wie ein Graphproblem als aussagenlogische Formel modelliert werden kann.

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[SAT]] | Polynomialzeit-Reduktion | Variablen codieren, ob ein Knoten eine bestimmte Farbe erhält. |

## Konstruktionsidee

Für jeden Knoten $v$ und jede Farbe $f$ wird eine boolesche Variable eingeführt:

$$
x_{v,f}
$$

Bedeutung:

$$
x_{v,f} = \text{wahr} \Longleftrightarrow v \text{ hat Farbe } f
$$

Die SAT-Formel erzwingt:

1. Jeder Knoten hat mindestens eine Farbe.
2. Jeder Knoten hat höchstens eine Farbe.
3. Benachbarte Knoten haben nicht dieselbe Farbe.

## Logische Entsprechung

$$
G \in 3\text{-}COLORABILITY \Longleftrightarrow \varphi_G \in SAT
$$

## Klausurmerksatz

Graphfärbung lässt sich gut in SAT übersetzen: Variablen stehen für „Knoten hat Farbe“, Klauseln für die erlaubten und verbotenen Farbkombinationen.

## Quelle / Zitat

- Folien_10, Folien_11
- „Reduktion: 3-COLORABILITY auf SAT“.

## Verwandte Notizen

- [[SAT]]
- [[3-SAT]]
- [[INDEPENDENT SET]]
