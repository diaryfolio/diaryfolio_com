---
title: "Build private video search with LFM3-VL-2B and Ollama"
date: "2026-10-28T22:30:00.000Z"
legacy_url: "/2026/10/private-video-search-lfm3-vl-2b-ollama.html"
research_id: "AR_1025"
author: "df"
labels:
  - "Artificial Intelligence"
  - "Enterprise Search"
  - "Ollama"
  - "Video"
description: "A practical architecture for turning private video into searchable, time-coded segments with LFM3-VL-2B, transcripts, embeddings and access controls."
---

<p class="article-lead">A vision-language model can describe what happens inside a video, but it is not a video search engine. The useful design is to let LFM3-VL-2B enrich selected frames, then place its output beside transcripts, timestamps and access controls in a separate search index.</p>

## Quick read

- Use LFM3-VL-2B to describe selected frames or short clips. Do not ask it to search an entire video archive directly.
- The current Ollama package accepts text and images. It says native video input is coming soon, so an Ollama pipeline needs to extract frames first.
- Store the model output with the transcript, video ID, start and end times, source permissions and model version.
- Use a separate embedding model and combine semantic retrieval with exact keyword search.
- The caveat: LFM3 was released on 27 October 2026. Runtime support is changing and production evidence is still limited.

<figure class="article-figure">
  <img src="/assets/images/original/2026/10/private-video-search-lfm3-vl-2b-ollama/private-video-search.svg" alt="Video scenes being converted into time-coded entries in a private search index" width="960" height="540" />
  <figcaption>LFM3-VL adds visual meaning. The surrounding system supplies segmentation, audio transcription, embeddings, permissions and retrieval.</figcaption>
</figure>

## What the model provides

