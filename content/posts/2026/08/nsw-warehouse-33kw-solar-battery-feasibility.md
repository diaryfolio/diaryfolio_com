---
title: "Does a battery make sense for a warehouse with 33 kW of solar?"
date: "2026-08-25T00:00:00.000Z"
legacy_url: "/2026/08/nsw-warehouse-33kw-solar-battery-feasibility.html"
research_id: "AR_1003"
author: "df"
labels:
  - "Energy Storage"
  - "Solar"
  - "Australia"
  - "Business"
description: "A practical NSW warehouse battery guide covering interval data, 22-200 kWh sizing, commercial products, incentives, payback, safety, and grid approval."
---

<p class="article-lead">A 33 kW solar array does not tell you what size battery to buy. The useful number is the solar left after the warehouse has consumed power during the day, matched against imports later in the day. For many warehouses, twelve months of interval meter data will save more money than starting with battery quotations.</p>

<figure class="article-figure">
  <img src="/assets/images/original/2026/08/nsw-warehouse-33kw-solar-battery-feasibility/nsw-warehouse-solar-commercial-battery.webp" alt="Commercial battery cabinet beside the electrical-services area of a warehouse with rooftop solar" width="960" height="640" />
  <figcaption>A commercial battery needs a complete site design, not just spare wall space. Original AI-generated image.</figcaption>
</figure>

> **Evidence cutoff: 25 August 2026.** Prices below are screening assumptions, not quotations. Product specifications, incentive rules and network requirements must be checked again before ordering.

## Quick read

- **Measure first.** Obtain 12 months of 5, 15 or 30 minute import, export and solar data, along with the complete electricity tariff.
- **Start around 44-66 kWh only when the data supports it.** That range is a reasonable first quotation target if the site regularly exports enough solar and imports 40-70 kWh during the evening.
- **Energy shifting alone may not repay the system quickly.** Demand-charge reduction can be equally important, but only when the battery can reliably avoid the billed peak.
- **A 100-200 kWh cabinet needs stronger evidence.** It may fit a larger evening load, sharp demand peaks or planned expansion, but is likely oversized for solar shifting from 33 kW of PV.
- **Tesla Megapack does not fit this case.** A single unit stores roughly 3.9 MWh, almost 39 times a 100 kWh candidate.

The practical answer is conditional: quote a 44-66 kWh system only after interval data confirms both a charge source and a later load. Otherwise, no battery may be the better investment.

## Collect these numbers first

| Required input | What it decides | Minimum useful evidence |
| --- | --- | --- |
| Grid import and export | Chargeable solar surplus and later grid demand | 12 months of interval data |
| Solar generation | Actual output, seasonality and faults | Inverter export or monitoring file |
| Retail energy rates | Value of each shifted kWh | Current contract and bills |
| Demand-charge rule | Value and timing of peak shaving | Rate, measurement window and monthly method |
| Existing equipment | Retrofit architecture and connection capacity | Single-line diagram, inverter and switchboard models |
| Critical loads | Whether backup has business value | Load list, phase, starting current and required runtime |
| Site and fire constraints | Safe location and project cost | Site plan and qualified risk review |

The warehouse location also determines whether the distribution network is Ausgrid, Endeavour Energy or Essential Energy. Each network has its own connection process. The application must include the existing and proposed inverter capacity, not just battery kWh.

## How much solar may be available

AEMO and CSIRO modelling uses a NSW rooftop-solar capacity factor of 14.6 percent. A separate AEMO/Aurecon regional NSW model uses about 17 percent. Applied mechanically to a 33 kW array, those assumptions produce this range:

| Planning case | Approximate annual generation | Daily average |
| --- | ---: | ---: |
| 14.6% capacity factor | 42.2 MWh | 116 kWh |
| 17.0% capacity factor | 49.1 MWh | 135 kWh |

These are gross averages, not battery energy. Orientation, shade, equipment condition, location, weather and winter output all matter. More importantly:

`chargeable surplus = solar generation - simultaneous warehouse load - unavoidable export`

A warehouse drawing 20-30 kW through the middle of the day may consume most of a 33 kW array even though its annual solar total looks substantial.

