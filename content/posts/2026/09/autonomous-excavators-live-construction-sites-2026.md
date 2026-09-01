---
title: "Autonomous excavators are digging on live sites. What is actually proven?"
date: "2026-09-01T00:00:00.000Z"
legacy_url: "/2026/09/autonomous-excavators-live-construction-sites-2026.html"
research_id: "AR_1006"
author: "df"
labels:
  - "Robotics"
  - "Construction"
  - "Autonomous Systems"
  - "Infrastructure"
description: "Bedrock says operator-out excavators are working on three US projects. Here is the deployment ladder, safety claim and data still missing."
---

<p class="article-lead">An autonomous excavator has crossed an important boundary: from a controlled demonstration into reported production work on named customer sites. The machine can dig without an operator in the cab, but people still define the job, manage the site and decide whether the system is ready to work.</p>

## Quick read

- **Live projects:** Bedrock Robotics says its retrofitted excavators are working operator-out on three US projects with Sundt, Champion Site Prep and Zachry.
- **Not a new excavator:** the Bedrock Operator is installed on existing machines. A site manager provides the initial plan, then the system perceives, plans and moves the excavator.
- **Safety claim:** Bedrock says the excavator stops if a person or unauthorised object comes too close. No public safety-case report or intervention rate accompanies that claim.
- **The caveat:** the deployment is more convincing than a lab demo, but public sources still lack comparable productivity, fuel, rework, incident and whole-job cost data.

<figure class="article-figure">
  <img src="/assets/images/original/2026/09/autonomous-excavators-live-construction-sites-2026/autonomous-excavator.svg" alt="Simplified illustration of a supervised construction site with an autonomous excavator working inside a monitored zone" width="960" height="540" />
  <figcaption>An original illustration of the work split: a manager defines the task, the excavator works inside a monitored area, and the site team remains responsible. It is not a drawing of Bedrock's exact hardware or safety system.</figcaption>
</figure>

## What changed in August

