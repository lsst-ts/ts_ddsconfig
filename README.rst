Configuration files for OpenSplice DDS

Documentation: `ts-ddsconfig.lsst.io <https://ts-ddsconfig.lsst.io/>`_

Contents:

* config: OpenSplice configuration files, including separate files
  for shared memory mode and single process mode.
* qos/QoS.xml: quality of service configuration file.
* python: functions to get the ``config`` directory and quality of service file.
* ups: Files for using this package with eups.

This code uses ``pre-commit`` to maintain ``black`` formatting and ``flake8`` compliance.
To enable this, run the following commands once (the first removes the previous pre-commit hook)::

    git config --unset-all core.hooksPath
    pre-commit install
