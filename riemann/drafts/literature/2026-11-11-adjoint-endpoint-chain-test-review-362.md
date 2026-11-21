# Finite endpoint-chain adjoint test — proposed continuation

TARGET: Test one zero-safe finite endpoint-chain adjoint for C997c's complete point kernel, seeking band measures of subexponential TV with slope-uniform residual O(exp(-n/64)).
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Source review362 completed the adjoint/moving-average/dilation/diagonal-zero comparison in review361; no inspected theorem supplies the simultaneous norms and no exact-range impossibility was found. No novelty inference.
SOURCE_EVIDENCE: Schuster–Quinto, SIAM J.Appl.Math.65(4)(2005), Section2 pp1371–1372, Definition2.1/(2.4)–(2.6)/Remark2.2, https://sites.tufts.edu/tquinto/files/2021/01/srt.pdf ; Schiefeneder–Haltmeier arXiv:1606.03486v1 AppendixA.1 pp16–17, LemmaA.1/TheoremA.2, https://arxiv.org/pdf/1606.03486v1 ; reuse review361's inspected contracts/scope screens and review322 continuation coverage. C997c(1),(4)–(6) is the accepted exact input.
COMPARISON: Adjoint reconstruction is conditional on an appropriate representer; diagonal-zero uniqueness is not existence or stability. This tests endpoint cancellation on the full slope interval, beyond C997j's scalar class and C997k's restricted polynomial cutoff, without repeating C997p's saddle or C997d's ambient envelope.
GAP: Derive the endpoint-chain equation and boundary conditions, verify all relevant zero compatibilities, and either construct band measures with both uniform estimates or identify a rigorous obstruction to this ansatz.
REASON: Separate literature approval completed in step363 with direct primary-source URLs and unchanged scope; EXPLORE authorizes one proposed test, not existence or a general obstruction. No mathematical invocation occurred.
LITERATURE_REASON: Supervisor-required direct-source-URL repair; reuse completed coverage rather than reopen discovery or derive mathematics.
SCOPE: Integer n>=2; I=[7/4,9/4], E=[15/8,17/8], z_star=1+i/8; finite complex band measures; complete C997c kernel, both beta terms, lower window, K's -1 and original TV; no assumed simple zeros or implicit inverse.

## One construction to test after approval

Use k_n(c,z)=H_n^+(z;delta_c) exactly as in C997c(1).
Try one finite chain of signed cancellations of the linked cn and
c(n+2) endpoints in C997c(4). Follow the dilation
t -> ((n+2)/n)t only to the finite window boundaries, retaining all
uncancelled terminal pieces and the separate lower window. This is an
ansatz to derive, not an established identity.

Derive the adjoint equation and boundary conditions directly from the
finite-measure representation. Test whether the chain lifts to a
Fourier–Stieltjes transform of a finite complex measure lambda_n on E.
A smooth time-domain solution or distributional representer alone is
insufficient. Do not divide by g_n across zeros: prove compatibility
and a bounded extension or record the precise failure of the ansatz.
Simple zeros, nonzero endpoint weights and uniform inverse bounds are
not hypotheses supplied by this review.

## Fixed discriminator

For all sufficiently large integers seek the SAME lambda_n satisfying

    ||lambda_n||_TV <= C_epsilon exp(epsilon*n) for every epsilon>0,
    sup_(c in I) |k_n(c,z_star)
        -integral_E k_n(c,gamma)dlambda_n(gamma)|
                                          <= C exp(-n/64).

Constants are independent of n; C_epsilon may depend on epsilon.
These are requested thresholds. They include the complete lower window
and both slope endpoints. An L2 or coefficient norm needs a proved
conversion before replacing a displayed norm.

Continue with a paid construction meeting both estimates or an
informative partial estimate with an explicit remaining rate/cost gap.
Abandon this ansatz upon proved zero/boundary incompatibility or an
unavoidable cost contradicting the thresholds. No such conclusion
applies to all band measures without a separate argument. If the one
chain leaves uncontrolled terminal terms or an unestimated inverse,
preserve them and return EXPLORATION; do not substitute a scalar bound
or uncertified fit.

## Relevance and limits

A band dual could address the positive-branch point bridge used in
signed slope selection. C997a(8)'s extra term, both-sign transfer,
original assay/reconstruction, recovery/complements/regulators, L993
and L984(H) remain independent gaps. L030–L032/C032a actual-Xi
positivity and L966/L968 forcing remain open. C997a/d/j/k are scope
comparisons only; their unaudited claims are not assumed. C997e/n/o/p
support the preserved fixed-family stop, not this construction.
No cross-notebook input; Mathlib matching coverage unchecked/unknown.

Proposed purpose after separate approval: proof_attempt/creative.
The obstruction is simultaneous exponential uniform residual decay
and subexponential dual cost on the exact response range. The pair
above, including explicit zero/boundary compatibility, is the bounded
test. No mathematical result or RH candidate is asserted.

## Separate source-link approval — step363, 11 November 2026

The exact TARGET, hypotheses, discriminator and ansatz are unchanged.
Direct primary URLs now appear in SOURCE_EVIDENCE. Review361's completed
comparison is reused; no new overlap or novelty finding is claimed.

[Schiefeneder–Haltmeier v1](https://arxiv.org/pdf/1606.03486v1),
Appendix A.1, printed pp16–17, was retrieved, including the full
Lemma A.1/Theorem A.2 statements and uniqueness propagation proof.
The real triangular kernel must be C^3, with finitely many simple
diagonal roots and positive 1+alpha1/(alpha1+alpha2) at each root.
A.2 gives at most one continuous solution for continuous data; the
preceding paragraph leaves range characterization to future work.
A.1 additionally requires a sole initial simple zero, the specified
linear expansion with regular quadratic remainder, and data
g(s)=(s-a)^2 h(s), h in C^1. None of these conditions is established
for the proposed complex band adjoint; no application is imported.

The [Schuster–Quinto author copy](https://sites.tufts.edu/tquinto/files/2021/01/srt.pdf)
returned HTTP502 in this invocation. Reuse the previously inspected
published-text contract in review361, Section2 pp1371–1372,
Definition2.1, (2.4)–(2.6), Remark2.2, DOI10.1137/S003613990343879X.
It assumes a solved adjoint equation in the stated distribution-space
pairing and does not ensure solvability for a prescribed mollifier.
No successful refetch is claimed. The retained source assessment is
adequate; no essential unread theorem is required for the bounded test.

C997c(1),(4)–(6) was checked at its finite-complex-measure representation;
the lower window and complete weight agree with this scope. Review361's
recorded scalar/polynomial/packet failures remain scope comparisons.
EXPLORE is approved for this single endpoint-chain test. Zero/boundary
compatibility, band representability and both uniform estimates remain
unproved. Mathlib matching remains unchecked. This is a process repair,
STALLED, with no mathematical advance, new lemma, script, RH candidate
or change to the PROOF/DAG argument.
