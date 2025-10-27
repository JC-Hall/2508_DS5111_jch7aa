import sys
import platform
sys.path.append('.')


import bin.normalize as nm
from bin.yahoo import Gaineryahoo
from bin.wsj import Gainerwsj

def test_normalize_yahoo():
    g = Gaineryahoo()
    g.normalize_data(filepath='ygainers.csv')
    assert os.path.exists('normalized_yahoo.csv'), "Yahoo normalized file missing"

    df = pd.read_csv('normalized_yahoo.csv')
    expected_cols = ['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']
    for col in expected_cols:
        assert col in df.columns, f"Column {col} missing in Yahoo output"
    assert not df.empty, "Yahoo normalized file is empty"

def test_normalize_wsj():
    g = Gainerwsj()
    g.normalize_data(filepath='wsjgainers.csv')
    assert os.path.exists('normalized_wsj.csv'), "WSJ normalized file missing"

    df = pd.read_csv('normalized_wsj.csv')
    expected_cols = ['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']
    for col in expected_cols:
        assert col in df.columns, f"Column {col} missing in WSJ output"
    assert not df.empty, "WSJ normalized file is empty"

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