## Evening load sets the first capacity screen

For a five-hour evening period, the energy calculation is simple:

| Average evening load | Energy over 5 hours | Practical first capacity screen* |
| ---: | ---: | ---: |
| 5 kW | 25 kWh | About 30 kWh |
| 10 kW | 50 kWh | About 60 kWh |
| 15 kW | 75 kWh | About 90 kWh |
| 20 kW | 100 kWh | About 120 kWh |

\*The capacity screen adds a modest allowance for conversion losses, operating reserve and degradation. Final engineering must also check continuous kW, short load spikes, phase balance and motor starting current.

Capacity and power solve different problems. A 100 kWh battery with a 10 kW inverter can run for a long time but cannot clip a 30 kW demand spike. A 30 kWh battery with a 30 kW inverter can handle the spike briefly but cannot supply a large evening energy requirement.

## What one shifted kWh is worth

Use the site's real contract in the final model. The following screening case makes the arithmetic visible:

| Assumption | Value |
| --- | ---: |
| Avoided grid import | AUD 0.30/kWh |
| Solar export forgone | AUD 0.05/kWh |
| AC round-trip efficiency | 90% |
| Value of delivered battery energy | AUD 0.244/kWh |

The formula is:

`value = import price - (export price / round-trip efficiency)`

IPART's 2026-27 all-day export benchmark is 3.4-6.5 cents/kWh, but a commercial contract may differ. The full retail plan matters more than a headline feed-in tariff.

### Energy-shift value by cycling level

| Usable battery capacity | 100 cycles/year | 200 cycles/year | 300 cycles/year |
| ---: | ---: | ---: | ---: |
| 22.1 kWh | AUD 540 | AUD 1,080 | AUD 1,621 |
| 44.2 kWh | AUD 1,080 | AUD 2,161 | AUD 3,241 |
| 66.3 kWh | AUD 1,621 | AUD 3,241 | AUD 4,862 |
| 100 kWh | AUD 2,444 | AUD 4,889 | AUD 7,333 |
| 200 kWh | AUD 4,889 | AUD 9,778 | AUD 14,667 |

The table assumes every cycle can be charged and discharged usefully. That is unlikely for an oversized battery. A 200 kWh system cannot achieve 300 solar cycles if the site does not export 60 MWh of suitable solar each year.

### Demand savings can change the result

If the electricity contract bills monthly demand at AUD 20/kW, the theoretical annual saving is:

| Peak reduction maintained in every billing month | Maximum annual demand saving |
| ---: | ---: |
| 5 kW | AUD 1,200 |
| 10 kW | AUD 2,400 |
| 20 kW | AUD 4,800 |

This saving is less forgiving than energy shifting. One short peak after the battery has emptied can set the monthly bill. The control system needs load forecasting, a state-of-charge reserve and enough inverter power to clip the qualifying peak.

## Indicative cost and payback screen

Australian Renewable Energy Agency project data shows why a single dollars-per-kWh rule is unsafe. Sampled battery projects ranged from AUD 0.73 to AUD 4.10 per Wh, while non-network behind-the-meter proposals had a weighted average around AUD 1.33 per Wh. Switchboard, transformer, civil, metering, communications and fire work create much of the variation.

The following bands are planning allowances, not vendor prices:

<div class="wide-table-wrap">
<table class="wide-table" aria-label="Indicative battery cost and simple payback screening table">
  <thead>
    <tr>
      <th scope="col">Capacity</th>
      <th scope="col">Gross installed screen</th>
      <th scope="col">Energy value at 200 cycles</th>
      <th scope="col">Simple payback after illustrative 30% discount*</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>22.1 kWh</td><td>AUD 25k-45k</td><td>AUD 1,080/year</td><td>16-29 years</td></tr>
    <tr><td>44.2 kWh</td><td>AUD 45k-75k</td><td>AUD 2,161/year</td><td>15-24 years</td></tr>
    <tr><td>66.3 kWh</td><td>AUD 65k-105k</td><td>AUD 3,241/year</td><td>14-23 years</td></tr>
    <tr><td>100 kWh</td><td>AUD 95k-160k</td><td>AUD 4,889/year</td><td>14-23 years</td></tr>
    <tr><td>200 kWh</td><td>AUD 160k-280k</td><td>AUD 9,778/year</td><td>11-20 years</td></tr>
  </tbody>
