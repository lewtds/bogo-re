# BoGo engine backed by Regular Expression

This is one of my experiments with the BoGo project. The engine uses regular
expressions solely as its logic. Side-effects and states are kept to the
minimum.

Its API is fairly simple:

	> import bogo
	> bogo.process_word("tuowngr")
	'tưởng'

Nevertheless, it does not know anything about word boundaries so "tuowngr s"
would be troublesome. I suggest you do the splitting part yourself (with
`str.split()` perhaps?).

You might want to read the tests first. Then run the benchmark
(I got 250 words/second).
