# Python Club

Sample repo for Python Club's developer tools lesson.

## Topics

- Git workflows
- Documentation (READMEs, requirements.txt, comments)
- Unit testing
- Some fun

## Git
Git is how we manage versions of our files. The Git program looks at your filesystem where you have Git repositories and watches for changes and tracks those changes line by line. We can then **commit** those changes and **push** to the repository so that others can see them and **pull** those changes to their own machines.

We can pull others' changes using:

`git fetch` - Just checks if there are any changes from others on the repository

`git pull` - Pulls changes on your current branch

We can commit and push our code using the following commands: 

`git commit -m "<commit_message>"`

`git push`

We can create a new branch and commit to it using:

`git branch <branch_name>`

`git checkout <branch_name>` Switch to a branch with checkout

You can also do all of these commands using the Sourcetree interface instead, where you can visually see your commits and branches, track changes, and more. 


## Documentation

### README files
You're reading one part of the documentation, the README. A `README.md` file is the first thing people see when they look at your project. It's written in the [Markdown](https://www.markdownguide.org/basic-syntax/) language, which lets your format plain text in a really simple, portable way. You can see how *different* **annotations** ***change*** the _format_ of the document.

### Comments, Docstrings, and Type Hints

Developers comment code to help people understand the intention, nuance, and details of what is written. We can comment in code using the hash/pound/octothorpe `#` or with a docstring, a string linked to a function that documents its inputs and outputs. 

> Comments should be informative but not redundant. This, for example, is a bad comment:
> ```python
> def is_even(n: int) -> bool:
>     # Return true if the number is divisible by 2, otherwise return false
>     return n % 2 == 0
> ```
> This comment doesn't give us any more information about what's happening or why this function is written the way it is. It's the equivalent of writing "Cat" on a photo of a cat. 


You can see in the function above that the input argument `n` is accompanied with the `: int` label. This is called a "type hint", and we use this to self-document our code. It tells the interpreter and your IDE that this function expects a certain input *type* for this argument. If you call that function with the wrong type, your IDE should highlight it for you before it runs and hits an error.  

### Requirements
Requirements are documentation too! We always want to keep track of which packages we use at which version so that others can pick up a project. The standard way to document that is in a text file called `requirements.txt`. We can install from a `requirements.txt` file using:

`pip install -r requirements.txt`

When creating a requirements.txt file, **always** use a virtual environment. We don't want to export your global packages; we just want what's in a project. We can export our current requirements with:

`pip freeze > requirements.txt`

## Unit Testing
Unit testing is one way we can ensure our code works as we expect. A unit test is designed to test the smallest pieces of your code (usually a single function) to make sure everything works individually. We can run tests to make sure everything passes before deploying, giving us more confidence that things are going to work for users. 

Tests for this project are in `test.py`, which we can run with:

`python -m unittest`

## Streamlit
I've included a quick demo of [Streamlit](https://streamlit.io/), a great library that I've used to create and deploy user interfaces for Python code. You can try it out by running:

`streamlit run app.py`

Take a look at that file to see what's going on under the hood, and check out Streamlit's site to see what's possible.