![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)

# OpenAI Paper - GDPVAL: EVALUATING AI MODEL PERFORMANCE
ON REAL-WORLD ECONOMICALLY VALUABLE TASKS

## Overview of the Paper

Source: [Link to Paper](https://arxiv.org/pdf/2510.04374)

```
GDPval covers the top 9 sectors contributing to U.S.
GDP (Gross Domestic Product), with at least 30 tasks per occupation in the full set (and 5 tasks per
occupation in the gold subset), across 44 occupations. Each task is constructed based on actual work
product created by an expert professional. Given the complexity of automatically grading these
tasks, our primary evaluation metric is head-to-head human expert comparison. 
```
-----------------------------
```
GDPval full set covers 1,320 tasks
across 44 occupations, sourced to cover the majority of Work Activities tracked by O*NET
for each occupation U.S. Department of Labor, Employment and Training Administration
(2024).
```
------------------------------------
```
To measure the potential for impact on occupations we define a holistic AI applicability score for each
occupation, where a higher score for an occupation means it is more likely to be impacted than an occupation
with a lower score. The score captures whether AI is being used (with sufficient activity share) for the work
activities of an occupation and whether that usage tends to be successful (completion rate) and cover a
moderate share of the work activity (scope), which we describe in turn.
```

**Notes**
- For this review, we're not going to go into the comparison to the prediction paper.
- I still don't know the difference between "coverage" and "scope"

## Background Information

- The paper covers only Microsoft Copilot
- The data is specific to US users (due to O\*NET being US focussed)


### Bureau of Labor and Statistics (BLS) Data Overview

- Standard Occupational Classification (SOC) - [https://www.bls.gov/soc/](https://www.bls.gov/soc/) 
- [SOC Structure](https://www.bls.gov/soc/2018/soc_structure_2018.pdf)
- [SOC Definitions](https://www.bls.gov/soc/2018/soc_2018_definitions.pdf)
- BLS also provided data used for number of people for each occupation, as well as wage data.


### O\*NET Overview

- Anyone have to take a caree aptitude test before?
- [https://www.onetonline.org/](https://www.onetonline.org/)
- Taxonomy - look at the paper top of page 4. It does a better job than the O*NET information
- Education Requirements are also pulled from this data
- The tasks associated with an occupation include relevance and importance metrics that are used in the paper.


# Discussion

- Biggest takeaway for me is that this framework could likely be used for additional research for other generative models and techniques.
- Major points from the Discuss section of the paper
- Open the floor for comments and questions
