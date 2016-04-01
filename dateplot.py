# Credit to Randal Olson for the starter code:
# http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/
# I've augmented this script to fit my PGP keyserver data.

import matplotlib.pyplot as plt  
import pandas as pd  
  
# Read the data into a pandas DataFrame.
data = pd.read_csv("newsdata.csv")
  
# These are the "Tableau 20" colors as RGB.    
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]    
  
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.)    
  
# Set the figure size.   
plt.figure(figsize=(12, 15))    
  
# Remove the plot frame lines.
ax = plt.subplot(111)    
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)    
  
# Only get tick marks on the left and bottom sides of the graph.
ax.get_xaxis().tick_bottom()    
ax.get_yaxis().tick_left()    
  
# Limit the range of the plot to only where the data is.    
plt.ylim(0, 202)    
plt.xlim(0, 256)    
  
# Adjust font size and spacing of axis ticks.
plt.yticks(range(0, 210, 10), [str(x) for x in range(0, 210, 10)], fontsize=14)    
plt.xticks(range(0, 256, 23), [str(x) for x in range(1994, 2018, 2)], fontsize=14)    
  
# Add tick lines for the y-axis.
for y in range(20, 220, 20):    
    plt.plot(range(0, 256), [y] * len(range(0, 256)), "--", lw=0.5, color="black", alpha=0.4)
  
# Remove tick marks.
plt.tick_params(axis="both", which="both", bottom="off", top="off",    
                labelbottom="on", left="off", right="off", labelleft="on")    
  
# I plotted the news orgs in order of the highest % in the final year.    
news_orgs = ['CNN', 'New York Times', 'ESPN', 'Huffington Post',    
          'Fox News', 'Washington Post', 'BuzzFeed',    
          'USA Today', 'Forbes', 'CNET']    
  
# Plot each line separately with its own color, using tableau20 colors.
for rank, column in enumerate(news_orgs):    
    plt.plot(data.Months.values,    
            data[column.replace("\n", " ")].values,    
            lw=2, color=tableau20[rank])    

    # We assign labels to each line, and offset their positions so they don't overlap.
    y_pos = data[column.replace("\n", " ")].values[-1] - 1      
    if column == "CNN":    
        y_pos -= 0.25    
    elif column == "New York Times":    
        y_pos += 0.25    
    elif column == "ESPN":    
        y_pos += 0.75    
    elif column == "Huffington Post":    
        y_pos -= 1.75
    elif column == "Fox News":    
        y_pos += 0.5    
    elif column == "Washington Post":    
        y_pos += 1.75    
    elif column == "BuzzFeed":    
        y_pos += 0.25    
    elif column == "USA Today":    
        y_pos += 0.75    
    elif column == "Forbes":    
        y_pos += 0
    elif column == "CNET":    
        y_pos += 0    
  
    # Again, make sure that all labels are large enough to be easily read    
    # by the viewer.    
    plt.text(257, y_pos, column, fontsize=14, color=tableau20[rank])    
  
# Plot the title.
plt.text(142, 206, "Number of public keys for emails tied to news orgs"    
       ", by organization (12/1994 - 03/2016)", fontsize=17, ha="center")    

# Plot some descriptive information and credits at the bottom of the graph.   
plt.text(10, -18, "Data source: pgp.mit.edu. Rankings: alexa.com/topsites"    
       "\nAuthor: Martin Shelton (mshelt.onl / @mshelton)"    
       "\nNote: credit for matplotlib and design genius goes to Randy Olson"
       "\nhttp://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/",
       fontsize=10)    
  
# Save the picture as a PNG. It can also be saved as PDF, JPEG, etc. by changing the file extension.
plt.savefig("pgp_adoption.png", bbox_inches="tight")  
