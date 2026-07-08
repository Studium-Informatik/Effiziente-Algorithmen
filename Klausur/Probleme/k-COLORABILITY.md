---
typ: Problem
bereich: Komplexitätstheorie / Graphen
klasse: P für k <= 2, NP-vollständig für k >= 3
aliases:
  - k-Colorability
  - k-Färbbarkeit
  - Graph-k-Färbung
tags:
  - reduktion
  - komplexitaet
  - graphen
  - faerbung
  - np-vollstaendig
  - homomorphismus
---

# k-COLORABILITY

## Kurzidee

**k-COLORABILITY** fragt, ob die Knoten eines Graphen mit höchstens `k` Farben gefärbt werden können, sodass benachbarte Knoten verschiedene Farben erhalten.

## Rolle im Reduktionsgraphen

[[k-COLORABILITY]] verallgemeinert [[3-COLORABILITY]]. Für festes `k >= 3` ist das Problem NP-vollständig; für `k = 2` ist es effizient über Bipartitheit lösbar.

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[HOMOMORPHISMUS]] | Modellierung als Homomorphismus | Eine k-Färbung ist ein Graphhomomorphismus nach `K_k`. |
| [[SAT]] | Kodierung | Farben werden durch Variablen kodiert, Kanten erzwingen Ungleichheit. |

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[3-COLORABILITY]] | Spezialfall | 3-COLORABILITY ist k-COLORABILITY für `k = 3`. |
| [[3-SAT]] | typische Reduktion | Variablen- und Klausel-Gadgets erzwingen eine konsistente 3-Färbung. |

## Konstruktionsidee

Für jedes Vertex wird eine Farbe aus `{1, ..., k}` gewählt. Für jede Kante wird verboten, dass beide Endpunkte dieselbe Farbe erhalten. Als Homomorphismus betrachtet ist die Zielfarbe der Knoten eine Abbildung in den vollständigen Graphen `K_k`.

## Klausurmerksatz

k-Färbbarkeit ist ab drei Farben NP-vollständig; 2-Färbbarkeit ist nur Bipartitheit.

## Quelle / Zitat

- Vorlesungsfolien / Übung: Graphfärbung und Homomorphismen
- Hinweis: konkrete Foliennummer ergänzen.

## Verwandte Notizen

- [[3-COLORABILITY]]
- [[HOMOMORPHISMUS]]
- [[3-SAT]]
