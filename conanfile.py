#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/2.0.0@bincrafters/testing")


class BoostLogConan(base.BoostBaseConan):
    name = "boost_log"
    version = "1.70.0"

    @property
    def boost_build_requires(self):
        return ["align", "asio", "interprocess"]

    def package_info(self):
        super(BoostLogConan, self).package_info()
        if self.options.shared:
            self.cpp_info.defines.append("BOOST_LOG_DYN_LINK=1")
            self.cpp_info.defines.append("BOOST_LOG_SETUP_DYN_LINK=1")
