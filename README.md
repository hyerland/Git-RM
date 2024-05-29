# Git-RM

Manage and install git repositories with caching, and more all within your terminal.

> [!WARNING]  
> **Git-RM** is currently under heavy development and **can change update to update.** We recommend you to regularly check our [**discussions board**](https://github.com/hyerland/Git-RM/discussions) for new announcements and more.

## What's Git-RM? 🤔

**Git-RM** *(short for Git Repository Manager)* is a way to **download, cache, and reuse** repositories from your local disk while providing many **quality of life features** with simple configuration editing and more!
**Git-RM was designed to be...**

- Easy to use, yet intuitive 🧑
- Powerful and fast 🚀
- No extra installs are needed 🚫
  - Requires **Git** and **Python 3.8 or greater**

## Installation ⚡

Installing Git-RM is simple as installing a normal pip package,

``` bash
pip install git-rm
```

## Basic Usage 💡

In order to use Git-RM, you would clone git repositories as usual with the difference of using `gitrm`, for example,

``` bash
gitrm clone https://github.com/hyerland/git-rm.git
```

This will use git and configured credintials to clone and store within `.gitrm` directory for future use.
