AnimatAI: A Framework for Artificial General Intelligence
=========================================================

Reference code for:

A General Model for Learning and Decision-Making in Artificial Animals by
Claes Strannegård, Nils Svangård, David Lindström, Joscha Bach
and Bas Steunebrink

Submitted to IJCAI-17 AGA workshop, Melbourne, Australia

This repo is work in progress and will contain a completely refactored
version of the original code. The repo [ecosystem](https://github.com/animatai/ecosystem)
contains the old version of the framework (which isn't maintained anymore).


Setup
=====

The easiest way to install `animatai` is with `pip install animatai`

At least Python 3.5 is needed since `async` is used in the web sockets server
(`wsserver.py`).



Run the program
==============

Examples using the ecosystem classes are available in the
repo [examples](https://github.com/animatai/examples)

A little setup is needed first:

* Create `config.py`. Start with copying `config.py.template` and try some of
the examples from the repo mentioned above.

Start a web server and a browser:

* Run the server: `python wsserver.py`
* Run `index.html` in a browser and follow the instructions.


Development
===========

First setup a development environment. I'm using `virtualenv`:

* First init `virtualenv` for Python3: `virtualenv -p python3.6 venv3`
(`virutalenv` needs to be installed)
* Activate `virtualenv`: `source venv3/bin/activate`
* Install the necessary Python packages: `pip install -r requirements.txt`.
Add `--no-compile` when running on ubuntu.

Use [Google Style Guide](https://google.github.io/styleguide/pyguide.html)
and make sure that the unit tests are maintained.

Build (lint and run unit tests) with: `./build.sh`
Building will also Create a source distribution in the `dist` folder.

Upload the build to the public package repo for installation with `pip`:
`twine upload dist/animatai-X.Y.Z.tar.gz`


Citing AnimatAI
===============

When using AnimatAI in research that is published, please cite the project properly. Here is an example in [APA-style](http://blog.apastyle.org/apastyle/2015/01/how-to-cite-software-in-apa-style.html):

```
AnimatAI: A Framework for Artificial General Intelligence [Computer software]. (2018).
Retrieved from http://animatai.org
```

and an example in [IEEE-style](https://www.ieee.org/documents/style_manual.pdf):

```
[1] J. Colmsjö, C. Strannegård, AnimatAI: A Framework for Artificial General Intelligence (2018)[Online]. Available: http://animatai.org
```

MIT provides a [summary](https://libguides.mit.edu/c.php?g=551454&p=3900280)
about citing software when used in research.


Credits
=======

Using some classes from the [AIMA book](https://github.com/aimacode/aima-python)
