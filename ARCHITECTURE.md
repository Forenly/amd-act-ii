# Architecture — GrootNet (AMD Developer Hackathon: ACT II)

> Decentralized multi-agent robotic brain and vision-language-action (VLA) inference on distributed **AMD Instinct MI300X** instances via ROCm 7.x. Specialized expert nodes are stitched into one composite brain by a central **Frankenstein Model Node** — no physics simulator in the loop.

---

## High-level distributed flow

```
   Natural-language task goal + observation (image / robot state)
                         │
                         ▼
   ┌────────────────────────────────────────────────────────┐
   │  Frankenstein Model Node (Central Fusion Hub)          │
   │  - Receives task goal + observation                     │
   │  - Routes to the relevant expert nodes (MoE gating)     │
   │  - Stitches distributed experts into one brain          │
   └─────────────────────────┬──────────────────────────────┘
                             │
            ┌────────────────┼────────────────┐
            │ Query Expert   │ Query Expert   │ Query Expert
            ▼ (REST/gRPC)    ▼ (REST/gRPC)    ▼ (REST/gRPC)
   ┌────────────────┐┌────────────────┐┌────────────────┐
   │ Node A (Visual)││ Node B (Loco)  ││ Node C (Manip) │
   │ - Frame decode ││ - Pretrained   ││ - Bimanual joint│  Distributed
   │ - SigLIP embeddings││   joint policy ││   trajectory   │  Inference Fleet
   │ - 3D coordinates││ - Balance control││   optimization │  on ROCm
   └────────┬───────┘└────────┬───────┘└────────┬───────┘
            │                 │                 │
            └─────────────────┼─────────────────┘
                              │ Return per-expert action logits
                              ▼
   ┌────────────────────────────────────────────────────────┐
   │  Frankenstein Fusion → single unified action command   │
   │  - Weighted late fusion / MoE gating of expert logits  │
   └─────────────────────────┬──────────────────────────────┘
                             │
                             ▼
   ┌────────────────────────────────────────────────────────┐
   │  Distributed LoRA Fine-Tuning & Skill Adaptation       │
   │  - Backpropagate successful experiences to models      │   ROCm-accelerated
   │  - Continuous offline/online training on MI300X        │   LoRA training
   └────────────────────────────────────────────────────────┘
```

---

## Component breakdown

| Component | Role | Compute Platform |
|---|---|---|
| **Frankenstein Model Node** | Central fusion hub: receives the task goal + observation, routes to the relevant VLA expert nodes (MoE gating), and stitches their returned action logits into one unified command. Every member's expert node connects here. | AMD Instinct MI300X / Cloud Host |
| **Node A (Visual Search)** | Decodes frames, runs vision backbones (e.g. SigLIP / ViT), and localizes objects (like abajurs/lamps) in 3D coordinate space. | AMD Instinct MI300X |
| **Node B (Locomotion)** | Serves joint control networks to generate high-frequency leg joint angles (using pre-trained gymnasium policy networks). | AMD Instinct MI300X |
| **Node C (Manipulation)** | Serves hand/arm VLA model experts to control bimanual tasks (grasping, reaching, operating switches). | AMD Instinct MI300X |
| **Distributed LoRA Tuner** | Executes background parameter-efficient fine-tuning on successful trajectories to adapt and improve skills over time. | AMD Instinct MI300X (ROCm) |

---

## Compute specifications (per expert node)

| Resource | Value |
|---|---|
| **GPU** | AMD Instinct MI300X |
| **VRAM** | 192 GB (unified HBM3 at 5.3 TB/s) |
| **Runtime** | ROCm 7.x |
| **Framework** | PyTorch (ROCm build) |
| **LoRA Accelerator** | PEFT / DeepSpeed (ROCm compatible) |

---

## Architectural advantages on AMD MI300X

1. **Elimination of Model Parallelism:** Standard VLA models require deep multi-modal stacks (giant vision encoders coupled with LLM policy backbones like Llama-3). Traditionally, this required model split over multiple small-VRAM GPUs. The MI300X's massive **192 GB unified memory pool** lets us fit the entire encoder-decoder stack in a single GPU pass with zero communication overhead.
2. **Distributed Reliability:** By distributing the specialized expert models across different team members' nodes, we build a redundant, highly-available robotic brain. If one node fails or undergoes fine-tuning, the Frankenstein node can fall back to standard heuristics or general VLA nodes.
3. **Decentralized Co-Training:** Training robotic skills is extremely compute-intensive. By distributing the training data backoff, each member's MI300X runs parallel LoRA fine-tuning for their specialized skill, allowing the entire system to develop capabilities in a decentralized fashion.
