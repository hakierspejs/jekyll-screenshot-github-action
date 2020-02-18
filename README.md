# jekyll-screenshot-github-action

Takes a screenshot of your Jekyll (e.g. Github Pages) website.
The image is then stored under the following path:

    /home/runner/work/_temp/_github_home/screenshot.png
    
The idea behind this action was to avoid hosting the website
when accepting PRs from third parties. Once you have the screenshot,
you can upload it as an artifact, post it online and automatically
comment on the PR or handle it in any other way.

# Example workflow

This workflow stores your screenshot as a build artifact:

    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
        - uses: actions/checkout@master
        - uses: hakierspejs/jekyll-screenshot-github-action@master
        - uses: actions/upload-artifact@v1
          with:
           name: screenshot
           path: /home/runner/work/_temp/_github_home/screenshot.png
