#!/usr/bin/python3

import sys
import shutil
import subprocess
import distutils.util

# Default options
BuildType = "Release"
Doxygen   = False
UnitTest  = False
UseCache  = True
UseNinja  = True

# Parse arguments
for arg in sys.argv[1:]:
    opt = arg.split("=")
    if len(opt) < 2:
        continue
    if opt[0] == "BuildType":
        BuildType = opt[1]
    if opt[0] == "Doxygen":
        Doxygen   = bool(distutils.util.strtobool(opt[1]))
    if opt[0] == "UnitTest":
        UnitTest  = bool(distutils.util.strtobool(opt[1]))
    if opt[0] == "UseCache":
        UseCache  = bool(distutils.util.strtobool(opt[1]))
    if opt[0] == "UseNinja":
        UseNinja  = bool(distutils.util.strtobool(opt[1]))

# Choose build system
if UseNinja and shutil.which("ninja"):
    BuildSystem = "ninja"
    Generator   = "Ninja"
else:
    BuildSystem = "make"
    Generator   = "Unix Makefiles"
BuildDir = "build/" + BuildSystem + "/" + BuildType
CacheBin = "ccache"

# Make commands
conf = [
    "cmake", ".",
    "-B", BuildDir, "-G", Generator,
    "-DCMAKE_BUILD_TYPE=" + BuildType
]
make = [
    BuildSystem,
    "-C", BuildDir
]
docs = {
    "doxygen"
}
test = [
    "ctest",
    "--test-dir", BuildDir
]
if UseCache and shutil.which(CacheBin):
    conf += [
        "-DCMAKE_C_COMPILER_LAUNCHER="   + CacheBin,
        "-DCMAKE_CXX_COMPILER_LAUNCHER=" + CacheBin
    ]
if UnitTest:
    conf.append("-DUNIT_TEST=1")
else:
    conf.append("-DUNIT_TEST=0")

# Execute
subprocess.run(conf)
subprocess.run(make)
if Doxygen:
    subprocess.run(docs)
if UnitTest:
    subprocess.run(test)
