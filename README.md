# redsun-plugin-template

[Copier](https://copier.readthedocs.io/en/stable/) template for authoring RedSun plugins.

> [!CAUTION]
> This template is still a work in progress. You should not use this until author removes this notice.

**NOTE: This repo is not meant to be cloned/forked directly! Please read "Getting Started" below**

## Getting Started

### Create your plugin package

For a safe usage of the template, it is reccomended to create a new environment before generating it:

<details>
<summary>conda</summary>

```bash
conda create -n redsun-template python=3.10
conda activate redsun-template
```

</details> 
<details>
<summary>mamba</strong></summary>

```bash
mamba create -n redsun-template python=3.10
mamba activate redsun-template
```
</details>

After creating the environment, install the requirements listed in `requirements.txt`:

```bash
python -m pip install copier copier-templates-extensions jinja2-time pytest pytest-copie
```

Then you can generate a new RedSun plugin project:

```bash
copier copy --trust https://github.com/redsun-acquisition/redsun-plugin-template my-redsun-plugin
```

Copier prompts you for information regarding your plugin. See [prompts reference](./PROMPTS.md) for a detailed description.

### Initialize a git repository in your package

NOTE: This is important not only for version management, but also if you want to
pip install your package locally for testing with `pip install -e .` (because
the version of your package is managed using git tags,
[see below](#automatic-deployment-and-version-management))

```bash
cd my-redsun-plugin
git init
git add .
git commit -m 'initial commit'
```

### Upload it to github

1. Create a [new github repository]

2. Add your newly created github repo as a remote and push:

   ```bash
   # here, continuing with the example above...
   # but replace with your own username and repo name

   git remote add origin https://github.com/yourgitusername/my-redsun-plugin.git
   git push -u origin main
   ```

### Monitor testing and coverage

The repository should already be setup to run your tests each time you push an
update (configuration is in `.github/workflows/test_and_deploy.yml`). You can
monitor them in the "Actions" tab of your github repository. If you're
following along, go have a look... they should be running right now!

Currently, the timeout for these runs is set to 30 minutes to save resources. You can modify the settings if necessary. Here you can find information on [GitHub workflows](https://docs.github.com/en/actions/learn-github-actions) and the [timeout parameter](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idtimeout-minutes).

When the tests are done, test coverage will be viewable at
[codecov.io](https://codecov.io/) (assuming your repository is public):
`https://codecov.io/gh/<your-github-username>/<your-package-name>`

You will need to enable the [codecov](https://github.com/apps/codecov) github app
for this to work. See [here](https://github.com/apps/codecov/installations/new)
to install the codecov github app and give it access to your RedSun plugin repository.

### Set up automatic deployments

Your new package is also nearly ready to automatically deploy to [PyPI]
(whenever you create a tagged release), so that your users can simply `pip install` your package. You just need to create an [API token to authenticate
with PyPi](https://pypi.org/help/#apitoken), and then add it to your github
repository:

1. If you don't already have one, [create an
   account](https://pypi.org/account/register/) at [PyPI]
2. Verify your email address with PyPI, (if you haven't already)
3. Generate an [API token](https://pypi.org/help/#apitoken) at PyPi: In your
   [account settings](https://pypi.org/manage/account/) go to the API tokens
   section and select "Add API token". Make sure to copy it somewhere safe!
4. [Create a new encrypted
   secret](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#creating-encrypted-secrets)"
   in your github repository with the name "TWINE_API_KEY", and paste in your
   API token.

You are now setup for automatic deployment!

### Automatic deployment and version management

Each time you want to deploy a new version, you just need to create a tagged
commit, and push it to your main branch on github. Your package is set up to
use [setuptools_scm](https://github.com/pypa/setuptools_scm) for version
management, meaning you don't need to hard-code your version anywhere in your
package. It will be inferred from the tag each time you release.

```bash
# the tag will be used as the version string for your package
# make it meaningful: https://semver.org/
git tag -a v0.1.0 -m "v0.1.0"

# make sure to use follow-tags so that the tag also gets pushed to github
git push --follow-tags
```

> Note: as of git 2.4.1, you can set `follow-tags` as default with
> `git config --global push.followTags true`

Monitor the "actions" tab on your github repo for progress... and when the
"deploy" step is finished, your new version should be visible on pypi:

`https://pypi.org/project/<your-package-name>/`

and available for pip install with:

```bash
# for example
pip install my-redsun-plugin
```

### Running tests locally

Tests are automatically setup to run on github when you push to your repository.

You can run your tests locally with [pytest](https://docs.pytest.org/en/stable/).
You'll need to make sure that your package is installed in your environment,
along with testing requirements (specified in the setup.cfg `extras_require` section):

```bash
pip install -e ".[testing]"
pytest
```

### Create your documentation

Documentation generation is not included in this template.
We recommend following the getting started guides for one of the following documentation generation tools:

1. [Sphinx]
2. [MkDocs]
3. [JupyterBook]

Alternatively, you can also create your documentation on GitHub using [Wikis]

### Pre-commit

This template includes a default yaml configuration for [pre-commit](https://pre-commit.com/).
Among other things, it includes checks for best practices in RedSun plugins.
You may edit the config at `.pre-commit-config.yaml`

To use it run:

```bash
pip install pre-commit
pre-commit install
```

You can also have these checks run automatically for you when you push to github
by installing [pre-commit ci](https://pre-commit.ci/) on your repository.

## Dependabot

This template also includes a default yaml configuration for [Dependabot](https://docs.github.com/en/code-security/dependabot). This can help you check for security updates to easily update vulnerable dependencies.

You will still need to enable Dependabot in your github settings, [see the instructions at this link](https://docs.github.com/en/code-security/dependabot/dependabot-security-updates/configuring-dependabot-security-updates#managing-dependabot-security-updates-for-your-repositories). Your Dependabot configuration file is located at `.github/dependabot.yml`.

## Features

- Installable [PyPI] package
- [nox] test suite, testing various python versions and platforms.
- `README.md` file that contains useful information about your plugin
- Continuous integration configuration for [github actions] that handles testing
  and deployment of tagged releases
- Choose from several licenses, including [BSD-3], [MIT], [MPL v2.0], [Apache
  v2.0], [GNU GPL v3.0], or [GNU LGPL v3.0]

## Resources

Details on why this plugin template is using the `src` layout can be found [here](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure) and [here](https://hynek.me/articles/testing-packaging/).

## License

Distributed under the terms of the [BSD-3] license, `redsun-plugin-template`
is free and open source software.

[copier]: https://github.com/copier-org/copier
[pypi]: https://pypi.org/
[nox]: https://nox.thea.codes/en/stable/
[file an issue]: https://github.com/redsun-acquisition/redsun-plugin-template/issues
[sphinx]: https://www.sphinx-doc.org/en/master/usage/quickstart.html
[mkdocs]: https://www.mkdocs.org/getting-started/
[jupyterbook]: https://jupyterbook.org/en/stable/start/your-first-book.html
[wikis]: https://docs.github.com/en/communities/documenting-your-project-with-wikis
[mit]: http://opensource.org/licenses/MIT
[mpl v2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[bsd-3]: http://opensource.org/licenses/BSD-3-Clause
[gnu gpl v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[gnu lgpl v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[apache v2.0]: http://www.apache.org/licenses/LICENSE-2.0
[travis ci]: https://travis-ci.com/
[appveyor]: http://www.appveyor.com/
[pypa code of conduct]: https://www.pypa.io/en/latest/code-of-conduct/
[osi_certified]: https://opensource.org/trademarks/osi-certified/web/osi-certified-120x100.png
[osi]: https://opensource.org/
[github actions]: https://github.com/features/actions
[new github repository]: https://help.github.com/en/github/getting-started-with-github/create-a-repo
