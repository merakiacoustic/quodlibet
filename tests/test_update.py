# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

from tests import TestCase

from quodlibet.update import UpdateDialog


class TUpdateDialog(TestCase):
    def test_main(self):
        UpdateDialog(None).destroy()
