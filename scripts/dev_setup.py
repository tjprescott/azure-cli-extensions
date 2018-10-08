#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

import sys
import os
from subprocess import check_call, CalledProcessError

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..', '..', 'azure-cli'))
extensions_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))


def py_command(command):
    try:
        print('Executing: python ' + command)
        check_call([sys.executable] + command.split(), cwd=root_dir)
        print()
    except CalledProcessError as err:
        print(err, file=sys.stderr)
        sys.exit(1)

def pip_command(command):
    py_command('-m pip ' + command)

print('Running dev setup...')
print('Extensions directory: {}'.format(extensions_dir))

py_command('install azure.cli')

#py_command('-m automation.setup.install_modules')set

print('Finished CLI extensions dev setup.')
