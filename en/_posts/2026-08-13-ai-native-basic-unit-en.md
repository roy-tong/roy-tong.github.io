---
layout: post
lang: en
title: "After AI-Native: The Basic Unit of a Product Has Changed"
subtitle: "Pages and files won't disappear — they will become different views of the same semantic and task state."
date: 2026-08-13 21:30:00 +0800
reading_time: 11
tags:
  - AI native
  - agent
  - product design
description: An AI-native product isn't a traditional editor with a chat box attached. It reconstructs product state — from pages, files and layers toward semantic objects, tasks, relationships and operation history.
permalink: /en/notes/ai-native-basic-unit/
---

Open any traditional editor and you first meet a set of stable basic units. Word processors revolve around pages and paragraphs; presentation software around slides and elements; design tools around canvases, frames and layers; video editors around footage, tracks and timelines. These units decide not just what the user sees, but how the product stores information, organizes features, allocates permissions and saves versions.

When AI entered software, many products simply added a chat box beside the existing interface: the user makes a request, the model generates content, the result is dropped back into the page, slide or timeline. That has value, but the AI is still operating on the old product's basic units. The architecture hasn't changed.

The change has to go deeper:

> The basic unit of a product is shifting from pages, files, layers and features toward semantic objects, relationships, tasks and operation history that both people and machines can understand.

Pages and files won't disappear; they remain the most familiar media for reading, editing and delivery. But in an AI-native product they become different views of the same state — no longer the product's only true state.

## Why traditional editors are built around files, pages and layers

The basic units of traditional editors were designed for direct human manipulation. A page suits reading and printing; a slide suits presentation; a layer suits selecting and stacking objects; a timeline suits controlling temporal order.

These structures also map cleanly onto software objects. Notion's public API represents page content as lists of blocks — paragraphs, headings, images and more; Figma's public API represents a file as a tree of nodes, where pages, frames, text and graphics are different node types. That object model is excellent for deterministic editing: select an object, execute a command, see the result.

Traditional feature trees follow from it:

- Select text, change font size and style;
- Select a layer, adjust position and constraints;
- Select a clip, trim, change speed or add a transition;
- Select a slide, modify layout and animation.

The problem: the things users actually want rarely exist in these units. The user wants "make management understand why this project should continue," "cut this interview into a short video with a clear point," or "find the conclusions in this report that lack evidence" — not "create three pages" or "move five layers." In the past, the product left the work of decomposing goals into operations to the human. For the first time, a machine can do that part.

## AI exposes the state-representation problem

Adding generation to a traditional editor solves the easy part: rewrite a paragraph, generate an image, fill a slide, remove a video background. But user intent usually spans multiple objects — even multiple applications. "Turn this industry research into an investor deck," for example, involves at least:

1. Deciding which points matter most;
2. Separating facts, inferences and assumptions;
3. Restructuring the narrative for the audience;
4. Choosing evidence and visual material;
5. Generating pages and checking the logic across them;
6. Revising in response to feedback.

If the underlying state only knows text boxes, coordinates and pages, even a model that understands the task cannot reliably write its understanding back. It may know "this is a core claim," while the system only stores "a text box at the top-left of page 3." So an AI-native product must answer a more fundamental question than generation: **does the product have a data structure that can express intent, semantics, relationships and task state?**

## The new first layer: semantic objects and relationships

A semantic object is not an extra tag wrapped around content. It means the product understands each object's identity within the task. The same text can be a heading, a claim, evidence, a counterexample, a quote or an unvalidated assumption; the same image can be source material, evidence, background or an emotional reference; the same video can be an event, a person's action, an interview point or a rhythm node.

These objects need relationships:

- Which evidence supports which conclusion;
- Which shot corresponds to which narration;
- Which narrative role each slide plays;
- Which design component serves which state;
- Which change came from which piece of user feedback.

Think of it as moving from storing "what an object looks like" toward storing "what it is, what it relates to, and why it exists."

| Product domain | Traditional operational unit | Semantic unit AI needs to understand |
| --- | --- | --- |
| Documents | Pages, paragraphs, characters | Claims, evidence, citations, audience, to-dos, decisions |
| Presentations | Slides, text boxes, images | Narrative nodes, page roles, argument relationships, visual assets |
| Video | Footage, clips, tracks, timecodes | People, events, actions, points, emotion, shot purpose |
| Design | Frames, layers, components | User tasks, interface states, design intent, constraints |

The right-hand column is not a unified industry standard; it is a modeling direction. Different categories will have different objects, and the point is not an all-encompassing knowledge graph but the minimal semantic set needed to complete the core task.

## The new second layer: tasks and result contracts

Semantic objects answer "what's in the product." Tasks answer "what is being changed now." Traditional software defines actions clearly: create, delete, move, export. AI products need a higher layer — the task: goal, inputs, tools, permissions, constraints, results, acceptance and failure handling. "Generate five slides" is a set of actions; "let someone new to the project understand the problem, the plan and the risks within five minutes" defines the result of a task.

A complete task should contain at least:

