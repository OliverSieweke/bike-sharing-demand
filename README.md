<!--suppress HtmlDeprecatedAttribute | JetBrains Inspection -->
<p align="center">
    <a title="Documentation" href="https://bike-sharing-demand.readthedocs.io/en/latest/?badge=latest">
        <img alt="Bikes Logo" src="bikes.svg"/>
    </a>
</p>


<h1 align="center">Bike Sharing Demand</h1> 

<p align="center">
    <a title="MIT License" href="https://choosealicense.com/licenses/mit">
      <img alt="License: MIT" src="https://img.shields.io/github/license/OliverSieweke/bike-sharing-demand" />
    </a>
    <a title="Documentation Status" href="https://bike-sharing-demand.readthedocs.io/en/latest/?badge=latest">
        <img alt="Documentation Status" src="https://readthedocs.org/projects/bike-sharing-demand/badge/?version=latest" />
    </a>
    <a title="MyBinder" href="https://mybinder.org/v2/gh/OliverSieweke/bike-sharing-demand/master?filepath=notebooks">
        <img alt="Binder" src="https://mybinder.org/badge_logo.svg" />
    </a>
</p>


This project proposes machine learning models to forecast bike rental demand in 
Washinton's [Capital Bikeshare](https://www.capitalbikeshare.com/) program.
Predictions are being submitted to Kaggle's
*[Bike Sharing Demand](https://www.kaggle.com/c/bike-sharing-demand/overview)* competition.

The project's scope was limited to exploring how far one could get with various 
feature engineering strategies in conjunction with linear regressions.

<p align="center">
    <img alt="Kaggle Submissions Graph" src="kaggle-submissions-graph.png"/>
</p>

## Data

The data is to be found in [`data/original`](data/original) and was downloaded from 
[Kaggle](https://www.kaggle.com/c/bike-sharing-demand/data) on the *04.05.20*. It consists 
of a time series containing various information on the type of day and weather conditions.

The data is split up into: 

- [`train.csv`](data/original/train.csv) which comprises the first 19 days of each month, for which 
the number of bike rentals is known.
- [`test.csv`](data/original/train.csv) which comprises the days following the 
20th of each month, for which the number of bike rentals is unknown and should be predicted.
