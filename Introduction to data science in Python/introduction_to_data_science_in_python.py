# -*- coding: utf-8 -*-
"""Introduction to Data Science in Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZjeOPFnO-m6pYbFag94PP5qQrcOKPzaO

Importing Python modules
Modules (sometimes called packages or libraries) help group together related sets of tools in Python. In this exercise, we'll examine two modules that are frequently used by Data Scientists:

statsmodels: used in machine learning; usually aliased as sm
seaborn: a visualization library; usually aliased as sns
Note that each module has a standard alias, which allows you to access the tools inside of the module without typing as many characters. For example, aliasing lets us shorten seaborn.scatterplot() to sns.scatterplot().
"""

# Use an import statement to import seaborn with alias sns
import seaborn as sns

"""Correcting a broken import
In this exercise, we'll learn to import numpy, a module for performing mathematical operations on lists of data. The standard alias for numpy is np.


"""

# Fix the import of numpy to run without errors
import numpy as np

"""Creating a float
Before we start looking for Bayes' kidnapper, we need to fill out a Missing Puppy Report with details of the case. Each piece of information will be stored as a variable.

We define a variable using an equals sign (=). For instance, we would define the variable height:

height = 24
In this exercise, we'll be defining bayes_age to be 4.0 months old. The data type for this variable will be float, meaning that it is a number.
"""

# Fill in Bayes' age (4.0)
bayes_age = 4.0

# Display the variable bayes_age
print(bayes_age)

"""Creating strings
Let's continue to fill out the Missing Puppy Report for Bayes. In the previous exercise, we defined bayes_age, which was a float, which represents a number.

In this exercise, we'll define favorite_toy and owner, which will both be strings. A string represents text. A string is surrounded by quotation marks (' or ") and can contain letters, numbers, and special characters. It doesn't matter if you use single (') or double (") quotes, but it's important to be consistent throughout your code.
"""

# Bayes' favorite toy
favorite_toy = "Mr. Squeaky"

# Bayes' owner
owner = 'DataCamp'

# Display variables
print(favorite_toy)
print(owner)

"""Correcting string errors
It's easy to make errors when you're trying to type strings quickly.

Don't forget to use quotes! Without quotes, you'll get a name error.
owner = DataCamp
Use the same type of quotation mark. If you start with a single quote, and end with a double quote, you'll get a syntax error.
fur_color = "blonde'
Someone at the police station made an error when filling out the final lines of Bayes' Missing Puppy Report. In this exercise, you will correct the errors.
"""

# One or more of the following lines contains an error
# Correct it so that it runs without producing syntax errors
birthday = "2017-07-14"
case_id = 'DATACAMP!123-456?'

"""Load a DataFrame
A ransom note was left at the scene of Bayes' kidnapping. Eventually, we'll want to analyze the frequency with which each letter occurs in the note, to help us identify the kidnapper. For now, we just need to load the data from ransom.csv into Python.

We'll load the data into a DataFrame, a special data type from the pandas module. It represents spreadsheet-like data (something with rows and columns).
We can create a DataFrame from a CSV (comma-separated value) file by using the function pd.read_csv().
"""

# Import pandas
import pandas as pd

# Load the 'ransom.csv' into a DataFrame
r = pd.read_csv('ransom.csv')

# Display DataFrame
print(r)

"""Correcting a function error
The code in the script editor should plot information from the DataFrame that we loaded in the previous exercise.

However, there is an error in function syntax. Remember that common function errors include:

Forgetting closing parenthesis
Forgetting commas between each argument
Note that all arguments to the functions are correct. The problem is in the function syntax.
"""

# One or more of the following lines contains an error
# Correct it so that it runs without producing syntax errors

# Plot a graph
plt.plot(x_values, y_values)

# Display the graph
plt.show()

"""Snooping for suspects
We need to narrow down the list of suspects for the kidnapping of Bayes. Once we have a list of suspects, we'll ask them for writing samples and compare them to the ransom note.

A witness to the crime noticed a green truck leaving the scene of the crime whose license plate began with 'FRQ'. We'll use this information to search for some suspects.

As a detective, you have access to a special function called lookup_plate.

lookup_plate accepts one positional argument: A string representing a license plate.
"""

# Define plate to represent a plate beginning with FRQ
# Use * to represent the missing four letters
plate = "FRQ****"
lookup_plate(plate)

"""Loading a DataFrame
We're still working hard to solve the kidnapping of Bayes, the Golden Retriever. Previously, we used a license plate spotted at the crime scene to narrow the list of suspects to:

Fred Frequentist
Ronald Aylmer Fisher
Gertrude Cox
Kirstine Smith
We've obtained credit card records for all four suspects. Perhaps some of them made suspicious purchases before the kidnapping?

The records are in a CSV called "credit_records.csv".
"""

