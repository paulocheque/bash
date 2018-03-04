bash-toolbelt
======================

[![Build Status](https://travis-ci.org/paulocheque/bash-toolbelt.png?branch=master)](https://travis-ci.org/paulocheque/bash-toolbelt)
[![Docs Status](https://readthedocs.org/projects/bash-toolbelt/badge/?version=latest)](http://bash-toolbelt.readthedocs.org/en/latest/index.html)
[![Coverage Status](https://coveralls.io/repos/paulocheque/bash-toolbelt/badge.png?branch=master)](https://coveralls.io/r/paulocheque/bash?branch=master)
[![Code Status](https://landscape.io/github/paulocheque/bash-toolbelt/master/landscape.png)](https://landscape.io/github/paulocheque/bash-toolbelt/)
[![PyPi version](https://img.shields.io/pypi/v/bash-toolbelt.svg)](https://crate.io/packages/bash-toolbelt/)
[![PyPi downloads](https://img.shields.io/pypi/dm/bash-toolbelt.svg)](https://crate.io/packages/bash-toolbelt/)

**Latest version: 0.0.2 (2016/01)**

Utility methods to facilitate automation of devops tasks. Good to be used with Fabric or Invoke.

Documentation
-------------

http://bash-toolbelt.readthedocs.org/en/latest/index.html

Git utilities:

    from bash import git

    next_tag = git.autoincrement_tag('1.2.3')
    assert git.current_git_branch() == 'master'
    git.last_git_tag() == '1.2.3'
    git.create_tag('1.0.0')
    git.auto_create_tag()
    git.reset_tag('1.2.3')
    git.reset_last_tag()

OS utilities:

    import bash.os

    output = bash.os.run('ls')
    bash.os.wait_for(10, 1, lambda x: None, arg1, arg2, arg3=None)
    data = bash.os.read_config_file('filepath')
    assert bash.os.str2bool('y')
    assert bash.os.is_mac()
    assert bash.os.is_linux()
