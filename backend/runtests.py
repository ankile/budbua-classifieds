import pytest
failures = pytest.main(["--cov"])

if failures:
    sys.exit(failures)