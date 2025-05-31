from packaging import version
import pandas as pd

MIN_VERSION = "1.5.0"

def test_pandas_version():
    assert version.parse(pd.__version__) >= version.parse(MIN_VERSION)

if __name__ == "__main__":
    test_pandas_version()
    print("Pandas version is correct!")
