# Ideal-counting residue error — separate continuation coverage

TARGET: Test whether Sunley's unconditional ideal-counting residue interval can have endpoint ratio below two for L96 at any X <= 10^6, using L051-L052 and Louboutin's Theorem 1.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed unconditional-analytic assessment's exact searches, duplicate/failure comparison and primary readings; no exact L96 interval-feasibility calculation was inspected or performed.
SOURCE_EVIDENCE: Sunley Bull. AMS 78 (1972) Theorem 2(1) p.75; Garcia–Lee arXiv:2007.10313v4 Theorem 5 and small/large-X scope discussion p.5; Louboutin JNT 85 (2000) Theorem 1 p.263 and concluding proof cases pp.270-271; Belabas–Friedman arXiv:1305.0035v1 Introduction p.1 for factor-two halting with ambient-generation premise. Direct sources: https://arxiv.org/pdf/2007.10313v4 ; https://doi.org/10.1090/S0002-9904-1972-12859-3 ; https://doi.org/10.1006/jnth.2000.2545 ; https://arxiv.org/pdf/1305.0035v1 . Statements and scope rechecked on 2026-10-11; accessible original-text mirrors and qualifications appear below.
COMPARISON: Known bounds cover all degree-36 number fields but do not evaluate their strength on L051-L052's discriminant interval or give the field-specific positive-interval feasibility implication. That bounded specialization is the only proposed mathematical difference.
GAP: Derive and check the correct interval-ratio criterion and uniform error comparison for 0<X<=10^6 across the certified discriminant interval; no actual ideal count, maximal order, class/unit completeness or independent ambient generation is known.
REASON: One independent numerical-bound question can determine whether this explicit unconditional residue input warrants further work, avoiding class enumeration, smaller-field relations and the disputed Euler-product passage.
SCOPE: Exactly TARGET; only the named counting/residue-upper-bound theorems and L051-L052. No GRH, Stark c8, actual signature, ideal enumeration, class computation or complete-certificate claim. Source-URL recovery completed on 2026-10-11; separate supervisor approval remains required before the calculation. The target and mathematical scope are unchanged.

The main gap is unconditional emptiness of L032's retained 96a1 disk;
other twists and residual signatures remain independent gaps. A useful
residue enclosure could assist a class/regulator certificate after an
independent ambient-generation proof. Failure can park this explicit
bound without claiming that all analytic certification is infeasible.

Reuse [the completed comparison](2026-10-11-ninety-six-unconditional-analytic-certification.md)
for citations, inspected cases and limitations. It records no new
specialization. Sunley's theorem is imported through its original
announcement and Garcia–Lee's all-X restatement; the thesis was not
independently audited. Use Louboutin's general-degree theorem, not its
CM clauses. No source-theorem reproof is proposed.

Essential inputs are L051 and L052. L032 supplies downstream scope;
L056 and ATTEMPTS/018-023 are preserved contrasts, not premises. No
cross-notebook input is used. Use n=36 and the exact certified interval

    3^30*11^33 <= |Delta_L96| <= |d12|^3*|d3|^12,

with d12,d3 as in L051. Test the cited radius Lambda(Delta) X^(-2/37)
while keeping the actual residue and ideal count unknown. The source
interval's center is I_L96(X)/X. An overlarge certified radius is not
a lower bound on actual error; it can reject only this certificate.
Do not confuse absolute and relative errors or substitute an upper
residue bound for an approximation. Write out the correct feasibility
implication with strict endpoints in the later research attempt.

The cap 10^6 is a diagnostic for this new residue computation, not a
necessary complexity bound or the parked class-generation cutoff.
Cover all 0<X<=10^6 by proved enclosures or monotonic bounds, not a
grid. If a script is needed, use rigorous outward enclosures or explicit
rational inequalities; save full evidence under
scripts/ninety-six-analytic-error/ and print actual/required bounds,
failures and paths. Do not enumerate ideals or collect class relations.

Continue if the explicit certificate could achieve positive endpoint
ratio strictly below two in this bounded range. Failure parks this
counting-error version. Success still proves neither an actual residue
interval nor ambient completeness. The maximal order, actual
discriminant/signature, class relations, units/regulator, torsion lifts,
support/norm maps and full-disk disjointness remain unverified.
No numerical result or interval-width lemma is supplied now. Novelty
is not asserted. Mathlib coverage is not checked.


## Direct-source recovery review — 2026-10-11

Reused the earlier assessment and history/158; checked the parked
Minkowski and smaller-auxiliary mechanisms in ATTEMPTS/019 and
ATTEMPTS/023. The bounded counting-error diagnostic is distinct from
both. No duplicate calculation was found in this targeted coverage;
this is not a novelty claim. No broader search was repeated.

Sunley, Bull. AMS **78** (1972), 74–76,
[Theorem 2(1), p.75](https://scispace.com/pdf/on-the-class-numbers-of-totally-imaginary-quadratic-8849my12mw.pdf),
was rechecked in the original announcement. The arbitrary-number-field
counting clause is separate from Theorem 1's CM setting. It does not
specify the range or give the full proof. The publisher identifier is
[10.1090/S0002-9904-1972-12859-3](https://doi.org/10.1090/S0002-9904-1972-12859-3).

Garcia–Lee, [arXiv:2007.10313v4, March 12, 2021](https://arxiv.org/pdf/2007.10313v4),
Theorem 5 and its range discussion, p.5, explicitly cover every number
field of degree n>=2 and every X>0. With D the absolute maximal-field
discriminant, their stated estimate is

    |I_K(X)-kappa_K X| <= Lambda_K X^(1-2/(n+1)),
    Lambda_K = exp(28.2 n+5)(n+1)^(5(n+1)/2)
               D^(1/(n+1))(log D)^n.

I_K counts nonzero integral ideals of the maximal order; kappa_K is
the Dedekind-zeta residue at one. The inspected discussion treats the
small-X case and identifies the thesis's complex-analytic large-X
case. The thesis itself was not audited. Import the named theorem;
no source reproof or Euler-product tail argument is required.

Louboutin, J. Number Theory **85** (2000), 263–282,
[DOI 10.1006/jnth.2000.2545](https://doi.org/10.1006/jnth.2000.2545),
[author-uploaded published text](https://www.researchgate.net/publication/222631087_Explicit_Bounds_for_Residues_of_Dedekind_Zeta_Functions_Values_of_L-Functions_at_s1_and_Relative_Class_Numbers),
Theorem 1, p.263, covers every number field of degree n>1:

    kappa_K <= (e log D/(2(n-1)))^(n-1).

The concluding proof, pp.270–271, was rechecked: Hecke's integral
representation and the zeta comparison lead to the endpoint estimate
via Lemmas 9–10; the separate imaginary-quadratic case does not affect
degree 36. There is no CM, normality or GRH premise.

The general degree hypotheses cover n=36 without knowing the actual
signature. L051–L052 remain the essential field-specific inputs, to be
read and checked when used in the mathematical turn. The specialization
is justified as an error-strength diagnostic, since neither source
performs this L96 comparison. No interval criterion, numerical bound,
ideal count or new lemma was derived here. Mathlib coverage is not
checked. The decision remains SPECIALIZE; the missing direct URLs are
now local to this assessment. This repair is STALLED mathematically:
it adds traceable coverage, not evidence that the proposed bound works.
