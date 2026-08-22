---
title: "China's humanoid robots are on factory lines, but not at factory scale"
date: "2026-08-22T00:00:00.000Z"
legacy_url: "/2026/08/china-humanoid-robots-factory-deployments-2026.html"
research_id: "AR_1002"
author: "df"
labels:
  - "Robotics"
  - "AI"
  - "Manufacturing"
  - "China"
description: "A practical look at China's real humanoid robot factory deployments, the tasks they perform, and the evidence still needed to prove factory-scale value."
---

<p class="article-lead">China can now build and ship humanoid robots in volume. A smaller group has also crossed the more important boundary: performing narrow, measurable work on live electronics and battery production lines. That is real progress, but it is not yet factory-scale replacement of human labour.</p>

<figure class="article-figure">
  <img src="/assets/images/original/2026/08/china-humanoid-robots-factory-deployments-2026/china-humanoid-robots-factory-deployments-2026.webp" alt="Two wheeled humanoid robots load tablet devices into test fixtures on a modern electronics production line" width="1536" height="1024" />
  <figcaption>Industrial humanoids are finding value in narrow production tasks. Original AI-generated illustration.</figcaption>
</figure>

> **Evidence cutoff: 22 August 2026.** Deployment figures below are dated snapshots. Most operating metrics are reported by robot suppliers or their customers, not independently audited.

## Quick read

- **The practical deployment is real.** Named robots are loading tablets into test fixtures, handling battery cells, and moving materials on live production lines.
- **The useful robot is often wheeled.** Long battery life, stable positioning, and reliable arms matter more than walking when the floor is flat.
- **Shipments are not deployments.** Omdia estimated that Chinese makers shipped about 18,500 humanoid robots globally in the first half of 2026, but many units still go to research, demonstrations, training, and entertainment.
- **The best public evidence is still narrow.** AgiBot's Longcheer deployment publishes useful task and uptime data. CATL and SAIC-GM confirm live tasks but disclose less operational detail.
- **Return on investment remains the missing result.** Public sources rarely show labour saved, intervention cost, maintenance cost, or cost per good unit over several months.

The fair conclusion is that China has moved beyond factory demonstrations, but has not yet proved broad, repeatable factory economics.

## What is actually working

<div class="wide-table-wrap">
<table class="wide-table" aria-label="Named Chinese humanoid robot factory deployments">
  <thead>
    <tr>
      <th scope="col">Factory and robot</th>
      <th scope="col">Work performed</th>
      <th scope="col">Evidence stage</th>
      <th scope="col">What is public</th>
      <th scope="col">Main gap</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Longcheer tablet plant, AgiBot G2</td>
      <td>Loads and unloads tablets at test stations; sorts passed and failed devices</td>
      <td>Live production</td>
      <td>AgiBot reports multiple robots, up to 310 units per hour, 19 to 20 second cycles, and more than 140 cumulative operating hours</td>
      <td>Metrics are supplier-reported; no full cost or multi-month reliability data</td>
    </tr>
    <tr>
      <td>CATL battery plant, Galbot S1</td>
      <td>Material handling and picking in module and battery-pack production</td>
      <td>Regular production operation</td>
      <td>CATL confirms the robot is deployed on its intelligent production lines and describes an 8-hour battery design</td>
      <td>No public robot count, intervention rate, cycle time, or return on investment</td>
    </tr>
    <tr>
      <td>SAIC-GM Ultium Center, AgiBot A2-W</td>
      <td>Identifies, picks, and loads battery cells</td>
      <td>Live mass-production task</td>
      <td>A Shanghai government report says the robot has begun work on a battery production line</td>
      <td>Limited public operating history and no independently audited economics</td>
    </tr>
    <tr>
      <td>NIO, BYD, Zeekr and other auto plants, UBTECH Walker series</td>
      <td>Inspection, handling, logistics, sorting, and selected assembly tasks</td>
      <td>Mostly training or pilot stages</td>
      <td>UBTECH names factories and tasks; its own reports use terms such as training, field trial, and production validation</td>
      <td>Few comparable measures of sustained output, human intervention, and cost</td>
    </tr>
  </tbody>
</table>
</div>

This table also explains why videos can mislead. A robot performing one difficult action may still be a demonstration. A production deployment must repeat the action at line speed, recover from errors, coordinate with people and equipment, and remain economical.

## A useful deployment ladder