# Import pandas under the alias pd
import pandas as pd

# Load the CSV "credit_records.csv"
credit_records = pd.read_csv("credit_records.csv")

# Display the first five rows of credit_records using the .head() method
print(credit_records.head())

"""Inspecting a DataFrame
We've loaded the credit card records of our four suspects into a DataFrame called credit_records. Let's learn more about the structure of this DataFrame.

The pandas module has been imported under the alias pd. The DataFrame credit_records has already been imported.

How many rows are in credit_records?
"""

# Use .info() to inspect the DataFrame credit_records
print(credit_records.info())

"""Two methods for selecting columns
Once again, we've loaded the credit card records of our four suspects into a DataFrame called credit_records. Let's examine the items that they've purchased.

The pandas module has been imported under the alias pd. The DataFrame credit_records has already been imported.
"""

# Select the column item from credit_records
# Use brackets and string notation
items = credit_records["item"]

# Display the results
print(items)

"""Correcting column selection errors
A junior detective tried to access the location columns of credit_records, but he made some mistakes. Help correct his code so that we can search for suspicious purchases.

In all exercises going forward, pandas will be imported as pd. The DataFrame credit_records has already been imported.
"""

# One or more lines of code contain errors.
# Fix the errors so that the code runs.

# Select the location column in credit_records
location = credit_records["location"]

# Select the item column in credit_records
items = credit_records.item

# Display results
print(location)

"""More column selection mistakes
Another junior detective is examining a DataFrame of Missing Puppy Reports. He's made some mistakes that cause the code to fail.

The pandas module has been loaded under the alias pd, and the DataFrame is called mpr.
"""

# Use info() to inspect mpr
print(mpr.info())

"""Logical testing
Let's practice writing logical statements and displaying the output.

Recall that we use the following operators:

== tests that two values are equal.
!= tests that two values are not equal.
> and < test that greater than or less than, respectively.
>= and <= test greater than or equal to or less than or equal to, respectively.
"""

# Is height_inches greater than 70 inches?
print(height_inches == 70)

"""Selecting missing puppies
Let's return to our DataFrame of missing puppies, which is loaded as mpr. Let's select a few different rows to learn more about the other missing dogs.

Instructions
100 XP
Select the dogs where Age is greater than 2.
Select the dogs whose Status is equal to Still Missing.
Select all dogs whose Dog Breed is not equal to Poodle.
"""

# Select the dogs where Age is greater than 2
greater_than_2 = mpr[mpr.Age > 2]
print(greater_than_2)

# Select the dogs whose Status is equal to Still Missing
still_missing = mpr[mpr.Status ==  "Still Missing"]
print(still_missing)

# Select all dogs whose Dog Breed is not equal to Poodle
not_poodle = mpr[mpr["Dog Breed"] != "Poodle"]
print(not_poodle)

"""Narrowing the list of suspects
In Chapter 1, we found a list of people whose cars matched the description of the one that kidnapped Bayes:

Fred Frequentist
Ronald Aylmer Fisher
Gertrude Cox
Kirstine Smith
We'd like to narrow this list down, so we obtained credit card records for each suspect. We'd like to know if any of them recently purchased dog treats to use in the kidnapping. If they did, they would have visited 'Pet Paradise'.

The credit records have been loaded into a DataFrame called credit_records.
"""

# Select purchases from 'Pet Paradise'
purchase = credit_records[credit_records.location == 'Pet Paradise']

# Display
print(purchase)

"""Working hard
Several police officers have been working hard to help us solve the mystery of Bayes, the kidnapped Golden Retriever. Their commanding officer wants to know exactly how hard each officer has been working on this case. Officer Deshaun has created DataFrames called deshaun to track the amount of time he spent working on this case. The DataFrame contains two columns:

day_of_week: a string representing the day of the week
hours_worked: the number of hours that a particular officer worked on the Bayes case'
"""

# From matplotlib, import pyplot under the alias plt
from matplotlib import pyplot as plt

"""Or hardly working?
Two other officers have been working with Deshaun to help find Bayes. Their names are Officer Mengfei and Officer Aditya. Deshaun used their time cards to create two more DataFrames: mengfei and aditya. In this exercise, we'll plot all three lines together to see who was working hard each day.

We've already loaded matplotlib under the alias plt.

Instructions 1/2
50 XP
Plot Officer Aditya's time worked with day_of_week on the x-axis and hours_worked on the y-axis.
Plot Officer Mengfei's time worked with day_of_week on the x-axis and hours_worked on the y-axis.
"""

