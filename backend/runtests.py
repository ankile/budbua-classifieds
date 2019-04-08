import pytest
import django
django.setup()

failures = pytest.main(["--cov"])

