---
layout: post
lang: en
title: "Robots Don't Replace People — They Give People New Bodies"
subtitle: "Beyond replacement rates: how robots extend human vision, presence, action and physical attributes."
date: 2026-08-14 09:12:00 +0800
reading_time: 10
tags:
  - robotics
  - embodied intelligence
  - human-robot collaboration
description: A capability-gain lens on robots: people keep intent, judgment and high-risk commitments, agents handle shared control, and robot bodies carry human capability to places the body can't reach.
permalink: /en/notes/robots-give-people-new-bodies/
---

I have worked on panoramic cameras, 360-degree drones and follow-cameras, and on consumer home-security robots. The hardware looks nothing alike — some you hold, some fly, some follow you around, some patrol the house.

But they all did the same thing.

They extended a person's vision, position or actions to places the body cannot reach.

That changed how I look at robots.

The industry's default question is: how many people does one robot replace? That has to be asked. Factories, warehouses, cleaning and standardized services need to compare efficiency, labor cost and payback period. But if you only look at replacement rates, a lot of robots get undervalued — or put in the wrong market.

The drone's early value was not replacing a helicopter shoot at a lower price. Most creators would never have rented a helicopter at all. Drones gave them, for the first time, a pair of eyes that could fly — and only then did new camera positions, shot language and workflows appear.

The photographer didn't leave the task. He gained a body capability: flight.

So next to "replace people," I want a second product line:

> Robots can also give people a new body.

"Body" here is a product metaphor, not a biological claim. And the headline is not denying that robots replace labor. It is a reminder to ask an additional question: once the user has this robot, what can they now do reliably for the first time?

## Replacement and augmentation are two different product problems

If the goal is replacement, the team decomposes the full human workflow, then asks how much of it the robot can cover, how low the intervention rate can go, and whether unit cost is lower.

If the goal is a new body, the starting point flips: where can people not see, not reach, not hold steady, not afford the risk? How does the robot connect that capability to the person?

| | Replacement product | "New body" product |
| --- | --- | --- |
| Starting point | Which labor can be automated | Which usable capability a person lacks |
| Human's role | Exit routine flows gradually, handle exceptions | Keep intent, judgment and high-risk commitments |
| Autonomy goal | Raise task coverage, lower human intervention | Reduce operating burden while keeping a sense of control |
| Core metrics | Completion rate, intervention rate, unit cost, ROI | Task reachability, outcome gain, control burden, recovery time |
| Market source | Existing, priced labor | Tasks that never happened due to distance, danger, scale or cost |

The two lines overlap. An inspection robot can both keep people out of the site and let engineers see what they could not observe before. The difference is what the product optimizes first.

With replacement as the goal, teams treat autonomy as a progress bar. With capability gain, they care whether the person and machine form a stable loop: was my intent transmitted correctly, what is the machine doing now, does feedback come back, and can I catch it when something goes wrong.

## Four verifiable body extensions

"A new body" cannot stay rhetorical. Break it into four capabilities.

| Extension | What the user gains | Typical products | What must be verified |
| --- | --- | --- | --- |
| Vision | See positions and scales the body can't | Drones, mobile cameras, inspection and endoscopic devices | Faster discovery, recording or understanding of targets |
| Presence | Observe, communicate and intervene without being there | Telepresence, home mobile terminals | Can the remote person understand the scene and act |
| Action | Reach farther, steadier, smaller, more precise | Robotic arms, surgical assistance, camera robots | Higher operation quality, errors caught in time |
| Attributes | Heat resistance, radiation resistance, endurance, flight | Firefighting, nuclear, deep-sea, pipeline and high-altitude robots | People removed from danger while keeping necessary control |

The extensions stack. A pipeline robot extends vision and changes body size and tolerance; surgical assistance adds 3D vision and fine action at once; a home security robot extends a user's "presence" beyond leaving the house.

This classification is closer to user value than "wheeled, quadruped, humanoid, flying." The body form explains how the capability is implemented; the body extension explains why the user needs it.

## When does a machine start to feel like "my body"?

In 1996, Iriki and colleagues trained macaques to retrieve distant objects with a rake and recorded that some neurons processing both touch and vision extended their visual receptive fields to the rake's length — the enlarged reachable space. They interpreted this as the tool being incorporated into a modified hand body schema. [Iriki et al.: Coding of modified body schema during tool use](https://pubmed.ncbi.nlm.nih.gov/8951846/)

One macaque experiment cannot prove that people treat robots as their bodies, and it cannot replace real product research. The clue it offers: whether a tool enters reachable space has little to do with how humanoid it looks — what matters is whether control and feedback form a stable correspondence.

So a robot cannot just be a remote switch.

The user needs to know where it is, which way it faces, what it sees; how their own action or intent becomes machine motion; when the system is correcting for them; how much latency there is; and whether a lost connection stops, retreats or continues.

Only when these relationships are stable does skill accumulate. The longer a user works with it, the better they should control it — not re-guess what the machine will do each time.

The feeling of "mine" comes from a predictable loop.

## Autonomy level is not a grade to graduate from

Giving someone a new body does not mean remote-controlling every joint.

Full manual control dumps every degree of freedom and every correction on the user — too much cognitive load. Full autonomy requires the system to understand intent, handle the long tail and own mistakes in open environments. Many viable products sit in between: the person gives goals and constraints; the robot handles stability, obstacle avoidance, path and local actions.

This division is usually called shared autonomy.

