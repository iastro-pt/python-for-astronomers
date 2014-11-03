Python for Astronomers
======================



Prelude
-------

If you use Windows, please come talk to one of us before the first practical class


Installation check
------------------

If you use Mac or Linux it's probable that Python is already installed in your system.
To test this, open a terminar and type

    $ python
    Python 2.7.8 |Anaconda 2.1.0 (32-bit)| (default, Aug 21 2014, 18:22:40) 
    [GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.


 -open a terminal, type python, if your shell then looks something like this, all is fine

 09:46:02 cvillforth@agnew: ~> python
 Enthought Canopy Python 2.7.3 | 64-bit | (default, Aug  8 2013, 05:37:06)
 [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
 Type "help", "copyright", "credits" or "license" for more information.


 -to check for numpy, pylab, do this:
 import numpy
 import pylab

 If it looks like this, ass is fine, if you get an import error, see below

 -to check for ipython, type ipython in a terminal, if it looks like this:
 09:46:02 cvillforth@agnew: ~> ipython
 Python 2.7.3 | 64-bit | (default, Aug  8 2013, 05:37:06)
 Type "copyright", "credits" or "license" for more information.

 IPython 2.3.0 -- An enhanced Interactive Python.
 ?         -> Introduction and overview of IPython's features.
 %quickref -> Quick reference.
 help      -> Python's own help system.
 object?   -> Details about 'object', use 'object??' for extra details.

 In [1]:

 all is fine

 -if you need to install numpy/pylab/ipython I recommend easy_install
 https://pypi.python.org/pypi/setuptools
 Install this using the instructions, then type:
 sudo easy_install numpy
 sudo easy_install matplotlib
 sudo easy_install ipython
>>
>> If you don’t like this, use the installation instructions on the package webpage:
>> http://docs.scipy.org/doc/numpy/user/install.html
>> http://ipython.org/install.html
>> http://matplotlib.org/users/installing.html
>>
>> If your python installation is old, annoying & generally crappy, I recommend Enthought Canopy (free with academic license)
>> https://www.enthought.com/products/canopy/
>>
>>
>>
>> --------------------------------------------------------------------------------
>> Dr Carolin Villforth
>> SUPA Advanced Fellow
>> University of St Andrews (SUPA)
>> School of Physics & Astronomy
>> North Haugh, St Andrews, Fife
>> KY16 9SS
>> UK
>> cv21@st-andrews.ac.uk
>> Office: 272
>> phone +44 (0) 1334 46 1612
>> http://www-star.st-and.ac.uk/~cv21/cv21/Home.html
>> --------------------------------------------------------------------------------
>



Raphaëlle D. Haywood

SUPA School of Physics & Astronomy
University of St Andrews
North Haugh
St Andrews, Fife KY16 9SS
United Kingdom

Room: 256
Tel.: +44 1334 463091
Web: http://star-www.st-and.ac.uk/~rdh4/







