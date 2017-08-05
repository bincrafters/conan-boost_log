from conans import ConanFile, tools, os

class BoostLogConan(ConanFile):
    name = "Boost.Log"
    version = "1.64.0"
    generators = "txt" 
    settings = "os", "arch", "compiler", "build_type"
    url = "https://github.com/boostorg/log"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "log"
    build_requires = "Boost.Build/1.64.0@bincrafters/testing" 
    requires =  "Boost.Array/1.64.0@bincrafters/testing", \
                      "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Atomic/1.64.0@bincrafters/testing", \
                      "Boost.Bind/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Date_Time/1.64.0@bincrafters/testing", \
                      "Boost.Exception/1.64.0@bincrafters/testing", \
                      "Boost.Filesystem/1.64.0@bincrafters/testing", \
                      "Boost.Function_Types/1.64.0@bincrafters/testing", \
                      "Boost.Fusion/1.64.0@bincrafters/testing", \
                      "Boost.Intrusive/1.64.0@bincrafters/testing", \
                      "Boost.Iterator/1.64.0@bincrafters/testing", \
                      "Boost.Lexical_Cast/1.64.0@bincrafters/testing", \
                      "Boost.Locale/1.64.0@bincrafters/testing", \
                      "Boost.Move/1.64.0@bincrafters/testing", \
                      "Boost.Mpl/1.64.0@bincrafters/testing", \
                      "Boost.Optional/1.64.0@bincrafters/testing", \
                      "Boost.Parameter/1.64.0@bincrafters/testing", \
                      "Boost.Phoenix/1.64.0@bincrafters/testing", \
                      "Boost.Predef/1.64.0@bincrafters/testing", \
                      "Boost.Preprocessor/1.64.0@bincrafters/testing", \
                      "Boost.Property_Tree/1.64.0@bincrafters/testing", \
                      "Boost.Proto/1.64.0@bincrafters/testing", \
                      "Boost.Range/1.64.0@bincrafters/testing", \
                      "Boost.Regex/1.64.0@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.64.0@bincrafters/testing", \
                      "Boost.Spirit/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.System/1.64.0@bincrafters/testing", \
                      "Boost.Thread/1.64.0@bincrafters/testing", \
                      "Boost.Throw_Exception/1.64.0@bincrafters/testing", \
                      "Boost.Type_Index/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing", \
                      "Boost.Utility/1.64.0@bincrafters/testing", \
                      "Boost.Winapi/1.64.0@bincrafters/testing", \
                      "Boost.Xpressive/1.64.0@bincrafters/testing"

                      #array3 assert1 atomic4 bind3 config0 core2 date_time11 exception5 filesystem8 function_types5 fusion5 intrusive6 iterator5 lexical_cast8 locale6 move3 mpl5 optional5 parameter10 phoenix9 predef0 preprocessor0 property_tree13 proto8 range7 regex6 smart_ptr4 spirit11 static_assert1 system3 thread11 throw_exception2 type_index5 type_traits3 utility5 winapi1 xpressive9
                      
    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="include", src=include_dir)

