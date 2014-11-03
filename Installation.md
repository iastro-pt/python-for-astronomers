Python for Astronomers
======================



Prelude
-------

If you use Windows, please come talk to one of us before the first practical class


Installation check
------------------

If you use Mac or Linux it's probable that Python is already installed in your system.
To test this, open a terminal and type

    $ python
    Python 2.7.8 |Anaconda 2.1.0 (32-bit)| (default, Aug 21 2014, 18:22:40) 
    [GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

you should see similar output to the above. If you don't, go to [(1)](#install-python).

Check Python's version number; it should be higher than 2.7.0. If your version is 3.x.x tell us before the practical class.

(Note: to exit the Python interpreter press Ctrl-D)


To check if you have Ipython installed just type 

    Python 2.7.8 |Anaconda 2.1.0 (32-bit)| (default, Aug 21 2014, 18:22:40) 
    Type "copyright", "credits" or "license" for more information.

    IPython 2.2.0 -- An enhanced Interactive Python.
    Anaconda is brought to you by Continuum Analytics.
    Please check out: http://continuum.io/thanks and https://binstar.org
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.
    
    In [1]: 

If you see similar output, all is fine. If you don't, go to [(2)](#install-ipython).

(Note: press Ctrl-D or type `exit` to get out of the IPython interpreter)


To check for numpy, matplotlib and scipy (the packages we will need for the practical classes) type the following

    $ python -c "import numpy"
    $ python -c "import matplotlib"
    $ python -c "import scipy"
    
if you see errors like this

    Traceback (most recent call last):
      File "<string>", line 1, in <module>
    ImportError: No module named numpy
    
from any of the above commands, go to [(3)](#install-packages). If there is no output from the commands, everything is fine.

<a name="install-python"/>
(1) Installing Python
-----------------

How the hell do you install Python?


<a name="install-ipython"/>
(2) Installing IPython
------------------

pip install ipython


<a name="install-packages"/>
(3) Installing Numpy, Matplotlib and Scipy
--------------------------------------

pip install numpy
pip install matplotlib
pip install scipy

