# Boolean local distributions through order four — source input

## Hypotheses

Let W be a finite Boolean variable set and m a real vector indexed by
all subsets of W, with m_empty=1. Repeated occurrences denote the same
variable. These variables may index supports; they are not evaluation
positions. For the cardinality source use H variables, integer N, uniform
variable weights, alphabet {0,1} and c_1=N/H.

## Conclusion

Import Laurent's Boolean cone description: m is a convex combination
of Boolean monomial vectors exactly when Z^(-1)m is nonnegative, where
Z_(I,J)=1_(I subset J). Its inverse has entries
(-1)^(|J\I|) for I subset J and zero otherwise. Thus its coordinates
are the atom masses, including the all-zero atom. The assertion applies
to a complete local vector on W; it does not give a global measure from
separate overlapping local vectors. The four-variable specialization and
elimination of its unknown highest moment remain research work.

Raghavendra–Tan's conditional-cardinality requirement applies to every
assignment on at most k-1 variables in a k-round local-distribution
system. Set k=4 for three-variable conditioning. Zero-probability
conditioning must be handled homogeneously, not by division. Its
specialization to the fixed triple, with all repeated indices, remains
research work. Consistent marginals alone do not imply cardinality.

## Proof

Monique Laurent, *A Comparison of the Sherali–Adams, Lovász–Schrijver,
and Lasserre Relaxations for 0–1 Programming*,
[CWI PNA-R0108, 31 July 2001](https://ir.cwi.nl/pub/4319/04319D.pdf),
Section 3.1, (11)–(12), Lemma 2(ii) and complete proof, printed pp.5–6;
Section 3.2, (14)–(16), printed pp.7–8. Inspected the inverse, diagonal
congruence proof, its closing cancellation and the linearized atom
inequalities. Import the finite Boolean result without reproof.

Prasad Raghavendra and Ning Tan,
[arXiv:1110.1064v1](https://arxiv.org/pdf/1110.1064v1), Section 3,
Definitions 3.1,3.3, printed p.7, local-distribution and conditional
cardinality displays p.8, global-distribution qualification p.9.
These passages were freshly inspected, including PDF page 10's display.
Foundations/13 retains the general scope and qualifications.

Polak's [arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
Section 1.1 (1)–(3), Proposition 1.1 and full indicator proof, p.2,
and Section 1.2 p.3 were reinspected for comparison. Full A_4 is a
stronger program, not the proposed scalar capacity test. Retain the
printed A(n,d) versus proved A(n,d,w) qualification in foundations/12.

## Mathlib

Full matching four-variable extension/cardinality specialization: not
checked. Supporting Boolean inversion and probability coverage: not
checked; unknown availability does not establish absence.
