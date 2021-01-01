from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import sys

# ---------------------------------------------------------------
# constant definitions
# ---------------------------------------------------------------
DEFAULT_GENERAL_DATA = 'VIX_SPY_Skew21_MooMO_sample.csv'
DEFAULT_SPECIFIC_DATA = 'TQQQ_EMA19_EMA39_sample.csv'
DEFAULT_ZOOM_RANGE = 0

# ---------------------------------------------------------------
# parse input (expecting sane input)
# ---------------------------------------------------------------
arg_count = len(sys.argv)

# set the values to their default first; change as necessary later
usage_type = 'general'
data_filename = DEFAULT_GENERAL_DATA
zoom_range = DEFAULT_ZOOM_RANGE

if arg_count >= 2:
  if sys.argv[1] == 'specific':
    usage_type = 'specific'
    data_filename = DEFAULT_SPECIFIC_DATA

  if arg_count >= 3:
    data_filename = sys.argv[2]
    if arg_count >= 4:
      zoom_range = int(sys.argv[3])

# ---------------------------------------------------------------
# load data
# ---------------------------------------------------------------
df = pd.read_csv(data_filename, parse_dates=['date'], index_col=['date'])

# ---------------------------------------------------------------
# modify data (if necessary)
# ---------------------------------------------------------------

# currently no data modification is needed in this script. Below is
# an example of what to do. Note that it assumes that the first
# row does not contain 0's... that was a NASTY bug.

# # all but the first column in the dataframe are normalized.
# columns_to_normalize = df.columns[1:]
# df[columns_to_normalize] = df[columns_to_normalize].apply(lambda each_column: each_column/each_column[0])

# ---------------------------------------------------------------
# configure the figure (ha!)
# ---------------------------------------------------------------
if usage_type == 'general':
  fig = go.Figure()
  
  for i in range(len(df.columns)):
    column_name = df.columns[i]
    fig.add_trace(
      go.Scatter(x=df.index, y=df[column_name], mode='lines', name=column_name)
    )
elif usage_type == 'specific':
  fig = make_subplots(specs=[[{'secondary_y': True}]])

  for i in range(1, len(df.columns)):
    column_name = df.columns[i]
    fig.add_trace(
        go.Scatter(x=df.index, y=df[column_name], mode='lines', name=column_name),
        secondary_y=False,
    )
  
  column_name = df.columns[0]
  fig.add_trace(
    go.Scatter(x=df.index, y=df[column_name], mode='lines', name=column_name),
    secondary_y=True,
  )
else:
  print('somehow usage_type is bogus... how??')
  quit()

# set the default hover mode to 'compare data' rather than 'show closest data'
fig.update_layout(hovermode='x')

# set the zoom range if necessary
if zoom_range > 0:
  start_date = df.index[-zoom_range]
  end_date = df.index[-1]
  fig.update_xaxes(range=[start_date, end_date])

# ---------------------------------------------------------------
# display the figure
# ---------------------------------------------------------------
fig.show()
