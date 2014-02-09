"""
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

# authentication
AUTH_ANONYMOUS = 0
AUTH_SIMPLE = 1
AUTH_SASL = 2
SASL_AVAILABLE_MECHANISMS = ['EXTERNAL', 'DIGEST-MD5']

AUTHZ_STATE_CLOSED = 0
AUTHZ_STATE_ANONYMOUS = 1
AUTHZ_STATE_UNAUTHENTICATED = 2

# search scope
SEARCH_SCOPE_BASE_OBJECT = 0
SEARCH_SCOPE_SINGLE_LEVEL = 1
SEARCH_SCOPE_WHOLE_SUBTREE = 2

# search alias
SEARCH_NEVER_DEREFERENCE_ALIASES = 0
SEARCH_DEREFERENCE_IN_SEARCHING = 1
SEARCH_DEREFERENCE_FINDING_BASE_OBJECT = 2
SEARCH_DEREFERENCE_ALWAYS = 3

# search attributes
ALL_ATTRIBUTES = '*'
NO_ATTRIBUTES = '1.1'  # as per RFC 4511
ALL_OPERATIONAL_ATTRIBUTES = '+'  # as per RFC 3673

# modify type
MODIFY_ADD = 0
MODIFY_DELETE = 1
MODIFY_REPLACE = 2
MODIFY_INCREMENT = 3

# client strategies
STRATEGY_SYNC = 0
STRATEGY_ASYNC_THREADED = 1
STRATEGY_LDIF_PRODUCER = 2

CLIENT_STRATEGIES = [STRATEGY_SYNC, STRATEGY_ASYNC_THREADED, STRATEGY_LDIF_PRODUCER]
ASYNC_STRATEGIES = [STRATEGY_ASYNC_THREADED]
NO_SERVER_STRATEGIES = [STRATEGY_LDIF_PRODUCER]

# communication parameters
RESPONSE_SLEEPTIME = 0.02
RESPONSE_WAITING_TIMEOUT = 1
RESPONSE_COMPLETE = -1
SESSION_TERMINATED_BY_SERVER = 0
SOCKET_SIZE = 4096

# LDAP protocol parameters
LDAP_MAX_INT = 2147483647

# ldif parameters
LDIF_LINE_LENGTH = 78

# result codes
RESULT_SUCCESS = 0
RESULT_OPERATIONS_ERROR = 1
RESULT_PROTOCOL_ERROR = 2
RESULT_TIME_LIMIT_EXCEEDED = 3
RESULT_SIZE_LIMIT_EXCEEDED = 4
RESULT_COMPARE_FALSE = 5
RESULT_COMPARE_TRUE = 6
RESULT_AUTH_METHOD_NOT_SUPPORTED = 7
RESULT_STRONGER_AUTH_REQUIRED = 8
RESULT_REFERRAL = 10
RESULT_ADMIN_LIMIT_EXCEEDED = 11
RESULT_UNAVAILABLE_CRITICAL_EXTENSION = 12
RESULT_CONFIDENTIALITY_REQUIRED = 13
RESULT_SASL_BIND_IN_PROGRESS = 14
RESULT_NO_SUCH_ATTRIBUTE = 16
RESULT_UNDEFINED_ATTRIBUTE_TYPE = 17
RESULT_INAPPROPRIATE_MATCHING = 18
RESULT_CONSTRAINT_VIOLATION = 19
RESULT_ATTRIBUTE_OR_VALUE_EXISTS = 20
RESULT_INVALID_ATTRIBUTE_SYNTAX = 21
RESULT_NO_SUCH_OBJECT = 32
RESULT_ALIAS_PROBLEM = 33
RESULT_INVALID_DN_SYNTAX = 34
RESULT_ALIAS_DEREFERENCING_PROBLEM = 36
RESULT_INAPPROPRIATE_AUTHENTICATION = 48
RESULT_INVALID_CREDENTIALS = 49
RESULT_INSUFFICIENT_ACCESS_RIGHTS = 50
RESULT_BUSY = 51
RESULT_UNAVAILABLE = 52
RESULT_UNWILLING_TO_PERFORM = 53
RESULT_LOOP_DETECTED = 54
RESULT_NAMING_VIOLATION = 64
RESULT_OBJECT_CLASS_VIOLATION = 65
RESULT_NOT_ALLOWED_ON_NON_LEAF = 66
RESULT_NOT_ALLOWED_ON_RDN = 67
RESULT_ENTRY_ALREADY_EXISTS = 68
RESULT_OBJECT_CLASS_MODS_PROHIBITED = 69
RESULT_AFFECT_MULTIPLE_DSAS = 71
RESULT_OTHER = 80
RESULT_LCUP_RESOURCES_EXHAUSTED = 113
RESULT_LCUP_SECURITY_VIOLATION = 114
RESULT_LCUP_INVALID_DATA = 115
RESULT_LCUP_UNSUPPORTED_SCHEME = 116
RESULT_LCUP_RELOAD_REQUIRED = 117
RESULT_CANCELED = 118
RESULT_NO_SUCH_OPERATION = 119
RESULT_TOO_LATE = 120
RESULT_CANNOT_CANCEL = 121
RESULT_ASSERTION_FAILED = 122
RESULT_AUTHORIZATION_DENIED = 123
RESULT_E_SYNC_REFRESH_REQUIRED = 4096

# get rootDSE info
GET_NO_INFO = 0
GET_DSA_INFO = 1
GET_SCHEMA_INFO = 2
GET_ALL_INFO = 3

# OID database definition
OID_CONTROL = 0
OID_EXTENSION = 1
OID_FEATURE = 2
OID_UNSOLICITED_NOTICE = 3
OID_ATTRIBUTE_TYPE = 4
OID_DIT_CONTENT_RULE = 5
OID_LDAP_URL_EXTENSION = 6
OID_FAMILY = 7
OID_MATCHING_RULE = 8
OID_NAME_FORM = 9
OID_OBJECT_CLASS = 10
OID_ADMINISTRATIVE_ROLE = 11
OID_LDAP_SYNTAX = 12

CLASS_STRUCTURAL = 0
CLASS_ABSTRACT = 1
CLASS_AUXILIARY = 2

ATTRIBUTE_USER_APPLICATION = 0
ATTRIBUTE_DIRECTORY_OPERATION = 1
ATTRIBUTE_DISTRIBUTED_OPERATION = 2
ATTRIBUTE_DSA_OPERATION = 3

ABSTRACTION_OPERATIONAL_ATTRIBUTE_PREFIX = 'OP_'


class LDAPException(Exception):
    pass

from .server import Server
from .connection import Connection
from .tls import Tls


