# Actual theta identities and the missing logarithmic positivity

Date: 2026-09-20

Outcome: park the proposed transfer from theta-kernel positivity to all-degree reciprocal-zero positivity. This is a review of the recorded argument, not an impossibility theorem for arguments using the full theta series. No new lemma is asserted.

## Required statement and downstream use

For the actual Ξ, the target is cᵀH_dc≥0 for every integer d≥0 and every real vector c, where H_d=(S_{m+n+2})_{0≤m,n≤d}. C032a would then imply RH using the reviewed polynomial detector. A rigorously negative actual form would instead contradict RH by that equivalence, but no such form has been found. Positivity of a different matrix or of finitely many H_d does not meet either target.

## What the exact theta inputs currently deliver

L016 proves the exact Gaussian theta transformation and all fixed derivative tail bounds. L019 uses its derivative at x=1 to obtain A′(0)=-1/4 and the positive series for K=2A″-A/2. These facts justify the cosine representation, moment integrals and their analytic manipulations. The additional reflection identity A(-u)=A(u)+sinh(u/2) gives evenness of K in L048. None of these recorded conclusions is an inequality on the logarithmic mixed forms.

The positivity operation actually available is the ordinary Gram identity in L043: cᵀG_dc=∫₀∞K(u)q(u²)²du>0 for nonzero c. Its entries are M_{2m+2n}, not S_{m+n+2}. L040 computes the latter from e_j=M_{2j}/((2j)!M_0) by the finite Newton recurrence. Already its k=2 case is S_2=e_1²-2e_2; the positive terms of K do not remove that subtraction. L044 proves with a full explicit counterexample that positivity of every ordinary Gram matrix can coexist with a negative first logarithmic test. Thus calling the theta summands positive does not identify a positivity-preserving operation at the needed step.

This leaves the precise unprovided input: an additional inequality using the actual Gaussian coefficients and their relations, which controls the signed Newton expressions for arbitrary degree and every coefficient vector. The boundary normalization and reflection identity have been used for the representation and symmetry; the inspected proofs supply no induction, real-square representation, or other sign argument for those expressions. This is a statement about the inspected proof, not a claim that all consequences of the theta transformation have been exhausted.

## Existing obstructions and their scope

The [Gram-transfer failure](2026-09-09-gram-logarithm-transfer.md) already records L044, so another example of that failure would be redundant. The [finite-test failure](2026-09-09-finite-hankel-extrapolation.md), proved in L057 using L055, rules out combining the recorded generic kernel properties, generic zero geometry and an arbitrary fixed finite number of positive tests as a sufficient condition. Its comparison function depends on the number of tests. These comparison kernels are not asserted to satisfy the exact arithmetic theta series or its full transformation; the obstruction does not rule out a future theorem that uses that extra structure.

The achieved actual bounds remain six scalar signs and the certified H_1 and H_2 positivity (with their arithmetic contracts). The required bound ranges over all d and c. No degree-uniform estimate or structural positivity theorem was obtained in this audit. Further finite certification or a restatement of C032a would leave exactly the same gap.

**WHY IT FAILS.** The proposed argument reaches positive ordinary moments through exact theta identities, then needs positivity after a nonlinear logarithm. The only recorded passage across that step is an algebraic recurrence with subtractions, and the proposed generic preservation law is already disproved by L044. L057 prevents repairing this with finitely many tests and the established generic conditions. The full theta arithmetic remains potentially relevant, but no mechanism exploiting it for all-degree mixed positivity has been supplied. Park this transfer and require a concrete additional mechanism before resuming it; this decision does not disprove RH or rule out every theta-based proof.

## 2026-09-21 arithmetic reopening audit

Reviewed the possible arithmetic reopening against the actual inputs, rather than adding another generic counterexample. The integer-square support and exact Gaussian coefficients in L016/L019, together with Poisson reflection, distinguish the actual theta series from the comparison family. L057 does not establish that its comparison family satisfies those exact identities, so it cannot rule out a theorem using them. However, the recorded uses of those identities give convergent moments and boundary normalization; L040 still supplies only a signed recurrence. No identity expressing its mixed forms as real squares, or induction preserving all their signs, was identified. This is an audit of available arguments, not an impossibility claim about theta arithmetic.

The other concrete arithmetic positivity input is unique factorization in L005 and the prime trigonometric square in L006. Its hypothesis is Re(s)>1. The coefficients in L025 are instead extracted locally at z=0 for Ξ(z)=ξ(1/2+iz). No recorded identity turns the former positive prime sum into those logarithmic mixed forms. The already archived [continued-prime failure](2026-09-09-continued-prime-positivity.md), with its canonical L010/L011 obstructions, prevents simply carrying the positive-series argument into that neighborhood. Repeating that calculation is not a new mechanism.

Decision: park technical extension of the retained theta/Hankel route as a whole, including further interface polishing and finite certificates pursued as a bridge to all degrees. Retain the reduction for reuse if a concrete actual-theta sign mechanism becomes available. The achieved bound remains positivity only in the recorded finite tests; the required bound is Q(q)≥0 for every real polynomial, with no degree cutoff. This audit obtains no improvement to that bound, no candidate, and no off-line zero. It changes the research decision from seeking another theta extension to screening a distinct existing representation for a specific missing input before doing technical work.
