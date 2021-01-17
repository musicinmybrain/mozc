# Copyright 2010-2021, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

{
  'variables': {
    'relative_dir': 'rewriter/calculator',
  },
  'targets': [
    {
      'target_name': 'calculator',
      'type': 'static_library',
      'sources': [
        'calculator.cc',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
      ],
      'msvs_disabled_warnings': [
        # switch statement contains 'default' but no 'case' labels
        # http://msdn.microsoft.com/en-us/library/te26h1tz.aspx
        # The parser code generated by Lemon parser contains this.
        '4065',
        # 'type' : forcing value to bool 'true' or 'false'
        # (performance warning)
        # http://msdn.microsoft.com/en-us/library/b6801kcy.aspx
        '4800',
      ],
    },
    {
      'target_name': 'calculator_mock',
      'type': 'static_library',
      'sources': [
        'calculator_mock.cc',
      ],
      'dependencies': [
        '../../base/absl.gyp:absl_strings',
        '../../base/base.gyp:base',
        'calculator',
      ],
    },
    {
      'target_name': 'install_calculator_test_data',
      'type': 'none',
      'variables': {
        'test_data': [
          '../../<(test_data_subdir)/testset.txt',
        ],
        'test_data_subdir': 'data/test/calculator',
      },
      'includes': [ '../../gyp/install_testdata.gypi' ],
    },
    {
      'target_name': 'calculator_test',
      'type': 'executable',
      'sources': [
        'calculator_test.cc',
      ],
      'dependencies': [
        '../../testing/testing.gyp:gtest_main',
        '../../testing/testing.gyp:mozctest',
        'calculator',
        'install_calculator_test_data',
      ],
      'variables': {
        'test_size': 'small',
      },
    },
    # Test cases meta target: this target is referred from gyp/tests.gyp
    {
      'target_name': 'calculator_all_test',
      'type': 'none',
      'dependencies': [
        'calculator_test',
      ],
    },
  ],
}
