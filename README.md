# scitemplate
Simple template for scientific Python projects.

## Conda shell snippets

- To export a conda environment:

	$ conda env export | grep -v "^prefix" > environment.yml

- To create a new conda environment with some libraries very fast:

	$ conda create --name <env_name> python=3 lib1 lib2 lib3

- To create a conda environment from YAML file:

	$ conda env create	# if you have a environment.yml in the directory
	$ conda env create --file <env_name>.yml

- To ensure you are installing stuff in the right conda environment:

	$ which pip	# or
	$ which python
	$ # should return something like "/.../miniconda3/envs/scitemplate/bin/pip"

## Setup shell snippets

- To install the package in development mode:

	$ pip install -e <project directory>

- To install the package in user mode:

	$ pip install <project directory>
