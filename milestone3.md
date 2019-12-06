# Milestone 3: Maintenance on Project 1 and Starting Project 2

**This week, you will be working on both R and python apps in parallel**.
For the python app, you will be doing maintenance of your app (details below).
For the R app, this week you will setup a new project on GitHub.com, create your plots in ggplot2 and ggplotly, and get started on your dashR framework.

In the DSCI 532 labs, you will work in [randomly assigned groups](https://github.ubc.ca/MDS-2019-20/DSCI_532_viz-2_students/blob/master/release/DSCI_532_groups.md) towards creating two interactive visualization apps using Dash, one in Python (using Altair) and one in R (using ggplot2 and ggplotly).
There are a total of four milestones, two for each dashboard. 
With these labs, we intend for you to practice and understand the mechanics of creating dashboards, deploying them using Heroku, and implementing principles of effective visualizations (and dashboards) discussed in lecture.
The projects will be developed on GitHub.com in public repos. 
You will be required to set-up a Github repository under the [UBC-MDS](https://github.com/UBC-MDS) organization.

## Mechanics
rubric={raw:20}

You will need to setup the project in the same way as outlined in [milestone1](https://github.ubc.ca/MDS-2019-20/DSCI_532_viz-2_students/blob/master/release/milestone1/milestone1.md).
You should take this opportunity to update your team contract after working with each other for 2 weeks.

In your milestone3 repo on GitHub.ubc.ca, this week you will submit:

- Updated (if necessary) team contract
- A README file that contains links to the following items:
	- Group project repo for DashR project on GitHub.com
	- Code of conduct file
	- LICENSE file
	- GitHub.com project README
	- Contributing.md if you chose to list it as a separate file, otherwise as part of the GitHub.com project README
	- Reflections (details below)
- ONE screenshot of your current progress on creating your plots in R (see below for a screenshot)
	- Note we do not expect this to be completed, but you should at least be finished creating the static plots in ggplot2.

### Overall Expectations

- You should be committing to git every time you work on this project.
- Every time you work on the project, you should first pull the upstream changes (see section below on how to catch up to a forked repo)
- Your git commit messages should be meaningful. These will be marked. It's OK if one or two are less meaningful, but most should be meaningful and useful.
- After the GitHub.com repository is created, each group member should fork the repository to their personal GitHub.com account and work on the app there, and send pull-requests of their work to the upstream repo that they forked). 
- Another team mate should review, review/critique the contribution (if necessary) and finally accept their teammates' pull request. **Do not accept & merge your own pull request.**
- Use GitHub issues to communicate with their teammates (as opposed to email or Slack)
- You should use proper grammar and full sentences in your README. Point form may occur, but should be less than 10% of your written documents.

## Maintainenance of Project 1 (Python app)
rubric={reasoning:20,quality:20}

As we discussed in Lecture 4, creating a good dashboard requires maintenance. This work goes beyond just creating the dashboard and includes (in order of priority from most important to least important):

1. Implement known bug-fixes and work-arounds.
1. Implement feedback you receive from peers during Lab 3's feedback session.
1. Clean-up and refactor code to make it more readable.
1. Reformat your code and add docstrings ([PEP8](https://www.python.org/dev/peps/pep-0008/) style).
1. If needed, reorganize and restructure your files/directory structure to separate different structures (see the [Dash docs](Structuring a Multi-Page App) for suggested organizations).
1. Apply principles of creating effective dashboards (Lecture 4)
1. Implement any new features (if time permits).

Note: **You are NOT expected to do all (or even most) of the above items for maintenance this week, and you will need to prioritize your efforts.** 
The list is provided in order of priority as each group will be in a different stage of development.
Your group should allocate about 3 hours per person to this task. 
Get as much done as you can and document what else should be done in your reflections.

## Reflection
rubric={reasoning:10,writing:10}

Large-scale changes you make since milestone2 must be documented in your `reflection.md` file and you should link to particular issues in your repos whenever possible. 
You **must** also add some justification for why you prioritized certain bugs/features over others and what your overall strategy was for maintenance. 
You should try to come up with a plan for this early in the week and then make adjustments/modifications as you learn more information and get additional feedback from user testing.

The `reflection.md` should live in your GitHub.com repo.
This file should be worked on collaboratively and each team member should submit a link to the same file.
Each group should submit the same `reflection.md` file. 
However the marked portion will be the Team's reflections, which will require a degree of coordination and discussion.

The `reflection.md` file you will submit will include several elements and link to issues when appropriate. 
Below is a list to help you get started.

- Start with the `reflection.md` file you included with milestone2
- Make any necessary edits or changes (for e.g., if you indicated in your milestone2 reflection that your app had a bug and you fixed it in week 3, you should update your reflections file)
- Wishlist features/bug-fixes
	- If there is anything you wish you had more time to implement or fix, you can list it here.
- Include a brief, high-level summary of any changes you decided to make
- Provide a brief, high-level summary of the feedback you received during the lab session (details below)
- Reflect on the feedback you received (more guidance is below)

### Lab session feedback activity

In lab 3, we will do a feedback activity as a group.
Note this is different from the [peer review]() assignment that is due at the same time as milestone 4.
Giving feedback on the user interface of a dashboard is slightly different from giving feedback on presentations, writing, or analysis.
We will show you how to give effective feedback on dashboards in the lab.

### Reflection on the usefulness of the feedback you received.

Here are some questions to get some ideas flowing. 
You aren't expected to (and probably shouldn't) answer all of these questions.

* Reflect on the usability of your app. How easy or hard was it for your peers to use your app? Did you expect them to use the app in they way they did?
* What things did you hear that's similar across reviewers? Is there a theme here?
* From the feedback, what things do you think are appropriate to change in your app, particularly given the time frame you have to improve the app?
* What is unreasonable to change, and why? Time restraints? Too technical?
* What feedback was the most/least valuable?
* What part of the feedback _process_ was most/least valuable?
* What did you learn from your experience being a "fly-on-the-wall". Was this useful? Why or why not?
* Did the feedback process lead to an improved app? What parts were valuable? What parts were not valuable?

## Starting Project 2 (R App)
rubric={reasoning:10,writing:10}

Similar to [milestone1](https://github.ubc.ca/MDS-2019-20/DSCI_532_viz-2_students/blob/master/release/milestone1/milestone1.md), you should setup your project on GitHub.com, add the necessary files, create forks, deal with access and permissions for your teammates.

Include ONE screenshot of your current progress on creating your plots in R (see below for a screenshot)

- Note we do not expect this to be fully completed, but you should have made good progress creating static plots in ggplot2.
- You should embed this file directly into the GitHub.ubc.ca milestone3 readme.
- You can export images of your R plots and lay them out using a graphics editor, or powerpoint/keynote.
- The purpose of this is to make sure you're making good progress on creating your plots using R, ggplot2, and ggplotly
- Below is an image of what we are expecting:

![](progress.png)

There are some important differences for those that are changing their datasets.

### If you are keeping the same dataset as Milestone 1 and 2

You will be recreating your app using DashR.
Now that your app is approaching its final state, you should update your README, proposal, and app sketch to match what your app will actually be doing and showing.
As a rough guideline of effort, you should spend no more than 1-2 hours in total for this section.
To help your TAs grading your work, instead of submitting a link to your file directly, you should submit a link that compares two commits of your proposal. 
We will show you how to do this in the lab session, but [here is a guide](https://help.github.com/en/github/committing-changes-to-your-project/comparing-commits-across-time) to do this.

### If you are changing your dataset

As you may have guessed by now, changing your dataset will take some extra effort. 
You will need to submit a new README, proposal, and app sketch. 
As a rough guideline of effort, you should aim to spend spend about 3-4 hours for this section.
The guidelines for the proposal are the same as in [milestone 1](https://github.ubc.ca/MDS-2019-20/DSCI_532_viz-2_students/blob/master/release/milestone1/milestone1.md).
It is recommended you let the TA that is grading you know that you're changing your dataset and get it approved if it isn't already.
