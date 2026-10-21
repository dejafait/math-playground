# L094 — Dyadic absolute different bound for the actual normal closure

## Hypotheses

Fix any survivor of audited L089, with its same original E/Q,
c,h,d_*,e_*, both fixed domains and fixed algebraic closure. For any
of the six orderings o retain audited L090's full-coordinate fields

    T=F_tpd=Q(E[2]),
    G_o=Q(t_o)(iota,E_o[15]), C_o=G_o^nor,
    T subset C_o subset M=Q(E[60]).

The normal closure is over Q, not over a completion. Let v be any
actual place of T above two and w any place of C_o above v; use
compatible completion embeddings. Retain audited L093's uniform
bound v_2([(C_o)_w:T_v])<=10. Here v_2 of an integer denotes its
exponent of two. Keep d=6 and epsilon_d=1 only in the qualified
source-comparison context; no initial theta-data are assumed.

For every finite extension K/Q_2 define

    d_2(K)=a_K/e(K/Q_2),
    D_(K/Q_2)=m_K^(a_K).

Thus d_2 is the valuation of the absolute different ideal under the
extension of v_2 normalized by v_2(2)=1. It is not the integer
uniformizer exponent a_K or a relative different over T_v.

## Conclusion

For every such survivor, all six orderings and all actual v,w,

    d_2((C_o)_w) <= d_2(T_v)+10+1/e(T_v/Q_2).

This is a sufficient upper bound, without a sharpness assertion.
It is a cited specialization (REPRODUCTION), not a new ramification
theorem, complete normal-closure repair or essential IUT flaw.

## Proof

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-20-normal-closure-dyadic-different-transfer.md`.
It covers exactly this target and its normalization. No general
local different theorem is reproved. Import:

- Mochizuki, *Inter-universal Teichmuller Theory IV*, April 2020
  [inspected reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
  Proposition 1.3(ii), printed pp.11–12, with the absolute ord(p)=1
  notation of Propositions 1.1–1.2, pp.9–10. For finite local fields
  k_0 subset k_1 subset k_i, with k_i/k_1 Galois and k_1/k_0 tame,
  it gives d_i<=d_0+n_i+1/e_0, where
  n_i=v_p([k_i:k_0]) and e_0=e(k_0/Q_p). Equality k_1=k_0 is
  permitted. The assessment records inspection of its entire proof.
- Milne, *Fields and Galois Theory*, v5.10 (September 2022),
  [Theorem 3.17 and proof, pp.39–40](https://www.jmilne.org/math/CourseNotes/FT.pdf):
  a finite Galois extension remains Galois over an intermediate field.
- Milne, *Algebraic Number Theory*, v3.08 (19 July 2020),
  [Proposition 8.10 and proof, p.139; Proposition 8.13 and proof,
  p.141](https://www.jmilne.org/math/CourseNotes/ANT.pdf): Galois
  completion and compatible towers at actual extending places.

Fix an arbitrary survivor, ordering o and pair v,w. L090 gives the
finite normal closure C_o over Q and the embedded intermediate T.
Characteristic zero makes C_o/Q separable, hence finite Galois.
The cited Galois correspondence gives C_o/T Galois. Applying the
completion theorem to this extension at the actual extending places
v,w gives (C_o)_w/T_v finite Galois. Both completed fields are finite
extensions of Q_2, so they are precisely finite local fields of the
residue characteristic required by Proposition 1.3(ii).

Set p=2, k_0=k_1=T_v and k_i=(C_o)_w. The first extension is the
identity: its ramification index is one and its residue extension is
trivial, so it is tame. This asserts nothing about tameness of
T_v/Q_2, which is not the tame-intermediate hypothesis. The second
extension is Galois by the preceding paragraph. Every hypothesis of
the imported different estimate now holds.

The source's absolute normalized d_i,d_0 are exactly d_2((C_o)_w)
and d_2(T_v) as defined above: both use valuation one on 2. Its n_i
is the integer degree valuation v_2([(C_o)_w:T_v]), not a valuation
of a uniformizer or of the relative different. Consequently its
conclusion is

    d_2((C_o)_w)
      <= d_2(T_v)+v_2([(C_o)_w:T_v])+1/e(T_v/Q_2)
      <= d_2(T_v)+10+1/e(T_v/Q_2),

where the final inequality is exactly audited L093. The choice of
survivor, ordering and actual places was arbitrary, proving all the
quantifiers. No global core is cancelled locally, no completions at
different places are identified, and the literal nonnormal G_o/T
is never asserted Galois.

The result closes one local sufficient different contribution to a
possible normal-closure repair. It neither restores the global
relative degree allowance nor verifies the exact field prescription,
other primes or all initial-data conditions. April-reproduction
current-version/authentication and the def= boundary remain qualified;
this proof does not authenticate source bytes or apply the corollary.
The height-selected prime, native input/action/factorization/pilot,
essentiality and original finite B>=A remain unresolved. There is no
complete-solution candidate. The separate step377 critical audit below
validates this specialization with these qualifications retained.

### Separate critical audit — 2026-10-20, step377

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-20-normal-closure-dyadic-different-critical-audit.md`
covers precisely this audit. Reuse the completed primary readings in
the transfer assessment: IV Proposition 1.3(ii), including its entire
proof and absolute normalization, and the cited Milne results.
This audit checks their application, not their reproof or a fresh
authentication of the April reproduction. It passes without changing
the bound or adding a mathematical input.

