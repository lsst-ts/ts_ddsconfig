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


def get_desired_data_root() -> pathlib.Path:
    return pathlib.Path(ddsconfig.__file__).parent / "data"


def test_get_data_root() -> None:
    pkg_root = ddsconfig.get_data_root()
    assert pkg_root.exists()
    assert pkg_root.is_dir()
    desired_pkg_root = get_desired_data_root()
    assert pkg_root.samefile(desired_pkg_root)


def test_get_config_dir() -> None:
    config_dir = ddsconfig.get_config_dir()
    assert config_dir.exists()
    assert config_dir.is_dir()
    desired_config_dir = get_desired_data_root() / "config"
    assert config_dir.samefile(desired_config_dir)


def test_get_qos_path() -> None:
    qos_path = ddsconfig.get_qos_path()
    assert qos_path.exists()
    assert qos_path.is_file()
    desired_qos_path = get_desired_data_root() / "qos" / "Qos.xml"
    assert qos_path.samefile(desired_qos_path)
