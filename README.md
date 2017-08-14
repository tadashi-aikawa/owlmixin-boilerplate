# owlmixin-boilerplate

![](https://img.shields.io/pypi/pyversions/owlmixin.svg)

Boilerplate for [Owlmixin](https://github.com/tadashi-aikawa/owlmixin).

First, make venv (>=3.6).

## Install dependencies

```
$ pip install -e .[test] -c constraints.txt
```

## Run

```
$ cd yourapp
$ python main.py --config config.yml 'owl'
- id: 61579222
  name: owl
  stargazers_count: 425
- id: 8249948
  name: owlapi
  stargazers_count: 260
- id: 9358435
  name: pellet
  stargazers_count: 171
```

Awesome !!

### One more things

Edit `config.yml`, and check both what is output and why outputs.

#### Default

```
$ cat config.yml
lower_star_count: 50
head: 3
```

#### `lower_star_count` is empty

```
$ cat config.yml
head: 3
```

#### `head` is empty

```
$ cat config.yml
lower_star_count: 50
```

#### Everything are empty

```
$ cat config.yml
{}
```

## Test

```
$ pytest
```

## Support for pip install

Install according to `constraints.txt`.

```
$ wget https://raw.githubusercontent.com/tadashi-aikawa/owlmixin-boilerplate/master/constraints.txt
$ pip install git+https://github.com/tadashi-aikawa/owlmixin-boilerplate.git -c constraints.txt 
```

Create empty `config.yml` and run.

```
$ echo '{}' > config.yml
$ yourapp --config config.yml 'git'
- id: 1062897
  name: gitignore
  stargazers_count: 53488
- id: 16752620
  name: gogs
  stargazers_count: 20409
- id: 36502
  name: git
  stargazers_count: 18650
```

Awesome !!
