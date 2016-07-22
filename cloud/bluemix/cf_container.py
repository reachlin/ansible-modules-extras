#!/usr/bin/python
# Copyright 2016 reachlin@gmail.com. All Rights Reserved.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

"""An Ansible module to utilize IBM Bluemix container APIs."""

DOCUMENTATION = '''
---
module: cf_container
version_added: ""
short_description: utilize IBM Bluemix container services
description:
    - This module can create, and delete containers on IBM Bluemix.
options:
  name:
    description:
      - the name of the container to create or delete
    required: true
    default: null
  description:
    description:
      - an optional description
    required: false
    default: null
  username:
    description:
      - Blumix user name
    required: true
    default: null
  password:
    description:
      - Blumix user password
    required: true
    default: null
  organization:
    description:
      - Blumix organization name
    required: true
    default: null
  space:
    description:
      - Blumix space name
    required: true
    default: null
  image:
    description:
      - the image name for the container
    required: false
    default: null
requirements:
    - "python >= 2.6"
author: "reachlin@gmail.com"
'''

EXAMPLES = '''
# Create an image named test-image from the disk 'test-disk' in zone us-central1-a.
- gce_img:
    name: test-image
    source: test-disk
    zone: us-central1-a
    state: present

# Create an image named test-image from a tarball in Google Cloud Storage.
- gce_img:
    name: test-image
    source: https://storage.googleapis.com/bucket/path/to/image.tgz

# Alternatively use the gs scheme
- gce_img:
    name: test-image
    source: gs://bucket/path/to/image.tgz

# Delete an image named test-image.
- gce_img:
    name: test-image
    state: absent
'''

import sys


def create_image(gce, name, module):



def delete_image(gce, name, module):


def main():
  module = AnsibleModule(
      argument_spec=dict(
          name=dict(required=True),
          description=dict(),
          source=dict(),
          state=dict(default='present', choices=['present', 'absent']),
          zone=dict(default='us-central1-a'),
          service_account_email=dict(),
          pem_file=dict(type='path'),
          project_id=dict(),
          timeout=dict(type='int', default=180)
      )
  )


# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.gce import *

main()
