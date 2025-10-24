# entropy

Generate a password with 4 words
```sh
$ ./generate-word-password.py 4
entropy: 57 bits
slogan device dismount carob
```

Generate a password with 23 lower and uppercase letters
```sh
$ ./generate-letter-password.py 23
entropy: 131 bits
XbrKdicXmcIgLMWsfdKnNQd
```

The actual entropy depends on the underlying entropy source.

The wordlist is from [1Password](https://github.com/1Password/spg/blob/master/testdata/agwordlist.txt).
