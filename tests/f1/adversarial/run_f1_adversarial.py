import importlib.util
import json
import pathlib
import sys
import unittest

test_path = pathlib.Path(sys.argv[1]).resolve()

spec = importlib.util.spec_from_file_location(
    "f1_adversarial_tests",
    test_path,
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

suite = unittest.defaultTestLoader.loadTestsFromModule(module)

result = unittest.TextTestRunner(
    verbosity=2,
    stream=sys.stderr,
).run(suite)

payload = {
    "testsRun": result.testsRun,
    "failures": len(result.failures),
    "errors": len(result.errors),
    "skipped": len(result.skipped),
    "expectedFailures": len(result.expectedFailures),
    "unexpectedSuccesses": len(result.unexpectedSuccesses),
    "successful": result.wasSuccessful(),
}

print(json.dumps(payload, sort_keys=True))

sys.exit(0 if result.wasSuccessful() else 1)
