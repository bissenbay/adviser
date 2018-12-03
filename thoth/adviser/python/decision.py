#!/usr/bin/env python3
# thoth-adviser
# Copyright(C) 2018 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Decisison functions available for dependency graph."""

import random


def random_uniform(_):
    """Retrieve a random stack."""
    return random.getrandbits(1), []


def everything(_):
    """Decide to include everything."""
    return 1.0, []


DECISISON_FUNCTIONS = {
    'random': random_uniform,
    'all': everything
}

DEFAULT_DECISION_FUNCTION = everything
