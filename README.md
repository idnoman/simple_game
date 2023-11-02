# zadanie-rekrutacyjne-robocik-Tomasz-Gadziński

W tym repozytorium znajduje się moje rozwiązanie zadania rekrutacyjnego do KN Robocik na stanowisko programisty robotów. Jest to prosta gra, w której poruszamy pionkiem po planszy.

## Spis treści

- [Specyfikacja techniczna](#specyfikacja-techniczna)
  - [Dane ogólne](#dane-ogólne)
  - [Uruchamianie paczki](#uruchamianie-paczki)

## Specyfikacja techniczna
### Dane ogólne
**Nazwa paczki ROS -** `simple_game`

**Wersja ROS** - ROS Noetic na Ubuntu 20.04

W paczce znajdują się wykonane przeze mnie trzy node'y w Pythonie oraz launchfile. Dodatkowo w /scripts/assets umieściłem dwie "grafiki" - pionka i planszy, które wykorzystywane są do graficznego przedstawienia gry.
 > **Uwaga!** - do uruchomienia paczki koniecznie jest zainstalowanie zewnętrznej biblioteki `Pygame`. Szczegóły znajdują się w pliku requirements.txt

Posczególne node'y:

`pawn_controller.py` - pobiera ruch od użytkownika i na jego podstawie zmienia pozycję pionka, a następnie publikuje ją na topic **/simple_game/get_pawn_position**

`session_stats.py` - pobiera informacje o ruchu z topicu **/simple_game/get_move_info** i na ich podstawie generuje na koniec gry podstawowe statystyki

`map_generator.py` - pobiera informacje o położeniu pionka z topicu **/simple_game/get_pawn_position** i generuje planszę oraz pionka wykorzystując bibliotekę Pygame

### Uruchamianie paczki
Po odpowiednim zbudowaniu paczki należy, używając komendy `chmod +x nawza_pliku.py`, nadać wszystkim node'om uprawnienia do uruchamiania. Po zrobieniu tego, dzięki launchfile, można uruchomić paczkę poniższą komendą:
```bash
 roslaunch simple_game simple_game.launch 
```
> **Uwaga!** - Nie należy zmieniać lokalizacji plików w paczce, w celu jej poprawnego uruchomienia. Zmiana ich lokalizacji może skutkować złym wczytaniem grafik, co uniemożliwi włączenie gry.

## Autor
**Tomasz Gadziński**

**tomasz.gadzinski04@gmail.com**