</table>
</div>

\*The 30 percent reduction is a sensitivity, not a promised rebate. Existing-solar-only projects may receive less. The payback excludes demand savings, degradation, maintenance, finance, tax, replacement and residual value.

Energy-only economics are not compelling in this model. A verified 10 kW demand reduction would add AUD 2,400/year and could materially improve a smaller system's result. Resilience can add business value too, but only when outage costs and the protected-load design are quantified.

## BYD and the commercial alternatives

Compare complete systems, not battery modules. The inverter, switchgear, energy management, backup equipment, warranty and local service are part of the product.

<div class="wide-table-wrap">
<table class="wide-table" aria-label="Commercial battery product families compared for the warehouse case">
  <thead>
    <tr>
      <th scope="col">Product family</th>
      <th scope="col">Published capacity and power</th>
      <th scope="col">Fit for this case</th>
      <th scope="col">What to verify</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BYD Battery-Box Premium HVM</td>
      <td>22.1 kWh per maximum-size tower; up to three matching towers. HVM 22.1 battery rating is 20.48 kW.</td>
      <td><strong>Plausible for 22, 44 and 66 kWh quotations</strong></td>
      <td>Compatible three-phase inverter, complete-system power, current approvals and parallel warranty</td>
    </tr>
    <tr>
      <td>GoodWe BAT-C</td>
      <td>About 60, 90 or 110 kWh usable; paired with 15-50 kW hybrid inverters</td>
      <td><strong>Plausible small C&I alternative</strong></td>
      <td>Exact inverter combination, backup scope and installed system efficiency</td>
    </tr>
    <tr>
      <td>Sigenergy SigenStack</td>
      <td>12.06 kWh modules; roughly 48-253 kWh; 50, 99.9 or 110 kW inverter range</td>
      <td>Capacity fits, but the smallest published C&I inverter may be large</td>
      <td>Site power match, Australian approval, service support and net cost</td>
    </tr>
    <tr>
      <td>AlphaESS STORION-T50/T100</td>
      <td>50 or 100 kVA; published battery configurations from about 62 kWh</td>
      <td>Possible commercial alternative</td>
      <td>Current Australian product combination, installer support and warranty response</td>
    </tr>
    <tr>
      <td>Huawei LUNA2000-215</td>
      <td>108 kW / 215 kWh; stated 91.3% maximum cycle efficiency</td>
      <td>Probably oversized for solar shifting</td>
      <td>Demand-management case, auxiliary load, approvals and local project support</td>
    </tr>
    <tr>
      <td>Sungrow PowerStack 200CS</td>
      <td>110 kW / 229 kWh; stated 90% system round-trip efficiency</td>
      <td>Probably oversized unless demand or expansion justifies it</td>
      <td>Fire design, network connection, civil work and binding installed price</td>
    </tr>
    <tr>
      <td>Tesla Megapack</td>
      <td>About 979 kW / 3,916 kWh in the four-hour Megapack 2 XL reference</td>
      <td><strong>Reject for this single warehouse</strong></td>
      <td>Only revisit for a much larger multi-site, microgrid or grid-services project</td>
    </tr>
  </tbody>
</table>
</div>

The BYD and GoodWe ranges are the closest dimensional fits. That does not make either a universal winner. A quote can lose on switchboard work, inverter compatibility, warranty exclusions or service coverage even when the battery capacity looks right.

## Choose the three-phase architecture

