---
title: "Decision models: where D3 and Jev-style routers fit"
date: "2026-10-28T23:00:00.000Z"
legacy_url: "/2026/10/decision-models-d3-jev-routing-layer.html"
research_id: "AR_1026"
author: "df"
labels:
  - "Artificial Intelligence"
  - "Model Routing"
  - "Ollama"
  - "Decision Models"
description: "A practical guide to using compact choice, yes/no and score models as a fast routing and gating layer inside AI products."
---

<p class="article-lead">A decision model does not write the answer. It looks at application state and returns a bounded signal: choose one route, estimate whether a proposition is true, or score an ordered rubric. That makes it useful as a small control layer in front of larger models, tools and human workflows.</p>

## Quick read

- Use a decision model when the product needs a route, gate or score rather than generated prose.
- Keep authentication, permissions, spending limits and irreversible actions in deterministic application code.
- A small local model can handle narrow semantic decisions. Ambiguous or high-consequence cases should move to a stronger model or a person.
- Add an `unknown` or `human_review` route. Do not force every input into a known class.
- Tune thresholds on labelled examples from the real product. A probability of `0.8` is a signal, not a guarantee of 80 percent accuracy.

<figure class="article-figure">
  <img src="/assets/images/original/2026/10/decision-models-d3-jev-routing-layer/decision-model-routing-layer.svg" alt="Request moving through hard rules and a compact decision model to local, specialist, frontier or human routes" width="960" height="540" />
  <figcaption>A useful decision model recommends the next lane. It does not own the policy or execute the action.</figcaption>
</figure>

## What changed

Traditional classifiers already choose labels. The recent interest comes from packaging that ability for modern application state: natural-language instructions, JSON fields, several candidate routes and calibrated-looking probabilities through one API.