[Liquid AI's model card](https://huggingface.co/LiquidAI/LFM3-VL-2B) describes LFM3-VL-2B as a 1.92 billion parameter vision-language model. The native model accepts text, images and video, uses a 128K combined input and output context, and samples video at 2 frames per second. Liquid lists video question answering, documents, charts, application screens, object finding and spatial reasoning among its intended tasks.

The small size is the interesting part. The current [Ollama package](https://ollama.com/library/lfm3-vl) is about 1.7 GB with a 125K context. That is small enough to test locally on ordinary development hardware rather than sending every frame to a hosted API.

However, the current Ollama package lists **Text** and **Image** as inputs and says video support is coming soon. That creates two different deployment paths:

| Runtime path | Input available now | Practical consequence |
| --- | --- | --- |
| Native model runtime | Text, image and video according to the model card | The runtime can sample a short video directly if its LFM3-VL support is complete |
| Current Ollama package | Text and image | Extract representative frames and preserve their timestamps before inference |

The model card also says LFM3-VL-2B is not recommended for coding, multi-turn conversation or complex reasoning. Keep its job narrow: observe visual content and return structured evidence.

## The complete search pipeline

<figure class="article-svg-figure" data-animate-svg>
  <button class="svg-replay" type="button" data-svg-replay aria-label="Replay the enterprise video search pipeline animation" title="Replay animation" hidden>
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 11a8 8 0 1 0-2.34 5.66" /><path d="M20 4v7h-7" /></svg>
    <span>Replay</span>
  </button>
  <svg viewBox="0 0 620 760" role="img" aria-labelledby="video-search-flow-title video-search-flow-desc">
    <title id="video-search-flow-title">Enterprise video search pipeline</title>
    <desc id="video-search-flow-desc">Six stages: ingest video with its permissions, extract scenes and audio, create transcripts and visual metadata, build lexical and vector indexes, filter queries by access control, and return time-coded results.</desc>
    <defs>
      <marker id="video-flow-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
        <path d="M0 0 10 5 0 10Z" fill="#087286" />
      </marker>
    </defs>
    <path data-svg-link d="M310 112V142" fill="none" stroke="#087286" stroke-width="5" stroke-linecap="round" marker-end="url(#video-flow-arrow)" />
    <path data-svg-link d="M310 224V254" fill="none" stroke="#087286" stroke-width="5" stroke-linecap="round" marker-end="url(#video-flow-arrow)" />
    <path data-svg-link d="M310 336V366" fill="none" stroke="#087286" stroke-width="5" stroke-linecap="round" marker-end="url(#video-flow-arrow)" />
    <path data-svg-link d="M310 448V478" fill="none" stroke="#087286" stroke-width="5" stroke-linecap="round" marker-end="url(#video-flow-arrow)" />
    <path data-svg-link d="M310 560V590" fill="none" stroke="#087286" stroke-width="5" stroke-linecap="round" marker-end="url(#video-flow-arrow)" />
    <g data-svg-step>
      <rect x="70" y="30" width="480" height="82" rx="13" fill="#edf2f4" stroke="#b8c7cd" />
      <circle cx="112" cy="71" r="24" fill="#087286" />
      <text x="112" y="78" text-anchor="middle" fill="#fff" font-family="system-ui, sans-serif" font-size="20" font-weight="700">1</text>
      <text x="154" y="63" fill="#18232c" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Ingest video and source ACLs</text>
      <text x="154" y="91" fill="#455760" font-family="system-ui, sans-serif" font-size="17">Keep provenance, tenant, retention and ownership</text>
    </g>
    <g data-svg-step>
      <rect x="70" y="142" width="480" height="82" rx="13" fill="#edf2f4" stroke="#b8c7cd" />
      <circle cx="112" cy="183" r="24" fill="#087286" />
      <text x="112" y="190" text-anchor="middle" fill="#fff" font-family="system-ui, sans-serif" font-size="20" font-weight="700">2</text>
      <text x="154" y="175" fill="#18232c" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Segment scenes and extract audio</text>
      <text x="154" y="203" fill="#455760" font-family="system-ui, sans-serif" font-size="17">Preserve timestamps for every frame or clip</text>
    </g>
    <g data-svg-step>
      <rect x="70" y="254" width="480" height="82" rx="13" fill="#e5f2f4" stroke="#087286" stroke-width="2" />
      <circle cx="112" cy="295" r="24" fill="#087286" />
      <text x="112" y="302" text-anchor="middle" fill="#fff" font-family="system-ui, sans-serif" font-size="20" font-weight="700">3</text>
      <text x="154" y="287" fill="#18232c" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Create evidence-rich metadata</text>
      <text x="154" y="315" fill="#455760" font-family="system-ui, sans-serif" font-size="17">LFM3-VL for vision; speech recognition for audio</text>
    </g>
    <g data-svg-step>
      <rect x="70" y="366" width="480" height="82" rx="13" fill="#edf2f4" stroke="#b8c7cd" />
      <circle cx="112" cy="407" r="24" fill="#087286" />
      <text x="112" y="414" text-anchor="middle" fill="#fff" font-family="system-ui, sans-serif" font-size="20" font-weight="700">4</text>
      <text x="154" y="399" fill="#18232c" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Build lexical and vector indexes</text>
      <text x="154" y="427" fill="#455760" font-family="system-ui, sans-serif" font-size="17">Embed the combined caption, transcript and metadata</text>
    </g>
    <g data-svg-step>
      <rect x="70" y="478" width="480" height="82" rx="13" fill="#f6ebe7" stroke="#b44a35" />
      <circle cx="112" cy="519" r="24" fill="#b44a35" />
      <text x="112" y="526" text-anchor="middle" fill="#fff" font-family="system-ui, sans-serif" font-size="20" font-weight="700">5</text>
      <text x="154" y="511" fill="#18232c" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Apply ACL filters during retrieval</text>
      <text x="154" y="539" fill="#455760" font-family="system-ui, sans-serif" font-size="17">The model must not decide who can view a source</text>
    </g>
    <g data-svg-step>
      <rect x="70" y="590" width="480" height="82" rx="13" fill="#e5f2f4" stroke="#087286" stroke-width="2" />
      <circle cx="112" cy="631" r="24" fill="#087286" />
      <text x="112" y="638" text-anchor="middle" fill="#fff" font-family="system-ui, sans-serif" font-size="20" font-weight="700">6</text>
      <text x="154" y="623" fill="#18232c" font-family="system-ui, sans-serif" font-size="22" font-weight="700">Return time-coded evidence</text>
      <text x="154" y="651" fill="#455760" font-family="system-ui, sans-serif" font-size="17">Open the source video at the matching segment</text>
    </g>
    <text x="310" y="721" text-anchor="middle" fill="#455760" font-family="system-ui, sans-serif" font-size="17">Optional: recheck the highest-ranked frames with LFM3-VL.</text>
  </svg>
  <figcaption>The visual model is one stage in the system. Search, permissions and timestamps remain deterministic application concerns.</figcaption>
</figure>

### 1. Ingest the source, not just its pixels

Create a stable `video_id` before processing. Preserve the source URI, tenant, owner, retention class and access-control list. Each derived segment must inherit those fields.

If the source can be deleted or its permissions can change, plan how the index will receive that change. A stale vector that still reveals a confidential caption is a data leak even when the original video has been removed.

### 2. Segment before sending frames to the model

Sending a 42-minute video at 2 frames per second would expose 5,040 frames. Many would be nearly identical. Scene detection plus a slower fallback sample is usually a better starting point.

This FFmpeg example extracts frames when the image changes substantially:

```bash
mkdir -p frames
ffmpeg -i input.mp4 \
  -vf "select='gt(scene,0.35)',scale=1280:-2" \
  -fps_mode vfr frames/scene-%06d.jpg
```

The `0.35` threshold is not universal. A screen recording with small cursor changes, a fixed security camera and a handheld inspection video need different settings. Persist each selected frame's presentation timestamp rather than deriving time from its output filename. [FFmpeg's filter documentation](https://ffmpeg.org/ffmpeg-filters.html) describes frame selection and scene scoring.

Also extract audio for speech recognition. LFM3-VL is a visual model. It cannot discover a warning spoken off camera unless a separate transcript supplies it.

### 3. Ask for constrained metadata

[Ollama's vision API](https://docs.ollama.com/capabilities/vision) accepts images with a text prompt. Use a strict JSON schema and validate the response before indexing it.

The following Python fragment shows the shape of a request. It assumes Ollama is running locally and `lfm3-vl` has been pulled.

```python
import base64
import json
import requests

with open("frames/scene-000042.jpg", "rb") as image_file:
    image_b64 = base64.b64encode(image_file.read()).decode("ascii")

schema = {
    "type": "object",
    "properties": {
        "caption": {"type": "string"},
        "visible_text": {"type": "array", "items": {"type": "string"}},
        "objects": {"type": "array", "items": {"type": "string"}},
        "actions": {"type": "array", "items": {"type": "string"}},
        "uncertainties": {"type": "array", "items": {"type": "string"}}
    },
    "required": ["caption", "visible_text", "objects", "actions", "uncertainties"]
}

response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "lfm3-vl",
        "stream": False,
        "format": schema,
        "messages": [{
            "role": "user",
            "content": (
                "Describe only visible evidence. Copy readable text exactly. "
                "Do not identify people or infer intent. Record uncertainty."
            ),
            "images": [image_b64]
        }]
    },
    timeout=120
)

metadata = json.loads(response.json()["message"]["content"])
```

JSON syntax does not make the result true. Validate types and lengths, keep the original frame, and treat any generated certainty score as uncalibrated until your own evaluation proves otherwise.

### 4. Build one searchable segment record

Merge visual metadata, transcript text and deterministic source fields. A practical record could look like this:

```json
{
  "video_id": "maintenance-2026-184",
  "segment_id": "maintenance-2026-184_0042",
  "start_ms": 183400,
  "end_ms": 197800,
  "caption": "Engineer presses the reset control on a red protection relay",
  "visible_text": ["FAULT 27", "RESET"],
  "objects": ["electrical panel", "protection relay", "insulated gloves"],
  "actions": ["opens panel", "presses reset control"],
  "transcript": "Reset the relay after confirming the circuit is isolated",
  "tenant_id": "factory-a",
  "acl": ["maintenance-engineering"],
  "source_uri": "videos/maintenance-2026-184.mp4",
  "visual_model": "lfm3-vl-2b",
  "prompt_version": "visual-index-v3"
}
```

Keep model and prompt versions. When either changes, you need to know which records require reprocessing and whether search quality moved for a technical reason rather than because the archive changed.

### 5. Use a separate retrieval model

LFM3-VL generates descriptions. It is not the embedding model used by the search index. Send a stable text representation of the caption, transcript, visible text and selected fields to a separate embedding model.

```bash
curl http://localhost:11434/api/embed -d '{
  "model": "your-embedding-model",
  "input": [
    "Engineer presses reset on red protection relay. Visible text: FAULT 27, RESET."
  ]
}'
```

[Ollama's embedding documentation](https://docs.ollama.com/capabilities/embeddings) recommends using the same embedding model for indexing and querying. Its text embeddings are useful after visual content has been converted into text. If the product needs direct image-to-text similarity without generated captions, add a multimodal embedding model such as a CLIP- or SigLIP-style encoder.

Use hybrid retrieval rather than vector search alone:

- lexical search catches serial numbers, product codes, exact warning text and names;
- vector search catches descriptions such as "the operator restarts the breaker" when the stored caption says "presses the reset control";
- metadata filters constrain tenant, site, date, content type and permissions;
- reciprocal rank fusion can merge lexical and vector result lists without assuming their raw scores are directly comparable.

[Elastic's hybrid-search guidance](https://www.elastic.co/docs/solutions/search/hybrid-search) describes reciprocal rank fusion. The same architecture can be implemented with another search engine that supports lexical fields, vectors and filtered retrieval.

## A worked factory-maintenance example

Assume a factory has thousands of maintenance recordings. A technician searches for:

> show where the operator resets the red protection relay after fault 27

The retrieval path is:

1. Apply the user's site and maintenance-team permissions.
2. Run lexical search for `FAULT 27`, `protection relay` and `reset`.
3. Run vector search for the complete natural-language query.
4. Merge the two result lists.
5. Return a thumbnail, transcript fragment and the source time range.
6. Optionally send the top three frames back to LFM3-VL with a narrow question: "Is the reset control visibly pressed?"

The result should say what evidence matched:

| Result field | Example |
| --- | --- |
| Video | `maintenance-2026-184.mp4` |
| Time range | `00:03:03.400` to `00:03:17.800` |
| Visual match | Red protection relay; operator presses reset control |
| Text match | `FAULT 27`, `RESET` |
| Transcript match | "Reset the relay after confirming isolation" |
| Access decision | Allowed by `maintenance-engineering` ACL |

These values are an architecture example, not a measured LFM3-VL benchmark. A real implementation should let the user open the original segment and judge the evidence.

## Six practical product uses

| Product | Useful query | Strongest evidence | Main failure boundary |
| --- | --- | --- | --- |
| Factory maintenance | "Where is the red relay reset?" | Actions, equipment, labels and transcript | Similar panels can be confused; verify the source frame |
| Training recordings | "Show where refund status changes to approved" | Application screen, visible text and narration | Small UI text may need specialist OCR |
| Retail video search | "Blue waterproof backpack shown from the side" | Colour, object view and catalogue metadata | Visual appearance does not prove waterproofing |
| Field inspection | "Corrosion near the lower pipe joint" | Location, visible condition and inspection notes | Safety decisions need a qualified reviewer |
| Meeting archive | "Slide with the deployment diagram" | Slide layout, OCR and transcript | Speech and slide timing can drift |
| Security review | "Forklift enters the marked pedestrian lane" | Object, action, lane markings and timestamp | Do not automate disciplinary action from one model result |

The model has the highest value when the sought fact is visible but absent from filenames and transcripts. If the archive is mainly spoken meetings, transcription quality will matter more than the visual model.

## Choose where inference runs

| Deployment mode | Good fit | Trade-off |
| --- | --- | --- |
| On the endpoint | Mobile inspection or privacy-sensitive capture | Limited battery, memory and processing time |
| Edge server at a site | Factory, shop or branch with local video storage | Requires site operations and model-update controls |
| Central private cluster | Large archive and scheduled batch indexing | More network movement and a larger security boundary |
| Query-time only | Small archive or expensive visual processing | Slow searches and repeated work |

A common design uses cheap batch enrichment during ingestion, then applies the VLM again only to a few top-ranked frames. This keeps interactive search responsive while allowing a narrow visual check before presenting an answer.

## Security and governance are part of retrieval

Video often contains faces, screens, badges, documents and conversations. Generated captions can expose the same information even when the original pixels remain in a protected store.

Enforce permissions inside the search query or vector store. Do not retrieve a confidential segment and hope a prompt tells the model not to reveal it. [OWASP's vector and embedding guidance](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/) recommends fine-grained access controls, logical partitioning, data classification and audit controls.

At minimum, test:

| Test | What to measure |
| --- | --- |
| Event recall | Percentage of labelled events that appear in the first relevant results |
| Timestamp accuracy | Distance between the returned start time and the labelled event |
| False visual claims | Objects, actions or text asserted without visible support |
| Permission isolation | Attempts to retrieve segments from another tenant or restricted group |
| Deletion propagation | Time taken for a removed source and its derived records to disappear |
| Throughput and cost | Frames processed per second, memory use and index growth |
| Model change | Search-quality difference after a runtime, weight or prompt update |

Do not use the system as the sole basis for medical, safety, employment or disciplinary decisions. Specialist OCR, face recognition or defect detection also need their own evaluation and governance rather than being assumed from general visual understanding.

## Check the licence before enterprise deployment

LFM3-VL uses the [LFM Open License v1.0](https://www.liquid.ai/lfm-license), not Apache 2.0. The licence applies a USD 10 million annual-revenue threshold to commercial use. Organisations at or above that threshold need to discuss a commercial licence with Liquid AI. Attribution and other licence conditions still need review below the threshold.

The licence text is the authority. Treat this section as an engineering gate, not legal advice.

## A sensible first pilot

Start with one bounded archive and 20 to 50 questions that users genuinely ask. Label the correct videos and time ranges by hand. Then compare:

1. transcript-only search;
2. transcript plus LFM3-VL captions;
3. hybrid lexical and vector retrieval;
4. hybrid retrieval with visual verification of the top results.

The model earns its place only if it improves relevant time-coded retrieval enough to justify processing, storage and review. A long context window does not turn a model into an archive, and a polished caption does not replace evidence from the source video.

*Evidence and runtime support checked on 28 October 2026. LFM3-VL and its integrations were newly released and may change quickly.*

## Sources and further reading

| External source | What it supports |
| --- | --- |
| [Liquid AI: LFM3 announcement](https://www.liquid.ai/blog/lfm3) | Release date, family positioning and vendor-reported capabilities |
| [LFM3-VL-2B model card](https://huggingface.co/LiquidAI/LFM3-VL-2B) | Parameters, context, native modalities, intended uses and limitations |
| [Ollama: lfm3-vl](https://ollama.com/library/lfm3-vl) | Current package size, context and image-only input status |
| [Ollama vision API](https://docs.ollama.com/capabilities/vision) | Sending images to a local vision model |
| [Ollama embeddings](https://docs.ollama.com/capabilities/embeddings) | Separate text embedding interface and retrieval guidance |
| [FFmpeg filters](https://ffmpeg.org/ffmpeg-filters.html) | Frame-rate and scene-based video sampling |
| [Elastic hybrid search](https://www.elastic.co/docs/solutions/search/hybrid-search) | Combining lexical and vector results with RRF |
| [OWASP vector and embedding weaknesses](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/) | Access control, partitioning and vector-store security |
| [LFM Open License v1.0](https://www.liquid.ai/lfm-license) | Commercial-use threshold and licence terms |