<div class="wide-table-wrap">
<table class="wide-table" aria-label="Three-phase battery architecture comparison">
  <thead>
    <tr>
      <th scope="col">Architecture</th>
      <th scope="col">Main advantage</th>
      <th scope="col">Main cost or limitation</th>
      <th scope="col">Best fit here</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AC-coupled retrofit</td>
      <td>Keeps the existing PV inverter and separates the storage retrofit</td>
      <td>Extra AC/DC conversion and separate controls</td>
      <td>Usually the first design to quote for an existing working PV system</td>
    </tr>
    <tr>
      <td>DC-coupled hybrid</td>
      <td>Can move PV into the battery with fewer conversion steps</td>
      <td>May require replacing or redesigning the PV inverter</td>
      <td>Worth testing when the existing inverter is due for replacement or explicitly compatible</td>
    </tr>
    <tr>
      <td>Integrated C&I cabinet</td>
      <td>Packaged battery, inverter, controls and thermal management</td>
      <td>Larger minimum size, auxiliary loads, siting, fire and network work</td>
      <td>Suitable only when measured load or expansion supports 100-200 kWh or more</td>
    </tr>
  </tbody>
</table>
</div>

A grid-connected battery does not automatically provide backup. Backup requires protected loads, deliberate isolation or transfer equipment, compatible controls, phase and motor-start analysis, and commissioning under outage conditions.

## Incentives available from September 2026

| Program | Relevant boundary | Important condition |
| --- | --- | --- |
| NSW batteries for businesses | New grid-connected batteries from 20 kWh to 30 MWh | Opens 1 September 2026; use an approved provider and satisfy project rules |
| Larger NSW discount | Battery installed with qualifying new or additional solar | The new solar must satisfy the scheme's timing and size tests |
| Federal Cheaper Home Batteries | Eligible small-business systems from 5 to 100 kWh nominal | Certificates apply to the first 50 kWh of usable capacity and taper under current rules |

Existing solar can qualify for the base NSW business discount. Do not apply the 30-40 percent headline for new solar plus battery to an existing-solar-only project. Ask each installer to show the gross price, NSW discount, federal certificates, tax and net payable amount as separate lines.

## Safety and grid approval are part of the design

| Check | Why it matters |
| --- | --- |
| Current approved battery and inverter combination | Product listings can expire, change or be suspended |
| DNSP connection approval | Grid-parallel batteries affect inverter capacity, export, protection and power quality |
| AS/NZS 5139 and electrical design | Covers battery-system installation risks and interfaces with the wider installation |
| Fire separation and emergency access | Lithium-ion failure can produce thermal runaway, toxic fumes and secondary ignition |
| Workplace risk assessment and procedures | The warehouse operator retains workplace health and safety duties |
| 200 kWh threshold review | AFAC guidance specifically addresses C&I installations at 200 kWh and above |
| Maintenance and end-of-life plan | Inspection, alarms, damaged equipment, transport and recycling need named responsibilities |

At 200 kWh, involve the fire and siting specialists early. A cabinet at this scale is not merely a larger wall battery. Location, access, building separation, fire response, noise, auxiliary consumption and civil work can decide whether the project is practical.

## The useful energy flow

