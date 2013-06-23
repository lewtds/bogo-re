# BoGo engine backed by Regular Expression

This is one of my experiments with the [BoGo][1] project. The engine uses
Regular Expressions solely as its logic. Side-effects and states are kept to the
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

Please note that it takes around 0.3s to initialize and compile the regular
expression. After that it's cool.

[1]: https://github.com/BoGoEngine/ibus-bogo-python

----

## License

**GPL v3** all the way down!
Copyright 2013 Trung Ngo, though.
