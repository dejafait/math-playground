# Selected-place quantifiers — source review, step 216

This is a literature-only step. The main gap remains the original finite
B>=A and the actual input/action/pilot/essentiality bridges. The bounded
target is the exact selected-place scope governing the use of L059 with
L053's fixed global U,Q. No simultaneous-place theorem is proved here.

## Inspected primary text and exact scope

[Mochizuki, IUT I, May 2020](https://www.kurims.kyoto-u.ac.jp/~motizuki/Inter-universal%20Teichmuller%20Theory%20I.pdf),
186 pages, Definition 3.1(b)–(f), printed pp.61–63, and Remark 3.1.3,
p.65, were read in full for these clauses through the
[reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf).
The author endpoint supplied title/version metadata and indexed remark
wording, but subsequent full-passage retrieval timed out. Byte identity
and journal-version equivalence are unverified; the inspected primary
author text, in this reproduction, is the precise version used.

The quantifiers extracted from that definition are:

- (b): the selected bad moduli places form a nonempty subset, with odd
  residue characteristics; multiplicativity is tested at every F-place
  above them. Places outside the subset may also have bad reduction.
- (c): l avoids those residue characteristics and the q-orders at all
  F-places above the selected subset.
- (d): one global basic orbicurve/cover is fixed.
- (e): the selected K-places form a section over all moduli places. The
  basic local type is required at its selected bad members. Algebraic
  closure lifts determine decomposition groups only up to conjugacy.
- (f): one global nonzero cusp is fixed; at each selected bad member,
  its image must have label ±1. Other selected members have no such
  label requirement.

Remark 3.1.3 concerns determination of data already satisfying these
conditions. Its comment about different sections is not an existence
or compatibility theorem for a prescribed global U,Q.

[Mochizuki, EtTh, PRIMS 45 (2009)](https://ems.press/content/serial-article-files/41069?nt=1),
Definition 2.5(i), p.265, and the label construction/Corollary 2.9 with
its proof and Remark 2.9.1, pp.268–269, were inspected. At a finite
extension of Q_p with odd p,l and K=double-dot K, the graph quotient
factorization and a splitting compatible with Theorem 1.10(iii)'s sign
structure are distinct conditions. Labels come from cusp closures on
the graph cover, reduced modulo l and sign. Corollary 2.9's orbit
bijection assumes a primitive l-th root and has the stated exceptions;
it is not used to relabel an arbitrary nonzero cusp as ±1. Reuse the
odd-level correction in IUT I Remark 3.1.6 as recorded in the existing
native source notes; the deleted even-level EtTh remark is not an input.

## Comparison with the unchanged local results

L053 fixes U, alpha, psi, V and Q globally, and only supplies their
retained completion's point-group description. L057 supplies the actual
arithmetic graph factorization there; L058 supplies the separate local
compatible splitting; L059 supplies its actual label ±Q. These results
do not assert that the same cover has graph type at any other place.

The extraction makes a materially narrower continuation available:
test a singleton bad moduli subset at the rational place 3, with a full
place section constrained to pass through w. The next attempt must
identify the actual field of moduli, justify the existence of that
section and compare the actual quotient-stack cusp with the ±Q label.
This review proposes that test; it does not construct its section or
prove its applicability. If another bad place is added later, its
compatibility with the same U,Q is a new obligation. One may not change
U,Q independently at different selected places.

The basic and theta covers must remain distinct. The local splitting
in L058 is data at the retained completion. The inspected clauses do
not impose a single global splitting of all the local cusp extensions;
this observation does not construct any additional theta data or
identify an actual numerical pilot.

L051 is relevant to the all-F-place quantifier in (b). The q-order
condition in (c) uses F-places, not ord_N(q_0) at a K-place. Its
normalization and coprimality are left for a separate application,
not inferred from the graph label. This turn does not certify full
initial Theta-data or an instance of Corollary 3.12.

## Duplicate, failure and source screen

Read L053's hypotheses and actual quotient construction, the conclusions
and hypotheses of L045,L051,L058,L059, and the existing native cover/cusp
and retained-label source records. Searched these relevant paths and
their assessments for singleton, section, simultaneous-place and
q-order coverage. The earlier notes explicitly left a complete place
section open. No existing result in this screen constructs this
particular singleton/section application.

ATTEMPTS/030 stops the full rank-two multiplication cover, whereas the
present continuation retains the audited rank-one factor. ATTEMPTS/031
stops an unverified marked coordinate comparison, whereas L059's
audited component argument is now available. Neither stop settles the
proposed section test. ATTEMPTS/027's exact-old-curve stop remains
parked; no old rational q or new curve is substituted. No cross-notebook
theorem input or sibling checkpoint was read.

Queries used the exact native Definition 3.1/section/rank-one terminology
and the exact Remark 3.1.3/existence terminology. Overview and unrelated
remark search hits were not treated as theorem evidence. Essential
clauses were read completely, rather than inferred from search excerpts.
The inaccessible author query variant and unavailable screenshot output
were not used as evidence. Existing source coverage for the known Tate,
isogeny and graph comparison inputs is reused without reopening it.
Full matching Mathlib coverage was not checked.

## Continuation and abandonment test

Use L053,L057,L058,L059, with inherited L045,L048,L051,L052,L054,L055,L056;
retain E_0/Q, F=Q(zeta_60,E_0[30]), K_glob=F(E_0[7]), Omega,u,w,
H subset N, M>=max(M_tors,31), full 30-torsion, fixed pointed Tate
isomorphism, changed q_0 in Q_3 with v_3(q_0)=30, and actual
U,alpha,psi,gamma,0_B,Q,c. Neither K_glob=N nor q_0=3^30 is assumed.

Continue only if the same global cover and cusp meet (e)–(f) using the
proposed singleton and a genuine full section through w. An unproved
second-place identification, forced incompatible lift or cusp marking
is a failure to be preserved, not permission to replace Q. Do not
require all places above 3 to be in the section. If an essential
additional theorem is needed, record that exact missing coverage for
a later literature step. Conditions outside (e)–(f), all actual
input/action/pilot/essentiality bridges and finite B>=A remain unresolved.
