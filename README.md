Snippets for Python projects using Anaconda and Jupyter Notebook. All files and folders are merely illustrative

## Anaconda

- To export a conda environment:

		$ conda env export | grep -v "^prefix" > environment.yml

- To create a new conda environment with some libraries very fast:

		$ conda create --name <env_name> python=3 lib1 lib2 lib3

- To create a conda environment from YAML file:

		$ conda env create	# if you have a environment.yml in the directory
		$ conda env create --file <env_name>.yml

- To ensure you are running pip/python in the right conda environment:

		$ which pip	# or
		$ which python
		$ # should return something like "/.../miniconda3/envs/scitemplate/bin/pip"

## Package setup

- To install the package in development mode:

		$ pip install -e .

- To install the package in user mode:

		$ pip install .

    The . here refers to the current working directory, which is assumed to be the directory where the setup.py can be found.

## Jupyter

- Install: ```pip install notebook```
- Install nbextensions: ```pip install jupyter_contrib_nbextensions```
- Magic commands: ```!```
- Shell commands: ```%``` 
- List all available magic commands: ```%lsmagic```
- To load python code snippets inside the notebook: ```!load snippets/snippet.py```
- Interactive mode: blue ("vim" alike). Typing mode: green.
- Navigate using j/k (up/down), x (delete cell), a (insert cell above), b (insert cell below) etc
