# Supported norm-kernel dimension — source approval

TARGET: Determine the unconditional dimension bound for L138's supported norm kernel from S-unit ranks and L137, and compare the induced Jacobian rank bound with two.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the pair-rank, odd-model/support and localization assessments; searched exact quintic coefficients and S-unit/norm-kernel Jacobian dimension terminology; checked L138, L137, L135 signature proof, L133 and ATTEMPTS/045,050,059–060. No inspected instance bound duplicates this calculation.
SOURCE_EVIDENCE: Cremona–Lingham, Finding all elliptic curves with good reduction outside a given set of primes, author manuscript https://johncremona.github.io/papers/egros.pdf Section 2 p.3, definition and complete m-Kummer sequence; Milne ANT v3.08 https://www.jmilne.org/math/CourseNotes/ANTc.pdf Theorem 5.11 and proof p.90, Corollary 8.4 and determinant proof p.136; Stoll Acta Arith. 98 (2001) https://www.impan.pl/shop/en/publication/transaction/download/product/83397 equation (1.1) p.245, Lemma 4.3 p.250, Lemmas 4.9–4.10 and full dimension proof pp.254–256; accessed 2026-10-26.
COMPARISON: Known S-Kummer exactness and S-unit structure cover the dimension method without explicit generators; L137 supplies only an upper bound on the finite S-class contribution. The existing rank assessment discusses a different ideal-image bound, not an evaluated bound for L138's full supported ambient group.
GAP: Apply these inputs to the actual Q times quartic algebra; bind the existing signature and complete prime count, verify supported norm splitting and rational two-torsion subtraction, and evaluate the bound. No value or rank consequence is derived in this literature turn.
REASON: Essential source hypotheses are now covered for one later fixed calculation. No complete class presentation, new relations or backend is required for this upper-bound test; the exact specialization remains to be proved.
LITERATURE_REASON: The target at invocation was REVIEW_REQUIRED: the localized S-Kummer sequence and rational two-torsion formula were essential unchecked coverage, beyond the audited model/support interface.
SCOPE: Exactly TARGET for L110/L138 over Q, L133's field, audited L134 maximal order, audited L135 signature and prime enumeration, and audited L137 bound. Ordinary classes, all primes above 2,3,5,11, no sign restriction. One dimension/rank-bound specialization only; no local-image search, new unit/relation/point box or backend probe.

## Gap and discriminating test

The main gap is exclusion of positive primitive solutions in residual
Beal signatures. This intermediate target tests the unconditional ambient
rank information supplied by the audited descent interface. A baseline
can quantify how much later local filtering must remove. It need not
settle rank or any independent recovery obligation.

Continue toward rank-below-genus point methods only if the justified
upper bound is strictly less than two. Otherwise record the exact
shortfall and end the dimension-only shortcut. An insufficient upper
bound is not a rank lower bound. No Selmer equality is licensed.

## Imported statements and applicability obligations

