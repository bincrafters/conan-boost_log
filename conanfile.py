#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostLogConan(ConanFile):
    name = "boost_log"
    version = "1.66.0"
    url = "https://github.com/bincrafters/conan-boost_log"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    lib_short_names = ["log"]
    is_header_only = False
    
    options = {"shared": [True, False]}
    default_options = "shared=False"

    requires = (
        "boost_package_tools/1.66.0@bincrafters/testing",
        "boost_align/1.66.0@bincrafters/testing",
        "boost_array/1.66.0@bincrafters/testing",
        "boost_asio/1.66.0@bincrafters/testing",
        "boost_assert/1.66.0@bincrafters/testing",
        "boost_atomic/1.66.0@bincrafters/testing",
        "boost_bind/1.66.0@bincrafters/testing",
        "boost_config/1.66.0@bincrafters/testing",
        "boost_core/1.66.0@bincrafters/testing",
        "boost_date_time/1.66.0@bincrafters/testing",
        "boost_exception/1.66.0@bincrafters/testing",
        "boost_filesystem/1.66.0@bincrafters/testing",
        "boost_function_types/1.66.0@bincrafters/testing",
        "boost_fusion/1.66.0@bincrafters/testing",
        "boost_interprocess/1.66.0@bincrafters/testing",
        "boost_intrusive/1.66.0@bincrafters/testing",
        "boost_iterator/1.66.0@bincrafters/testing",
        "boost_lexical_cast/1.66.0@bincrafters/testing",
        "boost_locale/1.66.0@bincrafters/testing",
        "boost_move/1.66.0@bincrafters/testing",
        "boost_mpl/1.66.0@bincrafters/testing",
        "boost_optional/1.66.0@bincrafters/testing",
        "boost_parameter/1.66.0@bincrafters/testing",
        "boost_phoenix/1.66.0@bincrafters/testing",
        "boost_predef/1.66.0@bincrafters/testing",
        "boost_preprocessor/1.66.0@bincrafters/testing",
        "boost_property_tree/1.66.0@bincrafters/testing",
        "boost_proto/1.66.0@bincrafters/testing",
        "boost_range/1.66.0@bincrafters/testing",
        "boost_regex/1.66.0@bincrafters/testing",
        "boost_smart_ptr/1.66.0@bincrafters/testing",
        "boost_spirit/1.66.0@bincrafters/testing",
        "boost_static_assert/1.66.0@bincrafters/testing",
        "boost_system/1.66.0@bincrafters/testing",
        "boost_thread/1.66.0@bincrafters/testing",
        "boost_throw_exception/1.66.0@bincrafters/testing",
        "boost_type_index/1.66.0@bincrafters/testing",
        "boost_type_traits/1.66.0@bincrafters/testing",
        "boost_utility/1.66.0@bincrafters/testing",
        "boost_winapi/1.66.0@bincrafters/testing",
        "boost_xpressive/1.66.0@bincrafters/testing"
    )


    def package_info_additional(self):
        if self.options.shared:
            self.cpp_info.defines.append("BOOST_LOG_DYN_LINK=1")
            self.cpp_info.defines.append("BOOST_LOG_SETUP_DYN_LINK=1")
        try:
            if not self.settings.threads:
                self.cpp_info.defines.append("BOOST_LOG_NO_THREADS=1")
        except:
            pass

    def package_id_additional(self):
        boost_deps_only = [dep_name for dep_name in self.info.requires.pkg_names if dep_name.startswith("boost_")]

        for dep_name in boost_deps_only:
            self.info.requires[dep_name].full_version_mode()

    # BEGIN

    description = "Please visit http://www.boost.org/doc/libs/1_66_0"
    license = "BSL-1.0"
    short_paths = True
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    build_requires = "boost_generator/1.66.0@bincrafters/testing"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()

    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()

    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()



    # END
