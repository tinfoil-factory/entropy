# entropy

*Note: the actual entropy depends on the underlying entropy source.*

### Generate a password with 4 words
```sh
$ ./generate-word-password.py 4
entropy: 57 bits
slogan device dismount carob
```

The wordlist is from [1Password](https://github.com/1Password/spg/blob/master/testdata/agwordlist.txt).

### Generate a password with 23 lower and uppercase letters
```sh
$ ./generate-letter-password.py 23
entropy: 131 bits
XbrKdicXmcIgLMWsfdKnNQd
```

### Compute TOTP
Enter the secret when prompted
```sh
./compute-totp.py
secret:
905814
```

