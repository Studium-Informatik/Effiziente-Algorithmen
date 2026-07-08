---
typ: Problem
bereich: Komplexitätstheorie / Graphen
klasse: NP-Problem
aliases:
  - Homomorphismus
  - Graphhomomorphismus
tags:
  - reduktion
  - komplexitaet
  - graphen
  - sat
---

# HOMOMORPHISMUS

## Kurzidee

Beim Graph-Homomorphismus fragt man, ob es eine strukturerhaltende Abbildung von einem Graphen $G_1$ in einen Graphen $G_2$ gibt.

Eine Abbildung $h: V(G_1) \to V(G_2)$ ist ein Homomorphismus, wenn für jede Kante gilt:

$$
\{u,v\} \in E(G_1) \Rightarrow \{h(u),h(v)\} \in E(G_2)
$$

## Rolle im Reduktionsgraphen

[[HOMOMORPHISMUS]] wird auf [[SAT]] reduziert. Die Reduktion zeigt, wie mögliche Abbildungen durch boolesche Variablen beschrieben werden können.

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[SAT]] | Polynomialzeit-Reduktion | Variablen beschreiben, welcher Knoten aus $G_1$ auf welchen Knoten aus $G_2$ abgebildet wird. |

## Konstruktionsidee

Für jeden Knoten $u \in V(G_1)$ und jeden Knoten $v \in V(G_2)$ wird eine Variable eingeführt:

$$
x_{u,v}
$$

Bedeutung:

$$
x_{u,v} = \text{wahr} \Longleftrightarrow h(u)=v
$$

Die Formel erzwingt:

1. Jeder Knoten aus $G_1$ wird auf mindestens einen Knoten aus $G_2$ abgebildet.
2. Jeder Knoten aus $G_1$ wird auf höchstens einen Knoten aus $G_2$ abgebildet.
3. Kanten aus $G_1$ werden auf Kanten in $G_2$ abgebildet.

## Logische Entsprechung

$$
\text{Es gibt einen Homomorphismus } G_1 \to G_2 \Longleftrightarrow \varphi \in SAT
$$

## Klausurmerksatz

Homomorphismen werden in SAT modelliert, indem Variablen mögliche Zielknoten der Abbildung repräsentieren.

## Quelle / Zitat

- Folien_10
- „Reduktion von Homomorphismus auf SAT [...] Wir müssen eine Formel $\phi$ definieren [...], sodass $\phi$ erfüllbar $\Leftrightarrow$ es gibt Homomorphismus from G1 to G2.“

## Verwandte Notizen

- [[SAT]]
- [[3-COLORABILITY]]
- [[INDEPENDENT SET]]
