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

General OSPL Environment Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OpenSplice contains a few environment variables that aid in setting up the system.

ADLINK_LICENSE
  This points to directory containing your `Vortex OpenSplice`_ license.
  Required if using the licensed version of `Vortex OpenSplice`_; ignored otherwise.
  Example value: ``/opt/ADLINK/Vortex_v2/Device/VortexOpenSplice/6.10.3/HDE/x86_64.linux/etc``
OSPL_HOME
  The directory of the `Vortex OpenSplice`_ software and should contain subdirectories ``bin``, ``include``, ``lib``, etc.
  This variable is **REQUIRED** for correct setup.
  Example: ``/opt/OpenSpliceDDS/V6.9.0/HDE/x86_64.linux``.
OSPL_URI
  A URI pointing to the main DDS configuration file, such as one of the config files in this package.
  This variable is **REQUIRED** for correct setup.
  Example value: ``file:///opt/OpenSpliceDDS/V6.9.0/HDE/x86_64.linux/etc/config/ospl.xml``
OSPL_TEMP
  A path to an alternate location for writing items OpenSplice writes into ``/tmp``.
  Example value: ``/var/run``
OSPL_INFOFILE
  A full path specifying the location for writing the STDOUT logging to a file.
  Example value: ``/var/log/my-process-info.log``
OSPL_ERRORFILE
  A full path specifying the location for writing the STDERR logging to a file.
  Example value: ``/var/log/my-process-error.log``

Environment Variables in OSPL Configuration Files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The OSPL configuration files, ``ospl-shmem.xml`` and ``ospl-sp.xml`` files have a number of environment variables to control behavior.
Except where noted, the environment variables are assumed to be present in both files.

LSST_DDS_DOMAIN_NAME
  This variable controls the name for the domain.
  Defaults to ``ospl_sp_ddsi`` in all configurations.
  See `/OpenSplice/Domain/Name <http://download.ist.adlinktech.com/docs/Vortex/html/ospl/DeploymentGuide/guide.html#name>`_.

LSST_DDS_DOMAIN_ID
  This variable controls the domain ID that system communicate on.
  All of our sites use **0** for the production environment.
  Other domain IDs maybe used to test systems without effecting the production environment.
  The default is **0** (zero).

LSST_DDS_SHMEM_SIZE
  This variable controls the size in bytes of the shared memory database.
  Defaults to 504857600 for standard shared memory configuration.
  Defaults to 209715200 for embedded shared memory configuration.
  See `/OpenSplice/Domain/Database/Size <http://download.ist.adlinktech.com/docs/Vortex/html/ospl/DeploymentGuide/guide.html#size>`_ for specifications.

LSST_DDS_REPORT_LEVEL
  This variable controls the overall verbosity level of the OSPL log files.
  The default is **INFO**.
  See `/OpenSplice/Domain/Report@verbosity <http://download.ist.adlinktech.com/docs/Vortex/html/ospl/DeploymentGuide/guide.html#id48>`_ for more options.

LSST_DDS_INTERFACE
  This variable controls the networking interface that DDS should bind to.
  The default is **AUTO**.
  See `/OpenSplice/DDSI2Service/General/NetworkInterfaceAddress <http://download.ist.adlinktech.com/docs/Vortex/html/ospl/DeploymentGuide/guide.html#id506>`_ for more specifications.

LSST_DDS_RESPONSIVENESS_TIMEOUT
  This variable determines how long unresponsive readers can block a transmit thread.
  Only the OSPL daemons, Kafka producers and single process CSCs run with anything other than **inf**.
  The default is **inf**.
  See `/OpenSplice/DDSI2Service/Internal/ResponsivenessTimeout <http://download.ist.adlinktech.com/docs/Vortex/html/ospl/DeploymentGuide/guide.html#id553>`_ for more specifications.

LSST_DDSI2_SERVICE_TRACING_VERBOSITY
  This variable controls the level of tracing for the DDSI2 service.
  The default is **none**.
  See `/OpenSplice/DDSI2Service/Tracing/Verbosity <http://download.ist.adlinktech.com/docs/Vortex/html/ospl/DeploymentGuide/guide.html#id616>`_ for more options.

LSST_DDSI2_SERVICE_TRACING_OUTPUT
  This variable controls the name of the log file for the tracing.
  The default is **ddsi2.log**.
  See `/OpenSplice/DDSI2Service/Tracing/OutputFile <http://download.ist.adlinktech.com/docs/Vortex/html/ospl/DeploymentGuide/guide.html#id612>`_ for more details.

LSST_ENABLE_DURABILITY_SERVICE_TRACING
  This variable controls the tracing for the durability service.
  **NOTE**: An output file (if one is specified) is written with size zero even if the tracing is disabled.
  The default is **FALSE**.
  See `/OpenSplice/DurabilityService/Tracing@enabled <http://download.ist.adlinktech.com/docs/Vortex/html/ospl/DeploymentGuide/guide.html#id110>`_ for more details.

LSST_DURABILITY_SERVICE_TRACING_VERBOSITY
  This variable controls the level of tracing for the durability service.
  The default is **FINER**.
  See `/OpenSplice/DurabilityService/Tracing/Verbosity <http://download.ist.adlinktech.com/docs/Vortex/html/ospl/DeploymentGuide/guide.html#id115>`_ for more options.

LSST_DURABILITY_SERVICE_TRACING_OUTPUT
  This variable controls the name of the log file for the tracing.
  The default is **durability.log**.
  See `/OpenSplice/DurabilityService/Tracing/OutputFile <http://download.ist.adlinktech.com/docs/Vortex/html/ospl/DeploymentGuide/guide.html#id112>`_ for more details.

LSST_DDS_PARTITION_PREFIX
  This variable controls the partition prefix applied to the common namespace.
  We use a different partition prefix per site.
  Not specifying this variable results in a partition of *****.
  See `/OpenSplice/DurabilityService/Namespaces/Namespace/Partition <http://download.ist.adlinktech.com/docs/Vortex/html/ospl/DeploymentGuide/guide.html#id100>`_ for more details.

LSST_DDS_ALIGNEE
  This variable controls the how the historical data is managed by the system.
  **NOTE**: Only the main daemon is allowed to set this to **Initial**.
  The default is **Lazy**.
  See `/OpenSplice/DurabilityService/Namespaces/Policy@alignee <http://download.ist.adlinktech.com/docs/Vortex/html/ospl/DeploymentGuide/guide.html#alignee>`_ for more details.

LSST_DDS_ALIGNER
  This variable determines if the durability service can provide historical data to other durability services.
  **NOTE**: Only the main daemon is allowed to set this to **true**.
  The default is **false**.
  See `/OpenSplice/DurabilityService/Namespaces/Policy@aligner <http://download.ist.adlinktech.com/docs/Vortex/html/ospl/DeploymentGuide/guide.html#aligner>`_ for more details.

OSPL_MASTER_PRIORITY
  This variable sets the priority level for which durability service is the main (master).
  The main daemon is set to a value ~200.
  All other daemons and CSCs are set to a much lower value or zero.
  See `/OpenSplice/DurabilityService/Namespaces/Policy@masterPriority <http://download.ist.adlinktech.com/docs/Vortex/html/ospl/DeploymentGuide/guide.html#masterpriority>`_ for more details.

.. _ts_salobj: https://ts-salobj.lsst.io/
.. _ts_sal: https://ts-sal.lsst.io/
.. _Vortex OpenSplice: https://istkb.adlinktech.com/article/vortex-opensplice-documentation/

Version History
===============

.. toctree::
    version_history
    :maxdepth: 1
