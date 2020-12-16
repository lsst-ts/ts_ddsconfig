.. py:currentmodule:: lsst.ts.ddsconfig

.. _lsst.ts.ddsconfig.version_history:

###############
Version History
###############

v0.4.1
======

* Make DurabilityService.Namespaces.Policy.aligner settable via LSST_DDS_ALIGNER environment variable.
* Set DurabilityService.Namespaces.Policy.aligner to false by default.

v0.4.0
======

* Change DurabilityService.Namespaces.Policy.alignee default to Lazy.
* Add attribute for turning off adaptive watermarks.
* Add attribute to set the size of the initial high watermark to max size.
* LSST_DDS_REPSONSIVENESS_TIMEOUT environment variable to assist with single process mode CSCs. Default is inf.

v0.3.1
======

* Update Jenkinsfile.conda to use Jenkins Shared Library.

v0.3.0
======

* Add `ospl-std.xml`, a non-shared-memory configuration, for unit testing and development.
* Increase topic database size from 1Gb to 5GB in the shared memory configurations.

v0.2.0
======
* Add LSST_DDS_ALIGNEE environment variable to aid setting DurabilityService.Namespaces.Policy.alignee. Default is Initial.
* Add LSST_DDS_DOMAIN_ID environment variable to aid setting Domain.Id. Default is 0.

v0.1.0
======
Initial release.
