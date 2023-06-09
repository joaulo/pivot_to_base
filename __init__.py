# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from . import (
    operators,
    # panels,
    # properties,
)

import bpy
from bpy.props import PointerProperty


bl_info = {
    "name" : "pivot_to_base",
    "author" : "joaulo <jsoftworks@joaulo.com>",
    "description" : "Move mesh center to the middle of bottom vertices",
    "blender" : (2, 80, 0),
    "version" : (1, 0, 1),
    "location" : "",
    "category" : "Mesh"
    # "warning": "",  # used for warning icon and text in addons panel
    # "doc_url": "https://",
    # "tracker_url": "",
}

# classes = properties.classes + operators.classes + panels.classes
classes = operators.classes


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    # bpy.types.Scene.pivot_to_base = PointerProperty(
    #     type=properties.PivotToBaseProperties)


def unregister():
    # del bpy.types.Scene.pivot_to_base
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()