<figure class="article-svg-figure deployment-ladder" data-animate-svg>
  <button class="svg-replay" type="button" data-svg-replay aria-label="Replay the deployment ladder animation" title="Replay animation" hidden>
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="M20 11a8 8 0 1 0-2.34 5.66" />
      <path d="M20 4v7h-7" />
    </svg>
    <span>Replay</span>
  </button>
  <svg viewBox="0 0 560 680" role="img" aria-labelledby="deployment-ladder-title deployment-ladder-desc">
    <title id="deployment-ladder-title">Humanoid robot deployment ladder</title>
    <desc id="deployment-ladder-desc">Five stages progress from a controlled demonstration through factory training, a live production task, repeated fleet rollout, and proven factory return on investment.</desc>
    <path d="M72 106 V574" fill="none" stroke="#b8c7cd" stroke-width="6" stroke-linecap="round" />
    <path data-svg-link d="M72 112 V185" fill="none" stroke="#087286" stroke-width="6" stroke-linecap="round" />
    <path data-svg-link d="M72 237 V310" fill="none" stroke="#087286" stroke-width="6" stroke-linecap="round" />
    <path data-svg-link d="M72 362 V435" fill="none" stroke="#087286" stroke-width="6" stroke-linecap="round" />
    <path data-svg-link d="M72 487 V560" fill="none" stroke="#087286" stroke-width="6" stroke-linecap="round" />
    <g data-svg-step>
      <circle cx="72" cy="80" r="28" fill="#edf2f4" stroke="#5e6c77" stroke-width="3" />
      <text x="72" y="87" text-anchor="middle" fill="#18232c" font-family="ui-monospace, monospace" font-size="20" font-weight="700">1</text>
      <rect x="122" y="34" width="400" height="92" rx="12" fill="#edf2f4" stroke="#b8c7cd" stroke-width="2" />
      <text x="148" y="70" fill="#18232c" font-family="Inter, system-ui, sans-serif" font-size="22" font-weight="700">Controlled demo</text>
      <text x="148" y="100" fill="#5e6c77" font-family="Inter, system-ui, sans-serif" font-size="16">One scripted task in controlled conditions</text>
    </g>
    <g data-svg-step>
      <circle cx="72" cy="205" r="28" fill="#edf2f4" stroke="#5e6c77" stroke-width="3" />
      <text x="72" y="212" text-anchor="middle" fill="#18232c" font-family="ui-monospace, monospace" font-size="20" font-weight="700">2</text>
      <rect x="122" y="159" width="400" height="92" rx="12" fill="#edf2f4" stroke="#b8c7cd" stroke-width="2" />
      <text x="148" y="195" fill="#18232c" font-family="Inter, system-ui, sans-serif" font-size="22" font-weight="700">Factory training</text>
      <text x="148" y="225" fill="#5e6c77" font-family="Inter, system-ui, sans-serif" font-size="16">Works around real equipment in a pilot</text>
    </g>
    <g data-svg-step>
      <circle cx="72" cy="330" r="28" fill="#087286" stroke="#065969" stroke-width="3" />
      <text x="72" y="337" text-anchor="middle" fill="#ffffff" font-family="ui-monospace, monospace" font-size="20" font-weight="700">3</text>
      <rect x="122" y="284" width="400" height="92" rx="12" fill="#e5f2f4" stroke="#087286" stroke-width="3" />
      <text x="148" y="320" fill="#18232c" font-family="Inter, system-ui, sans-serif" font-size="22" font-weight="700">Live production task</text>
      <text x="148" y="350" fill="#087286" font-family="Inter, system-ui, sans-serif" font-size="16" font-weight="700">Repeated work at production-line speed</text>
    </g>
    <g data-svg-step>
      <circle cx="72" cy="455" r="28" fill="#edf2f4" stroke="#5e6c77" stroke-width="3" />
      <text x="72" y="462" text-anchor="middle" fill="#18232c" font-family="ui-monospace, monospace" font-size="20" font-weight="700">4</text>
      <rect x="122" y="409" width="400" height="92" rx="12" fill="#edf2f4" stroke="#b8c7cd" stroke-width="2" />
      <text x="148" y="445" fill="#18232c" font-family="Inter, system-ui, sans-serif" font-size="22" font-weight="700">Repeated fleet rollout</text>
      <text x="148" y="475" fill="#5e6c77" font-family="Inter, system-ui, sans-serif" font-size="16">Multiple robots, lines, or customer sites</text>
    </g>
    <g data-svg-step>
      <circle cx="72" cy="580" r="28" fill="#b44a35" stroke="#8c3829" stroke-width="3" />
      <text x="72" y="587" text-anchor="middle" fill="#ffffff" font-family="ui-monospace, monospace" font-size="20" font-weight="700">5</text>
      <rect x="122" y="534" width="400" height="92" rx="12" fill="#f6ebe7" stroke="#b44a35" stroke-width="3" />
      <text x="148" y="570" fill="#18232c" font-family="Inter, system-ui, sans-serif" font-size="22" font-weight="700">Proven factory ROI</text>
      <text x="148" y="600" fill="#b44a35" font-family="Inter, system-ui, sans-serif" font-size="16" font-weight="700">Customer-verified cost, uptime, and safety</text>
    </g>
    <text x="280" y="656" text-anchor="middle" fill="#5e6c77" font-family="ui-monospace, monospace" font-size="14">Public evidence is strongest at stages 2 and 3</text>
  </svg>
  <figcaption>The evidence improves as a robot moves from a repeatable action to repeatable customer economics.</figcaption>
</figure>

Most public Chinese examples sit at stages 2 and 3. Longcheer provides some evidence toward stage 4 because multiple robots have worked inside the production system and AgiBot broadcast a six-day validation. The company reported more than 64 operating hours, 64,828 tasks, and 17,625 units of line output during that event.

