#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os

API_ID       = int(os.environ.get("API_ID", "5521321929"))
API_HASH     = os.environ.get("API_HASH", "42e049ac8d3d69b66a9768170c0bcff6")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "6589613024:AAGGxzWZ654yY2xk2dILUb0NaDDqr4BE7Gg")
SESSION      = os.environ.get("SESSION", "6589613024:AAGGxzWZ654yY2xk2dILUb0NaDDqr4BE7Gg")
TIME         = int(os.environ.get("TIME", 600))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1001925289959").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "5521321929").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Akrtech:Djdjegpw@cluster0.pfpnk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
PORT         = os.environ.get("PORT", "8080")
