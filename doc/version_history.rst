.. py:currentmodule:: lsst.ts.ddsconfig

.. _lsst.ts.ddsconfig.version_history:

###############
Version History
###############

v0.10.1
-------

* Add new ospl shmem configuration with no network.
  This is useful in isolating systems for unit tests or other single node tests in general.

v0.10.0
-------

* Convert to `noarch: python`.
* Breaking change: move `qos` and `config` directories into a `data` directory inside the package directory.
* Breaking change: rename `get_package_root` to `get_data_dir`.
* Switch to `pyproject.toml`.
  A minimal `setup.py` is required to be able to build the conda package.
* Add LSST_DDS_MERGE_POLICY environment variable to control the merge policy.

v0.9.0
------

* Update ownership QoS settings for Events and Telemetry from `EXCLUSIVE_OWNERSHIP_QOS` to `SHARED_OWNERSHIP`.

v0.8.0
------

* Add LSST_DDS_DOMAIN_NAME environment variable to control naming the domain.
* Add LSST_DDS_SHMEM_SIZE environment variable to control sizing the shared memory database.
* Fix an OpenSplice documentation URL.

v0.7.0
------

* Remove the ``<Heartbeat>`` entry from the config files, as recommended by ADLink.
  This entry only appeared in the four shmem config files.
  This change may require OpenSplice 6.11.
* Remove the ``<DSGracePeriod>`` entry from config files, because it is not relevant to our usage.
  This entry also only appeared in the four shmem config files.

v0.6.2
------

* Add optional 200MB shmem configuration for memory limited embedded systems
* Add documentation for OSPL setup environment variables.

v0.6.1
------

* Fix Jenkinsfile.conda to use noarch as arch.

v0.6.0
------

* Consolidate tracing/debugging attributes to standard files.
* Debug files should be deprecated and will be removed in the next version.

v0.5.3
------

* Add pre-commit support; see README.rst to configure it.

v0.5.2
------

* Modify the conda build to use noarch.

v0.5.1
------

* Introduce new environment variables for service tracing control in OSPL debug configurations

  * LSST_DDSI2_SERVICE_TRACING_VERBOSITY sets the logging level for tracing the DDSI2Service
  * LSST_DDSI2_SERVICE_TRACING_OUTPUT sets the output location for DDSI2Service tracing
  * LSST_DURABILITY_SERVICE_TRACING_VERBOSITY sets the logging level for tracing the DurabilityService
  * LSST_DURABILITY_SERVICE_TRACING_OUTPUT sets the output location for DurabilityService tracing


v0.5.0
------

* Increase startup attributes to maximums

  * Add DurabilityService.Network.InitialDiscoverPeriod and set to 10 seconds
  * Move DurabilityService.Network.Alignment.RequestCombinePeriod.Initial from 2.5 seconds to 5.0 seconds

v0.4.1
------

* Make DurabilityService.Namespaces.Policy.aligner settable via LSST_DDS_ALIGNER environment variable.
* Set DurabilityService.Namespaces.Policy.aligner to false by default.

v0.4.0
------

* Change DurabilityService.Namespaces.Policy.alignee default to Lazy.
* Add attribute for turning off adaptive watermarks.
* Add attribute to set the size of the initial high watermark to max size.
* LSST_DDS_REPSONSIVENESS_TIMEOUT environment variable to assist with single process mode CSCs. Default is inf.

v0.3.1
------

* Update Jenkinsfile.conda to use Jenkins Shared Library.

v0.3.0
------

* Add `ospl-std.xml`, a non-shared-memory configuration, for unit testing and development.
* Increase topic database size from 1Gb to 5GB in the shared memory configurations.

v0.2.0
------
* Add LSST_DDS_ALIGNEE environment variable to aid setting DurabilityService.Namespaces.Policy.alignee. Default is Initial.
* Add LSST_DDS_DOMAIN_ID environment variable to aid setting Domain.Id. Default is 0.

v0.1.0
------
Initial release.
