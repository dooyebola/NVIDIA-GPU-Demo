## Architecture Decision 002 — AI Workload Requirements

**Status:** Proposed — Not Yet Validated

### Business Objective

Design a conceptual enterprise AI inference platform
capable of serving large language models to multiple
customers while supporting performance, reliability,
and future infrastructure expansion.

### Proposed Workload

- Workload Type: Enterprise AI inference
- AI Model Class: 405B parameters
- Model Precision: BF16
- Maximum Context Length: 32,000 tokens
- Target Concurrent Active Requests: 100
- Availability Objective: 99.9%
- p95 Time to First Token: 5 seconds or less

### Proposed Infrastructure

- NVIDIA GB200 NVL72
- 72 NVIDIA Blackwell GPUs
- 36 NVIDIA Grace CPUs
- 18 Compute Trays
- 9 NVLink Switch Trays

### Proposed Software

- vLLM for AI model serving
- Kubernetes for workload orchestration
- NVIDIA GPU Operator for GPU integration

### Preliminary Memory Sizing

Model parameters: 405 billion
Precision: BF16 (2 bytes per parameter)

Estimated model weight memory:

405,000,000,000 x 2 = 810,000,000,000 bytes

Approximately 810 GB of model weights.

This does not include:
- KV cache
- Runtime overhead
- Temporary allocations
- Model replicas
- Other serving requirements

### Architecture Considerations

1. Estimate total GPU memory requirements.
2. Determine model parallelism strategy.
3. Evaluate concurrent request capacity.
4. Define latency and throughput objectives.
5. Plan networking and storage requirements.
6. Design monitoring and alerting.
7. Evaluate high availability and recovery.
8. Compare NVL72 against smaller alternatives.

### Validation Status

This architecture is a conceptual engineering study.

GPU sizing, concurrency, latency, availability,
and hardware selection require further analysis.

No physical GB200 NVL72 deployment has occurred.

## Architecture Decision 003 — GPU Capacity Sizing

**Status:** Preliminary Analysis

### Model Weight Memory

Model parameters: 405 billion
Precision: BF16
Bytes per parameter: 2

Estimated weights:
405,000,000,000 * 2 = 810 GB

### Additional Memory Requirements

- KV cache for active requests
- Model execution overhead
- Temporary GPU allocations
- Memory for concurrent inference
- Model replicas and redundancy

### Outstanding Calculations

1. Determine the model's KV-cache architecture.
2. Estimate average and maximum active tokens.
3. Calculate KV-cache memory requirements.
4. Estimate runtime memory overhead.
5. Calculate minimum GPU count for model weights.
6. Evaluate GPU parallelism configurations.
7. Compare smaller GPU cluster options.
8. Validate throughput and latency targets.

### Design Limitation

The current workload requirements are hypothetical.
No physical GB200 NVL72 system has been tested.

The full 72-GPU rack has not yet been
justified by capacity or performance analysis.


## Architecture Decision 004 — KV Cache and GPU Sizing

**Status:** Preliminary / Not Validated

### Reference Model

Meta Llama 3.1 405B Instruct

- Parameters: approximately 405 billion
- Layers: 126
- Attention heads: 128
- KV heads: 8
- Head dimension: 128
- Weight precision: BF16
- KV-cache precision: BF16 (assumed)

### Workload Assumptions

- Maximum active tokens per request: 32,000
- Concurrent active requests: 100
- All requests at full context: worst-case scenario
- Availability objective: 99.9%
- p95 first-token latency target: <= 5 seconds

### Model Weight Memory

405,000,000,000 parameters * 2 bytes

Estimated weight memory: 810 GB

### KV Cache Per Token

Formula:

2 * layers * KV heads * head dimension * bytes

2 * 126 * 8 * 128 * 2 = 516,096 bytes

KV cache per token: 504 KiB

### Total KV Cache

516,096 * 32,000 * 100

Total: 1,651,507,200,000 bytes

Approximately 1.652 TB of KV-cache memory.

### Combined Memory

Model weights: 810 GB
KV cache: 1,651.5 GB

Combined: approximately 2,461.5 GB (2.462 TB)

Excluded:
- Runtime overhead
- Memory fragmentation
- Communication buffers
- Temporary allocations
- Replica and failover requirements

### Preliminary GB200 GPU Comparison

Assumed nominal HBM3e per GPU: 186 GB

8 GPUs:
1,488 GB — insufficient.

16 GPUs:
2,976 GB — theoretical fit with limited headroom.

24 GPUs:
4,464 GB — more memory headroom.

72 GPUs:
13,392 GB — not justified by memory alone.

### Proposed Evaluation Baseline

24 GB200 GPUs

Initial candidate configuration:
- Tensor parallelism: 8
- Pipeline parallelism: 3

Requires validation of:
- Model partitioning
- vLLM and GB200 compatibility
- KV-cache distribution
- Runtime memory requirements
- Latency and throughput
- NVLink topology and scheduling
- Infrastructure cost

