# SurvivalDataScript
Script to transform meta information from animal experiments into survival tables that can be used in Prism.

v 0.0.1
4/15/20

Survival script effectively turns a meta data CSV into a survival csv that is easily used with prisms survival curve feature. Hopefully this saves you some time
-Joseph

Requires an updated python, numpy, and pandas

Requires that all dates be store in following format: MM/DD/YY (will probably fix this in an update)
	example 02/26/19 ( although I think you can get away without the leading zero, for example 2/26/19)

Requires that the pathname to your meta data csv contain a '/'

positional (required) arguments (in this order)
(1) the full pathname of your meta data 
	example: Scripts/JM_SurvivalData_Python/Example/Meta.csv
(2) the column header of the starting date to use in the meta csv
	example: inoculation.date
(3) the column header of the death date to use in the meta csv
	example death.date

keyword (optional) arguments 
(1) treatment column header (-t, --treatment)
	-default header is ‘treatment’ only change if your column header in the meta data csv for the treatments is not treatment
(2) mouseID column header (-m,--mouseID)
	-default header is ‘mouse.id’ only change if your column header in the meta data csv for the mouse identification is not mouse.id


an example usage of this script in the command line is as follows (if your meta header columns are treatment and mouse.id
python Scripts/JM_SurvivalData_Python/Survival.py Scripts/JM_SurvivalData_Python/Example/Meta.csv inoculation.date death.date

an example usage of this script in the command line if your treatment group header was entitled group 
python Scripts/JM_SurvivalData_Python/Survival.py Scripts/JM_SurvivalData_Python/Example/Meta.csv inoculation.date death.date -t group

an example usage of this script in the command line if your treatment group header was entitled group and your mouse identification was entitled mouseID
python Scripts/JM_SurvivalData_Python/Survival.py Scripts/JM_SurvivalData_Python/Example/Meta.csv inoculation.date death.date -t group -m mouseID
