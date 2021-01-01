Usage:

> python ./csvtlc.py <u>usage</u> \[<u>CSV file</u> \[<u>last X data points</u>\]\]

`usage`:
* "general": display the data as is, with the "date" column on the X-axis, and the other columns each as a line-plot. ([sample data](VIX_SPY_Skew21_MooMO_sample.csv))
* "specific": display the data in a specific way (currently: first column on the secondary Y-axis, and the other columns on the primary Y-axis). ([sample data](TQQQ_EMA19_EMA39_sample.csv))
* invalid input or no input will be treated as "general"

Assumes that `CSV file` contains a "date" column as its first column, with the value columns being the rest of the columns. Default: the sample data for each `usage`.

If `last X data points` is specified, the display zooms to show only the last X data points. Default: 0 (shows all data points).
