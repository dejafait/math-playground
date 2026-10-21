# L095 — Absolute different bounds at three and five for the normal closure

## Hypotheses

Fix any survivor of audited L089, retaining the same original E/Q,
c,h,d_*,e_*, both fixed domains and fixed algebraic closure. For each
of its six root orderings o use audited L090's full-coordinate fields

    T=F_tpd=Q(E[2])=Q(t_o),
    G_o=Q(t_o)(iota,E_o[15]), C_o=G_o^nor,
    T subset G_o subset C_o subset M=Q(E[60]).

The normal closure is over Q in this fixed closure. Use audited
L092's exact degree and comparison constant

    [C_o:T]=184320=2^12*3^2*5,
    C_0=46080=2^10*3^2*5.

For p in {3,5}, let v be any actual place of T above p and w any
actual place of C_o above v. Use the induced compatible completion
embeddings. For every finite extension K/Q_p define

    D_(K/Q_p)=m_K^(a_K), d_p(K)=a_K/e(K/Q_p).

Thus d_p is the absolute different order under the valuation v_p
with v_p(p)=1. When applied to an integer degree or to C_0, v_p
denotes the ordinary integer prime exponent. No initial theta-data
are assumed. The source comparison retains the April 2020
reproduction qualification; d=6 and epsilon_d=1 are comparison
parameters only.

## Conclusion

For every such survivor, all six orderings and every actual v,w,

    d_p((C_o)_w) <= d_p(T_v)+v_p(C_0)+1/e(T_v/Q_p), p=3,5.

Explicitly the allowances above d_p(T_v) are 2+1/e(T_v/Q_3) at
three and 1+1/e(T_v/Q_5) at five. These are sufficient upper bounds,
not exact differents or a complete normal-closure repair. This is a
known-theorem specialization (REPRODUCTION), validated by the separate
step381 critical audit below; it supplies no essential IUT flaw or
finite B>=A conclusion.

## Proof