On 17 August 2026, [Bedrock announced](https://www.globenewswire.com/news-release/2026/08/17/3346247/0/en/bedrock-robotics-launches-first-fully-autonomous-excavator-deployments-on-critical-u-s-infrastructure-projects.html) that excavators fitted with its system were operating fully autonomously on live customer sites. The company calls these **operator-out deployments**.

The announcement names real contractors and project scopes:

| Contractor and project | What is public and missing |
| --- | --- |
| Sundt Construction: Nevada water-treatment facility | Customer and project type are named. Exact site and production data are not disclosed. |
| Champion Site Prep: Texas earthwork site measuring several million cubic yards | State, contractor and scale are named. Autonomous share and completed volume are not disclosed. |
| Zachry Construction: 1.2 million cubic yard civil sitework project | Contractor and project size are named. Location and autonomous share are not disclosed. |

These are the company's deployment claims, supported by an attributed comment from Sundt's CEO. They are not independent audits. Bedrock also calls the milestone an industry first. That is a company claim, not something the available sources settle across every construction market and private project.

## The deployment ladder matters

Autonomy is not one switch. Bedrock's own reporting shows a progression:

| Stage | Human role and evidence |
| --- | --- |
| Testing on active sites | Human supervision throughout. Bedrock says this ran for about a year. |
| Large supervised deployment | People supervise repetitive excavation. Bedrock reports more than 70,000 cubic yards moved on a 130-acre manufacturing site. |
| Operator-out deployment | No operator in the cab; the site team still sets and manages the work. Three customer projects were named in August 2026. |
| Coordinated autonomous fleet | Machines would plan and sequence work across equipment types. This is a roadmap, not the current product result. |

The earlier supervised figure is useful because it shows repeated work at useful scale. It must not be presented as the output of the newer operator-out deployments. Bedrock also says its systems had been installed on excavators from **20 to 80 tons** before the August milestone. [Bedrock deployment update](https://bedrockrobotics.com/news/we-shouldnt-have-to-choose-what-gets-built)

## How the work is divided

Bedrock describes a same-day retrofit that adds sensing and computing without permanently changing the excavator. Once a site manager sets the initial plan, the machine-learning system perceives the area, plans motion and executes the excavation. [Deployment announcement](https://www.globenewswire.com/news-release/2026/08/17/3346247/0/en/bedrock-robotics-launches-first-fully-autonomous-excavator-deployments-on-critical-u-s-infrastructure-projects.html)

That division is important:

| Site team still owns | Autonomous system performs |
| --- | --- |
| Define the task and permitted work area | Interpret its immediate environment |
| Coordinate trucks, people and other equipment | Plan excavator motion for the assigned task |
| Inspect conditions and manage exceptions | Dig and load without continuous cab control |
| Apply site safety rules and stop work when needed | Stop automatically when its system detects a close person or unauthorised object |

The final row is Bedrock's description, not a published test result. The announcement does not disclose detection distance, difficult-object cases, false alarms, missed detections or the conditions that require a person to intervene.

It also says the excavators can work beside other equipment without operational barriers. That is a stronger claim than operating inside an isolated enclosure, and it deserves stronger evidence. Public information currently explains the intended behaviour but not the validation protocol.

## See the real machines

The original field photographs and videos are useful because they show ordinary excavators, trucks, workers and dusty sites rather than a laboratory rig. They remain on their publishers' pages because no open republication licence was identified.

| Source | What it shows and its limit |
| --- | --- |
| [Bedrock field update](https://bedrockrobotics.com/news/we-shouldnt-have-to-choose-what-gets-built) | Workers watch a Bedrock-equipped excavator load a truck. This is earlier supervised work, not proof of operator-out performance. |
| [Engineering News-Record](https://www.enr.com/articles/61982-bedrock-robotics-excavators-remove-65-000-cubic-yards-of-dirt-on-southwest-project) | An excavator and human-driven truck work together on a large site. This is independent field photography of an earlier supervised deployment. |
| [Bedrock partner page](https://bedrockrobotics.com/partners) | On-site videos and contractor comments, including Sundt. It is vendor-hosted customer material, not measured performance. |

## The numbers needed next

Moving dirt is not enough. A production system must improve the whole job, including setup, exceptions and rework. None of the following results was published for the August operator-out deployments.

| Missing metric | Why it matters |
| --- | --- |
| Operator interventions per shift | Reveals how close the job is to sustained autonomy |
| Completed load cycles per hour | Allows a fair comparison with skilled manual operation |
| Setup and remapping time | Captures work outside the digging cycle |
| Fuel per cubic yard | Tests whether smoother automation also saves energy |
| Grade accuracy and rework | Measures usable output, not just material moved |
| Detected hazards, emergency stops and incidents | Tests the safety claim under real site conditions |
| Cost per accepted cubic yard | Combines hardware, support, people, delays and rework |

A useful comparison should match machine class, material, haul pattern, weather and target grade. Otherwise a faster cycle on easy soil can be mistaken for a generally better system.

## My evidence verdict

**What is proven publicly:** Bedrock has named contractors and live project scopes, shown a path through large supervised work, and announced operator-out excavation on customer sites.

**What is not proven publicly:** that the system is safer, cheaper or more productive than skilled operation across a complete project.

That is still meaningful progress. Construction autonomy becomes valuable when it can handle repetitive earthwork while experienced people manage plans, exceptions and mixed-site coordination. The next milestone should be a boring one: several months of comparable operational data, including the difficult shifts.

Heavy equipment remains hazardous. An autonomous control system does not remove the need for qualified site management, exclusion rules, inspections and emergency procedures. This article is an evidence review, not operating guidance.

*Sources checked on 1 September 2026.*

## Sources and further reading

| External source | What it supports |
| --- | --- |
| [Bedrock deployment announcement](https://www.globenewswire.com/news-release/2026/08/17/3346247/0/en/bedrock-robotics-launches-first-fully-autonomous-excavator-deployments-on-critical-u-s-infrastructure-projects.html) | Named operator-out projects, retrofit description and safety claims |
| [Bedrock field update](https://bedrockrobotics.com/news/we-shouldnt-have-to-choose-what-gets-built) | Earlier supervised volume, site scale and machine-size range |
| [Bedrock partner page](https://bedrockrobotics.com/partners) | Contractor statements, field videos and product positioning |
| [Bedrock technology page](https://bedrockrobotics.com/technology) | High-level control and progress-monitoring description |
| [Engineering News-Record field report](https://www.enr.com/articles/61982-bedrock-robotics-excavators-remove-65-000-cubic-yards-of-dirt-on-southwest-project) | Independent field photography of an earlier supervised deployment |
| [Bedrock media page](https://bedrockrobotics.com/media-and-press) | Media contact and image-rights route |
