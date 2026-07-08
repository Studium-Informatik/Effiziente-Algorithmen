---
typ: Berechnungsmodell
bereich: Berechenbarkeit / Programmmodelle
klasse: berechnungsäquivalent zu Turingmaschinen
aliases:
  - Goto
  - Goto-Programm
  - Goto-Programme
tags:
  - reduktion
  - berechenbarkeit
  - programmierung
  - church-turing
---

# Goto-Programme

## Kurzidee

**Goto-Programme** sind imperative Programme mit markierten Befehlen und Sprunganweisungen.

Typische Bestandteile:

- Labels bzw. Marken,
- Zuweisungen,
- bedingte Sprünge,
- unbedingte Sprünge.

## Rolle im Reduktionsgraphen

Goto-Programme stehen in konstruktiver Äquivalenz zu [[While-Programme]] und können außerdem [[Turingmaschinen]] simulieren bzw. von ihnen simuliert werden.

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[While-Programme]] | konstruktive Reduktion | While-Schleifen werden durch Labels und Sprünge simuliert. |
| [[Turingmaschinen]] | Simulation | Konfigurationen und Übergänge der Turingmaschine werden als Variablen und Sprünge codiert. |

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[While-Programme]] | konstruktive Reduktion | Ein Marker bzw. Programmzähler wird durch eine Extra-Variable simuliert. |

## Konstruktionsidee: Goto zu While

Eine zusätzliche Variable $y$ speichert, an welcher Marke das Programm gerade ist. Eine große While-Schleife simuliert dann die Ausführung der einzelnen markierten Befehle.

## Konstruktionsidee: Turingmaschine zu Goto

Die Konfiguration einer Turingmaschine wird codiert:

- Zustand,
- Bandinhalt,
- Kopfposition,
- Übergangsfunktion.

Ein Goto-Programm simuliert anschließend Schritt für Schritt die Konfigurationsübergänge.

## Klausurmerksatz

Goto-Programme eignen sich gut, um Sprünge und Maschinenübergänge explizit zu simulieren.

## Quelle / Zitat

- Folien_03
- „Reduktion $R'(P_G)$: Konstruktion von $P_W$ mit Extra-Variable y, um Marker zu simulieren, sowie einer (sichtbaren) While-Schleife...“.
- „Reduktion $R_G$: Grundidee der Konstruktion von $P_G$ ist Codierung von Konfigurationen und Simulation der Konfigurationsübergänge“.

## Verwandte Notizen

- [[While-Programme]]
- [[Turingmaschinen]]
