"""
Created on 2014.03.29

@author: Giovanni Cannata

Copyright 2013 Giovanni Cannata

This file is part of python3-ldap.

python3-ldap is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

python3-ldap is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with python3-ldap in the COPYING and COPYING.LESSER files.
If not, see <http://www.gnu.org/licenses/>.
"""

import unittest

from ldap3.protocol.rfc4511 import LDAPDN, AddRequest, AttributeList, Attribute, AttributeDescription, AttributeValue, CompareRequest, AttributeValueAssertion, AssertionValue, ValsAtLeast1
from ldap3.core.connection import Connection
from ldap3.core.server import Server
from test import test_server, test_port, test_user, test_password, test_authentication, test_strategy, test_dn_builder, test_base

from ldap3 import Connection, Server, ServerPool, SEARCH_SCOPE_WHOLE_SUBTREE, STRATEGY_SYNC_RESTARTABLE, POOLING_STRATEGY_ROUND_ROBIN_PASSIVE, POOLING_STRATEGY_ROUND_ROBIN_ACTIVE, LDAPException


class Test(unittest.TestCase):
    def test_restartable_invalid_server(self):
        hosts = [test_server, '127.0.0.1']
        search_results = []
        servers = [Server(host=host, port=636, use_ssl=True) for host in hosts]

        connection = Connection(ServerPool(servers, POOLING_STRATEGY_ROUND_ROBIN_PASSIVE), user=test_user, password=test_password, client_strategy=STRATEGY_SYNC_RESTARTABLE, lazy=True)

        with connection as c:
            c.search(search_base='o=test', search_filter='(cn=test*)', search_scope=SEARCH_SCOPE_WHOLE_SUBTREE, attributes='*')

            for resp in connection.response:
                if resp['type'] == 'searchResEntry':
                    search_results.append(resp['dn'])
        self.assertTrue(len(search_results) > 15)