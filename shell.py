#!/usr/bin/env python2.7

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from IPython.terminal.prompts import Prompts, Token
from IPython.terminal.ipapp import load_default_config
from traitlets.config.loader import Config

import argparse
import sys
import os
import os.path
import traceback
import re
import sqlitedict

from sqlenv import *

class CustPrompt(Prompts):
    def in_prompt_tokens(self, cli=None):
        return [
            (Token.Prompt, '[sqlenv] <'),
            (Token.PromptNum, str(self.shell.execution_count)),
            (Token.Prompt, '>: '),
        ]

    def out_prompt_tokens(self):
        return [
            (Token.OutPrompt, '[sqlenv] Out<'),
            (Token.OutPromptNum, str(self.shell.execution_count)),
            (Token.OutPrompt, '>: '),
        ]

def main(quiet=True):
    try:
        get_ipython
    except NameError:
        nested = 0
        cfg = load_default_config()
        cfg.TerminalInteractiveShell.prompts_class=CustPrompt
    else:
        print 'Running nested copies of IPython. Augmenting configuration...'
        cfg = load_default_config()
        nested = 1

    from IPython.terminal.embed import InteractiveShellEmbed

    cfg.TerminalInteractiveShell.confirm_exit = False
    cfg.TerminalInteractiveShell.debug = True

    ipshell = InteractiveShellEmbed.instance(config=cfg, banner1='Welcome to the sqlenv IPython Shell...\n')

    # Setup sqlitedict as `sqdb`
    sqdb_path = os.path.join(os.path.abspath('.'), '.local_db.sqlite')
    sqdb = sqlitedict.SqliteDict(sqdb_path)

    ipshell()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A tool for helping track and manage WHM instances across multiple servers')
    parser.add_argument('-q', '--quiet', action='store_true', default=False)
    opts = parser.parse_args()
    main(quiet=opts.quiet)
