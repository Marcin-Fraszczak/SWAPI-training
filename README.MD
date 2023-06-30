# SWAPI - training app for django and API

App available at:

https://marcinfraszczak2.eu.pythonanywhere.com/

Main focus on working with API and data processing using pandas library.

Some additional JS features for displaying data.

Write to and read from CSV files.

Metadata written to MySQL database.

Bash script for config, database setup, testing and starting the server (see the bottom of this README)


<header>
    <div class="content">
        <h1>Coverage report:
            <span class="pc_cov">100%</span>
        </h1>
    </div>
    <div>    
        <p class="text">
            <a class="nav" href="https://coverage.readthedocs.io">coverage.py v7.1.0</a>,
            created at 2023-01-31 15:33 +0100
        </p>
    </div>
</header>
<main id="index">
    <table class="index" data-sortable>
        <thead>
            <tr class="tablehead" title="Click to sort">
                <th class="name left" aria-sort="none" data-shortcut="n">Module</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="s">statements</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="m">missing</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="x">excluded</th>
                <th class="right" aria-sort="none" data-shortcut="c">coverage</th>
            </tr>
        </thead>
        <tbody>
            <tr class="file">
                <td class="name left"><a href="d_509fd8af0f7a1b49_admin_py.html">accounts/admin.py</a></td>
                <td>3</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="3 3">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_509fd8af0f7a1b49_apps_py.html">accounts/apps.py</a></td>
                <td>4</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="4 4">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_509fd8af0f7a1b49_forms_py.html">accounts/forms.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_509fd8af0f7a1b49_models_py.html">accounts/models.py</a></td>
                <td>4</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="4 4">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_509fd8af0f7a1b49_views_py.html">accounts/views.py</a></td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="0 0">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_9df13ddeb1e47e46_admin_py.html">pages/admin.py</a></td>
                <td>3</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="3 3">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_9df13ddeb1e47e46_apps_py.html">pages/apps.py</a></td>
                <td>4</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="4 4">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_9df13ddeb1e47e46_functions_py.html">pages/functions.py</a></td>
                <td>71</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="71 71">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_9df13ddeb1e47e46_models_py.html">pages/models.py</a></td>
                <td>10</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="10 10">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_9df13ddeb1e47e46_urls_py.html">pages/urls.py</a></td>
                <td>4</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="4 4">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="d_9df13ddeb1e47e46_views_py.html">pages/views.py</a></td>
                <td>35</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="35 35">100%</td>
            </tr>
        </tbody>
        <tfoot>
            <tr class="total">
                <td class="name left">Total</td>
                <td>138</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="138 138">100%</td>
            </tr>
        </tfoot>
    </table>
    <p id="no_rows">
        No items found using the specified filter.
    </p>
</main>
<footer>
    <div class="content">
        <p>
            <a class="nav" href="https://coverage.readthedocs.io">coverage.py v7.1.0</a>,
            created at 2023-01-31 15:33 +0100
        </p>
    </div>
</footer>


# How to run it locally:

1. Clone the repository to your local machine, for example:
   `git clone https://github.com/Marcin-Fraszczak/SWAPI-training.git`
2. Inside the project folder, create and activate virtual environment, for example for virtualenv:

`python -m venv venv`

and then

`source venv/bin/activate`

3. In the main project folder (where manage.py is located), with virtual environment activated, use command:

`bash start.sh`

That will run the script, which does the following:

- installs required packages
- prepares and runs migrations (database file is created in main directory)
- flushes the database, in case script is run for the second time
- runs django development server, by default at http://127.0.0.1:8000/
- creates directories for storing csv files
- tests code with pytest
- saves all the above info to `log.txt` file in the main directory

[//]: # (- populates the database with starting data:)

[//]: # (    - one user)

[//]: # (    - one superuser)

[//]: # (    - couple of instances of all the necessary models)

### In case you run this script multiple times without killing the previous process, you'll get `port already in use` message

One easy way to free this port is:

`sudo lsof -t -i:8000`

or any other port number. This will output ID of the process that is running on this port,

for example `21987`, then

`sudo kill 21987`