[Ollama added a local decision endpoint](https://ollama.com/blog/ollama-now-supports-jev-style-decision-models) in September 2026. Its `/v1/systemone` API supports three useful question shapes:

| Question type | Output | Good use |
| --- | --- | --- |
| `choice` | One option plus a probability for each option | Select one mutually exclusive route |
| `noul` | Probability that a proposition is true | Ask whether an independent condition is present |
| `score` | Weighted result across ordered levels | Estimate urgency, risk or relevance on a defined rubric |

`noul` is Ollama's name for a yes/no proposition. The useful part is not the word. It is the returned probability, which lets the application choose different thresholds for different costs.

The [D3 family](https://ollama.com/library/d3) is a current example. Ollama offers 2B, 4B, 9B and 27B classes, with the 4B model as the default. The package accepts text, structured state and still images, then returns choices, yes/no probabilities or scores without a conversational answer. The [native D3 model card](https://huggingface.co/vllm-sr/d3) also describes video support, but runtime capabilities differ. Check the package actually being deployed.

## Why the category has attracted attention

The hype is partly justified, but the models are not a new form of autonomous intelligence.

| Attraction | Practical meaning | Caveat |
| --- | --- | --- |
| Typed output | The caller receives a known choice, Boolean probability or score | The allowed options and instructions can still be badly designed |
| No prose to parse | There is no need to recover JSON from an essay | Runtime implementations differ; validate every response |
| Small local checkpoints | A narrow route can run close to the application | Small size does not prove sufficient accuracy |
| Probability for every option | The caller can inspect uncertainty and margin | Model confidence is not the probability of being correct |
| Multimodal state | One gate can consider text, JSON and sometimes media | Media support and cost vary by model and runtime |
| One common API | Teams can replace models without rewriting product logic | Model behaviour is not interchangeable without re-evaluation |

The deeper reason is architectural. A full generative model is often asked to write `{"route":"billing"}` and nothing else. That uses a language generator as an expensive classifier. A decision model exposes the classification signal directly.

This is also why a yes/no model matters. A product may need to know whether a request contains personal data, needs a tool, lacks enough evidence or should enter a manual queue. Those conditions are independent. Asking four separate propositions is often clearer than forcing one label to encode every combination.

## It is not the same as every other router

| Component | Best at | Weak boundary |
| --- | --- | --- |
| Deterministic rule | Exact policy, permissions, formats and known thresholds | Cannot understand semantic ambiguity well |
| Classic classifier | Stable labels on a fixed feature and training pipeline | Less convenient for changing natural-language criteria |
| Embedding router | Nearest-intent or nearest-example matching | Similarity is not the same as a policy decision |
| Decision model | Bounded semantic choice, proposition or rubric score | Can be confidently wrong or forced into a bad option set |
| Generative LLM judge | Complex comparison with an explanation | Slower, more expensive and harder to constrain |
| Reward or verifier model | Ranking outputs from a particular task distribution | Not automatically a general application router |

A decision model is most valuable between exact rules and expensive reasoning. It should not replace either one.

## A safe routing layer

<figure class="article-svg-figure" data-animate-svg>
  <button class="svg-replay" type="button" data-svg-replay aria-label="Replay the decision routing animation" title="Replay animation" hidden>
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 11a8 8 0 1 0-2.34 5.66" /><path d="M20 4v7h-7" /></svg>
    <span>Replay</span>
  </button>
  <svg viewBox="0 0 640 870" role="img" aria-labelledby="decision-flow-title decision-flow-desc">
    <title id="decision-flow-title">A guarded decision-model routing flow</title>
    <desc id="decision-flow-desc">A request passes through deterministic rules, a compact local decision model and a confidence gate. Clear low-risk work is dispatched, ambiguous work goes to a stronger judge, and high-consequence work goes to a human. Application policy executes the final action.</desc>
    <defs><marker id="decision-flow-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 0 10 5 0 10Z" fill="#087286" /></marker></defs>
    <path data-svg-link d="M320 112V142" fill="none" stroke="#087286" stroke-width="5" stroke-linecap="round" marker-end="url(#decision-flow-arrow)" />
    <path data-svg-link d="M320 244V274" fill="none" stroke="#087286" stroke-width="5" stroke-linecap="round" marker-end="url(#decision-flow-arrow)" />
    <path data-svg-link d="M320 376V406" fill="none" stroke="#087286" stroke-width="5" stroke-linecap="round" marker-end="url(#decision-flow-arrow)" />
    <path data-svg-link d="M320 508V538" fill="none" stroke="#087286" stroke-width="5" stroke-linecap="round" marker-end="url(#decision-flow-arrow)" />
    <path data-svg-link d="M175 640V680H270" fill="none" stroke="#087286" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#decision-flow-arrow)" />
    <path data-svg-link d="M465 640V680H370" fill="none" stroke="#087286" stroke-width="5" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#decision-flow-arrow)" />
    <path data-svg-link d="M320 772V802" fill="none" stroke="#087286" stroke-width="5" stroke-linecap="round" marker-end="url(#decision-flow-arrow)" />
    <g data-svg-step><rect x="70" y="30" width="500" height="82" rx="14" fill="#edf2f4" stroke="#b8c7cd" /><text x="320" y="64" text-anchor="middle" fill="#18232c" font-family="system-ui, sans-serif" font-size="22" font-weight="700">1. Receive request and application state</text><text x="320" y="91" text-anchor="middle" fill="#455760" font-family="system-ui, sans-serif" font-size="17">Text, trusted metadata, media and user intent</text></g>
    <g data-svg-step><rect x="70" y="142" width="500" height="102" rx="14" fill="#edf2f4" stroke="#b8c7cd" /><text x="320" y="178" text-anchor="middle" fill="#18232c" font-family="system-ui, sans-serif" font-size="22" font-weight="700">2. Apply deterministic rules first</text><text x="320" y="207" text-anchor="middle" fill="#455760" font-family="system-ui, sans-serif" font-size="17">Auth, ACLs, privacy, spend limits and explicit user choice</text><text x="320" y="230" text-anchor="middle" fill="#b44a35" font-family="system-ui, sans-serif" font-size="16">A model cannot override these controls</text></g>
    <g data-svg-step><rect x="70" y="274" width="500" height="102" rx="14" fill="#e5f2f4" stroke="#087286" stroke-width="2" /><text x="320" y="310" text-anchor="middle" fill="#18232c" font-family="system-ui, sans-serif" font-size="22" font-weight="700">3. Ask a compact local decision model</text><text x="320" y="339" text-anchor="middle" fill="#455760" font-family="system-ui, sans-serif" font-size="17">Route choice + independent yes/no gates + risk score</text><text x="320" y="362" text-anchor="middle" fill="#455760" font-family="system-ui, sans-serif" font-size="16">Always include unknown or human review</text></g>
    <g data-svg-step><rect x="70" y="406" width="500" height="102" rx="14" fill="#edf2f4" stroke="#b8c7cd" /><text x="320" y="442" text-anchor="middle" fill="#18232c" font-family="system-ui, sans-serif" font-size="22" font-weight="700">4. Apply calibrated route thresholds</text><text x="320" y="471" text-anchor="middle" fill="#455760" font-family="system-ui, sans-serif" font-size="17">Check top probability, winning margin and consequence</text><text x="320" y="494" text-anchor="middle" fill="#455760" font-family="system-ui, sans-serif" font-size="16">Thresholds differ by route and business cost</text></g>
    <g data-svg-step><rect x="48" y="538" width="254" height="102" rx="14" fill="#e5f2f4" stroke="#087286" stroke-width="2" /><text x="175" y="574" text-anchor="middle" fill="#18232c" font-family="system-ui, sans-serif" font-size="21" font-weight="700">Clear + low risk</text><text x="175" y="605" text-anchor="middle" fill="#455760" font-family="system-ui, sans-serif" font-size="17">Dispatch to the selected</text><text x="175" y="628" text-anchor="middle" fill="#455760" font-family="system-ui, sans-serif" font-size="17">local or specialist lane</text></g>
    <g data-svg-step><rect x="338" y="538" width="254" height="102" rx="14" fill="#f6ebe7" stroke="#b44a35" stroke-width="2" /><text x="465" y="574" text-anchor="middle" fill="#18232c" font-family="system-ui, sans-serif" font-size="21" font-weight="700">Unclear or high risk</text><text x="465" y="605" text-anchor="middle" fill="#455760" font-family="system-ui, sans-serif" font-size="17">Use a stronger judge</text><text x="465" y="628" text-anchor="middle" fill="#455760" font-family="system-ui, sans-serif" font-size="17">or human review</text></g>
    <g data-svg-step><rect x="70" y="680" width="500" height="92" rx="14" fill="#edf2f4" stroke="#b8c7cd" /><text x="320" y="718" text-anchor="middle" fill="#18232c" font-family="system-ui, sans-serif" font-size="22" font-weight="700">5. Application policy chooses the action</text><text x="320" y="749" text-anchor="middle" fill="#455760" font-family="system-ui, sans-serif" font-size="17">Log the model version, inputs, decision and override</text></g>
    <g data-svg-step><rect x="160" y="802" width="320" height="52" rx="26" fill="#087286" /><text x="320" y="835" text-anchor="middle" fill="#fff" font-family="system-ui, sans-serif" font-size="20" font-weight="700">Execute, measure and monitor drift</text></g>
  </svg>
  <figcaption>The safe pattern is rules, bounded semantic decision, calibrated gate, then policy-controlled execution.</figcaption>
</figure>

The model should receive only state that the caller is allowed to disclose. Treat user-provided text as untrusted evidence, not as instructions that can change the route definitions.

## A practical Ollama route

The following request asks D3 for one route and two independent signals. The labels are examples; they need to match the real product and its escalation process.

```bash
curl http://localhost:11434/v1/systemone \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "d3",
    "state": {
      "request": "Compare two contracts and create a risk summary",
      "user_tier": "standard",
      "attachments": ["contract-a.pdf", "contract-b.pdf"]
    },
    "questions": {
      "route": {
        "type": "choice",
        "instructions": "Select the best processing lane.",
        "criteria": {
          "local_fast": "Simple rewrite, extraction or formatting",
          "document_specialist": "Document parsing or grounded comparison",
          "frontier_reasoning": "Difficult multi-step analysis",
          "human_review": "High-consequence legal, safety or financial work",
          "unknown": "No route fits with enough evidence"
        }
      },
      "needs_tools": {
        "type": "noul",
        "instructions": "Does this request require a document or search tool?"
      },
      "risk": {
        "type": "score",
        "instructions": "Rate the consequence of a wrong result.",
        "criteria": ["low", "medium", "high", "critical"]
      }
    }
  }'
```

Do not dispatch solely because `route.choice` is present. Apply product thresholds after validating the response:

```python
def choose_lane(request, decision):
    if hard_policy_blocks(request):
        return "reject"

    route = decision["route"]["choice"]
    probability = decision["route"]["probabilities"][route]
    margin = top_probability_margin(decision["route"]["probabilities"])

    if is_high_consequence(request) or decision["risk"]["score"] >= 3:
        return "human_review"

    if (
        route not in {"unknown", "human_review"}
        and probability >= ROUTE_THRESHOLDS[route]
        and margin >= MINIMUM_MARGIN
    ):
        return route

    return "stronger_judge_or_human"
```

The threshold values are deliberately absent. They must come from labelled product examples and the relative cost of each error.

## Lightweight does not mean one size

The category already spans sub-billion-parameter classifiers and 27B multimodal systems. These are not interchangeable quality tiers.

| Family | Published size or package | Inputs in the listed Ollama package | Useful starting point | Licence note |
| --- | --- | --- | --- | --- |
| [Laya](https://ollama.com/library/laya) | 421M main model, about 844 MB | Text | Narrow local triage, intent and safety signals | Check the model card for the selected tag |
| [d1-omni](https://ollama.com/library/d1-omni) | 587M, about 0.85 GB | Text, image and short speech | Edge multimodal gates | LFM Open License v1.0 |
| [Kev](https://ollama.com/library/kev) | 0.8B to 27B family | Text | Compact text routing through larger decision workloads | Apache 2.0 |
| [D3](https://ollama.com/library/d3) | 2B to 27B family | Text, structured state and still images | General routing where state or images matter | Apache 2.0 |
| Proprietary Jev | Hosted service; weights not published | Depends on service version | Benchmark or hosted deployment when policy permits | Proprietary service terms |

Start with the smallest candidate that covers the required modality and labels. Measure it on the target CPU, GPU or accelerator. A 421M text model can be a better product component than a larger multimodal model when the route is a narrow email or query classification. The larger model earns its place only when it improves decisions enough to justify memory and latency.

## Product patterns that benefit

| Product flow | Decision question | Action after the gate |
| --- | --- | --- |
| AI assistant router | Which model lane can answer this request? | Send easy work locally and difficult work to a specialist or frontier model |
| Agent tool gate | Does the request require a tool, and which one? | Expose only the permitted tool, then keep its arguments under schema and policy checks |
| Enterprise search | Is this result relevant and sufficiently grounded? | Re-rank, ask for clarification or send the top evidence to a larger answer model |
| Support operation | Which queue owns this ticket? Is it urgent? | Route to billing, returns, technical support or manual triage |
| Moderation queue | Is there enough evidence for review? | Prioritise a human queue; do not make irreversible account actions from one score |
| Document intake | Which document type and workflow fit? | Select OCR, extraction, review and retention policy already defined by the application |
| Notification system | Is this event useful enough to interrupt the user? | Send, batch or suppress according to a user-owned policy |
| Multimodal edge product | Does this image or short audio clip match a known operational condition? | Trigger a low-risk workflow or request human confirmation |

The best use cases have bounded options, repeat often, and tolerate an escalation path. The worst use cases hide a high-consequence decision behind a neat probability.

## Evaluate the gate, not just the model

An independent [evaluation of Jev 1.13](https://arxiv.org/abs/2609.37647) covered 37 datasets and found a mixed result: strong performance on several classification and reasoning tasks, but weaknesses on low-resource languages, fine-grained or noisy labels, and rubric judgments. On one legal dataset, moving away from a fixed `0.5` binary threshold raised reported micro-F1 from `0.50` to `0.75`.

That result does not rank D3, Laya or another model. It demonstrates why a production gate needs its own evaluation:

1. Collect representative, consented examples from the intended workflow.
2. Label the correct route and every independent yes/no condition.
3. Split by time, customer or source so near-duplicates do not inflate results.
4. Measure per-route precision, recall, calibration, abstention and end-to-end latency.
5. Assign a cost to false dispatch, unnecessary escalation and missed escalation.
6. Tune a separate threshold for each route or condition.
7. Re-run the set after a model, prompt, label or product change.
8. Monitor the live distribution and human overrides for drift.

Also test malformed state, prompt-injection text, missing fields, new languages and inputs that belong to no route. A perfect score on clean examples says little about the failure boundary.

## Where not to place one

Do not make a decision model the sole control for:

- authentication, authorisation or access-control changes;
- payment release, credit, employment or insurance outcomes;
- medical diagnosis or safety-critical intervention;
- destructive tool calls or irreversible data changes;
- legal conclusions or regulatory obligations;
- any workflow without a safe `unknown`, fallback or appeal route.

The useful mental model is a semantic control signal. It can reduce the load on larger models and people, but application code still decides what is allowed.

## Sources and further reading

| Source | What it supports |
| --- | --- |
| [Ollama decision API](https://docs.ollama.com/capabilities/decision) | `choice`, `noul`, `score`, response fields and confidence warning |
| [D3 on Ollama](https://ollama.com/library/d3) | Local tags, package classes, supported inputs and runtime use |
| [D3 model card](https://huggingface.co/vllm-sr/d3) | Native architecture, modalities, licence and publisher measurements |
| [Evaluating and Benchmarking the System One Model Jev](https://arxiv.org/abs/2609.37647) | Independent evaluation, calibration limits and threshold example |
| [Releasing the Inner Jev](https://arxiv.org/abs/2610.17205) | Open decision-model training and evaluation research |
| [vLLM Semantic Router](https://github.com/vllm-project/semantic-router) | An open routing architecture using programmable decisions and fallbacks |
| [Ollama decision-model directory](https://ollama.com/search?c=decision) | Current model families available through the runtime |
