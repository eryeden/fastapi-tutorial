# fastapi-tutorial
## Background
We're kicking off the [base architecture](https://github.com/eryeden/plan) development for our product powered by ChatGPT. The first milestone involves getting a grip on FastAPI, which will serve as the backbone for our base architecture.

## Key features
In this repository, we've achieved the following:
- Implemented basic API endpoints: /hello and /bye
- Set up a local testing environment for streamlined development


## Prerequisites
- python 3.11
- poetry

## References
- Fastapi tutorial: https://fastapi.tiangolo.com/ja/tutorial/

## Project memo

- Virtual environment set up
```bash
pyenv local 3.11.3
python -m venv .venv
poetry init
poetry shell
```

- FastAPI set up
```bash
poetry add fastapi[all]
```

Running the above command will install `fastapi` and also `uvicron`.
`uvicron` is a kind of webserver. `uvicron` will host FastAPI.