Those figures are more useful than a dance or a lifting demonstration, but they do not complete stage 5. A six-day run does not reveal annual maintenance, spare-part use, integration cost, or the number of operator interventions hidden behind a high task-success rate.

## Why wheels are winning practical work

The word "humanoid" often suggests a machine with two arms and two legs. The strongest production examples use a different compromise: a human-like upper body on a wheeled base.

That design makes sense on a factory floor:

- wheels use less energy than walking on flat ground;
- a wide base is stable during precise dual-arm work;
- a larger battery and computer can sit low in the chassis;
- navigation is easier in marked aisles; and
- the robot can reach workstations designed for standing people without needing to balance on every movement.

A biped still matters where stairs, floor obstacles, or human-shaped access make wheels impractical. For today's tablet, battery, and logistics lines, reliable manipulation is usually the harder and more valuable problem.

## The Longcheer case is the one to watch

AgiBot's G2 at Longcheer's Nanchang tablet factory is the clearest public test of the current model. The robots move tablets into multimedia test fixtures, remove them after testing, and sort the result. It is repetitive work, but the production mix and device positions can change.

AgiBot reported that integration took 36 hours, production reached about 3,000 units per shift, and downtime loss stayed below 4 percent over more than 140 cumulative hours. In June, the company followed with the six-day live-line broadcast.

All of those numbers come from AgiBot. They should be treated as a strong vendor case study, not an independent benchmark. The next useful disclosure would be a customer-verified comparison against the previous process: cost per unit, interventions per shift, output quality, changeover time, and payback period.

## China has a scale advantage, but the denominator matters

[Associated Press reported](https://apnews.com/article/f33facc61122faf0c0b08af5020bd170) Omdia's estimate of about 18,500 global shipments by Chinese humanoid makers in the first half of 2026. Official Chinese data also counted more than 140 domestic manufacturers and more than 330 models in 2025.

That is a manufacturing and supply-chain advantage. It lowers hardware cost, increases the amount of field data, and gives suppliers access to many possible factory partners. It does not tell us how many robots are doing productive work each day.

The denominator should be **paid productive hours**, not robots leaving a factory. A unit sold to a university, showroom, gala, data-collection centre, or internal development team is a valid shipment, but not evidence of industrial return.

## What factory-scale proof should include

| Measure | Why it matters |
| --- | --- |
| Productive hours per month | Separates sustained work from a short validation run |
| Human interventions per 1,000 cycles | Exposes how much supervision the autonomy still needs |
| Good units per hour | Connects robot activity to saleable factory output |
| Changeover time between products | Tests the flexibility advantage over fixed automation |
| Maintenance and spare-part cost | Captures the cost of keeping a complex body available |
| Total cost per good unit | Allows a fair comparison with people and conventional automation |
| Repeat deployment time | Shows whether one successful cell can scale to another line or factory |
| Safety events and near misses | Tests whether people and robots can share production space reliably |

Companies do not need to publish every commercial detail. A consistent subset of these measures, verified by named customers over six to twelve months, would make the case far stronger than shipment totals.

## Overall assessment

China's humanoid robot industry has crossed an important boundary. Live production tasks now exist at named electronics, battery, and automotive plants. The Longcheer case is particularly credible because it exposes a defined task and several operating measures rather than only a video clip.

The caveat is equally important. Today's success is task-specific, often wheeled, and supported by factory integration teams. Public evidence does not yet show general-purpose humanoids moving freely between many jobs or earning a proven return across large fleets.

The next race is therefore not about the most acrobatic robot. It is about the first supplier that can publish repeatable customer results for uptime, intervention rate, cost per good unit, and deployment time.

---

### Sources

| External source | Used for | Important limitation |
| --- | --- | --- |
| [Associated Press: Unitree listing and shipment estimates](https://apnews.com/article/f33facc61122faf0c0b08af5020bd170) | Omdia shipment estimate and independent ROI caveat | Shipments cover several end uses and do not measure productive deployments |
| [AgiBot: Longcheer production deployment](https://www.agibot.com/article/231/detail/60.html) | Task, cycle, throughput, integration, and operating figures | Supplier case study; figures are not independently audited |
| [AgiBot: six-day factory validation](https://www.agibot.com/article/231/detail/83.html) | Longer live-line task and output figures | Supplier-reported event rather than a multi-month customer audit |
| [CATL: Galbot S1 goes live](https://www.catl.com/en/news/6881.html) | Customer confirmation of battery-line material handling | No detailed economics or sustained output measures |
| [Shanghai Pudong government: AgiBot at SAIC-GM](https://english.pudong.gov.cn/2026-04/08/c_1175033.htm) | Confirmation of battery-line production work | Brief report with limited operating metrics |
| [UBTECH: industrial application cases](https://www.ubtrobot.com/en/humanoid/solutions/industry) | Named automotive partners, tasks, and deployment stages | First-party overview combines training, validation, and deployment examples |
| [China government: humanoid industry count](https://big5.www.gov.cn/gate/big5/www.gov.cn/zhengce/202601/content_7055631.htm) | Number of domestic makers and models in 2025 | Industry breadth does not establish commercial success |
