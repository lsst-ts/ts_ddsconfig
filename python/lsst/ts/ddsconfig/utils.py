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

__all__ = ["get_data_dir", "get_config_dir", "get_qos_path"]

import pathlib


def get_data_dir() -> pathlib.Path:
    """Return the data directory of this package."""
    return pathlib.Path(__file__).resolve().parents[0] / "data"


def get_config_dir() -> pathlib.Path:
    """Return the path to the ``config`` dir within this package."""
    return get_data_dir() / "config"


def get_qos_path() -> pathlib.Path:
    """Return the path to the OpenSplice quality of service config file."""
    return get_data_dir() / "qos" / "QoS.xml"
