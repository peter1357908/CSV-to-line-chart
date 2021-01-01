Script Usage:
* python ./csvtlc.py <ins>usage type</ins> \[<ins>CSV file</ins> \[<ins>last X data points</ins>\]\]

`usage type`:
* "general": display the data as is, with the "date" column on the X-axis, and the other columns each as a line-plot. ([sample data](VIX_SPY_Skew21_MooMO_sample.csv))
* "specific": display the data in a specific way (currently: first column on the secondary Y-axis, and the other columns on the primary Y-axis; the secondary Y-axis also has a hard-coded display range). ([sample data](TQQQ_EMA19_EMA39_sample.csv))
* invalid input or no input will be treated as "general".

`CSV file`:
* should contain a "date" column as its first column, with the value columns being the rest of the columns.
* default: the sample data for each `usage type`.

`last X data points`:
* if specified, the display zooms to show only the last X data points.
* default: 0 (shows all data points).
