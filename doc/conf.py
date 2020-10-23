"""Sphinx configuration file for TSSW package"""

from documenteer.sphinxconfig.stackconf import build_package_configs
import lsst.ts.ddsconfig


_g = globals()
_g.update(
    build_package_configs(
        project_name="ts_ddsconfig", version=lsst.ts.ddsconfig.__version__
    )
)