- **Goal**: what change should be produced;
- **Objects**: which content and state to operate on;
- **Constraints**: which facts, styles, formats and boundaries must not be broken;
- **Tools and permissions**: what may be read and modified;
- **Acceptance**: how to judge completion;
- **Exception handling**: what to do when evidence is insufficient, a tool fails, or a conflict exists.

Today's agent infrastructure is building this layer: MCP exposes standardized Tools and Resources so a model can read external context and call system capabilities, and agent frameworks increasingly emphasize tool calling, guardrails, tracing and execution. But "connected to tools" is only a necessary condition. The product must translate user goals into executable, checkable result contracts. Without one, an agent can only judge "what I did"; with one, it can judge "whether the thing got done."

## The new third layer: operation history, evidence and provenance

When AI can modify many objects at once, the traditional "undo one step" stops being enough. The product needs to record who proposed what goal and when; which materials and tools the AI used; which objects were created, deleted or modified; which conclusion came from which source; what is original content and what is model inference; and what the user accepted, rejected or manually corrected.

If the system only saves final pixels, users can't judge whether a result is trustworthy. If it saves object-level diffs, provenance and an operation log, users can compare versions, roll back locally, audit evidence, and turn effective changes into rules for the next task. So "history" must record file versions together with the relationships between tasks, objects, evidence and operations.

## Editors will stay — but their role becomes a View

A common misconception: since agents can complete tasks directly, editors and GUIs will disappear. They won't. People still need to scan the whole, compare alternatives, refine locally, organize space, make aesthetic judgments, handle exceptions and give final confirmation. Text, canvas, slides, web pages and timelines remain extremely efficient human-machine interfaces.

What changes: they no longer each need their own fragmented "truth." The same set of semantic objects can be presented as a complete document, a set of presentation slides, a whiteboard relationship diagram, a web page, or a video script and timeline.

The GUI shifts from being the only operation entry point to three roles:

1. **State feedback**: showing people what the AI understood and changed;
2. **Fine-grained control**: letting people handle the local problems models handle poorly;
3. **Exceptions and confirmation**: conflicts, high-risk actions and final acceptance.

## Why adding a chat box isn't enough

Chat is an efficient way to express open-ended intent, but it is not a complete product architecture. If every task starts from a fresh conversation, the system faces several problems:

- Context is scattered across message history and hard to maintain;
- Users can't tell which version of the content the model relies on;
- Multiple people and agents can't collaborate around one state;
- Changes lack object-level diffs;
- Memory keeps accumulating but can't be structurally checked or deleted.

The cleaner division of labor: conversation proposes intent and explains results, tasks manage execution, semantic objects carry state, operation history records changes, and the editor handles browsing, control and confirmation. Chat is one entry point, not the product.

## Migration won't happen in one step

Most mature products cannot abandon their file formats, user habits and ecosystems. AI-native will more likely pass through three stages.

### Stage one: AI actions inside the old editor

The model rewrites, generates, completes, classifies and edits locally; the underlying state remains files, pages, layers or timelines. Core metrics: does a single capability save time, and is the result controllable?

### Stage two: a semantic layer, synced bidirectionally with existing objects

The product begins recognizing people, claims, materials, tasks and relationships. AI operates on semantic objects; the interface maps changes back to pages and layers; manual edits sync back into the semantic state. The hardest part here is not generation quality — it is identity consistency, synchronization, conflict, permissions and user trust.

### Stage three: semantic and task state become the primary state

Files and editors become multiple views; one task spans documents, presentations, designs and external tools; agents collaborate over shared objects, permissions and operation history. This is still a long-term projection: it holds only if the product genuinely needs cross-medium tasks, and if the semantic layer's benefits outweigh its complexity.

## Roadmaps and metrics change too

If the basic unit changes, so does how product teams measure progress. Old roadmaps are feature-based: add a generation entry point, support a format, ship a model. AI-native products should track:

- Which complete tasks are reliably covered;
- Task completion rate and the cost of human correction;
- Whether key objects and relationships are correctly recognized;
- Whether provenance and evidence are complete;
- Whether large-scale changes are inspectable and reversible;
- Whether the same state stays consistent across views;
- Whether users hand the same task to the system again.

Generation quality still matters. It is just one part of task completion.

## Conclusion: the basic unit determines what the product becomes

Traditional editors were built around direct human manipulation, which is why pages, files, layers and timelines became their basic units. AI can understand higher-level intent and operate on many objects at once; to absorb that capability, products must re-express their own state. A chat box beside the old interface is only the first step.

Not every product needs agents, and not all content needs an elaborate semantic graph. The practical test:

> If the user's core task spans multiple pages, objects and tools, and the AI needs to keep understanding goals, relationships and history, then the product should elevate task and semantic state to first-class objects.

Pages will still exist, files will still be delivered, editors will still be used — but increasingly as windows through which people observe and control product state, not the state itself.

---

## References

- [Notion API: Block object](https://developers.notion.com/reference/block)
- [Figma Developer Docs: REST API and node structure](https://developers.figma.com/docs/rest-api/)
- [Model Context Protocol: Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)
- [Model Context Protocol: Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
- [OpenAI: New tools for building agents](https://openai.com/index/new-tools-for-building-agents/)
