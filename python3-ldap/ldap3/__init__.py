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
STRATEGY_SYNC_RESTARTABLE = 3
STRATEGY_REUSABLE_THREADED = 4

CLIENT_STRATEGIES = [STRATEGY_SYNC, STRATEGY_ASYNC_THREADED, STRATEGY_LDIF_PRODUCER, STRATEGY_SYNC_RESTARTABLE, STRATEGY_REUSABLE_THREADED]

# communication
SESSION_TERMINATED_BY_SERVER = 0
RESPONSE_COMPLETE = -1
RESPONSE_SLEEPTIME = 0.02  # seconds to wait while waiting for a response in asynchronous strategies
RESPONSE_WAITING_TIMEOUT = 10  # waiting timeout for receiving a response in asynchronous strategies
SOCKET_SIZE = 4096  # socket byte size

#restartable strategy
RESTARTABLE_SLEEPTIME = 2  # time to wait in a restartable strategy before retrying the request
RESTARTABLE_TRIES = 50  # number of times to retry in a restartable strategy before giving up. Set to True for unlimited retries

# reusable strategy
TERMINATE_REUSABLE = -1
REUSABLE_POOL_SIZE = 10
REUSABLE_CONNECTION_LIFETIME = 3600

# LDAP protocol
LDAP_MAX_INT = 2147483647

# LDIF
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

# class kind
CLASS_STRUCTURAL = 0
CLASS_ABSTRACT = 1
CLASS_AUXILIARY = 2

# attribute kind
ATTRIBUTE_USER_APPLICATION = 0
ATTRIBUTE_DIRECTORY_OPERATION = 1
ATTRIBUTE_DISTRIBUTED_OPERATION = 2
ATTRIBUTE_DSA_OPERATION = 3

# abstraction layer
ABSTRACTION_OPERATIONAL_ATTRIBUTE_PREFIX = 'OP_'

# pooling
POOLING_STRATEGY_FIRST = 0
POOLING_STRATEGY_ROUND_ROBIN = 1
POOLING_STRATEGY_RANDOM = 2
POOLING_STRATEGIES = [POOLING_STRATEGY_FIRST, POOLING_STRATEGY_ROUND_ROBIN, POOLING_STRATEGY_RANDOM]


# LDAPException hierarchy

class LDAPException(Exception):
    def __new__(cls, result=None, description=None, dn=None, message=None):
        if cls is LDAPException and result and result in exception_table:
            #exc = super(LDAPException, exception_table[result]).__new__(exception_table[result], result=result, description=description, dn=dn, message=message)  # create an exception of the required result error
            exc = super(LDAPException, exception_table[result]).__new__(exception_table[result])  # create an exception of the required result error
            exc.result = result
            exc.description = description
            exc.dn = dn
            exc.message = message
        elif cls is LDAPException:
            exc = super(LDAPException, cls).__new__(cls)
        return exc

    def __init__(self, result=None, description=None, dn=None, message=None):
        self.result = result
        self.description = description
        self.dn = dn
        self.message = message

    def __str__(self):
        s = [
            self.__class__.__name__,
            str(self.result) if self.result else None,
            self.description if self.description else None,
            self.dn if self.dn else None,
            self.message if self.message else None
        ]

        return ' - '.join(filter(None, s))

    def __repr__(self):
        return self.__str__()


class LDAPOperationsError(LDAPException):
    pass


class LDAPProtocolError(LDAPException):
    pass


class LDAPTimeLimitExceeded(LDAPException):
    pass


class LDAPSizeLimitExceeded(LDAPException):
    pass


class LDAPAuthMethodNotSupported(LDAPException):
    pass


class LDAPStrongerAuthRequired(LDAPException):
    pass


class LDAPReferral(LDAPException):
    pass


class LDAPAdminLimitExceeded(LDAPException):
    pass


class LDAPUnavailableCriticalExtension(LDAPException):
    pass


class LDAPConfidentialityRequired(LDAPException):
    pass


class LDAPSaslBindInProgress(LDAPException):
    pass


class LDAPNoSuchAttribute(LDAPException):
    pass


class LDAPUndefinedAttributeType(LDAPException):
    pass


class LDAPInappropriateMatching(LDAPException):
    pass


class LDAPConstraintViolation(LDAPException):
    pass


class LDAPAttributeOrValueExists(LDAPException):
    pass


class LDAPInvalidAttributeSyntax(LDAPException):
    pass


class LDAPNoSuchObject(LDAPException):
    pass


class LDAPAliasProblem(LDAPException):
    pass


class LDAPInvalidDNSyntax(LDAPException):
    pass


class LDAPAliasDereferencingProblem(LDAPException):
    pass


class LDAPInappropriateAuthentication(LDAPException):
    pass


class LDAPInvalidCredentials(LDAPException):
    pass


class LDAPInsufficientAccessRights(LDAPException):
    pass


class LDAPBusy(LDAPException):
    pass


class LDAPUnavailable(LDAPException):
    pass


class LDAPUnwillingToPerform(LDAPException):
    pass


class LDAPLoopDetected(LDAPException):
    pass


class LDAPNamingViolation(LDAPException):
    pass


class LDAPObjectClassViolation(LDAPException):
    pass


class LDAPNotAllowedOnNotLeaf(LDAPException):
    pass


class LDAPNotAllowedOnRDN(LDAPException):
    pass


class LDAPEntryAlreadyExists(LDAPException):
    pass


class LDAPObjectClassModsProhibited(LDAPException):
    pass


class LDAPAffectMultipleDSAS(LDAPException):
    pass


