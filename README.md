# L07E01: Generator function
Vytvořte modul `progression` obsahující funkci (generátorovou) `arithmetic_progression(begin, step, end)`. Uvažujme pouze rostoucí posloupnosti.

## Funkce `arithmetic_progression(begin, step, end)`
Generátor generující prvky [aritmetické posloupnosti](https://cs.wikipedia.org/wiki/Aritmetická_posloupnost) počínaje prvkem `begin`, diferencí `step` a končicí prvkem `end` (posloupnost posledni prvek neobsahuje).

```python
for number in arithmetic_progression(5, 2, 8):
    print(number)

# Vypíše následující čísla, v každý moment se vypočítá a uloží pouze jedno, celá posloupnost není nikde uložena
5
7
```