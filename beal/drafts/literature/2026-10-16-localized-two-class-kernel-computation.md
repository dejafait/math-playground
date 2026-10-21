# Localized two-class norm kernel — source assessment

TARGET: Determine the dimension of L074's localized two-class norm kernel for the fixed extension D/K.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L033/L069 field definitions, L074's complete class-section argument, L076's full supported-prime structure, the separated-eleven assessment and ATTEMPTS/025–026,034–036; searched localized class groups, ideal norms, the exact cubic and canonical scalar, and official PARI certificate/S-class entries. No inspected source supplies an unconditional value for this localized kernel.
SOURCE_EVIDENCE: Reused inspected Simon Proposition 1.3 and Milne Proposition 4.1 from the separated-eleven assessment; newly inspected official PARI stable General number fields entries and GRH warning, and FNS final author manuscript (10 June 2019), Introduction p.4, Section 7.2 PDF pp.26–27 and Table 5 (PDF p.27). Exact passages and limitations are recorded below.
COMPARISON: L074 already proves split surjectivity on localized two-torsion, so its dimension formula avoids an explicit norm matrix; PARI documents the actual S-class output. FNS's matching degree-36 descent computation is conditional on GRH, and its Selmer dimension is neither the requested class-kernel dimension nor an unconditional import.
GAP: General certificate-method coverage is ready, but no unconditional complete class data or executable checked class-group backend is available. No kernel dimension, runtime feasibility or maximal-order presentation has been established.
REASON: Approve only a future reproduction using certified complete localized class data and L074's existing dimension formula. Park execution here because the backend/data prerequisite persists; do not repeat backend probes or launch a replacement partial relation search.
SCOPE: Exactly ker(Cl(O_D[1/22])[2] -> Cl(O_K[1/22])[2]) for L033/L069's fixed fields and L074's ideal norm; ordinary maximal class groups localized at every prime above 2 and 11, no narrow groups, GRH premise or rank conclusion.
LITERATURE_REASON: The prior REVIEW_REQUIRED proposal lacked essential unconditional class-completeness and localization coverage; this turn inspects those interfaces and the matching published computational qualification.

## Gap, target and relevance

Primitive integer emptiness remains the main gap, even in the 54a1
branch of ordered (3,4,11). The intermediate target is the class-kernel
dimension above. By the already proved L074/L076 statements it measures
the nonunit contribution to W_S. Zero would remove that unknown
contribution; a positive answer would quantify additional necessary
pruning. Neither answer alone improves the current supported-unit
upper bound fourteen to the required eleven.

Essential inputs are L033's entire K and E0, L069's same degree-three
extension D/K, L074's localized norm sequence and section, and L076's
complete prime structure. No cross-notebook input is used. The class
section and dimension formula are existing results, not derived in this
literature turn. L077 and L078–L081 supply downstream unit/local context,
not class data. All class values, principality claims and independence
of further global restrictions remain unresolved.

## Primary interfaces actually inspected

[PARI official stable General number fields catalogue](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html),
accessed 16 October 2026; no release identifier displayed. Read the full
GRH warning and entries `bnfinit`, `bnfcertify`, `bnfisprincipal`,
`bnfsunit`, `idealprimedec`, plus the relative-polynomial complexity and generator-output passages.
The relevant documented guarantees are:

- `bnfinit(P,1)` retains exact algebraic data but remains GRH-conditional.
- `bnfcertify(bnf,0)=1` removes that assumption; flag one certifies only a quotient and is insufficient for equality of class groups.
- `bnfsunit(bnf,S)[5]` contains S-class number, cyclic factors and generators; component one alone is units modulo ordinary units.
- `idealprimedec(nf,p)` gives maximal primes; a nonzero third argument filters residue degrees and must be omitted here.
- `bnfisprincipal` supplies class coordinates and a principal factor; compact generators can avoid enormous expansions.
- The relative-to-absolute field interface can retain the original generators. Canonical polynomial reduction has exponential absolute-degree complexity.

These documented interfaces give a possible implementation, not an
execution certificate or feasible runtime bound. Full certification
must precede unconditional use of any bnf-dependent output.

