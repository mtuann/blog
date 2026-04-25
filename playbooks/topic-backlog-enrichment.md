# Topic Backlog Enrichment Playbook

Use this playbook when turning one topic hub or one backlog item into a research-first page that is current, opinionated, and easy to act on.

## Goal

Every enriched topic page should let a reader answer four questions quickly:

1. What belongs in this field, and what does not?
2. What is moving right now?
3. What should I read first if I want the canonical view and the current frontier?
4. What should I build, compare, or investigate next?

## Output Standard

An enriched topic page is successful only if it provides:

- a sharp boundary for the topic
- a compact field map
- active directions backed by recent evidence
- representative papers grouped by direction
- benchmark or workload context when relevant
- precise sources to follow
- short, actionable next steps

Do not treat the topic page as a generic overview, a course syllabus, or a dumping ground for links.

## Source Priority

Search in this order unless the topic clearly demands a different mix:

1. Primary research sources
   arXiv, conference proceedings, OpenReview, journals, official surveys
2. Official implementation and system sources
   framework docs, release notes, RFCs, CUDA or vendor docs, changelogs
3. Official research and engineering posts
   OpenAI, Anthropic, DeepMind, NVIDIA, Meta, PyTorch, vLLM, TensorRT-LLM, Flower, TensorFlow Federated, FedML
4. Courses and lectures
   use only for orientation, terminology, and canonical framing
5. Industry and practitioner analysis
   use only for triangulation, adoption signals, and deployment reality

## Source Mix By Topic

- `Machine Learning`, `Trustworthy AI`: academic-first
- `Generative AI`: academic plus company research
- `AI Systems`, `CUDA`: engineering-first plus papers
- `Efficient AI`: papers plus implementation evidence
- `Distributed Learning`, `Federated Learning`: papers plus systems/docs

## Recency Rules

- Prefer 2025-2026 work for current directions unless the field is unusually stable.
- Keep an older paper only if it still defines the problem, the baseline, or the vocabulary.
- Replace an older “recent” paper when newer work changes the dominant method, invalidates old assumptions, or becomes the standard citation in the last 12-24 months.
- For every important external item, record:
  - publication date
  - release or update date when relevant
  - observation date for fast-moving systems claims
- Use absolute dates, not only relative words like `recent` or `latest`.

## Evidence Threshold

Call a direction `active` only if at least one of these is true:

- there are at least 2 independent recent sources and at least 1 is primary
- there is clear paper velocity across multiple groups
- there is shipped-system or released-tool evidence
- the direction is repeatedly used in benchmarks, docs, or public repos

Do not call a direction active because one flashy paper or one vendor blog mentioned it.

## Foundation vs Frontier

For each topic, keep both:

- `Canonical anchor`
  1-3 references that still define the field
- `Recent representatives`
  3-6 references per active direction that show where the field moved

When in doubt, keep one canonical anchor and replace the rest with newer representatives.

## Topic Hub Format

Use this section order for topic hubs:

1. `Scope`
   1-2 sentences on what belongs here, what is excluded, and why it matters now.
2. `Field Map`
   Main subareas, core questions, typical methods, first papers, key benchmarks.
3. `What Is Moving Now`
   4-6 bullets only.
4. `Keywords To Track`
   Search phrases useful for arXiv, OpenReview, GitHub, docs, and company research pages.
5. `Benchmarks / Workloads To Watch`
   Include what each benchmark measures and misses.
6. `Recent Papers By Direction`
   Group by direction, not by date alone.
7. `Labs / Groups / Sources To Follow`
   Only sources that materially shape the topic.
8. `Canonical References`
   Short section, not a literature dump.
9. `Open Problems`
   Decision-oriented unresolved questions.
10. `Related Notes`
   Internal notes only when they deepen a specific direction.
11. `Suggested Next Steps`
   Short, opinionated, action-oriented.

## Backlog Note Format

Use this section order when expanding one backlog item into a deeper note:

1. `Backlog Item`
   State the exact question, claim, or direction being resolved.
2. `Why This Matters`
   2-4 bullets.
3. `Short Answer`
   3-5 bullets with the main conclusion first.
4. `Core Concepts You Need`
   Only what is necessary to understand the note.
5. `Paper Map`
   Explain how the papers differ and build on each other.
6. `Evidence / Benchmarks`
   What the experiments do and do not prove.
7. `Synthesis`
   Agreements, disagreements, overclaims, durable signals.
8. `Recommended Reading Order`
9. `Open Questions`
10. `Next Notes To Write`

## Writing Rules

- Keep intros functional, not atmospheric.
- Remove generic onboarding phrases such as `start here`, `zero to hero`, `this section explores`, or `overview of the basics`.
- Expand only the parts that reduce reading uncertainty:
  - subarea boundaries
  - benchmark caveats
  - paper-selection logic
  - disagreements
  - open problems
- Use compact tables when comparing subareas, methods, papers, or benchmarks.
- Keep the hub as a map, not the whole lecture.

## Recommendation Rules

Every `Suggested Next Steps` block must answer one of these:

- what to read next
- what to build next
- what to compare next

Use a short mix such as:

- 1 canonical read
- 1 frontier read
- 1 build idea
- 1 comparison

Phrase each item as `action + why now`.

Good examples:

- Read `canonical paper A` first, then `recent paper B`, because B changes the decision surface introduced by A.
- Build a small benchmark that stress-tests the claimed gain under realistic workload constraints.
- Compare method X vs method Y on a named axis such as `quality vs latency`, `dense vs sparse`, or `benchmark win vs deployment fit`.

## Citation Rules

- Put citations on factual claims, benchmark claims, trend claims, and disagreements.
- Do not attach citations to every sentence.
- Prefer 1 canonical reference plus 1 newer representative over a long citation spray.
- If a sentence needs more than 2 references, convert it into a short paper list or table.
- When sources disagree, name the tension explicitly and tie it to evidence conditions.

## Hype Filter

Treat a direction as durable only if at least 2 of these are true:

- repeated gains across labs
- survival across benchmark refreshes
- adoption in public systems or public tooling
- connection to a broader abstraction that explains other results
- usefulness under realistic resource limits

Treat a direction as hype-prone if it depends on:

- one lab only
- one benchmark only
- unclear baselines
- closed data with weak reproduction evidence
- gains that disappear once systems cost is included

## Maintenance Rules

- Revisit each topic hub on a fixed cadence, usually monthly or quarterly.
- On each pass, update only:
  - active directions
  - representative papers
  - disagreements
  - suggested next steps
- When adding a new radar item, try to prune at least one stale item.
- Keep `canonical references` stable unless the field’s core framing actually changed.

## Minimal Enrichment Workflow

1. Define the boundary of the topic in 1-2 sentences.
2. Search primary sources first, then implementation sources, then official blogs.
3. Keep only directions with enough evidence to count as active.
4. Split references into canonical anchors vs recent representatives.
5. Group the recent representatives by direction.
6. Identify the benchmarks, workloads, or deployment constraints that matter.
7. Write an opinionated `Suggested Next Steps` block.
8. Add exact references and absolute dates where recency matters.
9. Prune stale items before closing the update.

## Reviewer Checklist

Before publishing an enriched topic page, verify:

- The scope clearly says what belongs here and what does not.
- There are no generic intro paragraphs left.
- Each active direction has recent evidence.
- Older references are kept only because they are truly canonical.
- The page distinguishes consensus from contested claims.
- The page gives a concrete reading path and not just a bibliography.
- The page helps a reader decide what to read, build, or compare next.