<figure class="article-svg-figure warehouse-energy-flow" data-animate-svg>
  <button class="svg-replay" type="button" data-svg-replay aria-label="Replay the warehouse battery energy-flow animation" title="Replay animation" hidden>
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="M20 11a8 8 0 1 0-2.34 5.66" />
      <path d="M20 4v7h-7" />
    </svg>
    <span>Replay</span>
  </button>
  <svg viewBox="0 0 720 430" role="img" aria-labelledby="warehouse-flow-title warehouse-flow-desc">
    <title id="warehouse-flow-title">Warehouse solar and battery energy flow</title>
    <desc id="warehouse-flow-desc">During the day solar serves the warehouse first, then charges the battery, with remaining energy exported. In the evening the battery serves the warehouse before the grid supplies any shortfall.</desc>
    <defs>
      <marker id="flow-arrow-teal" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
        <path d="M0,0 L0,6 L9,3 z" fill="#087286" />
      </marker>
      <marker id="flow-arrow-grey" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
        <path d="M0,0 L0,6 L9,3 z" fill="#5e6c77" />
      </marker>
    </defs>
    <rect x="18" y="38" width="330" height="350" rx="16" fill="#f6fafb" stroke="#b8c7cd" stroke-width="2" />
    <rect x="372" y="38" width="330" height="350" rx="16" fill="#f8f7f4" stroke="#b8c7cd" stroke-width="2" />
    <text x="183" y="76" text-anchor="middle" fill="#18232c" font-family="ui-monospace, monospace" font-size="18" font-weight="700">DAYTIME</text>
    <text x="537" y="76" text-anchor="middle" fill="#18232c" font-family="ui-monospace, monospace" font-size="18" font-weight="700">EVENING</text>
    <g data-svg-step>
      <circle cx="88" cy="142" r="38" fill="#fff4c7" stroke="#b88a10" stroke-width="3" />
      <path d="M88 91v-16 M88 209v-16 M37 142H21 M155 142h-16 M52 106l-12-12 M136 190l-12-12 M124 106l12-12 M40 190l12-12" stroke="#b88a10" stroke-width="4" stroke-linecap="round" />
      <text x="88" y="148" text-anchor="middle" fill="#6b4d00" font-family="ui-monospace, monospace" font-size="15" font-weight="700">SOLAR</text>
    </g>
    <g data-svg-step>
      <rect x="215" y="104" width="106" height="76" rx="10" fill="#e5f2f4" stroke="#087286" stroke-width="3" />
      <path d="M232 137h72 M239 137v27 M260 137v27 M282 137v27 M303 137v27" stroke="#087286" stroke-width="2" />
      <text x="268" y="96" text-anchor="middle" fill="#18232c" font-family="ui-monospace, monospace" font-size="14" font-weight="700">WAREHOUSE</text>
    </g>
    <path data-svg-link d="M128 142 H203" fill="none" stroke="#087286" stroke-width="5" stroke-linecap="round" marker-end="url(#flow-arrow-teal)" />
    <text x="165" y="118" text-anchor="middle" fill="#087286" font-family="ui-monospace, monospace" font-size="10">USE FIRST</text>
    <g data-svg-step>
      <rect x="72" y="254" width="124" height="88" rx="10" fill="#edf2f4" stroke="#5e6c77" stroke-width="3" />
      <rect x="110" y="241" width="48" height="13" rx="4" fill="#5e6c77" />
      <rect x="91" y="275" width="86" height="42" rx="5" fill="#ffffff" stroke="#087286" stroke-width="2" />
      <rect x="98" y="282" width="55" height="28" rx="3" fill="#8dc5ce" />
      <text x="134" y="365" text-anchor="middle" fill="#18232c" font-family="ui-monospace, monospace" font-size="14" font-weight="700">BATTERY</text>
    </g>
    <path data-svg-link d="M268 188 C268 230 205 222 169 253" fill="none" stroke="#087286" stroke-width="5" stroke-linecap="round" marker-end="url(#flow-arrow-teal)" />
    <text x="267" y="218" text-anchor="middle" fill="#087286" font-family="ui-monospace, monospace" font-size="9">CHARGE SURPLUS</text>
    <g data-svg-step>
      <path d="M254 278h48 M262 295h32 M270 312h16" stroke="#5e6c77" stroke-width="4" stroke-linecap="round" />
      <text x="278" y="342" text-anchor="middle" fill="#5e6c77" font-family="ui-monospace, monospace" font-size="14" font-weight="700">GRID EXPORT</text>
    </g>
    <path data-svg-link d="M197 298 H244" fill="none" stroke="#5e6c77" stroke-width="4" stroke-linecap="round" marker-end="url(#flow-arrow-grey)" />
    <g data-svg-step>
      <rect x="400" y="112" width="124" height="88" rx="10" fill="#edf2f4" stroke="#5e6c77" stroke-width="3" />
      <rect x="438" y="99" width="48" height="13" rx="4" fill="#5e6c77" />
      <rect x="419" y="133" width="86" height="42" rx="5" fill="#ffffff" stroke="#087286" stroke-width="2" />
      <rect x="426" y="140" width="62" height="28" rx="3" fill="#8dc5ce" />
      <text x="462" y="223" text-anchor="middle" fill="#18232c" font-family="ui-monospace, monospace" font-size="14" font-weight="700">BATTERY</text>
    </g>
    <g data-svg-step>
      <rect x="572" y="112" width="106" height="76" rx="10" fill="#e5f2f4" stroke="#087286" stroke-width="3" />
      <path d="M589 145h72 M596 145v27 M617 145v27 M639 145v27 M660 145v27" stroke="#087286" stroke-width="2" />
      <text x="625" y="104" text-anchor="middle" fill="#18232c" font-family="ui-monospace, monospace" font-size="14" font-weight="700">WAREHOUSE</text>
    </g>
    <path data-svg-link d="M526 156 H560" fill="none" stroke="#087286" stroke-width="5" stroke-linecap="round" marker-end="url(#flow-arrow-teal)" />
    <text x="543" y="126" text-anchor="middle" fill="#087286" font-family="ui-monospace, monospace" font-size="9">DISCHARGE</text>
    <g data-svg-step>
      <path d="M446 294h48 M454 311h32 M462 328h16" stroke="#5e6c77" stroke-width="4" stroke-linecap="round" />
      <text x="470" y="358" text-anchor="middle" fill="#5e6c77" font-family="ui-monospace, monospace" font-size="14" font-weight="700">GRID IMPORT</text>
    </g>
    <path data-svg-link d="M496 310 C575 306 622 268 625 201" fill="none" stroke="#5e6c77" stroke-width="4" stroke-linecap="round" marker-end="url(#flow-arrow-grey)" />
    <text x="574" y="274" text-anchor="middle" fill="#5e6c77" font-family="ui-monospace, monospace" font-size="10">TOP UP ONLY</text>
  </svg>
  <figcaption>Use solar in the warehouse first. Store genuine surplus, then discharge when it avoids a higher-value import or demand peak.</figcaption>
