# cintel-01-interactive
P1Shiny

## Initial Project Setup
## Commands Used to update GitHub- use frequently throughout

```
git add .
git commit -m "initial commit"
git push -u origin main
```
## Create & Activate Virtual Environment

```
python -m venv .venv
.venv\Scripts\activate
```
## Install Packages into requirements.txt
# copy & paste into .txt file
```
from shiny import App, render, ui
import numpy as np
import matplotlib.pyplot as plt

```
# run to install into requirements.txt
python -m pip install -r requirements.txt

# run to update into requirements.txt
python -m pip install <package_name>

# Work through Module Requirements
Requirements

Your app must include at least the following (you are encouraged to add more as you like).  

A title for the page Hint: See page_opts in Example 2. 

One interactive input slider to select the number of bins. Pass in the following five arguments:

A string id ("selected_number_of_bins") that uniquely identifies this input value. 
A string label (e.g., "Number of Bins") to be displayed alongside the slider.
An integer representing the minimum number of bins (e.g., 0).
An integer representing the maximum number of bins (e.g., 100).
An integer representing the initial value of the slider (e.g., 20).
One reactive output chart to show the distribution using the selected number of bins. Use a matplotlib histogram for the chart:  created with plt.hist():
Pass in the numpy data array
Pass in the user input number of bins
Set the density to True to normalize the histogram so that the total area under the histogram equals 1.
 Reminders:

For the Python interpreter to understand our instructions we must get them exactly correct.
True and False both have an initial capital letter (in Python)
Capitalization matters - true is not the same as True. 
Punctuation matters. Things like colons (:) and commas (,) are very important. 
Spelling matters - variable and function names must be exact for things to work. Copying and pasting names to get them exactly the same can save a lot of time and avoid issues. 
Indentation matters. After a colon, we generally indent statements using exactly 4 spaces. Indenting has meaning - we can't mix tabs and spaces. 
Read error messages carefully - they tell us what line the error is on and what is wrong - they usually help a great deal. 
You are encouraged to consult wit an AI assistant and your peers to resolve errors. 
When you get stuck, post any issues, questions, and error messages here in the discussion. Read other posts and help out where you can. 
To get help, display your screenshot AND paste the error message so we can see clearly what is happening. 

#Work in VS Code, run to test, then Run in Shiny Examples.
