# -*- coding: utf-8 -*-
"""
Controls command line operations

The only particularly relevant command now i:  patella startup <path>

not all commands retain functionality - this will be updated eventually (read: it might not be)

"""

# \/ Third-Party Packages \/
import os
import os.path

import click
import pandas as pd
from . import app as flaskapp
from . import transcript_string_matcher as tsm

# \/ Local Packages \/
@click.group()
def nabla():
    pass

@click.command()
@click.argument('path', default='nabla')
def startserver(path):
    flaskapp.startserver(path)

# A test cli command
@click.command()
@click.argument('foo')
def testme(foo):
    pass

# add all the subcommands to the patella group
nabla.add_command(startserver, name='startup')
