from grader import *

@test_cases(['HELLO WORLD', 'HELLO NACHALNIK'], description='Searching for word {0}')
def test_printed_wanted_str(m, wanted_str):
    output = m.stdout.new()
    assert wanted_str in output, '{0} not in {1}'.format(wanted_str, output)