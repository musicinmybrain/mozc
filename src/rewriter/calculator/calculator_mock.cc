// Copyright 2010-2021, Google Inc.
// All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are
// met:
//
//     * Redistributions of source code must retain the above copyright
// notice, this list of conditions and the following disclaimer.
//     * Redistributions in binary form must reproduce the above
// copyright notice, this list of conditions and the following disclaimer
// in the documentation and/or other materials provided with the
// distribution.
//     * Neither the name of Google Inc. nor the names of its
// contributors may be used to endorse or promote products derived from
// this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
// A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
// OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
// SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
// LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
// DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
// THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
// OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#include "rewriter/calculator/calculator_mock.h"

#include <string>

#include "base/logging.h"

namespace mozc {
CalculatorMock::CalculatorMock() : calculation_counter_(0) {}

CalculatorMock::~CalculatorMock() {}

void CalculatorMock::SetCalculatePair(const std::string &key,
                                      const std::string &value,
                                      bool return_value) {
  calculation_map_[key] = std::make_pair(value, return_value);
}

int CalculatorMock::calculation_counter() const { return calculation_counter_; }

bool CalculatorMock::CalculateString(const std::string &key,
                                     std::string *result) const {
  ++calculation_counter_;
  DCHECK(result);
  CalculationMap::const_iterator iter = calculation_map_.find(key);
  if (iter == calculation_map_.end()) {
    result->clear();
    return false;
  }
  *result = iter->second.first;
  return iter->second.second;
}
}  // namespace mozc
