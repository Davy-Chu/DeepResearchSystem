# Research Run Log

## Run Summary

**System Version:** evidence-ledger-decomposer-verifier-v1

**Research Question**

How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

**Status:** Failed

**Failure Stage:** OpenAI Independent Verification — Iteration 1

**Error**

1 validation error for ClaimVerificationResult
  Value error, NEEDS_QUALIFICATION requires recommended_claim_text [type=value_error, input_value={'claim_id': 'C1', 'verdi...mmended_status': 'WEAK'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error

**Search Provider:** Tavily

**Model:** gpt-4o-mini

**Searches Performed:** 1 / 10

**Unique Sources:** 5

**OpenAI Calls:** 3

**Tavily Calls:** 1

**Verifier Model:** gpt-4o-mini

**Started:** 2026-09-01T14:08:35-04:00

**Ended:** 2026-09-01T14:08:54-04:00

**Total Runtime:** 19.51s

---

# Research Plan

## Subquestions

### SQ1 [CORE]

**Question:**

What specific commercial applications have already demonstrated quantum advantage over classical computers, and what metrics were used to measure this advantage?

**Success criteria:**

Identify at least three applications where quantum computing has shown demonstrable advantages, including metrics such as speed, efficiency, or accuracy compared to classical counterparts.

**Initial status:** UNRESEARCHED

### SQ2 [SECONDARY]

**Question:**

What theoretical or projected advantages of quantum computing exist that have not yet been realized in practical applications?

**Success criteria:**

List and describe at least five theoretical advantages, providing evidence from studies or projections that detail their expected impact on quantum versus classical computing.

**Initial status:** UNRESEARCHED

### SQ3 [CORE]

**Question:**

What are the major technical barriers currently hindering the development of commercially viable quantum computers?

**Success criteria:**

Identify at least four technical challenges that are widely recognized in the field, along with evidence or expert consensus on how these barriers affect the advancement of quantum computing.

**Initial status:** UNRESEARCHED

### SQ4 [SECONDARY]

**Question:**

What timelines have been proposed for overcoming current barriers and achieving commercial viability in quantum computing?

**Success criteria:**

Outline at least three proposed timelines from reputable sources, detailing the assumptions behind these estimates and any variability in expectations.

**Initial status:** UNRESEARCHED

### SQ5 [SECONDARY]

**Question:**

How do different jurisdictions compare in terms of investment and research efforts aimed at advancing quantum computing technologies?

**Success criteria:**

Provide a comparative analysis of investment levels, key initiatives, and research outputs in at least three different regions or countries involved in quantum computing.

**Initial status:** UNRESEARCHED

## Synthesis Requirements

- Aggregate findings about demonstrated quantum advantages with those of theoretical projections to provide a holistic view of the current landscape.
- Cross-reference technical barriers with established timelines to ascertain realistic pathways to commercial viability.

## Output Requirements

- Produce a comprehensive report summarizing the findings from each subquestion with clear distinctions between demonstrated and theoretical advantages, including graphical representations where appropriate.
- Ensure the final synthesis addresses the question's implications for future quantum computing developments.

---

# Iteration 1

## 1. Search

**Query**

> How close are quantum computers to providing commercially useful advantages over classical computers? Separate demonstrated quantum advantage from theoretical or projected advantages, and identify the biggest remaining technical barriers.

**Purpose:** GENERAL

**Why this query**

This is the user's original research question.

5 result(s) retrieved; 5 new unique source(s) added.

- **S1 — Quantum computing**
  URL: https://en.wikipedia.org/wiki/Quantum_computing
- **S2 — Practical quantum advantage signals a new commercial era for ... - Q-CTRL**
  URL: https://q-ctrl.com/blog/practical-quantum-advantage-signals-a-new-commercial-era-for-quantum-computing
- **S3 — Quantum Computing vs Classical Computing: Key Differences**
  URL: https://www.bluequbit.io/blog/quantum-computing-vs-classical-computing
- **S4 — Quantum computing: What leaders need to know now**
  URL: https://mitsloan.mit.edu/ideas-made-to-matter/quantum-computing-what-leaders-need-to-know-now
- **S5 — Quantum Computing – Strategic Recommendations for the ...**
  URL: https://arxiv.org/html/2601.08578v1

**Search Duration:** 2.83s

---

## 2. Evidence Processing

- New claim proposals: 4
- Existing claim updates: 0
- New gaps: 1
- Resolved gaps: 0

**Processing Duration:** 7.01s

---

## 3. Ledger Updates

### New Claim C1

**Claim**

Quantum computing has achieved Practical Quantum Advantage, demonstrating a 3,000 times speedup in materials simulation compared to classical computers, making it commercially viable for specific applications.

- S2 supports (direct): Demonstration of 3,000 times speedup in materials simulation using quantum computing.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C2

**Claim**

Quantum computing has significant advantages for specific applications such as optimization, cryptography, and large-scale simulations due to its ability to use qubits for parallelism and interference, which classical computers cannot achieve.

- S3 supports (direct): Quantum computers can solve complicated problems faster than classical systems for specific applications.

**Confidence:** HIGH

**Status:** SUPPORTED

### New Claim C3

**Claim**

The current barriers to practical quantum computing include hardware errors, the need for specialized operating conditions, and the nascent state of quantum algorithms, which are still being developed.

- S4 supports (direct): Identifies technical barriers related to hardware and algorithm development for quantum computing.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Claim C4

**Claim**

The timeline for achieving full quantum advantage in commercial applications is projected to extend until at least 2035, as significant hardware advancements are still needed.

- S5 supports (direct): Estimates for hardware readiness and commercial applicability stretch into the mid-2030s.

**Confidence:** MEDIUM

**Status:** SUPPORTED

### New Gap G1

The current evidence does not fully address the comparative analysis of investment levels and research efforts in different jurisdictions related to quantum computing.

---

## 4. Current Research State

- Claims: 4
- Supported: 4
- Weak: 0
- Conflicting: 0
- Insufficient Evidence: 0
- Open Gaps: 1
- Remaining Searches: 9

### Subquestion Progress

**SQ1:** UNRESEARCHED → SUFFICIENT

Reason: Linked ledger claims are supported and no open high- or medium-importance gap remains.

**SQ2:** UNRESEARCHED → SUFFICIENT

Reason: Linked ledger claims are supported and no open high- or medium-importance gap remains.

**SQ3:** UNRESEARCHED → SUFFICIENT

Reason: Linked ledger claims are supported and no open high- or medium-importance gap remains.

**SQ4:** UNRESEARCHED → SUFFICIENT

Reason: Linked ledger claims are supported and no open high- or medium-importance gap remains.

**SQ5:** UNRESEARCHED → PARTIAL

Reason: Open high- or medium-importance research gaps still block a sufficient answer.

### Research Plan Status

**CORE:**

- SQ1 → SUFFICIENT (targeted searches: 0)
- SQ3 → SUFFICIENT (targeted searches: 0)

**SECONDARY:**

- SQ2 → SUFFICIENT (targeted searches: 0)
- SQ4 → SUFFICIENT (targeted searches: 0)
- SQ5 → PARTIAL (targeted searches: 0)

**Remaining targeted searches:** 9

---

## 5. Independent Verification

No eligible claim was independently verified.

---

## 6. Research Decision

No research decision was completed for this iteration.

---

# Final Research Decision

**Research did not complete.**

**Failure Stage:** OpenAI Independent Verification — Iteration 1

**Remaining Uncertainty**

- The current evidence does not fully address the comparative analysis of investment levels and research efforts in different jurisdictions related to quantum computing.
- SQ5: How do different jurisdictions compare in terms of investment and research efforts aimed at advancing quantum computing technologies? (PARTIAL: Open high- or medium-importance research gaps still block a sufficient answer.)

---

# Performance Summary

| Component | Calls | Total Time |
|---|---:|---:|
| Question Decomposition | 1 | 5.72s |
| Tavily Search | 1 | 2.83s |
| Evidence Processing | 1 | 7.01s |
| Independent Verification | 1 | 0.00s |
| Research Decision | 0 | 0.00s |
| Report Generation | 0 | 0.00s |
| Total Run | — | 19.51s |

# Verifier Diagnostics

- Verification calls: 1
- Claims verified: 0
- VERIFIED verdicts: 0
- NEEDS_QUALIFICATION verdicts: 0
- CONTRADICTED verdicts: 0
- INSUFFICIENT_EVIDENCE verdicts: 0
- Counter-searches requested: 0
- Counter-searches executed: 0
- Counter-searches blocked by budget: 0
- Counter-searches blocked as duplicates: 0
- Claims whose wording changed: 0
- Claims whose confidence decreased: 0
- Claims whose status changed: 0
- Searches allocated to general research: 1
- Searches allocated to subquestions: 0
- Searches allocated to counter-search: 0