Cremona–Lingham, Experimental Mathematics 16(3) (2007), 303–312,
[author manuscript Section 2, p.3](https://johncremona.github.io/papers/egros.pdf),
defines K(S,m) using valuations divisible by m outside a finite set
of maximal-ring finite primes and gives the unnumbered exact sequence

    1 -> O_(K,S)^*/O_(K,S)^{*m} -> K(S,m) -> Cl(O_(K,S))[m] -> 1.

The map sends a class represented by a to the class of the ideal J
with (a)=J^m in the localized ring. Read the full definition, map and
finiteness paragraph. Set m=2; no odd-class-number hypothesis is needed.
This is the required supported version, rather than an assumption that
all supported classes have S-unit representatives. The elliptic-curve
algorithm in that paper is not an input.

[Milne, Algebraic Number Theory v3.08 (19 July 2020)](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
Theorem 5.11, printed p.90, states S-unit free rank r+s+|S|-1,
with torsion the roots of unity. Its complete proof uses ordinary units
as valuation kernel and class-number powers of each supported prime.
Count finite prime ideals once, without ramification weights; infinity
is counted through r+s. Retain the torsion modulo squares contribution.
The standard structure theorem for finite abelian groups identifies
mod-two quotient and two-torsion dimensions; reuse its approved coverage
in 2026-10-25-pair-quartic-parity-relations.md. It applies because this
ordinary S-class group is a finite quotient of the number-field class
group. Do not infer surjectivity on two-torsion under localization.
Milne Corollary 8.4 and its proof, printed p.136, give the product norm
via multiplication determinants. The later proof must check the rational
factor section, its support and the full norm codomain, rather than
subtract only a sign row or assume surjectivity of the quartic norm.

[Stoll, Implementing 2-descent for Jacobians of hyperelliptic curves](https://www.impan.pl/shop/en/publication/transaction/download/product/83397),
Acta Arith. 98 (2001), DOI 10.4064/aa98-3-4:
equation (1.1), p.245, bounds rank by Selmer dimension minus rational
two-torsion dimension. Lemma 4.3(3), p.250, gives the latter as m_Q-1,
where m_Q counts irreducible factors of the monic odd-degree polynomial.
Lemmas 4.9–4.10, pp.254–256, retain class two-torsion and explain bounds
without fundamental-unit generators. Read the entire dimension proof.
Lemma 4.10 uses its specified ideal-image group G, not arbitrary supported
classes: do not transplant its final minus-one correction to L138's group.
Reuse approved Lemma 4.1, Proposition 4.2 and Corollary 4.7 coverage for
the Kummer/support injection; no general theory reproof is warranted.

## Exact local inputs and duplicates

L138 fixes the actual monic quintic, its factorization (X-9075)H,
irreducibility, algebra Q times K, sufficient support and transported
maximal order. L133 identifies K; audited L134 supplies O_K. L135 already
proves the field signature with four disjoint sign-change intervals
in its Signature and rigorous integer cutoff section. Reuse that proof,
not a newly presumed signature. L137's Complete support argument supplies
the seven actual inverted prime ideals, and its audited finite quotient
bounds Cl(O_K[1/330])/2 by two. Reuse rather than rerun these certificates.
The next proof must explicitly connect each input to the sequence above.
L135 is an essential input to the continuation, added after this review
located the existing signature proof; no new signature calculation occurred.

Reused assessments: 2026-10-20-pair-jacobian-rank-bound.md,
2026-10-25-pair-genus-two-odd-model-support.md,
2026-10-25-pair-quartic-localized-parity.md. The first approves broad rank
theory but parks backend execution. The second prepares the interface;
the third evaluates only the localized class quotient. None evaluates
this supported norm-kernel baseline. The older supported-unit assessment
2026-10-16-supported-unit-dimension.md concerns a different extension;
its numerical dimensions and degree-three norm section are not inputs.

ATTEMPTS/045 parks a different octic class backend; ATTEMPTS/050 parks
fixed point/divisor caps; ATTEMPTS/059–060 finish the relation and
localization tests without attaining full parity rank. This calculation
reuses their valid partial information and reopens none of those tests.
Unfinished L108 is preserved. No cross-notebook input is used.

New queries: `"S-units" "norm kernel" "Jacobian" dimension bound` and
`"76835" "2196150000" Jacobian`. Results about other curves and unreviewed
online calculation packets were not used as theorem inputs. These
searches do not establish novelty. Exact-instance discovery and source
comparisons from the three adequate reviews above are reused.

No mathematical bound is evaluated here. Units or justified substitutes
for a filtered computation, full local/global descent, rank and point
control, marked lifts, degree-nine/integer recovery, L095's two systems
and other signatures remain unresolved. Full matching Mathlib coverage
is not checked, not asserted absent. The next specialization is
REPRODUCTION under SPECIALIZE; it imports general theory and proves only
the instance applicability and bound.
