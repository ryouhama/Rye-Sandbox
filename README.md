# Rye-Sandbox
This is a repository for studying [Rye](https://rye-up.com/).


## Why Rye
https://rye-up.com/

## Install
Rye is built in Rust. 

You can install it with the following command:

```shell
curl -sSf https://rye-up.com/get | bash
echo 'source "$HOME/.rye/env"' >> ~/.zshrc
```


## Update Rye
To update Rye to the latest, run the following command:
```shell
rye self update
```
To uninstall Rye, run the following command:
```shell
rye self uninstall
```


## Init Project

### Create Python Project
To use rye, you need a python project based on `pyproject.toml`.

```shell
rye init my-project
cd my-project
```

The following structure will be created.
```
.
├── .git
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
└── src
    └── my_project
        └── __init__.py
```

### Sync
```shell
rye sync
```

### Python version
```shell
rye pin 3.11
```

### Add dependency
```shell
rye add requests
```