class LDAPOther(LDAPException):
    pass


class LDAPLCUPResourcesExhausted(LDAPException):
    pass


class LDAPLCUPSecurityViolation(LDAPException):
    pass


class LDAPLCUPInvalidData(LDAPException):
    pass


class LDAPLCUPUnsupportedScheme(LDAPException):
    pass


class LDAPLCUPReloadRequired(LDAPException):
    pass


class LDAPCanceled(LDAPException):
    pass


class LDAPNoSuchOperation(LDAPException):
    pass


class LDAPTooLate(LDAPException):
    pass


class LDAPCannotCancel(LDAPException):
    pass


class LDAPAssertionFailed(LDAPException):
    pass


class LDAPAuthorizationDenied(LDAPException):
    pass


class LDAPESyncRefreshRequired(LDAPException):
    pass


exception_table = {
    RESULT_OPERATIONS_ERROR: LDAPOperationsError,
    RESULT_PROTOCOL_ERROR: LDAPProtocolError,
    RESULT_TIME_LIMIT_EXCEEDED: LDAPTimeLimitExceeded,
    RESULT_SIZE_LIMIT_EXCEEDED: LDAPSizeLimitExceeded,
    RESULT_AUTH_METHOD_NOT_SUPPORTED: LDAPAuthMethodNotSupported,
    RESULT_STRONGER_AUTH_REQUIRED: LDAPStrongerAuthRequired,
    RESULT_REFERRAL: LDAPReferral,
    RESULT_ADMIN_LIMIT_EXCEEDED: LDAPAdminLimitExceeded,
    RESULT_UNAVAILABLE_CRITICAL_EXTENSION: LDAPUnavailableCriticalExtension,
    RESULT_CONFIDENTIALITY_REQUIRED: LDAPConfidentialityRequired,
    RESULT_SASL_BIND_IN_PROGRESS: LDAPSaslBindInProgress,
    RESULT_NO_SUCH_ATTRIBUTE: LDAPNoSuchAttribute,
    RESULT_UNDEFINED_ATTRIBUTE_TYPE: LDAPUndefinedAttributeType,
    RESULT_INAPPROPRIATE_MATCHING: LDAPInappropriateMatching,
    RESULT_CONSTRAINT_VIOLATION: LDAPConstraintViolation,
    RESULT_ATTRIBUTE_OR_VALUE_EXISTS: LDAPAttributeOrValueExists,
    RESULT_INVALID_ATTRIBUTE_SYNTAX: LDAPInvalidAttributeSyntax,
    RESULT_NO_SUCH_OBJECT: LDAPNoSuchObject,
    RESULT_ALIAS_PROBLEM: LDAPAliasProblem,
    RESULT_INVALID_DN_SYNTAX: LDAPInvalidDNSyntax,
    RESULT_ALIAS_DEREFERENCING_PROBLEM: LDAPAliasDereferencingProblem,
    RESULT_INAPPROPRIATE_AUTHENTICATION: LDAPInappropriateAuthentication,
    RESULT_INVALID_CREDENTIALS: LDAPInvalidCredentials,
    RESULT_INSUFFICIENT_ACCESS_RIGHTS: LDAPInsufficientAccessRights,
    RESULT_BUSY: LDAPBusy,
    RESULT_UNAVAILABLE: LDAPUnavailable,
    RESULT_UNWILLING_TO_PERFORM: LDAPUnwillingToPerform,
    RESULT_LOOP_DETECTED: LDAPLoopDetected,
    RESULT_NAMING_VIOLATION: LDAPNamingViolation,
    RESULT_OBJECT_CLASS_VIOLATION: LDAPObjectClassViolation,
    RESULT_NOT_ALLOWED_ON_NON_LEAF: LDAPNotAllowedOnNotLeaf,
    RESULT_NOT_ALLOWED_ON_RDN: LDAPNotAllowedOnRDN,
    RESULT_ENTRY_ALREADY_EXISTS: LDAPEntryAlreadyExists,
    RESULT_OBJECT_CLASS_MODS_PROHIBITED: LDAPObjectClassModsProhibited,
    RESULT_AFFECT_MULTIPLE_DSAS: LDAPAffectMultipleDSAS,
    RESULT_OTHER: LDAPOther,
    RESULT_LCUP_RESOURCES_EXHAUSTED: LDAPLCUPResourcesExhausted,
    RESULT_LCUP_SECURITY_VIOLATION: LDAPLCUPSecurityViolation,
    RESULT_LCUP_INVALID_DATA: LDAPLCUPInvalidData,
    RESULT_LCUP_UNSUPPORTED_SCHEME: LDAPLCUPUnsupportedScheme,
    RESULT_LCUP_RELOAD_REQUIRED: LDAPLCUPReloadRequired,
    RESULT_CANCELED: LDAPCanceled,
    RESULT_NO_SUCH_OPERATION: LDAPNoSuchOperation,
    RESULT_TOO_LATE: LDAPTooLate,
    RESULT_CANNOT_CANCEL: LDAPCannotCancel,
    RESULT_ASSERTION_FAILED: LDAPAssertionFailed,
    RESULT_AUTHORIZATION_DENIED: LDAPAuthorizationDenied,
    RESULT_E_SYNC_REFRESH_REQUIRED: LDAPESyncRefreshRequired
}

from .core.server import Server
from .core.connection import Connection
from .core.tls import Tls
from .core.pooling import ServerPool
from .abstract import ObjectDef, AttrDef, Attribute, Entry, Reader, OperationalAttribute
