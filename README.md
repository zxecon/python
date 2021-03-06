## Python/Jupyter

>Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython 2nd Edition

>Visual Studio Code w/ Jupyter Environment

* ### July 2019 Updates: Jupyter Not Working through Anaconda Under Mac OS Catalina Beta Version:

If you are using Mac OS Catalina Beta Version released in June 2019, you might probably have difficulty in opening Anaconda, which appeared as follows under beta system:

![conda](https://github.com/zxecon/python/blob/master/conda.png)

Following is a way that I used to solve this issue (if you installed the Mac OS beta version on all of your PCs like me and still need to learn/use):

In Terminal, install Jupyter with pip; then open Jupyter notebook through Terminal/ working under vscode with respect interpreter

```
pip3 install jupyter
jupyter notebook
```
It will promote to Jupyter Notebook in your web browser.

VS code can also be used after select repected interpreter and you can begin using #%% comment as following:

![vsjupyter](https://github.com/zxecon/python/blob/master/vsjupyter.png)

References: [Install Jupyter](https://jupyter.org/install); [Working with Jupyter Notebooks in Visual Studio Code](https://code.visualstudio.com/docs/python/jupyter-support)
