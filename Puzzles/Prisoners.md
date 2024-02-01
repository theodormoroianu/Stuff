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

## Problem 3

There are an infinity of prisoners arranged in a line, each one being able to see every prisoner after himself.
More formally: For each natural number N, there is a prisoner with index N, able to see every single prisoner with index > N.

Each prisoner is given a hat, either white or black. Of course, a prisoner cannot see his/her hat, and can only see the hats of prisoners he/she is able to see.

They all have to say at the same time what color they beleive their hat is (being at the same time, they can't rely on what others are saying).

 * Is it possible to help them with a strategy such that an infinity of them guesses corectly?
 * By assuming the axiom of choice, is it possible to help them with a strategy such that only a finite number of prisoners have a wrong guess?

## Problem 4

There are N prisoners arranged in a line, with N + 2 colors on their hats. The colors are distinct.
Prisoner 1 can see 2 ... N, prisoner 2 can see 3 ... N etc.

Each prisoner, starting from the first one, says the color they beleive they have. They cannot repeat colors, but hear the answers of the other prisoners.
How many can guess right?

