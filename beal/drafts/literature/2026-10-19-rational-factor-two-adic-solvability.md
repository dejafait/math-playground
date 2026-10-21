# Rational-factor systems at two — completed source comparison

TARGET: Determine whether both complete L095 systems admit primitive two-adic points with nonzero coordinates.
CHECKED: 2026-10-19
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused exact-signature and rational-factor discovery assessments; targeted notebook searches and new equation, polynomial, coefficient and two-adic searches located no inspected theorem deciding both complete systems; precise queries and comparisons below.
SOURCE_EVIDENCE: Putz (2024), DOI 10.5463/thesis.832, Section 5.2 p.165 and Proposition 5.20 p.169, including its complete computational proof attribution; Zabradi (29 June 2022), Lemma 2.3 and Theorem 2.4 p.4, including their proofs, inspected in primary PDFs; Clark Theorem 1.79 reused from foundations/17-local-power-hensel-inputs.md.
COMPARISON: Putz supplies necessary entire-algebra covering data under odd coefficients, not simultaneous L095 witnesses or an exclusion; standard Hensel criteria support a bounded test but require an actual approximate root, derivative bound and common-coordinate reconstruction.
GAP: Neither exact primitive two-adic realizations of both complete systems nor an exhaustive obstruction has been obtained; global compatibility and integer lifting remain independent gaps.
REASON: Essential comparison and method coverage suffice for one separate bounded residue-and-lifting attempt; EXPLORE records absence of a matching result among sources checked, without a novelty claim.
LITERATURE_REASON: The changed prime requires checking Putz's precise two-adic scope; neither the three-adic nor eleven-adic assessments approved this specialization.
SCOPE: Exactly TARGET for the full L095 forms and both scales over Z_2, with nonzero m,u,a,A,B,C, min(v_2(m),v_2(u))=0 and min(v_2(A),v_2(B),v_2(C))=0; elementary finite residues and cited Hensel lifting, retaining one shared C; no unit-C assumption, global elimination or new descent machinery.

## Main gap and intermediate target

The main gap is integer elimination of L095's two rational-factor systems
within ordered (3,5,11), alongside other algebra types and residual
Beal signatures. A primitive local obstruction could exclude an integer
branch only after covering all permitted local branches. Exact local
points would instead retire standalone exclusion at two. They would
not give global compatibility, an integer solution or a Beal resolution.

Use audited L095's complete Q,H, identity (4) and both reconstructions:
I has C=5m+u^5, H(m,C)=a^3, A=ma, B=Q(m,C)u;
II has C=m+5^10u^5, H(m,5C)=5^11a^3, A=ma,
B=Q(m,5C)u. All coefficients of H must be retained. The scope is
the two-adic analogue, not integer positivity or conditions at other
primes. In particular gcd(C,15)=1 imposes no two-adic unit condition.
The local primitivity and nonzero conditions in SCOPE are required.

## Existing work, duplicates and failures

Read L095's statement, denominator argument, complementary identity,
converses and independent audit; read L093's statement and full audit.
Reused the adequate signature discovery in
`2026-10-18-ordered-three-five-eleven-coverage.md`, branch comparison in
`2026-10-18-ordered-three-five-eleven-rational-factor.md`, and the
method comparison in `2026-10-19-rational-factor-three-adic-realization.md`.
The broader signature search need not be repeated. ATTEMPTS/043 and
046 retire standalone exclusion at eleven and three respectively;
neither decides two. ATTEMPTS/045 preserves the octic execution park.
The earlier rational octic factor-descent stop, recorded in the supplied
overview, also remains intact. The new target requires neither class
arithmetic nor a new factorization of H. L001's unrestricted local points
do not impose either complete rational-factor system.

## Primary theorem comparison

P. H. C. Putz, *Enumeration of local and global etale algebras applied
to generalized Fermat equations*, VU Amsterdam thesis (2024), version
of record, DOI [10.5463/thesis.832](https://doi.org/10.5463/thesis.832),
[primary PDF](https://research.vu.nl/ws/portalfiles/portal/367784086/Thesis_CasperPutz.pdf).
Inspected Section 5.2 p.165 and Proposition 5.20 p.169 (PDF indices
171,175), statement and full proof. Its nonzero pairwise coprime
coefficients must have odd product; solution coordinates need not all
be odd. Coefficients (1,1,1) and coordinates (B,A,C) meet that scope
for an original primitive solution. The necessary full completion is
unramified with degree lists (10,1), (5,3,2,1), or (4,4,2,1).
Its proof cites Algorithm 2.74 and local_algebras.m; no replay was
performed. This is a covering list, not realization of each entry,
classification of global rational roots, or a solution of L095's systems.
A local factor is not a global factor. The terminal exclusions in
Section 5.3 retain their special coefficient set, as the reused branch
assessment checks. No coefficient-one exclusion is imported.

Gergely Zabradi, *Notes for the course p-adic methods in arithmetic*,
ELTE summer school, 29 June 2022,
[primary notes](https://zabradi.web.elte.hu/Jegyzetek/p-adic-meth-arith.pdf),
Lemma 2.3 and Theorem 2.4, printed p.4 (PDF index 3), reread with proofs.
The latter applies to an integral polynomial, an approximate zero modulo
p^n and one partial derivative of valuation k with 0<=2k<n. It produces
an exact zero congruent modulo p^(n-k), fixing the other coordinates;
the proof iterates the one-variable lemma. There is no odd-prime
restriction on this theorem. This supplies method coverage at two,
not a system-specific root. Retain the strict inequality even when
a derivative is nonunit. No square- or fourth-root surjectivity at two
is assumed. The unit-group decomposition alone would not decide this
simultaneous question. Clark's stronger Newton formulation is already
precisely cited in foundations/17-local-power-hensel-inputs.md and is
reused without reproof or fresh browsing.

## Bounded discovery and decision

New queries: `"Putz" "3,5,11" "2"`,
`"(3t^2+t+1)" "Fermat"`,
`"generalized Fermat" "rational" "factor" "2-adic"`,
`"Putz" "Fermat" "two-adic"`,
`"1215" "1782" "2970" "cube"`, and
`"x^5" "y^3" "z^11" "local" Putz`.
Results on other signatures and numerical coefficient lists supply no
matching theorem and were not used as evidence. The bounded search
establishes neither originality nor literature-wide absence. Dahmen's
map-provenance page remains an unread nonessential lead in the reused
assessment; no new theorem from it is required. No essential source is
blocked for the approved elementary scope. Mathlib matching coverage
is not checked; unknown coverage is not evidence of absence.

After separate approval, perform one bounded test: substitute the
defining C in each complete system, inspect primitive residue triples
modulo at most 32, and seek a certified Hensel lift. Start with any
convenient parity branch for existence, but do not report branch
nonexistence from its failure. Record full polynomial and derivative
values, actual and required valuation bounds, all nonzero coordinates,
local primitivity, both original equations and identity (4) under the
same C. A residue preview alone proves no exact lift. If claiming an
obstruction, cover every primitive residue branch, including even C;
a restricted search failure is only a failed search. A nonzero value
requires an exact value or a finite valuation certificate, not just
being nonzero as a formal expression.

Continuation/abandonment test: exact common witnesses for both systems
retire standalone exclusion at two; an exhaustive obstruction excludes
only the affected system. If the bounded test yields neither, save
its full evidence and reassess rather than silently expanding precision
or changing target. Integer lifting, other local primes, other algebra
types and residual signatures remain open. This literature turn runs
no mathematical test and derives no lemma. Its new ready assessment
is for a separate approval, not authorization to calculate this turn.
