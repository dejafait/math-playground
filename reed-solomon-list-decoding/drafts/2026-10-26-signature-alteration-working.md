# Signature-conditioned alteration working record

Approved target: Assess whether signature-randomizing L131's right map can preserve S1–S4 while admitting cross-packed subfamilies of size at least 1532496 on each side.

Inputs are L030, L130 and audited L131, with the unchanged fixed left map,
p=0, r=Z-16, sigma(16,1)=b and right d_0 mapped to a. Reuse the
invocation-start SPECIALIZE assessment in
`literature/2026-10-26-signature-randomized-planted-obstruction.md`.
No claim of universal occurrence, prescribed laws or RS realization is made.

Bounded test: delete left polynomials with f(16)=1 and then every left
support conflicting with fixed S3 or S4. Check that p,r survive. Partition
Y by membership in R3=S3 minus C' and R4=S4 minus C', giving part sizes
949,6,6,1. For a right polynomial, its graph has occupancy n in the
corresponding domain parts. Each image part is a uniform n_i-subset of
its target part, independently between parts. For left residual occupancy
m, the intersection law is the convolution of four hypergeometric laws.
Enumerate the two occupancy histograms and count the exact expectation
of all remaining cross conflicts (intersection at least four).

Deleting all right endpoints of these conflicts costs at most their
number and never deletes p,r: their left neighbors were removed first.
Thus only one random loss needs averaging; protected-left conflicts are
included in that same edge count. The deterministic left loss must be at
most 1020088 and the integer averaged right loss at most 1038857. Stop
this sufficient test if either bound fails; failure does not disprove
existence. Count the singleton and both planted polynomials explicitly.

Completed state: the bounded test passes, as the UNVERIFIED CANDIDATE
L134 records canonically. The exhaustive eligible left histogram has no
conflict with either protected right support, so its size stays 2552584.
The exact mean is 953535880348964195654027/4237514312360044716, whose
floor is 225022. One right-endpoint deletion leaves at least 2346331,
with all four witnesses protected. Complete histograms and all 238
probability laws, each compared with an independent binomial-moment
tail calculation, are in `scripts/finite-support/signature-alteration.json`.
All 18 checks pass. This is a standard alteration specialization, not
a new general theorem or certified novelty. Separate critical audit
of the full enumeration, conditional law and existence argument is
pending. Mathlib coverage is not checked; 67/68 and 955–957 are unchanged.
