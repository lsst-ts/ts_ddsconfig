.. py:currentmodule:: lsst.ts.ddsconfig

.. _lsst.ts.ddsconfig:

#################
lsst.ts.ddsconfig
#################

.. image:: https://img.shields.io/badge/GitHub-gray.svg
    :target: https://github.com/lsst-ts/ts_ddsconfig
.. image:: https://img.shields.io/badge/Jira-gray.svg
    :target: https://jira.lsstcorp.org/issues/?jql=labels+%3D+ts_ddsconfig

.. _lsst.ts.ddsconfig.overview:

Overview
========

ts_ddsconfig contains configuration files for ADLink OpenSplice.

.. _lsst.ts.ddsconfig.user_guide:

User Guide
==========

* Install the package with ``pip`` or ``conda`` (warning: ``python setup.py install`` does *not* work).
  You can also use the package "in place" by adding ``ts_ddsconfig/python`` to the ``PYTHONPATH``.
* Pick an OpenSplice configuration:

    * For SAL components that listen to events from other SAL components:
      use the shared memory configuration, which runs the DDS durability service in a dedicated daemon.
      This is required because the node will have to maintain late-joiner data
      and the single process mode will be overwhelmed by all our DDS data.
      Note that use of shared memory requires the licensed version of OpenSplice.
    * For SAL components that do not listen to events from other SAL components, and for local development:
      you may safely use the single process mode, because no durability service is needed.
      This allows use of the community edition of OpenSplice,
      which is a bit more convenient than the licensed version.

* Set environment variable ``OSPL_URI`` to point to your chosen OpenSplice configuration.
  For example ``file:///home/saluser/repos/ts_ddsconfig/config/ospl-shmem.xml``.
* Set environment variable ``LSST_DDS_QOS`` to point the QoS file.
  For example: ``file:///home/saluser/repos/ts_ddsconfig/qos/QoS.xml``.
  Note that ts_sal_ uses this environment variable, but ts_salobj_ calls ``lsst.ts.ddsconfig.get_qos_path`` instead.

.. _ts_salobj: https://ts-salobj.lsst.io/
.. _ts_sal: https://ts-sal.lsst.io/

Version History
===============

.. toctree::
    version_history
    :maxdepth: 1
