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

