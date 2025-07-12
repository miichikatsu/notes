# Secure Shell Protocol (SSH)

## Definitions
The Secure Shell Protocol is a cryptographic protocol 
for operating network services.

## Features
- Allows establishing a secury connection to a remote server in an insecure network.
- Based on public-key cryptography.

## Workflows
1. Create the `~/.ssh` directory and move to it: `mkdir ~/.ssh && cd ~/.ssh`.
2. Create a key pair: `ssh-keygen -t ed25519`.
3. Activate an agent: `eval "$(ssh-agent -s)"`.
4. Add the private key to the agent: `ssh-add id_ed25519`.
5. Copy the public key: `pbcopy < id_ed25519.pub`.
6. Add the public key to the server: `~/.ssh/id_ed25519.pub`.
7. Establish a connection: `ssh username@ip -p port`.
8. Terminate the connection: `exit`.

## Examples
```bash
~/.ssh $ mkdir gitlab && cd gitlab 
~/.ssh/gitlab $ ssh-keygen -t ed25519 
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/mikhailshkarbanenko/.ssh/id_ed25519): id_ed25519 
Enter passphrase for "id_ed25519" (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in id_ed25519
Your public key has been saved in id_ed25519.pub
The key fingerprint is:
SHA256:dRrLgCeKgocSOepJcFgKQ4o+hMEot7PfbTF0w6xA7zk mikhailshkarbanenko@Mikhails-MacBook-Pro.local
The key's randomart image is:
+--[ED25519 256]--+
|B..              |
|BO.   ..         |
|%o.. .o.ooo .    |
|*=o. ..oo+==     |
|*+oo.  +S++.     |
|+o+     E        |
| o . . . +       |
|    . . o        |
|       .         |
+----[SHA256]-----+
~/.ssh/gitlab $ ls -a
.               ..              id_ed25519      id_ed25519.pub
~/.ssh/gitlab $ pbcopy < id_ed25519.pub
~/.ssh/gitlab $ ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIL9VgphhuOTggstyOayxsWajwjktOXM6rXovvW0cZt2F username@host.local
```

## References
[1] [Wikipedia: Secure Shell](https://en.wikipedia.org/wiki/Secure_Shell)

[2] [Heidelberg University: SSH Tutorial Linux](https://zah.uni-heidelberg.de/it-guide/ssh-tutorial-linux)