# Prime-twist calibration and finite-lattice certificate: continuation scope

TARGET: Prove a conditional exact-normalization and all-argument denominator certificate for L027 from a finite relative Manin-symbol presentation, a certified one-dimensional real plus eigensymbol, and an independently certified nonzero total-Neron-normalized central value of a prime twist ell congruent to 1 modulo 4 and coprime to p times the minimal discriminant.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the 2026-10-06 exact-normalization search and ATTEMPTS/022; on 2026-10-07 retrieved the primary URLs below and checked the integral presentation, positive-twist period case and calibration passage for this unchanged target.
SOURCE_EVIDENCE: Stein Proposition 1.24/Theorem 1.25 https://www.wstein.org/books/modform/modform/modular_symbols.html ; Cremona second edition Section 2.11 pp. 38--39 https://johncremona.github.io/book/fulltext/chapter2.pdf ; Pal v2 Corollary 2.6/Theorem 3.2 https://arxiv.org/pdf/1012.0094v2 ; Stein--Wuthrich Section 3.7 p. 1769 https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=13 ; primary statements and essential cases retrieved 2026-10-07, with earlier comparison reused.
COMPARISON: Known twist calibration and integral finite generation cover the mechanism; the remaining difference is exact orientation/period and generator-denominator bookkeeping in L027's convention.
GAP: No actual presentation, certified normalized twist value, numerical C or nonzero quadratic coefficient is produced; independent value certification and eigenline identification remain explicit premises.
REASON: Assemble a finite conditional input certificate from known results without redoing convergence, proving twist nonvanishing or trusting numerical rounding.
SCOPE: Non-CM global minimal E/Q; ordinary p>=5; primitive untwisted trivial branch, total real Neron period, kappa(gamma)=1+p; full torsion-free relative weight-two symbol presentation for Gamma_0(N); nonzero rational real-integration eigenfunctional identified by a certified one-dimensional space; prime ell=1 modulo 4 with ell coprime to p times the minimal discriminant; exact independently certified q=L(E^ell,1)/Omega(E^ell) != 0. Permit L(E,1)=0; assume neither BSD nor finite Sha nor rational rank.

The [completed assessment](2026-10-06-exact-symbol-normalization-certificate.md)
contains the earlier primary comparison and discriminating test. Separate
source approval completed on 2026-10-07, with direct primary URLs now
recorded in this assessment. No mathematical attempt was performed in
this literature-only step; the unchanged target remains SPECIALIZE.

Essential local inputs are L027, L004 and foundations/05; L026 is a
possible downstream application with additional hypotheses. Use the
named presentation, twist identity and period comparison by citation.
Do not reprove those results or silently infer Manin constant one.

Seek an exact scalar recovering the real-Neron functional and a finite
generator certificate proving v_p(S(r))>=-C at every rational argument.
Keep full relative paths, torsion removal, cusp-path orientation and
the distinction between real integration and a software involution.
Generator values are acceptable only with complete generating and
relation evidence. Avoid a half-projection with unrecorded factors.

Continue if those inputs suffice for both conclusions without circular
normalization. A raw nonzero L-value, a rounded period quotient or a q
computed using the unknown original scale fails the premise. If the
proposed certificate needs an additional unproved eigenline, isogeny
or integral-lattice assertion, isolate it and stop the uncovered part.
The independent q need not be produced by this conditional theorem,
but its absence must stay explicit in the result and checkpoint.

This is reproduction of known mechanisms; no originality is claimed.
Its use would reduce L027's map/denominator premises to finite data,
not ensure that L027 excludes zero. Rational Kummer membership,
L026's other hypotheses and complex-order comparison remain unresolved.
Mathlib coverage of the full certificate or its supporting presentation
has not been checked.

## Separate approval and source-link recovery, 2026-10-07

This is a process repair and source reapproval, not a new mathematical
advance. The exact target and assumptions are unchanged. Earlier search
coverage is reused rather than restarted. No lemma or mathematical
script is written. ATTEMPTS/022 stops repeating L027's enclosure audit;
this target instead concerns its still-missing symbol inputs.

[Stein, online *Modular Forms, a Computational Approach*, General Modular
Symbols](https://www.wstein.org/books/modform/modform/modular_symbols.html),
Definition 1.23, Proposition 1.24 and Theorem 1.25: the finite-index
subgroup and integer-weight hypotheses include Gamma_0(N), weight two.
Read the integral continued-fraction generation proof and full relation
statement: quotient by the two-term, three-term and central-element
relations and all torsion. The displayed proof verifies the relations;
completeness is a cited theorem, not fully proved on this page. A rational
functional kills torsion, but any coordinates in a rational basis still
require their denominators to be recorded. No theorem reproof is needed.

[Cremona, *Algorithms for Modular Elliptic Curves*, corrected second
edition, Chapter 2](https://johncremona.github.io/book/fulltext/chapter2.pdf),
Section 2.11, pp. 38--39: read the Gauss-sum period identity through
(2.11.4), including its odd-prime, prime-to-N assumptions and real
character case. The coprimality to the minimal discriminant in our
target implies good reduction at ell and hence ell does not divide N.
The nonzero twist is supplied, not inferred from this book's prime-search
existence discussion. Cusp orientation must be matched at specialization.

[Pal, *Periods of quadratic twists of elliptic curves*, arXiv:1012.0094v2,
21 January 2011](https://arxiv.org/pdf/1012.0094v2), Corollary 2.6
(p. 6), Lemma 3.1 and Theorem 3.2 (pp. 7--8): reread the minimal-model
condition, the coprime-discriminant and d=1 modulo 4 case, and the
positive-d proof integrating the absolute differential over the full
real locus. These cover the restricted prime and total-period convention.
Neither negative twists nor arbitrary minimalization factors are imported.
Earlier assessment page references count the PDF cover differently; the
numbering here uses the printed arXiv page labels.

[Stein--Wuthrich, *Algorithms for the arithmetic of elliptic curves using
Iwasawa theory*, Math. Comp. 82 (2013)](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=13),
Section 3.7, p. 1769, explicitly discusses calibrating sign and rational
scale using a nonzero twist when the original central value vanishes.
Its preceding conductor-lowering hypotheses are not assumed for our
prime twist: Cremona's prime identity and Pal's restricted period
comparison provide the load-bearing inputs here. This passage supplies
a comparison with a known mechanism, not independent certification of q.

Decision: SPECIALIZE retained. The independently certified q, full
presentation and correctly identified real eigenfunctional remain granted
inputs. The future test must account for orientation and every coordinate
denominator; any additional unproved assertion must be isolated and its
dependent work stopped. No actual q, C, coefficient, rank bound or
Mathlib coverage check results from this approval.