# Plot Officer Deshaun's hours_worked vs. day_of_week
plt.plot(deshaun.day_of_week, deshaun.hours_worked)

# Plot Officer Aditya's hours_worked vs. day_of_week
plt.plot(aditya.day_of_week, aditya.hours_worked)

# Plot Officer Mengfei's hours_worked vs. day_of_week
plt.plot(mengfei.day_of_week, mengfei.hours_worked)

# Display all three line plots
plt.show()

"""Adding a legend
Officers Deshaun, Mengfei, and Aditya have all been working with you to solve the kidnapping of Bayes. Their supervisor wants to know how much time each officer has spent working on the case.

Deshaun created a plot of data from the DataFrames deshaun, mengfei, and aditya in the previous exercise. Now he wants to add a legend to distinguish the three lines.

Instructions 1/4
25 XP
Using the keyword label, label Deshaun's plot as "Deshaun".
"""

# Add a label to Deshaun's plot
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label = "Deshaun")

# Officer Aditya
plt.plot(aditya.day_of_week, aditya.hours_worked)

# Officer Mengfei
plt.plot(mengfei.day_of_week, mengfei.hours_worked)

# Display plot
plt.show()

"""Adding labels
If we give a chart with no labels to Officer Deshaun's supervisor, she won't know what the lines represent.

We need to add labels to Officer Deshaun's plot of hours worked.

Instructions
100 XP
Add a descriptive title to the chart.
Add a label for the y-axis.
"""

# Lines
plt.plot(deshaun.day_of_week, deshaun.hours_worked, label='Deshaun')
plt.plot(aditya.day_of_week, aditya.hours_worked, label='Aditya')
plt.plot(mengfei.day_of_week, mengfei.hours_worked, label='Mengfei')

# Add a title
plt.title("Hours worked")

# Add y-axis label
plt.ylabel("Working Hours")

# Legend
plt.legend()
# Display plot
plt.show()

"""Adding floating text
Officer Deshaun is examining the number of hours that he worked over the past six months. The number for June is low because he only had data for the first week. Help Deshaun add an annotation to the graph to explain this.

Instructions
100 XP
Place the annotation "Missing June data" at the point (2.5, 80).

Adding floating text
Officer Deshaun is examining the number of hours that he worked over the past six months. The number for June is low because he only had data for the first week. Help Deshaun add an annotation to the graph to explain this.

Instructions
100 XP
Place the annotation "Missing June data" at the point (2.5, 80).
"""

# Create plot
plt.plot(six_months.month, six_months.hours_worked)

# Add annotation "Missing June data" at (2.5, 80)
plt.text(2.5, 80, "Missing June data")

# Display graph
plt.show()

"""Tracking crime statistics
Sergeant Laura wants to do some background research to help her better understand the cultural context for Bayes' kidnapping. She has plotted Burglary rates in three U.S. cities using data from the Uniform Crime Reporting Statistics.

She wants to present this data to her officers, and she wants the image to be as beautiful as possible to effectively tell her data story.

Recall:

You can change linestyle to dotted (':'), dashed('--'), or no line ('').
You can change the marker to circle ('o'), diamond('d'), or square ('s').
Instructions
100 XP
Change the color of Phoenix to "DarkCyan".
Make the Los Angeles line dotted.
Add square markers to Philadelphia.
"""

# Change the color of Phoenix to `"DarkCyan"`
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix", color = "DarkCyan")

# Make the Los Angeles line dotted
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles", linestyle = ":")

# Add square markers to Philedelphia
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia", marker = 's')

# Add a legend
plt.legend()

# Display the plot
plt.show()

"""Playing with styles
Help Sergeant Laura try out a few different style options. Changing the plotting style is a fast way to change the entire look of your plot without having to update individual colors or line styles. Some popular styles include:

'fivethirtyeight' - Based on the color scheme of the popular website
'grayscale' - Great for when you don't have a color printer!
'seaborn' - Based on another Python visualization library
'classic' - The default color scheme for Matplotlib
Instructions 1/3
35 XP
Change the plotting style to "fivethirtyeight".
Change the plotting style to "ggplot".
View all styles by typing print(plt.style.available) in the console.
Pick one of those styles and see what it looks like.
"""

# Change the style to fivethirtyeight
plt.style.use("fivethirtyeight")

# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")

# Add a legend
plt.legend()

# Display the plot
plt.show()

