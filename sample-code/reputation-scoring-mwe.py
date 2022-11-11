# Copyright (c) 2022 Infoblox, Inc.

# Imports
import random
import pandas as pd
import numpy as np

# Only needed if visualizing the score distribution
visualize_dist = True
if( visualize_dist ):
    import matplotlib.pyplot as plt
    import seaborn as sns



# Configuration parameters

# For this example, the values were chosen arbitrarily.  Ultimately, they
# are determined by the specific use case and the nature of the data associated
# with it.

# Number of items to score
number_of_items = 100

# Maximum number of values per item
max_values_per_item = 250

# Minimum number of values per item
min_values_per_item = 0

# The number of bins below and above the mean
bin_width = 5

# The threshold for high-confidence in the ordinal score
confidence_threshold = 30



# Create sample data
# Note: The data is randomly generated using a uniform distribution.  Data in
#       a specific use case may have a different distribution.

# Create data for each item
items = []
for i in range( number_of_items ):

    # Generate the total number of values per item
    total_number_of_values = random.randint( min_values_per_item,
            max_values_per_item )
    
    # Generate the number of values meeting our criteria (e.g., the number of
    # malicious domains in the TLD use case)
    values_meeting_criteria = random.randint( 0, total_number_of_values )
    
    # Save the values
    items.append( ( 'Item-{0:04d}'.format( i ),
            total_number_of_values,
            values_meeting_criteria ) )

# Create a Pandas dataframe to organize the data
items_df = pd.DataFrame( items, columns=['id',
        'total_number_of_values',
        'values_meeting_criteria'] )



# Compute the raw score
# This is simply the ratio of values meeting a specific criteria and the total
# number of values.  In the TLD reputation use case described in the whitepaper,
# these values would be the number of observed malicious domains in the TLD and
# the total number of observed domains in the TLD.
items_df[ 'raw_score' ] = items_df[ 'values_meeting_criteria' ] \
        / items_df[ 'total_number_of_values' ]

# "Normalize" the raw score using a logarithm
# This makes the distribution almost normal, which simplifies analysis and
# comparison of items.
ratio = items_df[ 'raw_score' ]
ratio = ratio.fillna(0)

# Note: This may generate a warning when dividing by zero.  The situation is
#       handled below so it isn't a problem, but warnings are disabled to avoid
#       confusion.
np.seterr(divide = 'ignore') 
items_df[ 'log_score' ] = np.log( ratio / ( 1 - ratio ) )
np.seterr(divide = 'warn') 

# Compute the mean and standard deviation
# Don't include -inf/+inf as they are edge cases that will throw off the
# calculations of the mean and standard deviation.  They are given scores of
# 0 and 10, respectively, using the binning process below.
finite_items_df = items_df[ (items_df[ 'log_score' ] != np.inf)
        & (items_df[ 'log_score' ] != -np.inf) ]
mean = finite_items_df[ 'log_score' ].mean()
std_dev = finite_items_df[ 'log_score' ].std()

# Compute the bins for the ordinal scores using the standard deviation
bin_edges = [ mean + std_dev * (n + 0.5) for n in range( -bin_width, bin_width ) ]

# Assign ordinal scores using the bins
items_df[ 'ordinal_score' ] = np.digitize( items_df[ 'log_score' ], bin_edges )

# Calculate the confidence in the scores
items_df[ 'high_confidence' ] = ( items_df[ 'total_number_of_values' ] \
        > confidence_threshold )



# Display the results fo the calculations
print( items_df )
print( str( mean ) + ' +/- ' + str( std_dev ) )
print( bin_edges )



# Visualize the score distributions
if( visualize_dist ):
    # Visualize the log score to illustrate the distribution is approximately
    # normal
    sns.histplot( finite_items_df[ 'log_score' ], kde = True )
    plt.title( "Distribution of Log Scores for Items" );
    plt.ylabel( "Number of items" );
    plt.xlabel( "Log Score" );
    plt.show()

    # Visualize the ordinal score
    sns.histplot( items_df[ 'ordinal_score' ], kde = True, bins=11 )
    plt.title( "Distribution of Oridnal Scores for Items" );
    plt.ylabel( "Number of items" );
    plt.xlabel( "Ordinal Score" );
    plt.show()
