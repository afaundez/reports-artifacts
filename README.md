# Report Example

This repository contains a simple example of a report which can be use with the report argo workflow.

The report consists of:

- an [loop items file](report.loop.json)
- a [notebook](report.ipynb)
- an HTML report template:
    - an [Jinja2 template](report.template.html)
    - a [variables file](report.template.yml)

## Loop items file

A JSON file with an array if hashes. Each hash represent an instace of the report, and the values will be use to configure the notebook. This file will be use with an [Argo Workflow loop](https://argoproj.github.io/argo-workflows/examples/#loops).

Default name: `report.loop.json`

## Notebook

A regular notebook that must generate a variables file `report.variables.json` based on the variables file [report.template.yml](report.template.yml). This variables will be use to render the HTML version of the report report.

The notebook will receive arguments through enviroment variables, that will usually come from the loop items file.

THe notebook will be executed using [nbconvert](https://nbconvert.readthedocs.io/en/latest/usage.html).

Default name: `report.ipynb`

## HTML report template

The following files will be used using  the [Jinja2 CLI](https://github.com/mattrobenolt/jinja2-cli).

### Jinja2 template

An [HTML template](https://github.com/mattrobenolt/jinja2-cli#usage) that uses the notebook's output as variables. Every asset needed by the template must be in the same folder as the template: in this example the folder `assets` containes the CSS file, fonts and images.

The CSS used must ensure that the HTML is printable in a paged PDF document.

Default name: `report.template.html`

### Variables file

A YAML file template that will be used as reference of all the variables needed in the template, all set to `null` or default values.

The noteebook will read this file and output a JSON file with all the varables set to something different than `null`.

Default name: `report.template.yml`
