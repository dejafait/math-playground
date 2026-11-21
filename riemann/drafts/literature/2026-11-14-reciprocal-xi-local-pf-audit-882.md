# Reciprocal-Xi boundary PF: source-audit coverage

TARGET: Audit Sra's Proposition C.8 for fixed-order local PF positivity of the actual reciprocal-Xi density Theta, checking the complex saddle estimate, weighted Fourier domination, determinant normalization and passage to ordered minors without asserting an order-uniform neighborhood.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Discovery882 checked local PF/Proposition C.8/boundary and Wronskian terms against the named prior assessments; C.6 has prior coverage, while this C.8 analytic argument was not audited in the inspected records. No novelty claim.
SOURCE_EVIDENCE: Sra, On some positivity properties of the Riemann Xi function, version-specific primary text https://hub.valency.io/works/W_pr5z5huy_v1 , Appendix C Proposition C.8/complete proof, Lemmas C.1/C.6/complete proofs; Theorem1.1/Lemmas2.1-2.4/Corollary2.5 and Appendix B's complete density proof; NIST DLMF5.11.1 fixed-sector hypothesis. This HTML version is not equated with an author PDF version.
COMPARISON: This is fixed-order local density positivity, not L030's reciprocal-zero Hankel forms or global PF infinity. Standard saddle/Fourier/Wronskian methods cover the proof tools; the actual complex-domain and uniform-domination applicability is the exact audit obligation.
GAP: Independently check the selected analytic chain, retaining external density/existence inputs by citation. No effective epsilon_m, order-uniform bound, global PF extension, logarithmic-Hankel sign or RH conclusion is covered.
REASON: One bounded conceptual source audit can validate or reject a specific root-free boundary input before a separately assessed extension uses it; this is reproduction, not a new central mechanism or a reproof of general theory.
SCOPE: Only the version-specific Proposition C.8 proof and cited prerequisites; no new PF-order certificate, zero data, numerical inversion, U12 retry or uniform-degree derivation. Newly written ready coverage requires separate approval next turn.

## Object, inputs and downstream use

Use the source's c_0=xi(1/2)>0, h(z)=xi(1/2+sqrt(z))/c_0,
B=log h and Theta=theta_1/c_0. The density theta_1 has Laplace
transform1/h; Theta has mass1/c_0. Existence and smooth positive
support are imported by Theorem1.1/Lemma2.4/Corollary2.5 with their
critical-strip, counting and verified-low-zero hypotheses, not by RH.
The review inspected their statements and relevant proofs; it did
not independently certify all external inputs. Trace their exact
hypotheses if necessary, without reopening the entire paper.

Local essential IDs: L018/L024 for actual-Xi conventions and product;
L030-L032/C032a for the destination and algebraic-square trap. They
do not supply Theta determinant signs. Parked U12 diagnostics are
contrasts only. No cross-notebook result is used. Boundary data might
initialize a future extension, but order uniformity, global extension
and transfer to L030 remain independent unresolved assumptions.

## Source assertion to audit; not a new derivation

For each fixed m>=1, Proposition C.8 asserts epsilon_m>0 such that
all ordered minors det[Theta(x_i-y_j)] of sizes1<=k<=m are strictly
positive when every cross difference is in(0,epsilon_m). It defines

    D_k(p;x)=(-1)^(k(k-1)/2) det[p^(i+j)(x)]_(0<=i,j<k),
    x_s=B'(s), v_s=-B''(s).

The precise source-stated limit for every fixed k is

    D_k(Theta;x_s) /
      (Theta(x_s)^k v_s^(-k(k-1)/2) prod_(j=0)^(k-1) j!) -> 1.

Citation: [primary version](https://hub.valency.io/works/W_pr5z5huy_v1),
Appendix C, “Fixed-order positivity near the one-sided boundary,”
Proposition C.8 and proof, HTML equations31-33 and the final
tilt/scale identity. Source equation labels C.8-C.10 are rendered
numerically in the HTML. The fixed-order ratio limit is the decisive
threshold, not a computed margin. Nothing in it was derived or
mathematically approved in literature step882.

Audit one coherent chain:

1. Check the branch and zero exclusion for B on the large right-half-
   plane region actually used. Apply [DLMF5.11.1](https://dlmf.nist.gov/5.11#E1)
   to the actual shifted gamma argument; check the claimed uniform
   remainder and Cauchy disks for derivatives, with fixed sector.
2. Check tilt, centering and variance using theta_1, including the
   fixed-frequency Gaussian limit and every normalization constant.
3. Check the all-frequency bound on Re B(s+isu)-B(s), including large
   u. The majorant must be independent of sufficiently large s and
   integrable with |t|^r for every fixed0<=r<=2m-2. Weak convergence
   or a bounded-frequency preview is insufficient for inversion.
4. Check the Gaussian determinant, triangular tilt congruence and
   variance exponent. Check x_s maps onto a whole interval next to
   zero, then check both Wronskian transfers stay in the admissible
   cross-difference interval, retaining strictness and regularity.

Use the claimed theorem and standard results by citation. Scrutiny
is justified by the specific unverified weighted-inversion step on
which a boundary application depends. Do not reprove unrelated
probability laws or the general Wronskian criterion. Lemmas C.1/C.6
and their short supplied proofs already have coverage; revisit only
the domain/sign interface needed here. A newly uncovered analytic gap
requires preservation and a separate gate, not an original repair
approved in this audit.

## Decision test and qualifications

Accept only a fixed-order statement with every hypothesis paid or
precisely cited. State epsilon_m may depend on m; no effective value
is promised. If a load-bearing estimate fails, record its precise
range/premise and downgrade the proof chain. A defective proof does
not refute its conclusion. A sound proof does not give global PF
infinity or any L030 mixed sign. No numerical script is necessary.

This is proof_audit/conceptual_audit and REPRODUCTION under SPECIALIZE.
Full matching/supporting Mathlib coverage is unchecked, not absent.
