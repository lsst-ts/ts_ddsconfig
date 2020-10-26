# This file is part of ts_ddsconfig
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License

import pathlib

from lsst.ts import ddsconfig


def get_desired_pkg_root() -> pathlib.Path:
    return pathlib.Path(__file__).parent.parent


def test_get_pkg_root() -> None:
    pkg_root = ddsconfig.get_pkg_root()
    assert pkg_root.exists()
    assert pkg_root.is_dir()
    assert (pkg_root / "config").exists()
    assert (pkg_root / "qos").exists()


def test_get_config_dir() -> None:
    config_dir = ddsconfig.get_config_dir()
    assert config_dir.exists()
    assert config_dir.is_dir()
    desired_config_dir = get_desired_pkg_root() / "config"
    # The two paths may not match, because when conda runs this test
    # the ddsconfig function is in the installed package
    # but the unit test is not.
    # But they should contain the same xml files.
    config_files = [path.name for path in config_dir.glob("*.xml")]
    desired_config_files = [path.name for path in desired_config_dir.glob("*.xml")]
    assert set(config_files) == set(desired_config_files)


def test_get_qos_path() -> None:
    qos_path = ddsconfig.get_qos_path()
    assert qos_path.exists()
    assert qos_path.is_file()
    desired_qos_path = get_desired_pkg_root() / "qos" / "QoS.xml"
    # The two paths may not match, as explained in test_get_config_dir,
    # so test that the QoS files match, instead.
    with open(qos_path, "r") as f:
        qos_data = f.read()
    with open(desired_qos_path, "r") as f:
        desired_qos_data = f.read()
    assert qos_data == desired_qos_data
