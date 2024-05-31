from os import path, getcwd
from shutil import copytree
from click import command, argument, echo


@command()
@argument('project_name')
def create_python_template(project_name):
    """
    generate a python project template folder.

    Args:
    - project_name (str): The name of the new project.
    """
    template_path = 'C:/ProjectTemplates/templates/python-template'
    project_path = path.join(getcwd(), project_name)
    copytree(template_path, project_path)
    echo(f"Created project '{project_name}' in '{project_path}'")

@command()
@argument('project_name')
def create_notebook_template(project_name):
    """
    generate a python notebook project template folder.

    Args:
    - project_name (str): The name of the new project.
    """
    template_path = 'C:/ProjectTemplates/templates/notebook-template'
    project_path = path.join(getcwd(), project_name)
    copytree(template_path, project_path)
    echo(f"Created project '{project_name}' in '{project_path}'")

if __name__ == "__main__":
    create_python_template()
