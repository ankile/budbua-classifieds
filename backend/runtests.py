import pytest
import django
django.setup()

failures = pytest.main(["--cov"])

if failures:
    sys.exit(failures)