# GrootNet — Decentralized Multi-Agent Robotic Brain on AMD Instinct MI300X

> [!IMPORTANT]
> ### 🏆 GRAND PRIZE POOL: Elite Developer GPUs & Cash!
> **Prizes:** State-of-the-art AMD Instinct / Radeon hardware & cash rewards to accelerate our AI models locally! Let's unlock raw performance! 🚀🔌

> Entry for the **AMD Developer Hackathon: ACT II** (lablab.ai × AMD). *"Build AI agents and high-performance AI apps on AMD GPUs in the cloud."* Online · build **Jul 6–11, 2026** · **$10,000 prize pool.**

**GrootNet** is a decentralized, distributed robotic brain network for autonomous robot skill acquisition, served across a fleet of AMD Instinct MI300X GPUs via ROCm.

Instead of deploying one monolithic model on one GPU, **GrootNet** splits the brain into specialized **Groot 1.7** VLA (Vision-Language-Action) expert nodes — one per team member's cloud-allocated MI300X — and stitches them together at inference time into a single composite **Frankenstein Model Node**. Each member's expert node connects to this central Frankenstein node, which fans out every task, then fuses the experts' returned action logits into one unified command. A brain assembled from many distributed parts — hence *Frankenstein*.

## Community

Building this in the open — join the team chat on Discord: https://discord.gg/wWwUrHhyqg

## The hackathon

Centered on **AI Agents** — intelligent workflows, automation, and real AI applications — built on **AMD AI Developer Cloud**, **ROCm**, and cloud-accessible **AMD Instinct MI300X** GPUs. Everything runs in the cloud; the focus is building, experimenting, benchmarking, and scaling AI workloads. Full challenge details drop at the kickoff.

Members of the AMD AI Developer Program get **$100 in Dev Cloud credits**, MI300X access, AMD AI Academy resources, a 1-month DeepLearning.AI Pro membership, and expert office hours.

## What we're building

We are building a **peer-to-peer network of specialized Groot 1.7 expert nodes** fused by a central **Frankenstein Model Node**. Each expert runs a large VLA model (e.g., fine-tuned LLaVA-based policies or OpenVLA) on an **AMD Instinct MI300X** instance (192 GB VRAM, ROCm 7.x). By utilizing each member's $100 AMD credit, we spin up a distributed cluster of specialized neural experts:

* **Node A (Visual Search Expert):** Camera observation analysis, frame decoding, and 3D coordinate detection on MI300X.
* **Node B (Locomotion Expert):** High-frequency joint angles and balance metrics for walking.
* **Node C (Manipulation Expert):** Bimanual hand and arm trajectory control for dexterous interaction.

At the center, the **Frankenstein Model Node** stitches these distributed experts into one brain: for each task goal + observation it fans out to the relevant experts and **fuses their returned action logits** into a single unified command (MoE-style late fusion / weighted gating). Every member's node connects to this Frankenstein node, creating a **collaborative, decentralized robotic brain** powered entirely by high-performance AMD hardware — no physics simulator in the loop.

Key components:
- **Distributed VLA Inference** — Multiple decentralized Groot 1.7 expert nodes served with PyTorch on ROCm.
- **Frankenstein Model Node** — Central fusion hub that stitches the distributed experts into one brain, routing each task to the relevant experts and fusing their action logits (MoE gating / weighted late fusion) into a unified command.
- **Skill Co-Training & Adaptation** — Saving successful trajectory data to dynamically fine-tune expert models on their respective MI300X GPUs via LoRA.
- **Performance Harness** — Throughput and latency benchmarking comparing FP16 vs INT8 execution on MI300X.

## Architecture

See [`ARCHITECTURE.md`](./ARCHITECTURE.md) for the full system diagram.

```
   Natural-language task goal + observation (image/state)
                         │
                         ▼
             ┌────────────────────────┐
             │  Frankenstein Model     │
             │  Node (Fusion Hub)      │
             │  route → fuse logits    │
             └───────────┬────────────┘
                         │ fan-out (REST/gRPC)          ▲ fuse action logits
        ┌────────────────┼────────────────┬────────────┴───┐
        ▼ (Query Expert)  ▼ (Query Expert) ▼ (Query Expert)  ▼ (Query Expert)
   ┌───────────┐    ┌───────────┐    ┌───────────┐    ┌───────────┐
   │  Node A   │    │  Node B   │    │  Node C   │    │  Node D   │
   │ (Visual   │    │(Locomotion│    │ (Dexterous│    │ (Anomaly  │
   │  Search)  │    │  Expert)  │    │ Manipulation)  │ Detection)│
   └───────────┘    └───────────┘    └───────────┘    └───────────┘
   ────────────────────────────────────────────────────────────────
                    AMD Instinct MI300X GPU Fleet
                     (192 GB VRAM per Node · ROCm)
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

🚧 Enrolled, pre-kickoff. Concept: Decentralized VLA expert nodes fused by a central **Frankenstein Model Node** on AMD MI300X (ROCm) — no physics simulator. See [`docs/HACKATHON_REQUIREMENTS.md`](./docs/HACKATHON_REQUIREMENTS.md).

— *Part of the [Cadence](https://github.com/Forenly) multi-hackathon initiative.*