### Imported theorems, relevance and stopping test

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-20-normal-closure-odd-bad-prime-differents.md`.
Its completed comparison covers precisely these fields, primes,
places and normalization, reusing the inspected general-p theorem
and its entire proof. L094 treats only two and is a precedent rather
than a mathematical input here. The scoped duplicate check finds no
previous application at three and five. ATTEMPTS/034's cyclic test
and ATTEMPTS/035's source-authentication stop are not reopened.

Import the following known results without reproof:

- Milne, *Fields and Galois Theory*, v5.10 (September 2022),
  [Theorem 3.17(b–d), pp.39–40](https://www.jmilne.org/math/CourseNotes/FT.pdf):
  finite Galois correspondence, in particular Galoisness over an
  intermediate field.
- Milne, *Algebraic Number Theory*, v3.08 (19 July 2020),
  [Proposition 8.10 and proof, p.139; Proposition 8.13 and proof,
  p.141](https://www.jmilne.org/math/CourseNotes/ANT.pdf): the
  completion of a finite Galois number-field extension at extending
  places is Galois with its decomposition subgroup as Galois group;
  compatible towers have the stated subgroup intersections and
  quotient images. The subgroup order equals the local degree.
- Mochizuki, *Inter-universal Teichmuller Theory IV*, April 2020
  [inspected reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
  Proposition 1.3(ii), printed pp.11–12, with absolute ord(p)=1
  notation on pp.9–10: for finite local fields k_0 subset k_1
  subset k_i, k_i/k_1 Galois and k_1/k_0 tame,

      d_i <= d_0+n_i+1/e_0,
      n_i=v_p([k_i:k_0]), e_0=e(k_0/Q_p).

  Here d_i,d_0 are absolute different orders. The identity
  intermediate k_1=k_0 is permitted. The prior assessment records
  inspection of all proof cases; this application does not retry
  authentication against current author/journal bytes.

The main unresolved gap is original finite B>=A. The present target
could supply two local different contributions to a normal-closure
repair, independently of the already-proved relative degree excess.
The continuation test is actual Galois completion, local-degree
divisibility and agreement of the absolute normalization. A failed
hypothesis would stop this application; an insufficient upper bound
alone would not refute the target. The following checks pass.

### Actual local degrees

Fix an arbitrary survivor, ordering o, prime p in {3,5} and actual
places v,w. L090 places G_o in the finite Galois field M/Q; its
normal closure C_o is the finite compositum of its Q-conjugates in
M. It contains T and is normal and separable over Q. Thus C_o/Q is
finite Galois, and the cited Galois correspondence gives C_o/T
finite Galois. This uses no Galois assertion for the literal G_o/T.

Let H=Gal(C_o/T). The cited completion theorem identifies

    Gal((C_o)_w/T_v) = D_w(C_o/T) subset H,
    [(C_o)_w:T_v]=|D_w(C_o/T)|.

The equality of groups here means the canonical restriction
identification for these actual compatible places. In particular
the local extension is finite Galois. Lagrange's theorem and L092
give the integer divisibility

    [(C_o)_w:T_v] divides |H|=[C_o:T]=2^12*3^2*5.

Consequently, writing n_p=v_p([(C_o)_w:T_v]),

    n_3<=2=v_3(C_0), n_5<=1=v_5(C_0).

The argument uses a decomposition subgroup of the actual global
Galois extension C_o/T. It neither infers divisibility from a
nonnormal global extension nor cancels the ambient order-two core
inside a local group. No equality of completions at distinct places
is used. The extra factor four in [C_o:T]/C_0 remains present;
it has zero valuation at both primes under consideration.

### Different specialization and normalization

Both T_v and (C_o)_w are finite extensions of Q_p. In Proposition
1.3(ii) set

    k_0=k_1=T_v, k_i=(C_o)_w.

The second extension is Galois by the preceding paragraph. The
first is the identity, whose ramification index is one and residue
extension is trivial, hence tame. This does not require T_v/Q_p
to be tame.

A uniformizer of any finite K/Q_p has absolute v_p-value
1/e(K/Q_p). Therefore the valuation of D_(K/Q_p)=m_K^(a_K)
is a_K/e(K/Q_p), exactly the source's absolute different order.
The source's d_i,d_0 and e_0 are respectively d_p((C_o)_w),
d_p(T_v) and e(T_v/Q_p). Its n_i is precisely the integer n_p
bounded above, not a relative different exponent. The imported
inequality thus gives

    d_p((C_o)_w)
      <= d_p(T_v)+n_p+1/e(T_v/Q_p)
      <= d_p(T_v)+v_p(C_0)+1/e(T_v/Q_p).

Every choice was arbitrary within the stated hypotheses, proving
both bounds for all the required survivors, orderings and actual
places. No calculation of exact differents or new ramification
theorem is needed: the only specialization is the actual field
tower, subgroup-order divisibility and substitution of the two
known prime exponents.

This establishes the approved local input using the checked known
methods. It does not repair the factor-four global relative excess,
prove the exact generation prescription for a repaired field or
assemble all source hypotheses. Authentication/current-version and
the def= boundary remain qualified. Other places, the height-selected
prime, independent initial data, native input/action/factorization,
pilot transport, essentiality and original finite B>=A remain open.
No complete-solution candidate is asserted.

### Separate critical audit — 2026-10-20, step381

**Scope and verdict.** The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-20-normal-closure-odd-bad-prime-different-critical-audit.md`.
The stated bounds pass without a mathematical correction or additional
direct input. This audit checks the complete L095 application against
the load-bearing tower and all-conjugate argument in audited L090,
the complete degree proof and audit in L092, and the reused primary
readings recorded in the application assessment. L094 is only a
precedent. The imported general theorems are not reproved.

**Actual embedded tower.** For each arbitrary L089 survivor, L090
places the full-coordinate field G_o inside the same finite Galois
M=Q(E[60]). This uses its actual pointed coordinate maps in both
directions and the original curve's full joint image. It also proves
Q(t_o)=Q(E[2])=T, so T is a subfield of G_o, not just an abstract
isomorphic field or a bound on the parameter degree. The complete
conjugate computation sends G_o to G_(sigma o) for every ambient
sigma and realizes every root permutation. Thus C_o is exactly the
compositum of all Q-conjugates in M, contains G_o and T, and is finite
normal and separable over Q. Milne FT 3.17 applies to give C_o/T
Galois. It does not require the intermediate T to be Galois over Q.
No old survivor, convenient root ordering or selected completion
has been substituted.