</figure>

## Recommendation by measured site pattern

| What the interval data shows | Recommendation | Reason |
| --- | --- | --- |
| Little regular midday export | No battery for solar arbitrage | Charging from solar would be infrequent; review efficiency and tariff first |
| 20-35 kWh regular evening import | Quote about 22-30 kWh | Small system can cycle more often without carrying unused capacity |
| 40-70 kWh regular evening import plus matching export | Quote 44-66 kWh and roughly 15-30 kW | Best initial fit for the stated medium case |
| 75-120 kWh evening import plus enough export or cheap grid charging | Model about 90-120 kWh | Larger system requires strong cycle evidence and an appropriate tariff |
| Measurable demand spikes dominate the bill | Size inverter kW first, then reserve enough kWh | Peak shaving is a power and control problem before it is an energy problem |
| Planned load growth or paid resilience justifies 200 kWh | Run a formal C&I design and fire review | Integrated cabinets may fit, but the project scope changes materially |
| Interest in Tesla Megapack for this site | Do not procure | Product power and energy are orders of magnitude above the source and load |

The likely first quote range is 44-66 kWh, not because it wins a product table, but because it aligns with a regular 40-70 kWh evening requirement while remaining chargeable from a 33 kW solar system. If the data does not show that pattern, change the recommendation.

## A procurement request that produces comparable quotes

Ask at least three qualified suppliers to price the same scope:

1. State usable battery kWh, continuous AC kW and overload capability.
2. Provide expected whole-system AC round-trip efficiency, not battery-only efficiency.
3. Include switchboard, metering, communications, civil, protection and DNSP application work.
4. Price backup separately and list the protected circuits, transfer equipment and test procedure.
5. Show gross price, each incentive, tax and net payable amount on separate lines.
6. State warranty years, cycles or throughput, retained capacity, labour, travel and response time.
7. Provide a month-by-month simulation using the supplied interval data and tariff.
8. Report savings separately for energy shifting, demand reduction, resilience and any market revenue.
9. Include degradation, maintenance and inverter or battery replacement assumptions.
10. Supply the single-line diagram, risk assessment, commissioning records and emergency information at handover.

Do not accept a payback graph that cannot be reproduced from the meter file, tariff and stated assumptions.

---

### Sources

