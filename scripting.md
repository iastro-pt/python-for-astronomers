Class 4 - Scripting
===================

There may be some confusion on the difference between **scripts** and
**programs**, with good reason. A *script*, as we call it here (also known as a command-line application) is a particular kind of computer program designed to be used from a shell. Scripts usually accept various inputs as arguments, often referred to as parameters or sub-commands, as well as options, often referred to as flags or switches.

A *program*, in this sense, can be thought of as some Python code that always runs the same way and always performs the same action. Therefore programs are meant to be run as `python program.py` (or `run program.py` from within IPython) and do not take extra options. 

As an example of a script, consider the `ls` command on Linux systems. Notice how the output of that command changes when you call it with some options: the output of `ls` is different from that of `ls -lrt`. Run `man ls` and you will see the help (or manual) page of the command, where you can get a thorough overview of the available options. 


In this class we would like to present some modules for creating scripts in Python that might be interesting.


## [argparse](https://docs.python.org/3/library/argparse.html)
If you work with scripts this module is essential and should already be
installed on your system. We only go through some basic here, but it should
already be enough to use it.

This module creates help text and usage for very few lines of code with the
`-h` or `--help` flag by default.

### Example

In a python file (test1.py), the following is added:

    import argparse
    parser = argparse.ArgumentParser(description='Description of software.')
    parser.add_argument('input', help='Input file')
    parser.add_argument('-o', '--output', help='Output file', default=False)
    parser.add_argument('-r', '--rv', help='RV velocity in km/s', default=False, type=float)
    args = parser.parse_args()

    print args
    print dir(args)

When we run this in the terminal we get the following message

    $ python test1.py
    usage: test.py [-h] [-o OUTPUT] [-r RV] input
    test.py: error: too few arguments

It complains about `too few arguments`. This is because the `input` should
_always_ be specified. However, let's try to run with the `-h` flag.

    $ python test1.py -h
        usage: test.py [-h] [-o OUTPUT] [-r RV] input

    Description of software.

    positional arguments:
      input                 Input file

    optional arguments:
      -h, --help            show this help message and exit
      -o OUTPUT, --output OUTPUT
                            Output file
      -r RV, --rv RV        RV velocity in km/s

It is conventional to use `-h` or `--help` to obtain the help page for a command (notice that we did not define this option in `test1.py`). This is the same thing as when we ran `man ls` before.

The `optional arguments` are only invoked when the flag is specified. Let's
try:

    $ python test1.py inputfile -r 42.0
    Namespace(input='inputfile', output=False, rv=42.0)
    ['input', 'output', 'rv']

Note that there is a lot more in the `dir(args)` than shown here. We only
included the interesting part. Instead of print the attributes, let us print
the value and type. The new line in our script will be

    print args.input, type(args.input)
    print args.output, type(args.output)
    print args.rv, type(args.rv)

We now get the following output

    $ python test1.py inputfile -r 42.0
    Namespace(input='inputfile', output=False, rv=42.0)
    inputfile <type 'str'>
    False <type 'bool'>
    42.0 <type 'float'>

Not that by default the type will be `str` if not otherwise specified. And if
the flag is not used it will return `False`. For completeness, let us try to
crash it by giving the script something it can not convert to a float for the
`rv` flag.

    python test1.py inputfile -r hello
    usage: test.py [-h] [-o OUTPUT] [-r RV] input
    test.py: error: argument -r/--rv: invalid float value: 'hello'

The script gives an error as suspected, which is easy to understand.

Note that the above should be enough for your daily hacking, but it can do a
lot more, like giving choices, subcommands, etc. There are also other arguments
parsers, but this is the most mature.

Please stop using something like `sys.argv`. Many people can use your scripts,
and you should be embarrassed to share something like that.


### See also

   * [Click](http://click.pocoo.org/3/). This looks very powerful and not too
   complicated (install with `sudo pip install click`).
   * [docopt](http://docopt.org/). This package allows creating command-line interfaces 
   easily and intuitively, by parsing POSIX-style usage instructions.
   * [optparse](https://docs.python.org/2/library/optparse.html). This is
   deprecated but can still be useful.


Other tools
===========

There are several other tools you can use to improve your scripts and their visual presentation in the terminal. Here we will present only a few.

## [clint](https://github.com/kennethreitz/clint) - colors in the terminal

A thing we do not consider when programming is the power of coloring our
terminal output. This can increase the readability drastically.

`clint` can be installed with `pip` as well. Just run

    $ sudo pip install clint

and you should be ready to go. `clint` can do a lot more than giving colors to
your output, but that it does in a very nice way.

### Example
Here follows an example (`test2.py`):

    from clint.textui import puts, colored

    puts('This is ' + colored.green('green text'))
    puts('This is ' + colored.red('red text'))
    puts('This is ' + colored.yellow('yellow bold text', bold=True))

This can not be shown in this markdown file, but try it out for yourself. Save
the file and run it with

    $ python test2.py

Check out `clint` for more information.


## [Progressbar](https://pypi.python.org/pypi/progressbar)
This is in the same category as colors in the terminal; it might not seem
necessary, but it can be very nice to have. There are many ways to get a
progressbar, one way is from the `progressbar` module which can be installed
the usual way: `sudo pip install progressbar`.

### Example
First of all, a very primitive "progressbar" we are all guilty of using is
something like this

    for i in range(int(1e9)):
        print i, '/', '1e9

First of all, this is can be better by just printing every 1000 element, but
your terminal is now filled with text that you really don't care about.

Here is how to use `progressbar` written in `test3.py`

    from progressbar import ProgressBar
    import time  # need the sleep command
    from numpy import random  # Let's use some random numbers for sleeping


    progress = ProgressBar()
    for i in progress(range(int(1e4))):
        time.sleep(random.random() * 0.0005)

As seen, the syntax is very simple. A `ProgressBar` object is created which
then wraps the `for` loop as shown.

There are many more things it can do, like using other symbols, show time left,
etc. But this is enough for basic usage.


Sharing your scripts
====================
It is advisable to share your scripts with the world. This is not part of the
course, but the teachers can help. A good place to start is at
[GitHub](http://github.com) where all code for this course is also available.

Feel free to step by our offices if you need help setting up git. This also
gives you backup and version control of all your code... For free!


Conclusion
==========

It seems after some research that `Click` have much if not all of the above
features: argument parsing, colors in the terminal, progressbar, etc.

If you want to learn a new module, I think this will be a good one (if not the
best).

Any missing documentation here is due to lack of knowledge :)






