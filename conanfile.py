from conans import ConanFile


class BoostLogConan(ConanFile):
    name = "Boost.Log"
    version = "1.66.0"

    options = {"shared": [True, False]}
    default_options = "shared=False"

    requires = \
        "Boost.Align/1.66.0@bincrafters/testing", \
        "Boost.Array/1.66.0@bincrafters/testing", \
        "Boost.Asio/1.66.0@bincrafters/testing", \
        "Boost.Assert/1.66.0@bincrafters/testing", \
        "Boost.Atomic/1.66.0@bincrafters/testing", \
        "Boost.Bind/1.66.0@bincrafters/testing", \
        "Boost.Config/1.66.0@bincrafters/testing", \
        "Boost.Core/1.66.0@bincrafters/testing", \
        "Boost.Date_Time/1.66.0@bincrafters/testing", \
        "Boost.Exception/1.66.0@bincrafters/testing", \
        "Boost.Filesystem/1.66.0@bincrafters/testing", \
        "Boost.Function_Types/1.66.0@bincrafters/testing", \
        "Boost.Fusion/1.66.0@bincrafters/testing", \
        "Boost.Interprocess/1.66.0@bincrafters/testing", \
        "Boost.Intrusive/1.66.0@bincrafters/testing", \
        "Boost.Iterator/1.66.0@bincrafters/testing", \
        "Boost.Lexical_Cast/1.66.0@bincrafters/testing", \
        "Boost.Locale/1.66.0@bincrafters/testing", \
        "Boost.Move/1.66.0@bincrafters/testing", \
        "Boost.Mpl/1.66.0@bincrafters/testing", \
        "Boost.Optional/1.66.0@bincrafters/testing", \
        "Boost.Parameter/1.66.0@bincrafters/testing", \
        "Boost.Phoenix/1.66.0@bincrafters/testing", \
        "Boost.Predef/1.66.0@bincrafters/testing", \
        "Boost.Preprocessor/1.66.0@bincrafters/testing", \
        "Boost.Property_Tree/1.66.0@bincrafters/testing", \
        "Boost.Proto/1.66.0@bincrafters/testing", \
        "Boost.Range/1.66.0@bincrafters/testing", \
        "Boost.Regex/1.66.0@bincrafters/testing", \
        "Boost.Smart_Ptr/1.66.0@bincrafters/testing", \
        "Boost.Spirit/1.66.0@bincrafters/testing", \
        "Boost.Static_Assert/1.66.0@bincrafters/testing", \
        "Boost.System/1.66.0@bincrafters/testing", \
        "Boost.Thread/1.66.0@bincrafters/testing", \
        "Boost.Throw_Exception/1.66.0@bincrafters/testing", \
        "Boost.Type_Index/1.66.0@bincrafters/testing", \
        "Boost.Type_Traits/1.66.0@bincrafters/testing", \
        "Boost.Utility/1.66.0@bincrafters/testing", \
        "Boost.Winapi/1.66.0@bincrafters/testing", \
        "Boost.Xpressive/1.66.0@bincrafters/testing"

    lib_short_names = ["log"]
    is_header_only = False

    def package_info_after(self):
        if self.options.shared:
            self.cpp_info.defines.append("BOOST_LOG_DYN_LINK=1")
            self.cpp_info.defines.append("BOOST_LOG_SETUP_DYN_LINK=1")
        try:
            if not self.settings.threads:
                self.cpp_info.defines.append("BOOST_LOG_NO_THREADS=1")
        except:
            pass

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost-log"
    description = "Please visit http://www.boost.org/doc/libs/1_66_0"
    license = "www.boost.org/users/license.html"
    build_requires = "Boost.Generator/1.66.0@bincrafters/testing"
    short_paths = True
    generators = "boost"
    settings = "os", "arch", "compiler", "build_type"
    exports = "boostgenerator.py"

    def package_id(self):
        getattr(self, "package_id_after", lambda:None)()
    def source(self):
        self.call_patch("source")
    def build(self):
        self.call_patch("build")
    def package(self):
        self.call_patch("package")
    def package_info(self):
        self.call_patch("package_info")
    def call_patch(self, method, *args):
        if not hasattr(self, '__boost_conan_file__'):
            try:
                from conans import tools
                with tools.pythonpath(self):
                    import boostgenerator  # pylint: disable=F0401
                    boostgenerator.BoostConanFile(self)
            except Exception as e:
                self.output.error("Failed to import boostgenerator for: "+str(self)+" @ "+method.upper())
                raise e
        return getattr(self, method, lambda:None)(*args)
    @property
    def env(self):
        import os.path
        result = super(self.__class__, self).env
        result['PYTHONPATH'] = [os.path.dirname(__file__)] + result.get('PYTHONPATH',[])
        return result
    @property
    def build_policy_missing(self):
        return (getattr(self, 'is_in_cycle_group', False) and not getattr(self, 'is_header_only', True)) or super(self.__class__, self).build_policy_missing

    # END
