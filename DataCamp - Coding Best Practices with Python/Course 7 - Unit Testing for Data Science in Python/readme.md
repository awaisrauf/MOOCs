# Unit Testing for Data Science in Python

certificate [Link](https://www.datacamp.com/statement-of-accomplishment/course/dd980ac9a3d4cb3961f388539a6dab23c74cb634)

## Useful Concepts

### Beginning with Unit Testing 

- Units tests can make the manual-console-level testing easy and flexible.

- `pytest` is simple python library for unit-testing. All files containing tests should start with test i.e..  `test_file_name.py`. Example:

  ```python
  import pytest
  from square import square 
  
  def test_square():
      assert square(2) == 4
      assert square(h) == None
  ```

  To run the test:

  ```bash
  cd tests
  pytest
  ```

- Test of float can cause errors because of approximation so use `pytest.approx(float_num)`

- To add message in assert statement: 
  ```python
  message = "Exected value x, real y"
  assert function(args)==expected, message
  ```
  
- Use context manager to test raising error behavior:

  ```python
  def raise_error():
      raise("ValueError")
  
  def test_check_error():
      with pytest.raises(ValueError):
            raise_error()
  ```

- Test cases: bad arguments; special arguments (boundary values and arguments triggering special logic) and normal arguments. 

- Test Driven Development: write tests first and develop later. 

### Organization

- File structure: use a `tests` folder in the top level directory and mirror all the normal folders inside it for testing.

  ![](imgs/1.png)

- Use classes to organize all the tests for a function.

  ```python
  class TestFunctionName(object):
      
      def __init__(self):
          pass
      
      def test_normal_case():
          # test logic
          pass
      
      def test_error_raise():
          # test logic
          pass
  ```

  

### Command Line to Run Tests

- to run all tests
```bash
cd tests
pytest
```
- before pushing, sometimes we only want to know if all test pass oro fail. In this case, it is better to stop if any test fails. To test this, we use
```bash
pytest -x
```
- to run one test class
```bash
pytest folder::test_file_name.py::TestClassName
```
- to test one test function inside the class
```bash
pytest folder/test_file_name.py::TestClassName::test_function_name
```

- to test only phrases that match a specific name
```bash
pytest -k expression-to-match
```

### ### Expected to Fail
- if we expect a test to fail, we can use `@pytest.mark.xfail` as follows;
    ```python
    # whole test class will be skipped
@pytest.mark.xfail
    class TestABC(object):
        pass
    ```
    - to skip a function 

    ```python
    class TestABC(object):
        
        def __init__(self):
            pass
        
        @pytest.mark.xfail
        def test_a_function(self):
            pass
    ```
    
- can also add reason for the failure

    ```python
    @pytest.mark.xfail(reason="test has not been implemented yet")
    class TestABC(object):
        pass
    ```
    
- can skip tests conditionally 
```python
    @pytest.mark.xskipif(sys.version > (2, 7))
    def test_function():
        pass
```

- to get only the reason of the test failure 
```bash
pytest -rs models/test_train.py
```

​    

### Continuous Integration of Tests
- To run tests automatically whenever we push into github, use Travis CI

**Step 1: Create a file `.travis.yml` in the root directory and populate it with following:**

![](imgs/2.png)

**Step 2: Install it on Github marketplace**

**Step 3: Open TravisCI dashboard**
- we can also get badge 

### Code Coverage
To enable the code coverage test from CodeCoverage
1. add following in the `.travis.yml` file.
![](imgs/4.png)
2. go to github marketplace and install CodeCoverage
3. Get markdown for the badge

### Workflow

- If tests involves creation of temporary files etc.., use setup -> assert -> teardown like workflow. 

- `pytest` provides `@pytest.fixture` decorator to do this kind of stuff

  ```python
  # fixture function 
  @pytest.fixture
  def clean_data_file():
      # setup
      file_path = "clean_data_file.txt"
      with open(file_path, "w") as f:
          f.write("201\t305671\n7892\t298140\n501\t738293\n")
      yield file_path
      # teardown
      os.remove(file_path)
      
  # pass the fixture function as argument
  def test_on_clean_file(clean_data_file):
      expected = np.array([[201.0, 305671.0],
                           [7892.0, 298140.0],
                           [501.0, 738293.0]])
      # clean_data_file is provided by yield function 
      actual = get_data_as_numpy_array(clean_data_file, 2)
      assert actual == pytest.approx(expected)
  ```

- To make it even better, use pytest's tmdir which creates and deletes temporary directory for temp files 
  setup of `tempdir()`--> setup of file --> test --> tear down file --> teardown of tmpdir 

  ```python
  @pytest.fixture
  def empty_file(tmpdir):
      # file path in tmpdir
      file_path = tmpdir.join("empty.txt")
      open(file_path, "w").close()
      yield file_path
  ```

### Mocking 

- To avoid having errors in dependencies, we can use mock which replaces original functions with mock functions
  ![](imgs/6.png)
- Two helpful librararies: pytest-mock, unittest.mock

### Test for Data Science Models
- Models are hard to test because results are uncertain. One way is to test with a data that we know the result of. 
- For example: to test a linear regression model, use a simple dataset from a linear line i.e. just sample three data points and test model on those points. 

### Test for Plots
- Images are hard to test. One idea is to generate a baseline in the start with all the possible test arguments, look at it and verify and then run tests to see if new images are same. To avoid differences due to different OS, use library `pytest-mpl`.
![](imgs/7.png)

- Coding part
![](imgs/8.png)

pytest baseline image to be in directory called baseline. To generate baseline run following,
```bash
!pytest -k "test_plot_for_linear_data" --mpl-generate-path visulization/baseline
```
To compare and teset with baseline
```bash
pytest -k "test_plot_for_linear_data" --mpl
```