The FDA's description of computer-assisted surgical systems is a mature example: the surgeon moves instruments via a console and software, observes a 3D operative field, and performs complex maneuvers in tight spaces — while the FDA is explicit that these devices do not perform surgery independently without direct human control. [FDA: Computer-Assisted Surgical Systems](https://www.fda.gov/medical-devices/surgery-devices/computer-assisted-surgical-systems)

That doesn't diminish the machine's value. The doctor keeps diagnosis, strategy and critical judgment; the system brings vision and motion to places the hand cannot directly reach.

Shared autonomy has costs. A 2017 study had a robot assist when the user's exact goal was unknown; some tasks improved in completion speed and input efficiency, while the study also observed that autonomous assistance could lower some users' sense of control, and different people adopted different strategies. [Javdani et al.: Shared Autonomy via Hindsight Optimization](https://arxiv.org/abs/1706.00155)

So more autonomy is not automatically better, and not every product ends at the same place. Optimize the outcome of the collaboration: how much low-level burden the machine absorbs, and how much understanding and control it preserves for the person.

## Agents can be the motor nerves of this body

When a person picks up a cup, they don't compute each muscle contraction. They express high-level intent; the nervous system handles joints, force and balance; vision and touch send results back.

An agent paired with a robot can form a similar abstraction layer.

A creator tells a follow-camera: "stay low and follow the person ahead." They keep narrative, composition and timing; the agent handles tracking, route, speed, obstacle avoidance and stabilization.

A remote user tells a home robot: "go to the kitchen and check whether the faucet is still running." The robot handles navigation, finding the sink and streaming video. Whether to shut the valve, contact family or keep going is confirmed with the person, based on risk and permissions.

A maintenance engineer tells a robot: "move to the right of the valve so the nameplate and the joint are both in frame." The system plans posture and avoids collisions while the engineer judges the anomaly.

The control chain has to be bidirectional:

> Human intent ⇄ Agent shared control ⇄ Robot body ⇄ Physical world

With commands only going out — no position, vision, force, collision or failure state coming back — the user cannot form a sense of control. And when the agent corrects an action without saying why, the body becomes foreign.

A drone shared-autonomy experiment gives a concrete example: when an autonomous system intervenes for safety, it changes the operator's control; adding haptic feedback — returning how the system is correcting to the person — improves human-robot agreement and satisfaction. [Mullen et al.: Haptic Feedback Improves Human-Robot Agreement](https://arxiv.org/abs/2103.03453)

Feedback is not interface decoration. It is half of the loop.

## A "new body" has to pass six product gates

A camera, a chassis and a remote control don't make a robot an extension of a person.

I check six things.

1. **Locatable**: the user always knows where the robot is, which way it faces, and its relationship to the target.
2. **Perceivable**: video, audio, depth, force or touch sufficiently support the current judgment — not just a streamed picture.
3. **Predictable**: same inputs produce similar actions; latency and autonomous corrections stay within understandable bounds.
4. **Takeover-able**: the user knows when they are in direct control and when the agent is planning; high-risk steps can be paused, taken over, or returned to a safe state.
5. **Learnable**: with more use, the user gets faster and more accurate and forms stable strategies.
6. **Recoverable**: after network loss, recognition errors, jamming or mistakes, the robot can stop safely or return to a known state.

Missing one or two of these, a demo can still look great; in long-term use, users will treat it as a remote device they constantly have to watch.

Capability gain needs its own accounting. What could this person accomplish without the robot? Of the new tasks the robot enables, how many repeat reliably, produce benefit or reduce risk? Does the gain exceed the burden of training, attention, maintenance and failure recovery?

If the user has only swapped a simple action for operating a complex machine, the product hasn't augmented them.

## The first users often know what a new capability is worth

A "new body" robot doesn't have to sell to everyone first.

Photographers know whether a new camera position changes the final shot; maintenance engineers know what one fewer trip into a dangerous space is worth; doctors know what vision and control precision mean for outcomes; professional inspectors can calculate the value of one avoided shutdown.

These users being willing to learn doesn't mean the interaction can be crude. It means they can judge whether the capability gain is real, and translate it into revenue, quality, time and risk — which is exactly the Professional role I described in [Geek, Professional, B2B, Consumer: Markets as Evidence Environments](/en/notes/market-roles-remove-uncertainty/). Professionals are the right first environment to validate workflow value and quality thresholds; the mass market then tests onboarding, maintenance and long-term reuse.

Augmentation is not automatically more valuable commercially than replacement. If a new capability has no high-frequency task, the outcome is invisible, or control costs eat the benefit, users won't pay. The lens just puts demand that replacement rates miss back into product judgment.

From now on, when I look at a robot, I ask two questions together.

How much existing labor does it save?

And what capability does a person gain for the first time?

The first question points at an efficiency market.

The second may open a market that didn't exist.

---

## References

- [Iriki et al.: Coding of modified body schema during tool use](https://pubmed.ncbi.nlm.nih.gov/8951846/)
- [FDA: Computer-Assisted Surgical Systems](https://www.fda.gov/medical-devices/surgery-devices/computer-assisted-surgical-systems)
- [Javdani et al.: Shared Autonomy via Hindsight Optimization](https://arxiv.org/abs/1706.00155)
- [Mullen et al.: Haptic Feedback Improves Human-Robot Agreement](https://arxiv.org/abs/2103.03453)
- [Agents go left, embodiment goes right: how AI diverges in information space and the physical world](https://roy-tong.github.io/notes/agent-left-embodied-right/)
- [Why home robots are technically harder and economically richer](https://roy-tong.github.io/notes/home-robots-harder-richer/)
