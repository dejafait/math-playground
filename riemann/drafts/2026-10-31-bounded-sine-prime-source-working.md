# Bounded sine probe: source-review working notes

Literature-only step; no new mathematical result or script. Startup
assessment is `literature/2026-10-31-bounded-sine-prime-peano-dual.md`.
Existing modifications and unfinished work are preserved.

Main gap: actual-Xi positivity. Reviewed target: source coverage for the
signed density sine moment and complete Peano-smoothed chirp correlation.
Downstream use: test the fixed-square little-o residual route only.

Read the relevant statements/proofs of L574, C574a, L482 and L319,
the L477 definitions/finite norm interface, C481a's Peano transfer,
and the earlier constructive-linear-dual and density-Peano assessments.
The old stops do not themselves refute a bounded sine amplitude.

Primary inspection so far:

- Curran 2303.10123v2, Section 2, Lemmas 2.2--2.5. Arbitrary-coefficient
  finite mean square remains usable after grouping. Prime-only moments
  require N^r<=T/log T; they do not state a density-weighted moment.
  Disjoint-support splitting is unavailable for the long density factor.
- Fazzari 1912.08127v2, Theorem 1.1, Propositions 1.1/1.2, Lemma 2.1
  and Section 3.1 opening. Distinguish the RH-dependent log-zeta
  approximation from the unconditional prime-polynomial proposition.
  The proposition uses x=T^(epsilon/k), epsilon=1/log log log T,
  full-zeta weighting and centered moments. It is not the specified
  prime block, shifted finite density or complete chirp pairing.
- Bettin--Chandee--Radziwill, author PDF, Theorem 1, pp. 1--2:
  smooth [1,2]-supported cutoff, full |zeta|^2, finite polynomial
  coefficients a_n<<n^epsilon, length exponent <17/33. No direct
  theorem for the proposed sine or its finite-cutoff residual.
- NIST DLMF 4.19.1 states the sine series. A future finite truncation
  must use Taylor's theorem with its real remainder bound, and pay
  that remainder in each actual weighted integral.
- Reuse the already inspected McKee--Sun--Ye finite-endpoint weighted
  stationary-phase tools; they retain a stationary main term.
  A newly followed lead is Banks 2405.11084v1 Lemma 2.8, citing Gonek
  1984 Lemmas 2/3 for an endpoint-uniform logarithmic saddle formula.
  Original Gonek text found at the author's Rochester site; its exact
  Lemmas 1--3, pp. 129--130, and central/outer/endpoint proof cases
  were subsequently read. The completed assessment retains the full
  endpoint error and stationary main term. No source-proof audit.

No source-access blocker so far. No sine moment, leakage estimate,
compatible Taylor budget, stationary cancellation or Xi conclusion has
been proved. Final decision: EXPLORE for the first-order Taylor budget
test named in the completed assessment's COVERED_TARGET, subject to the
supervisor's separate approval of changed coverage. No Mathlib coverage
claim. Local-shell source download failed DNS; accessible web primary
text was used instead. No mathematical script was run.
