---
layout: post
title: "My Three AIs Left Me 24 Unaccounted Debts"
date: 2026-10-02 18:00:00 +0800
permalink: "/en/notes/ai-workspace-debt/"
content_id: ai-workspace-debt
knowledge_topic: product-research
knowledge_units: [research-workflows]
translation_of: /notes/ai-workspace-debt/
lang: en
reading_time: 7
description: "24 complete versions and 7 forked scripts. The real cost of copied agent output is losing track of what is authoritative."
generated_translation: true
---

<p>One day in September, I opened the workspace to find a file. I have forgotten what to look for, because as soon as I entered the catalog, I first saw 24 full versions of the same plan.</p>

<p>24 versions.</p>

<p>Each round drops a full-volume file, neatly and tilled, adding up to 40M. There is also a project presentation next to it, 20 versions, each version can store three formats of web pages, PDF and presentation files at the same time, and more than 60 files are stacked in the root directory.</p>

<p>Who makes these things? It&#x27;s my three AI working environments. Each of the three entrances has its own catalog, and the session, dependency and skill copies are produced separately. No one knows what the other party has produced.</p>

<p>I took a look at the volume: 28G. After two rounds of cleaning, the same directory is 22G. The 6G saved is the least important number. The real problem is that the production mode of files has changed, and the directory structure is still growing in the era of human code.</p>

<h2 id="占空间只是表象分叉才是成本">Occupying space is just an appearance, and forking is the cost.</h2>

<p>There are six types of symptoms in that inventory:</p>

<ul>
  <li>Leave 24 full versions of the same plan;</li>
  <li>One project retains three export formats at the same time;</li>
  <li>There are 15 scattered dependencies in the directory, with a total of 1.34G;</li>
  <li>The same collection script was copied into 7 projects with different contents;</li>
  <li>Temporary rendering and candidate files have accumulated 330M, never recycled;</li>
  <li>After the browser cache is cleared, it will grow back to more than 2G in a few days.</li>
</ul>

<p>The most worth seeing is Article 4. 7 scripts are of the same origin, but they have been changed to 7 different things in their respective projects. The repair in any copy has not flowed back to the other 6 copies. The same bug needs to be repaired in each of the 7 copies, and there is no reminder mechanism.</p>

<p>There was another almost accident: the two paths looked like two files, but they were actually the same batch of data. One side was deleted, and the other side was lost. After deleting duplicate files, I will compare the identity of the file first, and then compare the content.</p>

<h2 id="ai-生产文件的三种垃圾">Three kinds of garbage of AI production files</h2>

<p>In the era of people writing code, there is also garbage: temporary scripts are forgotten to be deleted, download directories are full, and old projects are reluctant to be cleared. After the participation of AI, the quantity and nature have changed.</p>

<p><strong>The first category is the complete intermediate version.</strong>A new file is dropped in each round, which is the most natural way for AI to save results. People often change the same document, and AI is more likely to continuously produce complete copies. Therefore, the copy folder has degenerated into version management, and the directory tree is full of history that should have been saved by the version management tool.</p>

<p><strong>The second category is dependent on copies.</strong>There is no psychological burden to execute the installation command, and a command will drop a directory starting from tens of megabytes. 15 places depend on the directory, corresponding to more than a dozen &quot;install an environment first and run it out&quot;.</p>

<p><strong>The third category is tool fork.</strong>The method has been written as a skill, but the engineering assets are still wandering in the whole catalog. Every time a new project is opened, one is copied and changed, and it is changed into several parallel universes.</p>

<p>The methodology has been skilled, but the engineering assets have not yet been.</p>

<h2 id="两轮清理改了四件事">Two rounds of cleaning changed four things.</h2>

<p><strong>Version chain: the finalization area is separated from the historical archive.</strong>Only the current representative version is placed in the final draft area, and the historical version is archived as a whole, and only the milestones are retained; the round of pure format fine-tuning is directly deleted.</p>

<p><strong>Tool Center: an entity, multi-end mounting.</strong>The skills and pipelines are compiled into a single entity, and each work entrance is mounted and used. The bifurcated collection script is merged back to one copy, and the difference is changed to parameters.</p>

<p><strong>The garbage that will return will be handed over to the scheduled task.</strong>The cache is cleaned regularly; the temporary product task is deleted at the end, and the rules of each work entrance are written.</p>

<p><strong>The project directory is merged.</strong>Archive or delete the wreckage of a one-time task. There is a pitfall here: the virtual environment binds the absolute path, and the script reports an error collectively after the warehouse moves. Think clearly before moving the catalog of this kind of thing.</p>

<h2 id="每个资产只允许一个上游">Each asset, only one upstream is allowed.</h2>

<p>After two rounds of liquidation, the governance experience is crushed into a principle: each asset is only allowed to have one upstream.</p>

<p>The only upstream here is not that there can only be one physical copy on the disk, but only one copy has the right to modify and the status of true source. Other copies must be reconstructible and traceable derivatives.</p>

<p>Copying itself is not foul. Package release, cloning, backup, construction products, cache, all of which are copied and reasonable, because there is only one real source, and it can be regenerated at any time after modification. The foul is to let the copy quietly get the right to modify. The problem with 7 forked scripts is that 7 copies can be saved, and 7 copies can be changed. No one is an authority.</p>

<p>The physical mounting of a tool is the embodiment of this principle in space; the entry of the version into version management is the embodiment of its time; the temporary product will be deleted when it is used up, which is to recognize that such files do not deserve to have upstream at all.</p>

<h2 id="先分清什么算资产">First, distinguish what is an asset.</h2>

<table>
  <thead>
    <tr>
      <th>Classification</th>
      <th>What are you pretending to be?</th>
      <th>Governance rules</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>True source</td>
      <td>Prompts, skills, source code, templates, original data, rules</td>
      <td>Versioning</td>
    </tr>
    <tr>
      <td>Sentis</td>
      <td>Web pages, PDFs, presentations and reports exported from Zhenyuan</td>
      <td>Can be rebuilt</td>
    </tr>
    <tr>
      <td>Temporary status</td>
      <td>Rendering, candidate file, cache, dependent directory</td>
      <td>There is a survival period</td>
    </tr>
  </tbody>
</table>

<p>There are no ready-made seats for conversation memory in this table. The conclusions worth reusing are precipitated back to the true source, and the rest are treated as temporary, and the total amount is controlled by archiving.</p>

<p>The debt is not reflected on the disk. The 7 bifurcated scripts do not take up much space, occupying the repair time spent repeatedly on each copy, and there is no reminder mechanism.</p>

<h2 id="下一轮">The next round</h2>

<p>22G is not a number that can declare victory. In the next round, two things should be checked: whether the mount will be quietly copied by an entrance; and whether the temporary product can expire automatically according to the whitelist instead of relying on consciousness.</p>

<p>After scanning a copy, the generation rules are not changed, and the next round will grow back.</p>

<p>I opened the folder again today. There is a plan in the final draft area, and there is an archive directory next to it, which is quiet. The history is handed over to the version management, and the directory tree is only placed in the current state.</p>

<p>As for the 24 debit notes, the account has been settled.</p>

<hr/>

<p><strong>Public explanation</strong>: This article deletes specific AI tools, platforms, customers and internal paths, and retains problems, numbers and governance methods. The personal experience in the original text can be checked, but the identity of the partner cannot be restored accordingly.</p>
