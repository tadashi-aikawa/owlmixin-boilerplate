# owlmixin-boilerplate

![](https://img.shields.io/pypi/pyversions/owlmixin.svg)

Boilerplate for [Owlmixin](https://github.com/tadashi-aikawa/owlmixin).

## Requirements

* Pipenv
* make

## Install dependencies

```
$ make init
```

## Run

```
$ make run
- id: 18782726
  name: OwlCarousel2
  stargazers_count: 5153
- id: 45591174
  name: NightOwl
  stargazers_count: 571
- id: 61579222
  name: owl
  stargazers_count: 511
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
$ make test
```