### Architecture Recommendation

Do not assume the full 72-GPU NVL72 rack is
necessary for this workload.

Evaluate smaller GPU allocations first.

Select the final GPU count based on measured
performance, memory utilization, availability,
and total cost.

### Limitations

All calculations are theoretical.

No GB200 NVL72 hardware has been tested.

The 99.9% availability objective cannot be
established from memory sizing alone.

Additional failure-domain and redundancy
analysis is required.


## Architecture Decision 005 — GPU Configuration Comparison

**Status:** Under Evaluation

### Business Objective

Identify a technically feasible and cost-effective
GPU configuration for enterprise large-model inference.

### Workload Requirements

- Reference model: Llama 3.1 405B Instruct
- Precision: BF16
- Active context: 32,000 tokens per request
- Concurrent active requests: 100
- Availability target: 99.9%
- p95 first-token latency target: <= 5 seconds

### Option A — 16 GB200 GPUs

Nominal GPU memory: 2,976 GB
Theoretical memory headroom: 514.49 GB

Advantages:
- Lower allocated GPU count
- Potentially lower compute resource consumption

Risks:
- Limited memory headroom
- Runtime overhead not included
- Performance and feasibility unvalidated

### Option B — 24 GB200 GPUs

Nominal GPU memory: 4,464 GB
Theoretical memory headroom: 2,002.49 GB

Advantages:
- Greater theoretical memory headroom
- Additional capacity for runtime allocations

Risks:
- Parallelism configuration requires validation
- Latency and throughput remain unknown
- Infrastructure cost remains unknown

### Option C — Full GB200 NVL72 Rack

Nominal GPU memory: 13,392 GB
Theoretical memory headroom: 10,930.49 GB

Advantages:
- Full rack-scale GPU infrastructure
- Substantial aggregate GPU memory
- Potential capacity for additional workloads

Risks:
- High infrastructure and facility requirements
- Power and liquid-cooling dependencies
- May be oversized for the reference workload

### Cost Evaluation

The following must be established:

1. Supported hardware deployment configurations
2. Capital or rental infrastructure costs
3. GPU utilization and workload throughput
4. Power and cooling requirements
5. Networking and storage costs
6. Operations and support costs
7. Availability and disaster recovery
8. Total cost per million generated tokens

### Preliminary Recommendation

No final GPU configuration selected.

Memory sizing alone cannot establish the
optimal GPU count or production feasibility.

Additional compatibility, performance,
cost, and failure-domain analysis is required.

### Validation Status

Conceptual architecture comparison only.

No NVIDIA GB200 NVL72 deployment has occurred.

## Architecture Decision 006 — GPU Cost and Performance Evaluation

**Status:** Hypothetical Analysis — Not Validated

### Objective

Compare the potential cost efficiency of
16-, 24-, and 72-GPU allocations for
enterprise AI inference.

### Modeling Assumptions

- Hypothetical GPU cost: $10 per GPU-hour
- Monthly operating hours: 730
- Workload load factor: 60%
- Full NVL72 rack: 72 GPUs
- All throughput values are fictional.

### Assumed Peak Output Throughput

- 16 GPUs: 1,000 tokens/second
- 24 GPUs: 1,600 tokens/second
- 72 GPUs: 4,200 tokens/second

### Allocated GPU Cost Results

| GPUs | Monthly Cost | Cost / 1M Output Tokens |
|---|---|---|
| 16 | $116,800 | $74.07 |
| 24 | $175,200 | $69.44 |
| 72 | $525,600 | $79.37 |

### Full-Rack Billing Results

| Active GPUs | Cost / 1M Output Tokens |
|---|---|
| 16 | $333.33 |
| 24 | $208.33 |
| 72 | $79.37 |

### Preliminary Findings

Under the fictional allocated-GPU billing
and throughput assumptions, the 24-GPU
option has the lowest modeled cost per
million generated tokens.

Under full-rack billing, the 72-GPU
configuration produces the lowest modeled
cost per million tokens for this workload.

These findings are entirely dependent on
the assumed prices, throughput and load.

### Risks and Limitations

- No NVIDIA GB200 throughput was measured.
- GPU hourly pricing is hypothetical.
- Independent deployment feasibility is unverified.
- Real hardware topology may restrict allocations.
- Power, cooling and networking costs are excluded.
- Storage, support and maintenance are excluded.
- Input-token processing costs are excluded.
- Latency and availability targets are unvalidated.
- Idle rack capacity may serve other workloads.

### Recommendation

No final GPU configuration is selected.

Obtain actual vendor pricing and performance
measurements before making a procurement
or deployment recommendation.

Evaluate hardware topology, workload latency,
throughput, resilience and total cost of ownership.

### Validation Status

Conceptual cost-modeling exercise only.

No GB200 NVL72 system was deployed or benchmarked.