**Embedded global tower.** Audited L090 identifies Q(t_o)=T for
each of the six orderings, and G_o contains Q(t_o) by its definition.
Its full-coordinate comparison places G_o in the finite Galois
M=Q(E[60]). Every Q-conjugate of G_o remains in M. Their compositum
is therefore the finite normal closure C_o inside that same M;
in particular T subset G_o subset C_o. This is the tower needed
here. The degree or the order-two core is not used to infer local
normality. Since C_o/Q is finite normal and has characteristic zero,
it is finite Galois. Milne FT 3.17 applies over its intermediate
T and gives C_o/T Galois. It does not require G_o/T to be Galois,
nor is transitivity of normality being assumed.

**Actual places and completion.** Fix an arbitrary v of T over two
and an arbitrary w of C_o over v. Completion of the inclusion using
these places gives T_v subset (C_o)_w; Milne ANT 8.10 identifies
the latter extension as finite Galois, with the actual decomposition
group. Both fields are finite extensions of Q_2. Compatible towers
are exactly those of ANT 8.13 and L093. No isomorphism between
different completed places, or equality of their embedded images,
is needed. The argument does not discard places at which T/Q is wild.

**Tame intermediate and source hypotheses.** In IV 1.3(ii) take
k_0=T_v, k_1=T_v and k_i=(C_o)_w. The source requires k_i/k_1
Galois and k_1/k_0 tame; it has no requirement that the latter be
proper. The first check follows from the actual completion theorem.
The second is the identity extension, with ramification index one
and trivial separable residue extension. Thus it is tame even when
the different of T_v/Q_2 is nontrivial. Requiring T_v/Q_2 to be
tame would be a different, unnecessary hypothesis.

**Normalization and numerical substitution.** For each completed
field K the integer exponent a_K is defined by
D_(K/Q_2)=m_K^(a_K). Its absolute valuation is a_K/e(K/Q_2),
because a uniformizer of K has valuation 1/e(K/Q_2) when 2 has
valuation one. This matches the source's d_i and d_0 separately;
no relative different exponent is substituted. The source's e_0
is e(T_v/Q_2), not e((C_o)_w/T_v) or e((C_o)_w/Q_2).
Its n_i is v_2([(C_o)_w:T_v]), the exponent of two in an integer.
The cited theorem therefore yields exactly the first displayed
inequality in the proof.

The full L093 proof and its separate step372 audit were inspected.
Their statement uses this same original survivor, T, C_o and every
actual v,w. It bounds the larger ambient completed degree by ten,
using the joint odd-torsion inertia, cyclic residue quotient and
full four-division over T_v, then passes to the intermediate degree
by the tower formula. It never cancels the global core locally.
Thus its bound supplies n_i<=10 here with no missing ordering or
place condition. Substitution gives the claimed allowance
10+1/e(T_v/Q_2) above d_2(T_v). This is an upper estimate, not
an assertion of equality or an attained different.

All choices in these checks were arbitrary within the hypotheses,
so the quantifiers are unchanged. The direct mathematical inputs
remain L090 and L093; the audited L089 data enter through them.
This certifies one local input using the checked known results.
It provides no result beyond those methods, no complete repair,
and no change to the original finite B>=A gap. The independent
global relative-degree excess, exact generation, other primes,
source-version/def= qualifications and essentiality remain open.

## Mathlib

Full matching and supporting Mathlib coverage for this specialization
have not been checked. Unknown availability is not absence. The
argument imports the precisely cited local different and Galois
completion results; no formal verification or numerical certificate
is claimed.
