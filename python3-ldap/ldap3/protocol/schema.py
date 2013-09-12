"""
Created on 2013.09.11

@author: Giovanni Cannata

Copyright 2013 Giovanni Cannata

This file is part of Python3-ldap.

Python3-ldap is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Python3-ldap is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with Python3-ldap in the COPYING and COPYING.LESSER files.
If not, see <http://www.gnu.org/licenses/>.
"""
from collections import namedtuple
from os import linesep
import re
from OCDef import fromDefinition
from ldap3 import CLASS_ABSTRACT, CLASS_STRUCTURAL, CLASS_AUXILIARY

def quotedStringToList(string):
        string = string.strip()
        if string[0] == '(' and string[:-1] == ')':
            string = string[1:-1]
        elements = string.split()
        return [element.strip("'").strip() for element in elements]

def oidsStringToList(string):
        string = string.strip()
        if string[0] == '(' and string[:-1] == ')':
            string = string[1:-1]
        elements = string.split('$')
        return [element.strip() for element in elements]

def extensionToTuple(string):
        string = string.strip()
        name, _, values = string.partition(' ')
        return (name, quotedStringToList(values))

class ObjectClassInfo():
    def __init__(self, oid = None, name = None, description = None, obsolete = False, superior = None, kind = None, mustContain = None, mayContain = None, extensions = None, experimental = None):
        self.oid = oid
        self.name = name
        self.description = description
        self.obsolete = obsolete
        self.superior = superior
        self.kind = kind
        self.mustContain = mustContain
        self.mayContain = mayContain
        self.extensions = extensions
        self.experimental = experimental

    def __str__(self):
        r = self.oid
        r += (': ' + self.name) if self.name else ''
        r += (' [OBSOLETE]' + linesep) if self.obsolete else linesep
        r += ('  Description: ' + self.description + linesep) if self.description else ''
        r += ('  Type: ' + self.kind + linesep) if self.kind else ''
        r += ('  Must contain attributes: ' + self.mustContain + linesep) if self.mustContain else ''
        r += ('  May contain attributes: ' + self.mayContain + linesep) if self.mayContain else ''
        r += ('  Extensions: ' + self.extensions + linesep) if self.extensions else ''
        r += ('  Experimental: ' + self.experimental + linesep) if self.experimental else ''

        return r
    @staticmethod
    def fromDefinition(objectClassDefinition):
        if not objectClassDefinition:
            return None

        if [objectClassDefinition[0] == ')' and objectClassDefinition[:-1] == ')']:
            splitted = re.split('( NAME | DESC | OBSOLETE| SUP | ABSTRACT| STRUCTURAL| AUXILIARY| MUST | MAY | X-| E-)', objectClassDefinition[1:-1])
            values = splitted[::2]
            separators = splitted[1::2]
            separators.insert(0, 'OID')
            defs = list(zip(separators, values))
            objectClassDef = ObjectClassInfo()
            for d in defs:
                key = d[0].strip()
                value = d[1].strip()
                if key == 'OID':
                    objectClassDef.oid = value
                elif key == 'NAME':
                    objectClassDef.name = quotedStringToList(value)
                elif key == 'DESC':
                    objectClassDef.description = value
                elif key == 'OBSOLETE':
                    objectClassDef.obsolete = True
                elif key == 'SUP':
                    objectClassDef.description = oidsStringToList(value)
                elif key == 'ABSTRACT':
                    objectClassDef.kind = CLASS_ABSTRACT
                elif key == 'STRUCTURAL':
                    objectClassDef.kind = CLASS_STRUCTURAL
                elif key == 'AUXILIARY':
                    objectClassDef.kind = CLASS_AUXILIARY
                elif key == 'MUST':
                    objectClassDef.mustContain = oidsStringToList(value)
                elif key == 'MAY':
                    objectClassDef.mayContain = oidsStringToList(value)
                elif key == 'X-':
                    if not objectClassDef.extensions:
                        objectClassDef.extensions = list()
                    objectClassDef.extensions.append(extensionToTuple('X-' + value))
                elif key == 'E-':
                    if not objectClassDef.experimental:
                        objectClassDef.experimental = list()
                    objectClassDef.experimental.append(extensionToTuple('E-' + value))
                else:
                    raise Exception('malformed Object Class Definition key:' + key)
            return objectClassDef
        else:
            raise Exception('malformed Object Class Definition')


class SchemaInfo():
    """
       This class contains info about the ldap server schema read from an entry (default to DSE)
       as defined in rfc 4512. Unkwnown attributes are stored in the "other" dict
    """

    def __init__(self, schemaEntry, attributes):
        self.schemaEntry = schemaEntry
        self.createTimeStamp = attributes.pop('createTimestamp', None)
        self.modifyTimeStamp = attributes.pop('modifyTimestamp', None)
        self.attributeTypes = attributes.pop('attributeTypes', None)
        self.ldapSyntaxes = attributes.pop('ldapSyntaxes', None)
        self.objectClasses = [objectClassDef for objectClassDef in ObjectClassInfo.fromDefinition(attributes.pop('objectClasses', []))]
        self.other = attributes

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        r = 'DSA Schema from: ' + self.schemaEntry + linesep
        r += ('  Attribute Types:' + linesep + '    ' + ', '.join([s for s in self.attributeTypes]) + linesep) if self.attributeTypes else ''
        r += ('  Object Classes:' + linesep + '    ' + ', '.join([s for s in self.objectClasses]) + linesep) if self.objectClasses else ''
        r += ('  LDAP Syntaxes:' + linesep + '    ' + ', '.join([s for s in self.ldapSyntaxes]) + linesep) if self.ldapSyntaxes else ''
        r += 'Other:' + linesep

        for k, v in self.other.items():
            r += '  ' + k + ': ' + linesep
            if isinstance(v, str):
                r += v + linesep
            else:
                r += linesep.join(['    ' + str(s) for s in v]) + linesep
        return r