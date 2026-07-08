---
typ: Berechnungsmodell
bereich: Berechenbarkeit / Programmmodelle
klasse: Standardmodell der Berechenbarkeit
aliases:
  - Turingmaschine
  - Turingmaschinen
  - TM
tags:
  - reduktion
  - berechenbarkeit
  - programmierung
  - church-turing
---

# Turingmaschinen

## Kurzidee

Eine **Turingmaschine** ist ein formales Berechnungsmodell mit Zuständen, Band bzw. Bändern, Schreib-Lese-Kopf und Übergangsfunktion.

Sie dient als Standardmodell für Berechenbarkeit.

## Rolle im Reduktionsgraphen

[[Turingmaschinen]] werden mit [[While-Programme]] und [[Goto-Programme]] konstruktiv verglichen. Die Reduktionen zeigen, dass diese Modelle berechnungsäquivalent sind.

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[While-Programme]] | Simulation | Variablen werden durch Bänder simuliert. |

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[Goto-Programme]] | Simulation | Konfigurationen und Kopfbewegungen werden als Variablen und Sprünge codiert. |

## Konstruktionsidee: While zu Turingmaschine

Ein While-Programm wird so simuliert, dass Variableninhalte auf Bändern gespeichert werden. Einzelne Programmanweisungen werden durch Turingmaschinen-Teile realisiert.

## Konstruktionsidee: Turingmaschine zu Goto

Eine Turingmaschinenkonfiguration wird in Variablen codiert. Das Goto-Programm führt dann eine Schleife über die Übergänge der Maschine aus.

Zu codieren sind insbesondere:

- aktueller Zustand,
- Bandinhalt,
- Kopfposition,
- Übergangsfunktion.

## Klausurmerksatz

Turingmaschinen sind das Referenzmodell. Wenn While- und Goto-Programme Turingmaschinen simulieren können und umgekehrt, stützt das die formale Äquivalenz dieser Berechnungsmodelle.

## Quelle / Zitat

- Folien_03
- „Reduktion $R_T(P'_W)$ via $P'_W = R'(R(P_W))$ [...] Simulation mit TM M mit $IP'_W +1$ Bändern“.
- „Reduktion $R_G$: Grundidee der Konstruktion von $P_G$ ist Codierung von Konfigurationen und Simulation der Konfigurationsübergänge“.

## Verwandte Notizen

- [[While-Programme]]
- [[Goto-Programme]]
