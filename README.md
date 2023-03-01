# README: Trends in SAT Participation Rates

## Problem Statement

The ACT and the SAT are standardized tests used to assess college readiness in the United States. In 2005, the College Board, the makers of the SAT, released a revision of the SAT that was met with critcism by both students and educators alike [(1)](https://www.nytimes.com/2014/03/09/magazine/the-story-behind-the-sat-overhaul.html). According to critiques, this revision of the SAT did not properly assess students' writing abilities, penalized students for wrong answers, and widened the opportunity gap between students on high or low ends of the socioeconomic spectrum [(1)](https://www.nytimes.com/2014/03/09/magazine/the-story-behind-the-sat-overhaul.html). As a result of the 2005 revision, SAT participation dropped in 29 states from 2006 to 2013, and some states decided to switch to the ACT as their preferred standardized test [(2)](https://www.washingtonpost.com/local/education/sat-usage-declined-in-29-states-over-7-years/2014/03/15/f4504cfc-a5ff-11e3-8466-d34c451760b9_story.html). 

In response to critism and declining use, the college board underwent a mission to revamp the SAT and decrease the opportunity gap that it created [(1)](https://www.nytimes.com/2014/03/09/magazine/the-story-behind-the-sat-overhaul.html
). As a result of these changes, the SAT announced a partnership with Khan Academy to offer test preparation materials to students [(3)](https://blog.collegeboard.org/college-board-khan-academy-for-better-sat-prep), began to offer fee waivers to students who are eligible for financial assistance [(4)](https://collegereadiness.collegeboard.org/sat/register/fees/fee-waivers), and completely revised the SAT to better assess students' abilities [(5)](https://greentestprep.com/resources/sat-prep/new-sat-march2016/why-is-the-college-board-changing-the-sat/ ).

Historically, ACT participation has been low in the midwestern states, with standardized testing dominated by The ACT, a company based out of Iowa City, IA [(6)](https://www.studypoint.com/ed/sat-and-act-test/).

As a data scientist with the College Board who specifically investigates engagement with the midwestern states, I am interested in exploring recent trends in SAT participation, with special emphasis on whether or not the "new SAT" has impacted participation rates in the midwest.

## Executive Summary

To answer this question, we obtained SAT and ACT data for 2017, 2018, and 2019. These data sources provided information on participation rates for each state in the United States and the District of Columbia, as well as average testing scores per state. Data was cleaned to account for data entry errors and missing values, and all data files were merged into one large dataset. Exploratory data analysis was conducted to identify patterns and trends in participation rates.

### Contents:
* [Project Files](#Project-Files)
* [Data Dictionary](#Data-Dictionary)
* [Key Findings](#Key-Findings)
* [Recommendations](#Recommendations)
* [References](#References)

### Project Files:
- [2017 SAT Scores](../data/sat_2017.csv)
- [2017 ACT Scores](../data/act_2017.csv)
- [2018 SAT Scores](../data/sat_2018.csv)
- [2018 ACT Scores](../data/act_2018.csv)
- [2019 SAT Scores](../data/sat_2019.csv)
- [2019 ACT Scores](../data/act_2019.csv)
- [Merged Data Set](../data/final.csv)

The source for the SAT data can be found here for [2017](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/), [2018](https://blog.prepscholar.com/average-sat-scores-by-state-most-recent), and [2019](https://blog.prepscholar.com/average-sat-scores-by-state-most-recent).

The source for the ACT data can be found [here](https://blog.prepscholar.com/act-scores-by-state-averages-highs-and-lows).

### Data Dictionary 
#### For [Merged Data Set](../data/final.csv):
Column|Data Type| Description
-|-|-
state| String| State name
sat17_participation|Float|Proportion of graduates who participated in the SAT in 2017
sat17_eb_reading_writing|Integer|Average score on the Evidence-Based Reading and Writing test of the SAT in 2017
sat17_math|Integer|Average score on the Math test of the SAT in 2017
sat17_total|Integer|Average score on the SAT in 2017
act17_participation|Float|Proportion of graduates who participated in the ACT in 2017
act17_english|Float|Average score on the English test of the ACT in 2017
act17_math|Float|Average score on the Math test of the ACT in 2017
act17_reading|Float|Average score on the Reading test of the ACT in 2017
act17_science|Float|Average score on the Science test of the ACT in 2017
act17_composite|Float|Average composite score on the ACT in 2017
sat18_participation|Float|Proportion of graduates who participated in the SAT in 2018
sat18_eb_reading_writing|Integer|Average score on the Evidence-Based Reading and Writing test of the SAT in 2018
sat18_math|Integer|Average score on the Math test of the SAT in 2018
sat18_total|Integer|Average score on the SAT in 2018
act18_participation|Float|Proportion of graduates who participated in the ACT in 2018
act18_composite|Float|Average composite score on the ACT in 2018
sat19_participation|Float|Proportion of graduates who participated in the SAT in 2019
sat19_eb_reading_writing|Integer|Average score on the Evidence-Based Reading and Writing test of the SAT in 2019
sat19_math|Integer|Average score on the Math test of the SAT in 2019
sat19_total|Integer|Average score on the SAT in 2019
act19_participation|Float|Proportion of graduates who participated in the ACT in 2019
act19_composite|Float|Average composite score on the ACT in 2019

## Key Findings
* From 2017 to 2019, nationwide, the median participation rate for the SAT increased from 38% to 54%. Highest growth was seen from 2017 to 2018.
* From 2017 to 2019, nationwide, the median participation rate for the ACT decreased from 69% to 54%.
* In 2017, Michigan was the only midwestern state to have 100% participation on the SAT, but by 2019, Illinois had also joined the list. 
* Although variability of SAT participation in the midwestern states increased from 2017 to 2019, the median participation was stable.

## Recommendations
* In order to increase SAT participation in midwest states, we can learn lessons from the ACT to SAT transitions that happened in Michigan and Illinois.
* Illinois announced a switch from the ACT to the SAT in 2016 [(7)](https://www.chicagotribune.com/news/ct-illinois-chooses-sat-met-20160211-story.html). Officials from Illinois State Board of education cited cost, test preparations materials, and exam content as motivators for the switch [(7)](https://www.chicagotribune.com/news/ct-illinois-chooses-sat-met-20160211-story.html). Opponents of the change cited previous exposure to ACT test preparation and students' comfort with the ACT as evidence against the switch [(8)](https://www.chicagotribune.com/news/breaking/ct-iillinois-act-exam-met-20170414-story.html).
* Michigan announced a switch from the ACT to the SAT in 2015, citing cost as the leading catalyst for the change. Though, content was also stated as a factor in the switch [(9)](https://www.hollandsentinel.com/article/20150107/News/150109433). Opponents of the SAT worried that current curriculums did not adequately prepare students for SAT content, that college admissions could be impacted by the change, and that comparisons between the SAT and ACT could be difficult [(9](https://www.hollandsentinel.com/article/20150107/News/150109433)-[10)](https://www.detroitnews.com/story/news/local/michigan/2015/01/07/michigan-schools-sat-act/21388179/).
* In order to increase participation among midwestern states, I recommend that the College Board emphasize the cost of testing as well as the benefits that come with administering the SAT, such as test preparation with Khan Academy and fee waivers. 
* Additionally, effort should be made to compare the SAT with the ACT and emphasize similarities.


## References
1. [Balf, T. (2014, March 6). The Story Behind the SAT Overhaul. *The New York Times*.](https://www.nytimes.com/2014/03/09/magazine-the-story-behind-the-sat-overhaul.html)
2. [Anderson, N. (2014, March 16). SAT usage declined in 29 states over seven years. *The Washington Post*.](https://www.washingtonpost.com/local/education/sat-usage-declined-in-29-states-over-7-years/2014/03/15/f4504cfc-a5ff-11e3-8466-d34c451760b9_story.html)
3. [College Board. (2018, May 7). The College Board and Khan Academy Team Up for Better SAT Prep. [Blog Post].](https://blog.collegeboard.org/college-board-khan-academy-for-better-sat-prep)
4. [SAT Fee Waivers. (2020, June 08).](https://collegereadiness.collegeboard.org/sat/register/fees/fee-waivers)
5. [Green Test Prep. Why is the new SAT even here?](https://greentestprep.com/resources/sat-prep/new-sat-march2016/why-is-the-college-board-changing-the-sat/)
6. [Study Point. SAT and ACT Test Popularity - Whiich test is more popular in your state?](https://www.studypoint.com/ed/sat-and-act-test/)
7. [Rado, D. (2016, February 11). Illinois moves ahead with new testing plan, replacing ACT with SAT. *Chicago Tribune*](https://www.chicagotribune.com/news/ct-illinois-chooses-sat-met-20160211-story.html)
8. [Rado, D. (2017, April 17). As state switches to SAT exam, some distriricts also paying to offer ACT. *Chicago Tribune*](https://www.chicagotribune.com/news/breaking/ct-iillinois-act-exam-met-20170414-story.html)
9. [Biolchini, A. (2015, January 7). Michigan to switch from ACT to SAT for high school juniors. *Holland Sentinel*](https://www.hollandsentinel.com/article/20150107/News/150109433)
10. [Lewis, S. (2015, January 7). Michigan to drop ACT for the SAT. *The Detroit News*](https://www.detroitnews.com/story/news/local/michigan/2015/01/07/michigan-schools-sat-act/21388179/)