Freitas–Naskręcki–Stoll, *The generalized Fermat equation with exponents
2,3,n*, Compositio Math. 156 (2020), 77–113,
[final author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
10 June 2019: newly read the Introduction's degree-36 class-computation
qualification (printed p.4) and Section 7.2's GRH statement and Table 5
(PDF pp.26–27, counted from one). The polynomial in the 54a1 row matches L033's K. The
reported two-Selmer dimension is four, under GRH. The authors explicitly
identify adjoining a two-torsion x-coordinate as the degree-36 field
construction whose class certification causes the conditionality;
unconditional verification was finite but impractical in their
implementation. This historical statement establishes no 2026 complexity
lower bound and no unconditional localized class-kernel value. We do not
identify a Selmer dimension with a class-kernel dimension or import the
conditional computation into the notebook's unconditional argument.

Reuse, without another retrieval or reproof, Simon, *Computing the rank
of elliptic curves over number fields*, LMS J. Comput. Math. 5 (2002),
Proposition 1.3, pp.8–9, and Milne ANT v3.08, Proposition 4.1(a),(c),
pp.68–69, as inspected in
`drafts/literature/2026-10-16-separated-eleven-supported-unit.md`.
L074 already checks their exact localization, norm and degree-three
specialization, including the full section proof. No new norm lemma is
needed. The two-torsion must be taken after localization; ordinary
two-torsion need not surject onto it.

## What a complete computation would have to retain

A future certificate must retain the fixed K and both generators of D,
an exact absolute-field identification, maximal-ring correctness,
complete class presentations for both fields with unconditional
certification, and all supported prime classes. Compare the full prime
lists with L076: two and three primes for K above two and eleven,
respectively; two and seven for D. No residue-degree filter is allowed.
Keep the class-coordinate relations killing all these primes and the
resulting complete localized invariant factors. Independent exact ideal
identities can check positive relation outputs; they cannot establish
completeness of an otherwise partial relation lattice.

Apply the standard structure theorem for finite abelian groups to the
certified localized presentations, and then use precisely L074's existing
dimension formula. An explicit norm matrix is unnecessary for this
scalar target because L074 already provides a section. If a later task
needs actual kernel representatives or filtered classes, that is a
stronger task and requires their maps and representatives. We do not
perform the invariant-factor calculation, derive a new formula or
certify any field model in this turn.

## Feasibility, overlap and stopping decision

Read ATTEMPTS/025–026: missing exact arithmetic infrastructure previously
blocked ideal enumeration. Those attempts concern different class-five
witness tests; their mathematical failures are not asserted for the
present two-class target. Read the separated-eleven assessment's backend
qualification and retain ATTEMPTS/034–036's finite-search exhaustion.
Neither supported elements nor local Kummer images compute this kernel.

A bounded infrastructure check in this turn found no `gp`, `sage` or
`magma` on PATH, no executable gp in /opt/homebrew/bin, /usr/local/bin or
/usr/bin, and no executable Sage in the first two locations. The active
python3 is /opt/homebrew/bin/python3; import-spec checks for cypari2,
sage and sympy were all false. This is an availability observation only,
not mathematical evidence or an exhaustive search of the machine.
No backend was installed, no class computation ran and no mathematical
script or lemma was written. Repeating this absence is not progress.

Continuation test: reopen execution only with an actual working exact
backend and a bounded plan that requires full certification, or supplied
independently verified complete class certificates. Stop that bounded
attempt if certification does not finish within its recorded cap; retain
conditional/partial outputs as such and infer no class value. A positive
localization relation alone cannot close this target. Here the data and
backend prerequisites are unmet, so direct computation is parked rather
than approved for immediate invocation.

Searches included `localized class group S class group computation ideal
norm two torsion number field algorithm`, official PARI certificate,
S-class and relative-norm queries, `"9261/8" "class" Stoll`, and the
exact cubic coefficients with class-group terminology. General torsion
bounds, quantum algorithms and unrelated exact-polynomial hits did not
supply this arithmetic value and were not used as theorem inputs. This
bounded search makes no novelty claim. Mathlib matching and supporting
coverage remains not checked.

The independent continuation proposed in the checkpoint concerns the
restricted dyadic *two*-descent image, reusing the audited full local
image. It does not require this global class-kernel value. Its exact
target is separately REVIEW_REQUIRED: no local restriction or new
mathematics is approved by this class-computation assessment.
