# Architecture — AMD Developer Hackathon: ACT II (Forenly)

> Skeleton. Centered on an **AI-agent system** running on the **AMD AI Developer Cloud / ROCm / MI300X** stack. Refined to the concrete concept once the full challenge details are announced.

## High-level flow

```
        User / task
            │  request
            ▼
   ┌──────────────────────────────┐
   │  Agent system                 │
   │   ┌────────────────────┐      │
   │   │ Agent orchestration │      │   planning · tool use · automation
   │   └─────────┬──────────┘      │
   │             ▼                 │
   │   ┌────────────────────┐      │
   │   │ Model inference     │      │   served on AMD GPUs via ROCm
   │   │ (PyTorch on ROCm)   │      │
   │   └─────────┬──────────┘      │
   └─────────────┼─────────────────┘
                 ▼
   ┌──────────────────────────────┐
   │  AMD Instinct MI300X          │   AMD AI Developer Cloud
   │  (192GB VRAM, ROCm 7.x)       │   fully cloud-based
   └──────────────────────────────┘
                 │
                 ▼
        Output / hosted demo + URL
```

## Components

| Component | Role |
|---|---|
| **Agent orchestration** | Plans tasks, calls tools, runs the automated workflow (the "AI agent" core of the challenge). |
| **Model inference** | Open-source models served via **ROCm** (PyTorch/TensorFlow on AMD), tuned/benchmarked on GPU. |
| **AMD Instinct MI300X** | The compute layer — on-demand via AMD AI Developer Cloud (192GB VRAM, ROCm 7.x). No local setup. |
| **Hosted demo** | Public deployment + application URL, with a public MIT-licensed GitHub repo. |

## Notes
- Forenly's existing MI300X Dev Cloud workflow (ROCm 7.x, from_pretrained pipelines) is directly reusable here.
- Performance experimentation / benchmarking on MI300X is explicitly encouraged by the challenge.

_(Diagram and detail to be completed after the full challenge reveal and concept lock.)_
