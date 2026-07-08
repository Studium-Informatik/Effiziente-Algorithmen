---
typ: Problem
bereich: Berechenbarkeitstheorie
klasse: unentscheidbar
aliases:
  - H̄
  - Komplement des Halteproblems
  - Non-Halting Problem
tags:
  - reduktion
  - berechenbarkeit
  - unentscheidbar
  - komplement
  - semi-entscheidbarkeit
---

# Nichthalteproblem H̄

## Kurzidee

**Nichthalteproblem H̄** fragt, ob eine gegebene Maschine auf einer gegebenen Eingabe **nicht** hält.

Formal ist es das Komplement von [[Halteproblem H]].

## Rolle im Reduktionsgraphen

[[Nichthalteproblem H̄]] steht in direkter Komplementbeziehung zu [[Halteproblem H]]. Da [[Halteproblem H]] unentscheidbar ist, ist auch sein Komplement unentscheidbar. Außerdem zeigt die Beziehung, dass semi-entscheidbare Probleme unter Komplementbildung im Allgemeinen nicht abgeschlossen sind.

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[Halteproblem H]] | Komplementargument | Ein Entscheider für H̄ würde durch Vertauschen der Antwort einen Entscheider für H liefern. |

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[Halteproblem H]] | Komplementbeziehung | H und H̄ beschreiben dieselbe Frage mit vertauschten Ja-/Nein-Instanzen. |

## Konstruktionsidee

Angenommen, H̄ wäre entscheidbar. Dann könnte man auf Eingabe `(M, x)` den Entscheider für H̄ starten und die Antwort invertieren. Dadurch entstünde ein Entscheider für [[Halteproblem H]], was dem Unentscheidbarkeitsresultat widerspricht.

## Klausurmerksatz

Das Komplement des Halteproblems ist ebenfalls unentscheidbar und im Standardmodell nicht semi-entscheidbar.

## Quelle / Zitat

- Vorlesungsfolien / Übung: Halteproblem und Komplementsprachen
- Hinweis: konkrete Foliennummer ergänzen.

## Verwandte Notizen

- [[Halteproblem H]]
- [[Selbstanwendungsproblem S]]
- [[Turingmaschinen]]
