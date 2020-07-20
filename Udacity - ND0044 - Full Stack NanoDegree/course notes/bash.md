### Use Linux commands on windows
Download [git bash](https://git-scm.com/downloads)


### Connect to Remote Server with SSH
```
ssh -p <port number> user_name@ip
```


### Copying File From Remote Server
Copy file from another system to this system:
```bash
scp -P <port number> username@hostname:/path/to/remote/file /path/to/local/file
```
Copy folder from another system to this system with -r for recursive
```bash
scp -r -P <port number> username@hostname:/path/to/remote/file /path/to/local/file
```
Copy something from some hostname1 to some other hostname2:

```
scp username1@hostname1:/path/to/file username2@hostname2:/path/to/other/file   
```

# General Commands
Run two commands at once
```
command 1 | command 2
```
