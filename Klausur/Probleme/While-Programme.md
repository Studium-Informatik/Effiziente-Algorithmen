---
typ: Berechnungsmodell
bereich: Berechenbarkeit / Programmmodelle
klasse: berechnungsäquivalent zu Turingmaschinen
aliases:
  - While
  - While-Programm
  - While-Programme
tags:
  - reduktion
  - berechenbarkeit
  - programmierung
  - church-turing
---

# While-Programme

## Kurzidee

**While-Programme** sind ein einfaches imperatives Berechnungsmodell mit Variablen, Zuweisungen und While-Schleifen.

Typisches Konstrukt:

```text
while x do
  P
end
```

## Rolle im Reduktionsgraphen

While-Programme werden konstruktiv mit [[Goto-Programme]] und [[Turingmaschinen]] verglichen. Die Reduktionen zeigen, dass die Modelle dieselben berechenbaren Funktionen erfassen.

## Eingehende Reduktionen

| Ausgangsproblem | Art | Idee |
|---|---|---|
| [[Goto-Programme]] | konstruktive Reduktion | Sprungbefehle werden durch eine große While-Schleife und Marker simuliert. |

## Ausgehende Reduktionen

| Zielproblem | Art | Idee |
|---|---|---|
| [[Goto-Programme]] | konstruktive Reduktion | While-Schleifen werden durch Labels und Sprünge übersetzt. |
| [[Turingmaschinen]] | Simulation | Variablen werden durch Bänder simuliert. |

## Konstruktionsidee: While zu Goto

Ein While-Konstrukt wird durch bedingte Sprünge und Labels ersetzt.

Beispielidee:

```text
M_i: if x_i = 0 goto M_{i+1}
     P
     goto M_i
M_{i+1}: ...
```

## Konstruktionsidee: While zu Turingmaschine

Variablen eines While-Programms werden durch Bänder einer Turingmaschine repräsentiert. Die einzelnen Programmanweisungen werden durch entsprechende Maschinenübergänge simuliert.

## Klausurmerksatz

While-Programme sind ein bequemes Programmmodell, das sich sowohl durch Goto-Programme als auch durch Turingmaschinen simulieren lässt.

## Quelle / Zitat

- Folien_03
- „Reduktion $R(P_W)$: Konstruiere zunächst $M_1 : A_1; ...; M_n : A_n;$ Ersetze jedes $M_i$: while $x_i$ do $P$ end durch $M_i$: if $x_i = 0$ goto $M_{i+1}$...“.
- „Reduktion $R_T(P'_W)$ via $P'_W = R'(R(P_W))$ [...] Simulation mit TM M mit $IP'_W +1$ Bändern“.

## Verwandte Notizen

- [[Goto-Programme]]
- [[Turingmaschinen]]
