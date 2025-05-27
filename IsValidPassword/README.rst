# Szoftverfejlesztési eszközök és módszerek képzés

## Ez a könytár tartalmazza a fenti képzéshez elkészített házi feladatokat.

A könyvtár tartalmazza gyakorlás céljából azt a kódsort, amely a Password Game (https://neal.fun/password-game/)
nevezetű játékot valósítja meg.

A kódsor fejlesztéséhez szabály ötleteket maga a játék ad, mint ahogy az alábbi képen is látható. A kódbázis két fontos
részből áll. Az egyik a szabályok megfogalmazása, a másik a szabályok futtatása.

    def is_valid_*rule(s): --> a *rule helyére kerüljön a szabály rövid elnevezése
        return *True --> a *True helyére kerüljön egy olyan szabály, ami beteljesülése esetén True értéket ad

    elif not is_valid_rule(input_str): --> a fenti szabály meghívása, ahol fontos a *not* előtag
         print("Must contain ...") --> a szabály szöveges megfogalmazása