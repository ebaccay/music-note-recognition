import neural_net as np
import sound_engine as se

sound_engine_test_suite = ("sound_engine.py", [])
neural_net_test_suite = ("neural_net.py", [])


def all_tests():
    """Runs all unit tests."""
    print("Starting all unit tests...\n")
    se_passed, se_total = suite_tester(sound_engine_test_suite)
    nn_passed, nn_total = suite_tester(neural_net_test_suite)
    num_passed = se_passed + nn_passed
    total = se_total + nn_total
    if total == num_passed:
        print("Every test case passed! " + str(total) + " test cases were run.")
    else:
        print(str(num_passed) + " test cases passed out of " + str(total) + " total test cases.")
    return


def suite_tester(suite):
    """Runs tests specified by the input tuple of the test suite name and the functions themselves."""
    name = suite[0]
    tests = suite[1]
    print("Testing " + name + "...\n")
    cases_passed = 0
    total_cases = 0
    failed_cases = []
    for f in tests:
        test_name = f.__name__
        print("Testng " + test_name + "...")
        try:
            f()
            cases_passed += 1
        except AssertionError as err:
            print(err)
            print("Test failed.")
            failed_cases.append(f)
        total_cases += 1
    if cases_passed == total_cases:
        print("All " + str(total_cases) + " test cases passed for " + name + "!\n")
    else:
        print(str(cases_passed) + " test cases passed out of " + str(total_cases) + " for 'sound_engine.py'.\n")
        print("Failed cases:")
        for c in failed_cases:
            print(c.__name__)
        print("")
    return cases_passed, total_cases


def assert_equals(actual, expected):
    """Sets up easy AssertionError throws for easier unit testing."""
    assert actual == expected, "Expected " + str(expected) + " but got " + str(actual) + "."
    return


def se_sound_dictionary():
    ndict, vdict = se.note_dictionary()
    assert_equals(vdict[0], "a_0")
    assert_equals(vdict[39], "c_4")
    assert_equals(vdict[38], "b_3")
    assert_equals(ndict["b_3"], 38)
    assert_equals(ndict["a_0"], 0)
    assert_equals(ndict["c_4"], 39)
    assert_equals(len(ndict), 88)
    assert_equals(len(vdict), 88)

sound_engine_test_suite[1].append(se_sound_dictionary)

if __name__ == "__main__":
    all_tests()
    raise SystemExit