L090's complete kernels each have order eight and their full core
has order two, including both uniform scalar sectors. L092 uses
the actual product group, rather than independence of marginal
images, to obtain

    [M:Q]=96*48*480=2^14*3^3*5,
    [T:Q]=6, [M:C_o]=2,
    [C_o:T]=[M:Q]/(2*6)=2^12*3^2*5=184320.

These indices have the correct tower direction. In particular the
factor two for the core is used globally before forming the actual
extension C_o/T; it is not cancelled in any local group.

**Every actual completion and both allowances.** Fix p in {3,5},
an arbitrary v of T above p and w of C_o above v. The completion
embeddings are those induced by this extending pair. Milne ANT 8.10
identifies Gal((C_o)_w/T_v) with the subgroup of Gal(C_o/T)
stabilizing w, and its order is [(C_o)_w:T_v]. The global extension
is Galois by the preceding check, so the hypotheses of the completion
theorem hold; ANT 8.13 is consistent with this actual tower. Lagrange
therefore gives divisibility of the local degree by 184320, not just
an upper bound on it. Consequently

    v_3([(C_o)_w:T_v]) <= 2,
    v_5([(C_o)_w:T_v]) <= 1.

Separately, C_0=2*48*480=2^10*3^2*5, giving the required allowances
2 and 1. The quotient [C_o:T]/C_0=4 has zero exponent at both odd
primes, so these comparisons preserve the factor-four global excess
rather than removing it. No divisibility assertion for a nonnormal
extension, local equality across places or assumption on inertia is
used. The calculation covers every ordering because L090 and L092
establish the tower and degree for every one of them.

**The theorem's hypotheses and absolute normalization.** The reused
IV April 2020 Proposition 1.3(ii) reading includes the entire proof,
including the zero-degree-exponent case, p-group induction and
degree-p Kummer estimate. Its general-p statement allows the identity
intermediate. For the present actual fields set k_0=k_1=T_v and
k_i=(C_o)_w. These are finite extensions of Q_p; k_i/k_1 is Galois
by the completion check. The extension k_1/k_0 has ramification
index one and trivial residue extension, so is tame even when
T_v/Q_p is wild. Local degree one, and local degree prime to p,
are included in the cited theorem; no positive exponent is assumed.

For D_(K/Q_p)=m_K^(a_K), a uniformizer has absolute valuation
v_p equal to 1/e(K/Q_p), since v_p(p)=1. Thus the source's absolute
different order is exactly a_K/e(K/Q_p). Substitution identifies
d_i with d_p((C_o)_w), d_0 with d_p(T_v), e_0 with e(T_v/Q_p),
and n_i with the integer exponent of [(C_o)_w:T_v]. In particular,
the additive term is 1/e(T_v/Q_p), not the reciprocal of the
relative ramification index or of e((C_o)_w/Q_p). The imported bound
then gives, separately for each prime,

    d_3((C_o)_w) <= d_3(T_v)+2+1/e(T_v/Q_3),
    d_5((C_o)_w) <= d_5(T_v)+1+1/e(T_v/Q_5).

These are precisely the asserted sufficient upper bounds. No relative
different exponent is substituted for an absolute one, and no
sharpness, equality or attained lower bound is inferred.

**Limits and decision.** The audit certifies these two local inputs
by known methods, with no progress claimed beyond the checked sources.
It does not establish the complete different/conductor estimate of
IV 1.10, treat other primes, repair exact generation or resolve the
factor-four relative degree excess. The April reproduction's
authentication/current-version and def= qualifications, height-selected
prime, independent initial data, actual native input/action/factorization,
pilot and essentiality gaps remain. Original finite B>=A is open;
there is no complete-solution candidate. No mathematical script is
needed for the displayed exact factorizations. The audit supersedes
the overview's pending-audit wording without changing its mathematical
argument or L095's direct inputs L090 and L092.

## Mathlib

Full matching and supporting Mathlib coverage for this specialization
are unchecked. Unknown availability is not absence. The proof imports
the precisely cited different and Galois completion theorems and
uses ordinary Lagrange divisibility; no formal verification is claimed.
