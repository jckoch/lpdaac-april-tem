# Python Examples

## Python Environment Setup

### Anaconda3 for Windows

* [Download](https://www.anaconda.com/distribution/#download-section "Download Anaconda3") and install [Anaconda3](https://docs.anaconda.com/anaconda/install/ "Install Docs")

* Create the environment

  ```bash
  # create a virtual environment
  $ conda create -n april-tem python=3.8.2

  # use that env
  $ activate april-tem
  cd <project-root>examples/python

  # install packages
  (april-tem) $ pip install -r requirements.txt
  ```

  If you run into issues with SSL validation when using `pip`, you can configure it to use a CA, or specify it in the command thusly:

  ```bash
  # identify a CA to validate SSL certs
  (april-tem) $ pip install -r requirements.txt --cert <path-to-cert>
  ```

## Running Examples

Activate your virtual environment and run them.

e.g.

```bash
$ activate april-tem
$ cd <project-root>examples/python

$ python generator.py
```
