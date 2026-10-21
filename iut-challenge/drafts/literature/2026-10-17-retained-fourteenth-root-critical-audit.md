# Retained fourteenth-root specialization — approved audit scope

TARGET: Critically audit L069's same-field fourteenth-root membership, including full torsion, representative exponents, coprime-root algebra and all root choices, without native field or pilot identifications.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact theorem search and source comparison in 2026-10-17-retained-fourteenth-root-membership.md; compared complete L069 with L045's torsion/completion proof, L048's hypotheses and Tate-parameter proof, L054's membership proof and audit, history/264 and ATTEMPTS/027,031,032. Reopened only the load-bearing author-hosted theorem statements and relevant proof cases; no broader discovery search was needed for this unchanged specialization.
SOURCE_EVIDENCE: Milne, Elliptic Curves, second edition (2021), II.6 Proposition 6.3 pp.70–71 (characteristic-zero proof p.70) and III.3 p.103 after (26), https://www.jmilne.org/math/Books/EC2.pdf; Kedlaya, Introduction: the Tate curve, fall 2004, Theorem 1 p.3 including its finite-extension parenthesis, group-law discussion p.4, https://kskedlaya.org/18.727/tate-curve.pdf. Statements and relevant proof discussions were read directly on 2026-10-17; Silverman Advanced Topics (1994), V.3.1/V.4 remains an unread proof reference, not an independently inspected source.
COMPARISON: The ready construction assessment already supplies every essential external theorem for the proposed independent audit. Known uniformization and full geometric torsion cover the claimed field and parameter hypotheses; they do not themselves certify L069's completion bookkeeping, exponent counting or simultaneous root identities. Those are precisely the remaining audit obligations, using L054's existing square-root conclusion without reproof.
GAP: No essential source gap remains for this exact audit. Its mathematical verdict is still pending; native field applicability, a source-marked rho, all-image factorization, independent initial-data hypotheses, essentiality and original finite B>=A remain outside scope.
REASON: Source-scope comparison changes the continuation from REVIEW_REQUIRED to a ready mathematical audit, without self-certifying L069 or deriving a new result. Reuse these sources on the next turn.
SCOPE: Only TARGET with direct inputs L045,L048,L054 and the complete L069 proof; L042 is retained background, not a changed parameter or new direct input. Allow an independent check of full torsion, same-field representatives, integral exponent ambiguity, Bezout algebra, simultaneous identities, primitive root order and exhaustion. No new radical level, field enlargement, curve reselection, native identification or marked factorization is approved.
LITERATURE_REASON: The supplied literature-only gate requires separate source-scope approval of the newly written L069 critical-audit continuation. This review compares that audit with ready coverage; it does not repeat construction research or seek additional literature to fill a quota.

## Exact source scope

Milne II.6 Proposition 6.3 gives rank-two geometric torsion for
positive levels prime to field characteristic. Its characteristic-zero
proof transfers the complex case; the later Witt-vector case is
irrelevant. This is the source input for full torsion counts, not a
rationality theorem for the retained completion.

Milne III.3 p.103 after (26) states Tate uniformization for a nonzero
parameter in Q_p of absolute value below one over every finite
extension. Kedlaya Theorem 1 p.3 explicitly includes those extensions;
p.4 discusses its group property and refers the hard surjectivity
proof to Silverman. Import the named theorem, with the standard
coefficient convention from Milne; no analytic reproof is required.
These sources cover actual same-field representatives, rather than
only Galois-fixed geometric classes. Versions are author-hosted copies
read on the check date; no byte-identity claim is made.

The remaining work is an independent check of the specialization
already written in L069. Standard integer Bezout and polynomial
root-counting arguments require no new research theorem. No root
calculation or audit verdict is performed in this literature-only step.
Full matching Mathlib coverage remains unchecked; this is not an
absence claim and is not an audit gate.

## Inputs, duplicate screen and preserved failures

L045's full-torsion/completion argument and L048's same-curve Tate
parameter argument are the relevant input ranges. L054's first
membership proof and its separate audit are sufficient here; its later
native-field application is not needed. L053's geometric root, screened
in the reused assessment, was not a same-N representative result.
L054 supplies the square-root part only; L069 adds the requested
seventh/fourteenth-root bookkeeping. No duplicate lemma is proposed.

ATTEMPTS/027 excludes exact-curve globalization at the old rational
parameter; the changed curve is retained. ATTEMPTS/031 concerns actual
marked coordinate transport, and ATTEMPTS/032 stops the conditional
tensor-enclosure objection. Existential radical membership does not
reopen either route. No source promises a native pilot marking or an
all-image statement from torsion rationality.

## Ready continuation and discriminating test

The main gap is original finite B>=A. The intermediate target is a
critical audit of existential fourteenth-root membership in unchanged
embedded N; a passing audit could secure that particular input for
L068's conditional scalar stage. The independent native and global
bridges listed in GAP would still be unresolved.

Retain L069,L045,L048,L054; the same E_0,F,K_glob=F(E_0[7]),Omega,
u,w,H=F_u,N=(K_glob)_w=Q_3(zeta_420,3^(1/7)), fixed embedding,
primitive zeta_420, full geometric 30-torsion over F, full geometric
7-torsion over K_glob, M>=max(M_tors,31), pointed Q_3 Tate
isomorphism, q_0 in Q_3 and v_3(q_0)=30 with v_3(3)=1.
L054 supplies the chosen s in H. Do not assume q_0=3^30,
K_glob=N, native K_w=N or any source-marked rho.

Pass only after separately checking full global/local torsion-set
agreement, applicability over N itself, representative-exponent
invariance and counting, the Bezout sign and all integral powers,
every simultaneous root identity, primitive order and all root choices,
and the absolute valuation, with no field enlargement. A failure must
name the exact invalid step and whether a repair stays within scope;
new essential source hypotheses return to review. Do not infer a
native marking, reopen a stopped objection or claim an IUT flaw.
