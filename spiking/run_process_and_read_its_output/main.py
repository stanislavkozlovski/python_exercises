import subprocess


def convert_to_normal_text(lines: list):
    """ Given a list with byte strings with a new-line at the end, return a concatenated string """
    return ''.join([st.decode('utf-8') for st in lines])

proc: subprocess.CompletedProcess = subprocess.Popen(['sudo', 'python3', '-m', 'grader', '--sandbox', 'docker', 'tester.py', 'test_script.py'], stdout=subprocess.PIPE)
output = proc.stdout.readlines()
print(convert_to_normal_text(output))
