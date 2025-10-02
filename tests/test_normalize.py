import sys
import platform
sys.path.append('.')


import bin.normalize as nm

def test_normalize():
    assert True

def test_python_version():
    print(f"Python version: {sys.version}")
    assert sys.version_info

def test_os():
    print(f"OS platform: {platform.system}")
    assert platform.system()

def test_linux_run():
    """Fail if the OS is not Linux."""
    os = platform.system()
    assert os == "Linux", f"This isnt Linux, this is {os}"

def test_specific_python_v():
    """Fail if Python version is not 3.12 or 3.13."""
    v1, v2 = sys.version_info[:2]
    allowed_v = [(3, 12), (3, 13)]
    assert (v1, v2) in allowed_v
