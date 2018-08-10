# -*- coding: utf-8 -*-
# Copyright 2015 Objectif Libre
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# @author: Stéphane Albert
#
import abc
import six

from oslo_config import cfg

FETCHER_OPTS = 'fetcher'
DEPRECATED_FETCHER_OPTS = 'tenant_fetcher'
fetchers_opts = [
    cfg.StrOpt('backend',
               default='keystone',
               help='Driver used to fetch tenant list.',
               deprecated_group=DEPRECATED_FETCHER_OPTS)
]
cfg.CONF.register_opts(fetchers_opts, 'fetcher')


@six.add_metaclass(abc.ABCMeta)
class BaseFetcher(object):
    """CloudKitty tenants fetcher.

    Provides Cloudkitty integration with a backend announcing ratable tenants.
    """

    @abc.abstractmethod
    def get_tenants(self):
        """Get a list of tenants to rate."""
