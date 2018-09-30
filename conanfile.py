#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostLogConan(base.BoostBaseConan):
    name = "boost_log"
    url = "https://github.com/bincrafters/conan-boost_log"
    lib_short_names = ["log"]
    options = {"shared": [True, False]}
    default_options = "shared=False"
    source_only_deps = [
        "align",
        "asio",
        "interprocess",
        "io",
        "random"
    ]
    b2_requires = [
        "boost_array",
        "boost_assert",
        "boost_atomic",
        "boost_bind",
        "boost_config",
        "boost_container",
        "boost_core",
        "boost_date_time",
        "boost_exception",
        "boost_filesystem",
        "boost_function_types",
        "boost_fusion",
        "boost_intrusive",
        "boost_iterator",
        "boost_lexical_cast",
        "boost_locale",
        "boost_move",
        "boost_mpl",
        "boost_optional",
        "boost_parameter",
        "boost_phoenix",
        "boost_predef",
        "boost_preprocessor",
        "boost_property_tree",
        "boost_proto",
        "boost_range",
        "boost_regex",
        "boost_smart_ptr",
        "boost_spirit",
        "boost_static_assert",
        "boost_system",
        "boost_thread",
        "boost_throw_exception",
        "boost_type_index",
        "boost_type_traits",
        "boost_utility",
        "boost_winapi",
        "boost_xpressive"
    ]
    
    b2_build_requires = [
        "boost_align",
        "boost_asio",
        "boost_interprocess",
    ]

    def package_info_additional(self):
        if self.options.shared:
            self.cpp_info.defines.append("BOOST_LOG_DYN_LINK=1")
            self.cpp_info.defines.append("BOOST_LOG_SETUP_DYN_LINK=1")
        try:
            if not self.settings.threads:
                self.cpp_info.defines.append("BOOST_LOG_NO_THREADS=1")
        except:
            pass