| External source | Used for | Important limitation |
| --- | --- | --- |
| [NSW Climate and Energy Action: batteries for businesses](https://www.energy.nsw.gov.au/business-and-industry/programs-grants-and-schemes/business-equipment/batteries-businesses-incentive) | NSW eligibility, capacity range and September 2026 start | Exact discount depends on the approved quote and project |
| [Clean Energy Regulator: solar batteries](https://cer.gov.au/schemes/renewable-energy-target/small-scale-renewable-energy-scheme/small-scale-renewable-energy-systems/solar-batteries) | Federal small-business eligibility and certificate limits | Eligibility is not automatic for every warehouse configuration |
| [AEMO and CSIRO: solar PV and battery projections](https://aemo.com.au/-/media/files/major-publications/isp/2025/CSIRO-2024-Solar-PV-and-Battery-Projections-Report) | NSW rooftop-PV planning capacity factor | Not a substitute for this site's generation history |
| [AEMO and Aurecon: distributed-resource parameters](https://www.aemo.com.au/-/media/files/stakeholder_consultation/consultations/nem-consultations/2025/2025-electricity-network-options-report/aurecon-2025-generation-and-storage-technical-parameter-and-cost-report-for-distributed-resources.pdf) | Regional NSW solar-yield comparison | Regional planning archetype rather than a site model |
| [IPART: solar export benchmarks](https://www.ipart.nsw.gov.au/Home/Industries/Energy/Retail-prices/Solar-Energy) | 2026-27 export-value range | Retailers are not required to match the benchmark |
| [Ausgrid: NS194 Embedded Generation](https://www.ausgrid.com.au/asp-and-contractors/technical-document-library/ns194) | Example NSW connection and protection requirements | The site may use a different NSW distribution network |
| [Clean Energy Council: approved batteries](https://cleanenergycouncil.org.au/industry-programs/products-program/batteries) | Product-list and standards checks | Listing does not establish site suitability or service quality |
| [SafeWork NSW: lithium-ion batteries](https://www.safework.nsw.gov.au/hazards-a-z/lithium-ion-batteries) | Workplace hazards and emergency planning | General guidance, not a site-specific fire design |
| [AFAC: C&I BESS installations](https://www.afac.com.au/public-resources/battery-energy-storage-systems-commercial-and-industrial-installations) | Fire-service guidance for 200 kWh and larger systems | Authority and building requirements remain project-specific |
| [BYD: Australian HVS/HVM datasheet](https://site.bydbatterybox.com/uploads/downloads/BYD%20Battery-Box%20Premium%20HVS%26HVM%20Datasheet%20-AU%20V1.5%20EN-6262732c2b8fc.pdf) | HVM capacity, power, chemistry and warranty | Battery figures depend on a compatible complete system |
| [GoodWe Australia: BAT-C](https://www.goodwe.com.au/bat-60-112-series) | 60-110 kWh small C&I configurations | Vendor specifications need quote-time verification |
| [Sigenergy Australia: C&I system files](https://www.sigenergy.com/au/support/files/925) | SigenStack and three-phase inverter range | Site fit and local support require a binding quote |
| [AlphaESS: STORION-T50/T100](https://www.alphaess.com/storion-t50-t100-50kw-100kw-commercial-and-industrial-energy-storage-system) | Modular commercial alternative | Global page does not prove current Australian availability |
| [Sungrow: PowerStack 200CS Australia](https://www.sungrowpower.com/en/products/residential-energy-storage-system/b-st225kwh-110kw-2h-au) | 110 kW/229 kWh integrated cabinet | Vendor performance figures are configuration-specific |
| [Huawei Australia: C&I product list](https://solar.huawei.com/au/products/utility/) | LUNA2000-215 Australian listing | Public page is not an installed-price quote |
| [Tesla: Megapack system design](https://www.tesla.com/megapack/design) | Megapack 2 XL scale and efficiency | Exact Australian order configuration may differ |
| [ARENA: Community Battery Market Snapshot](https://arena.gov.au/assets/2024/11/Distributed-Energy-Integration-Community-Battery-Market-Snapshot-Report.pdf) | Broad Australian project-cost evidence | Community-battery proposals are not warehouse quotes |
