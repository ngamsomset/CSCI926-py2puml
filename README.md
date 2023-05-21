# Test cases generating by Pynguin for Py2puml

Pynguin is an automated testing tool that our group selected to generate test cases for Py2puml. We used Pytest as the test runner for all the test cases generated by Pynguin.

## Installation

To install Pynguin, use the package manager [pip](https://pip.pypa.io/en/stable/) You can find Pynguin on [Github ](https://github.com/se2p/pynguin).

```bash
pip install pynguin
```

You can also install Pytest using the package manager. Pytest can be found on [GitHub](https://github.com/pytest-dev/pytest).


```bash
pip install pytest
```
Additionally, install Pytest-html to create the test report.
```bash
pip install pytest-html
```

## Usage

After installing Pynguin and Pytest, move the Py2puml package file to the root directory. This is necessary due to limitations in Pynguin's execution.

Next, use Pynguin to generate test cases for each Python file.
```bash
pynguin --project-path <rootfolder of project(Py2puml)> --output-path <outputdirectory> --module-name <targetpythonfile> --max-sequence-length <int of sequence> --algorithm <Select Algorithm> --maximum_iteration <int of Iteration> --maximum_slicing_time <maxtimeout>
```
The test cases will be generated by Pynguin. Once you have gathered all the test cases, use Pytest to execute them.

```bash
pytest --html=<reportname>.html
```
Run the above command in the root directory of the project to execute all the test cases in the directory and generate a report that provides information on the execution of each test case. The report will also explain why certain test cases are expected to fail.
## References

[Pytest](https://github.com/pytest-dev/pytest), 
[Py2puml](https://github.com/lucsorel/py2puml),
[Pynguin](https://github.com/se2p/pynguin)