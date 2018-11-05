# Flatline Python bridge

This package provides a python interface to the local JS Flatline
interpreter, allowing checking Flatline Lisp and JSON s-expressions
for correctnes and applying them to local dataset samples to generate
new fields.

Typically, you will use the functions in this package to experiment in
your computer with the data transformations and filters you plan to
eventually execute in BigML servers, after you're satisfied with the
results of your explorations on small data samples.

## Installation

The bridge uses [nodejs](http://nodejs.org) under the rug, and hence
needs it to be
[installed in your system](https://nodejs.org/download/) as a
prerequisite.

With that in place, you can use `setup.py` script for installing this
package in the usual way.  For instance

```
$ python setup.py develop
```

will perform an in-place installation, possibly in a local virtualenv
(recommended):

```
$ virtualenv --distribute ~/.virtualenvs/flatline
$ workon flatline
$ python setup.py develop
```

## Running the sample code in iPython

We provide a [sample notebook](./notebooks/Flatline.ipynb) to
illustrate the workings of this library.  To use them, install
[ipython and jupyter](http://ipython.org) with `pip`:

```
$ pip install jupyter
```

then
[set up your BIGML enviroment variables for authentication](https://bigml.readthedocs.org/en/latest/#authentication):

```
$ export BIGML_USERNAME=<your user name>
$ export BIGML_API_KEY=<your api key>
```

and start the notebook server in the [notebooks](./notebooks)
directory:

```
$ cd notebooks
$ jupyter notebook Flatline.ipynb
```
