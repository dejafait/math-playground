# Tame-normalizer scalar comparison: source record

Completed source comparison, step 518, 2026-10-26.
L124 is read in full but has not been critically audited. No scalar
identity is accepted. The target is the unchanged target of
`drafts/literature/2026-10-26-tame-normalizer-moment-scalar.md`.

## Primary passages inspected

- Fornea, *Plectic Heegner classes*, arXiv:2603.28327v2,
  13 April 2026, https://arxiv.org/html/2603.28327v2:
  Remark 2.1; Section 2.1.2; Section 2.2, including (22);
  Corollary 3.9 and its construction in Proposition 3.8;
  Proposition 4.18 with proof; Corollary 4.19 with proof;
  Definition 4.23 and Corollary 4.24 with proof, especially (68).
- Gonzalez--Rotger, *Non-elliptic Shimura curves of genus one*,
  author-hosted 20-page manuscript,
  https://web.mat.upc.edu/victor.rotger/docs/ShimuraGenusOne.pdf:
  Appendix, pp.13--18, especially Theorem 5.4, the standing square-free-level
  assumption on p.14, Definition 5.5, Proposition 5.6, Lemma 5.10
  and its proof on pp.17--18. The manuscript's printed pagination
  is used here; no identification with final journal pagination is
  presumed.
- Blasius--Guerberoff, *Complex conjugation and Shimura varieties*,
  Algebra & Number Theory 11 (2017), 2289--2322,
  https://msp.org/ant/2017/11-10/ant-v11-n10-p02-s.pdf,
  Section 2.2, Lemmas 2.2.1/2.2.4 and Remark 2.2.3 with proofs,
  pp.2295--2297; the remaining canonical-model applicability record
  is reused from the step-516 assessment. This is an outer-action
  input, not a scalar-action theorem.

## Exact classical comparison

In the Gonzalez--Rotger manuscript the appendix assumes D>1 and,
from p.14 onward, square-free N coprime to D. Here R is an imaginary
quadratic order of conductor f, CM(R) uses normalized optimal
embeddings into the Eichler order, and sigma_a is the ring-class
Artin action. Lemma 5.10 states that every P in CM(R) satisfies
bar(P)=omega_m(P^{sigma_a}) for some ideal a, with
m=D(R)N*(R). Its definitions are

\[
D(R)=\prod_{q\mid D,\ (R/q)=-1}q,\qquad
N^*(R)=\prod_{q\mid N,\ q\nmid f,\ (R/q)=1}q,
\]

where (R/q) is the Eichler symbol. The lemma controls [a] modulo
squares independently of P, not one identical representative a for
all points. Its proof distinguishes division primes, split level
primes away from f, and primes dividing both N and f, including 2.
Theorem 5.4 also retains a factor (-1)^{#{q | (D,m)}} when comparing
quaternionic and modular Atkin--Lehner actions through its isogeny.
This prevents importing a remembered modular sign without comparison.
These statements are source records, not new specializations.

## Applicability and decision

Fornea's Remark 2.1 assumes a finite uniformizing place; here that
place is infinity. Corollary 4.19's proof specifies good spherical
Hecke operators. Sections 2.1.2/3.0.1 use full coset sums; (22)
retains the unit-normalized auxiliary Hecke map. Corollary 3.9
specifies individual CM cells; Corollary 4.24 gives the complete
character trace after integration. None identifies L124 (10)'s
selected lifts with a full correspondence fiber. These distinct
source statements cannot be substituted for that identity.

The following are comparison obligations, not proved obstructions:
L124 allows split tame conductor exponent two and uses deep
K_{p^m}, rather than just square-free Eichler level. The CM order at
a deep cell cannot be identified with the conductor-one shallow
order without checking its stabilizer. Even in a square-free tame
subcase the cited lemma does not track those cells, their chosen
lifts, the kernel weight and the completed projection together.
Dropping to a shallow quotient would need an injectivity or lifting
argument in the actual moment domain. No such statement was read.

Thus direct import of b_n=epsilon b is **not justified by these
theorems**. This is an informative negative source comparison, not
a counterexample, proof of nonscalarity, or claim of novelty. A
bounded full-level proof attempt remains eligible under EXPLORE,
but only after the independent audit of L124 specified in the new
audit assessment. Stop a later scalar attempt unless it produces
an actual branch/trace identity with normalization, or a concrete
obstruction to that identity. No repeated kernel-sign test is useful.

## Reuse, search and limits

The local comparison read L124 fully, L123's hypotheses/definitions,
the step-516 source assessment, and ATTEMPTS/003/004/030/058/059.
The initial descent and pr_A construction coverage is reused from
the step-515 audit; no audit of L124 is claimed here.

Searches on 2026-10-26 included: CM points Atkin-Lehner complex
conjugation Shimura reciprocity trace; CM points complex conjugation
full level Hecke; plectic Heegner classes Hecke Fornea; plectic
Heegner Atkin-Lehner conjugation; and Gonzalez Rotger Shimura 5.10
conjugation. The named primary passages above were inspected.
No search result or failed search establishes a nonexistence theorem.
The journal's official index confirms J. Math. Soc. Japan 58 (2006),
927--948 (https://mathsoc.jp/publication/JMSJ/onlineindex/58-4.htm);
the theorem comparison used the author manuscript, not the journal PDF.

A search hit points to a Disegni prepublication Lemma 8.0.2 on a
classical Heegner trace. The author-hosted PDF timed out; the publisher
PDF at https://msp.org/ant/2015/9-7/ant-v9-n7-p03-s.pdf was retrieved,
but that lemma and its proof were not located/read in it. It is an
unimported optional lead, not essential missing coverage or grounds
for an access-recovery turn. No full-level scalar claim is attributed
to Disegni. Other search hits on higher-level CM points were not
inspected theorem inputs.

No mathematical scripts or lemma files were changed. Mathlib coverage
for a matching full-level scalar/moment theorem was not checked.
No numerical local certificate, rational Kummer membership,
nonvanishing, multiplicative-prime rank criterion, or BSD case follows.