"""Identifying Bayes' kidnapper
We've narrowed the possible kidnappers down to two suspects:

Fred Frequentist (suspect1)
Gertrude Cox (suspect2)
The kidnapper left a long ransom note containing several unusual phrases. Help DataCamp by using a line plot to compare the frequency of letters in the ransom note to samples from the two main suspects.

Three DataFrames have been loaded:

ransom contains the letter frequencies for the ransom note.
suspect1 contains the letter frequencies for the sample from Fred Frequentist.
suspect2 contains the letter frequencies for the sample from Gertrude Cox.
Each DataFrame contain two columns letter and frequency.

Instructions 1/4
25 XP
Plot the letter frequencies from the ransom note. The x-values should be ransom.letter. The y-values should be ransom.frequency. The label should be the string 'Ransom'. The line should be dotted and gray.
"""

# x should be ransom.letter and y should be ransom.frequency
plt.plot(ransom.letter, ransom.frequency,
         # Label should be "Ransom"
         label="Ransom",
         # Plot the ransom letter as a dotted gray line
         linestyle=':', color='gray')

# Display the plot
plt.show()

"""Charting cellphone data
We know that Freddy Frequentist is the one who kidnapped Bayes the Golden Retriever. Now we need to learn where he is hiding.

Our friends at the police station have acquired cell phone data, which gives some of Freddie's locations over the past three weeks. It's stored in the DataFrame cellphone. The x-coordinates are in the column 'x' and the y-coordinates are in the column 'y'.

The matplotlib module has been imported under the alias plt.

Instructions
100 XP
Display the first five rows of the DataFrame and determine which columns to plot.
Create a scatter plot of the data in cellphone.
"""

# Explore the data
print(cellphone.head())

# Create a scatter plot of the data from the DataFrame cellphone
plt.scatter(cellphone.x, cellphone.y)

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()

"""Build a simple bar chart
Officer Deshaun wants to plot the average number of hours worked per week for him and his coworkers. He has stored the hours worked in a DataFrame called hours, which has columns officer and avg_hours_worked. Recall that the function plt.bar() takes two arguments: the labels for each bar, and the height of each bar. Both of these can be found in our DataFrame.

Instructions 1/3
35 XP
Display the DataFrame hours using a print command.
"""

# Display the DataFrame hours using print
print(hours)

"""Where did the time go?
Officer Deshaun wants to compare the hours spent on field work and desk work between him and his colleagues. In this DataFrame, he has split out the average hours worked per week into desk_work and field_work.

You can use the same DataFrame containing the hours worked from the previous exercise (hours).

Instructions 1/2
50 XP
Create a bar plot of the time each officer spends on desk_work.
Label that bar plot "Desk Work".
"""

# Plot the number of hours spent on desk work
plt.bar(hours.officer, hours.desk_work, label="Desk Work")

# Display the plot
plt.show()

"""Modifying histograms
Let's explore how changes to keyword parameters in a histogram can change the output. Recall that:

range sets the minimum and maximum datapoints that we will include in our histogram.
bins sets the number of points in our histogram.
We'll be exploring the weights of various puppies from the DataFrame puppies. matplotlib has been loaded under the alias plt.

Instructions 1/3
35 XP
Create a histogram of the column weight from the DataFrame puppies.
Change the number of bins to 50.
Change the range to start at 5 and end at 35.
"""

# Create a histogram of the column weight from the DataFrame puppies
plt.hist(puppies.weight)

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()

"""Modifying histograms
Let's explore how changes to keyword parameters in a histogram can change the output. Recall that:

range sets the minimum and maximum datapoints that we will include in our histogram.
bins sets the number of points in our histogram.
We'll be exploring the weights of various puppies from the DataFrame puppies. matplotlib has been loaded under the alias plt.

Instructions 1/3
35 XP
Create a histogram of the column weight from the DataFrame puppies.
Change the number of bins to 50.
Change the range to start at 5 and end at 35.
"""

# Create a histogram of the column weight from the DataFrame puppies
plt.hist(puppies.weight)

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()

"""Heroes with histograms
We've identified that the kidnapper is Fred Frequentist. Now we need to know where Fred is hiding Bayes.

A shoe print at the crime scene contains a specific type of gravel. Based on the distribution of gravel radii, we can determine where the kidnapper recently visited. It might be:

blue-meadows-park
shady-groves-campsite
happy-mountain-trailhead
The radii of individual gravel pieces has been loaded into the DataFrame gravel, and matplotlib has been loaded under the alias plt.

Instructions 1/4
25 XP
Instructions 1/4
25 XP
Create a histogram of gravel.radius.
"""

# Create a histogram of gravel.radius
plt.hist(gravel.radius)

# Display histogram
plt.show()