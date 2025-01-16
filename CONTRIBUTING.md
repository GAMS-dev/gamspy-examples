Contributing to GAMSPy-examples
===============================

Pull Requests
-------------
Contributions are made via pull requests. In order to create a pull request 
with your changes, you follow these steps:

- Fork `GAMS-dev/gamspy-examples` repository.
- Make your changes and commit them to the forked repository (`<your_username>/gamspy_examples`).
- Then, create a pull request to the `GAMS-dev/gamspy-examples` repository.

For a pull request to be accepted, it must pass the tests. You can run the tests locally with:

```
python <your_model>.py
```

for Python models and with:

```
pytest --nbmake --nbmake-kernel=python3 notebooks
```

for notebooks.

Contributing a Python model
---------------------------
The example GAMSPy model files are stored under the `models` directory. In order 
to add a new model to this directory, create a new folder with the name of 
your model and add all necessary files under it to run your model. You should also 
update the table in the README.md file which lists all the available models.

Contributing a Notebook
-----------------------
The notebooks are stored under the `notebooks` directory. If you want to contribute 
a notebook, you can just place your notebook under this directory.
