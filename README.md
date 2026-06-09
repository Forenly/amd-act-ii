# RoboPerceive — Robot Perception & VLA on AMD MI300X

> [!IMPORTANT]
> ### 🏆 GRAND PRIZE POOL: Elite Developer GPUs & Cash!
> **Prizes:** State-of-the-art AMD Instinct / Radeon hardware & cash rewards to accelerate our AI models locally! Let's unlock raw performance! 🚀🔌


> Entry for the **AMD Developer Hackathon: ACT II** (lablab.ai × AMD). *"Build AI agents and high-performance AI apps on AMD GPUs in the cloud."* Online · build **Jul 6–11, 2026** · **$10,000 prize pool.**

**RoboPerceive** is a vision-language-action (VLA) inference and evaluation system for autonomous robots, served on AMD Instinct MI300X GPUs via ROCm. Given a camera stream and a natural-language goal, the model interprets the scene and emits structured action commands — closing the perception→reasoning→action loop entirely on AMD hardware.

## Community

Building this in the open — join the team chat on Discord: https://discord.gg/wWwUrHhyqg

## The hackathon

Centered on **AI Agents** — intelligent workflows, automation, and real AI applications — built on **AMD AI Developer Cloud**, **ROCm**, and cloud-accessible **AMD Instinct MI300X** GPUs. Everything runs in the cloud; the focus is building, experimenting, benchmarking, and scaling AI workloads. Full challenge details drop at the kickoff.

Members of the AMD AI Developer Program get **$100 in Dev Cloud credits**, MI300X access, AMD AI Academy resources, a 1-month DeepLearning.AI Pro membership, and expert office hours.

## What we're building

A **robot-perception agent** that runs a VLA model (e.g. OpenVLA or a fine-tuned LLaVA-based policy) on **AMD Instinct MI300X** (192 GB VRAM, ROCm 7.x). The system takes image observations and a task description as input and outputs discrete robot actions (move, grasp, navigate). The MI300X's unified memory bandwidth makes it possible to run large vision-backbone + language-policy stacks in a single forward pass — something that previously required multi-GPU setups.

The agent wraps the VLA model in a lightweight inference server, exposes a REST API, and connects to a simulated environment so the full perception→planning→action loop can be demonstrated live.

Key components:
- **VLA model inference** — open-source VLA checkpoint served with PyTorch on ROCm
- **Perception pipeline** — frame decode, embedding, language conditioning on MI300X
- **Action agent** — structured output parsing → robot command dispatch
- **Sim environment** — lightweight PyBullet/MuJoCo sim for end-to-end demo
- **Benchmarking harness** — throughput / latency report comparing FP16 vs INT8 on MI300X

> AMD MI300X is the mandated compute platform. All training, fine-tuning, and inference run exclusively on AMD Developer Cloud / ROCm.

## Architecture

See [`ARCHITECTURE.md`](./ARCHITECTURE.md) for the full system diagram.

```
  Camera frames + task goal
          │
          ▼
  ┌───────────────────────────────────┐
  │  Perception pipeline              │
  │  (vision encoder on MI300X/ROCm)  │
  └──────────────┬────────────────────┘
                 │  visual tokens
                 ▼
  ┌───────────────────────────────────┐
  │  VLA policy model                 │
  │  (language-conditioned, ROCm)     │  AMD Instinct MI300X
  └──────────────┬────────────────────┘  192 GB VRAM · ROCm 7.x
                 │  action logits
                 ▼
  ┌───────────────────────────────────┐
  │  Action agent                     │
  │  (parse → dispatch → sim step)    │
  └───────────────────────────────────┘
                 │
                 ▼
       Robot / simulation output
```

## Requirements & source of truth

Full compiled brief — stack & access, prizes, submission fields, judging criteria — in [`docs/HACKATHON_REQUIREMENTS.md`](./docs/HACKATHON_REQUIREMENTS.md).

## Submission checklist

- [ ] Basic info: title · short + long description · technology & category tags
- [ ] Cover image · video presentation · slide presentation
- [ ] **Public GitHub repository** (MIT) · demo platform · application URL
- [ ] Signed up for the **AMD AI Developer Program** (unlocks credits + approval)
- [ ] Submitted before the deadline on the Schedule tab (**Jul 11, 2026, 7:00 PM TRT** at capture)

## Status

🚧 Enrolled, pre-kickoff. Concept: robot-perception VLA on AMD MI300X (ROCm). See [`docs/HACKATHON_REQUIREMENTS.md`](./docs/HACKATHON_REQUIREMENTS.md).

— *Part of the [Cadence](https://github.com/Forenly) multi-hackathon initiative.*
