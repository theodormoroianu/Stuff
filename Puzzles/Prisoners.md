# Prisoners Problems

## Problem 1

There are `N` prisoners. Guards decide to play a game with them, promising to set them free if the prisoners win (they are not very good guards).

The rules of the game are the following:

1. The `N` prisoners are all placed in the same room, where they can see each other, but are unable to communicate in any way (no talking, making signs etc).
2. On the forehead of each prisoner is written by the guards a number between `1` and `N`. Note that while a prisoner can't see his/her own number, everybody else can. Also note that the number can repeat (they don't necessarily form a permutation).
3. After they have a good look at each other, the prisoners are isolated, each one in its cell, where they can't hear each other.
4. Each prisoner tells the guards what number he/she thinks he/she has on the forehead. Note that prisoners can't hear each other's guesses.
5. The prisoners win the game if AT LEAST one the the `N` prisoners guesses correctly. 

Can the prisoners find a strategy before the start of the game, such that they are guaranteed to win the game?

## Problem 2

There are `N` prisoners. Guards decide to play a game with them, promising to set them free if the prisoners win (they are not very good guards).

The rules of the game are the following:

1. Each prisoner is isolated in his/her cell, where there is no sunlight, watch or any way to tell the time. In other words, prisoners don't have a sense of time.
2. From time to time, guards take one prisoner uniformly at random from the `N` prisoners, and brings him/her to the interogation cell.
3. In the interrogation cell, there is a light switch, that guards never touch. The prisoners that go to the interrogation cell can choose to turn the light on/off, or leave it as it is (at the very beggining the light is turned off).
4. If at some point a prisoner enters the interrogation room, and claims "All of the other prisoners came here at least once!", and is able to prove it, then the prisoners win.

Can the prisoners decide a strategy before the start of the game, that guarantees them a victory?