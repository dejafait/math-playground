# L099 — All-support q-order coprimality over the actual normal closure

## Hypotheses

Retain the same arbitrary L089 survivor E/Q, fixed c,h,d_*,e_*,
both domains and algebraic closure, and all six L090 ordered-root
models. Use audited L092 and L098 in precisely this setting. For
any ordering o the unchanged fields and curve are

    T=Q(E[2])=Q(t_o), E_o: V^2=X(X-1)(X-t_o),
    G_o=T(iota,E_o[15]), iota^2=-1, C_o=G_o^nor over Q.

Division fields contain both coordinates of every geometric torsion
point. In particular j(E_o)=j(E) is a nonzero rational number. Put

    S={rational primes p : v_p(j(E))<0},
    n_p=-v_p(j(E)) for p in S, with v_p(p)=1.

Retain the explicit L098 hypothesis that ell>=7 is prime and
v_ell(j(E))>=0. No assertion about the actual height-selected prime
is assumed or proved. For every actual w|p of C_o, write
K_w=(C_o)_w, e_w=e(K_w/Q_p), and ord_w for the surjective integer
valuation on K_w. At p in S define h_w to be the curve's local
height in GenEll Definition 3.3/Remark 3.3.1, using ord_w downstairs.
This is the integer q-order convention being tested, not the order
at a place of the subsequent ell-division field.

## Conclusion

For every survivor, ordering, p in S and actual w|p,

    h_w=-ord_w(j(E_o))=e_w n_p is a positive integer,
    ell does not divide e_w.                              (1)

Consequently the following statements are equivalent:

    gcd(ell,h_w)=1 for every p in S and every actual w|p of C_o;
    ell does not divide n_p for every p in S.              (2)

This is a known-method specialization, not a result beyond the sources
checked. It isolates an arithmetic prerequisite for a possible
normal-closure repair. It establishes neither condition in (2) for
the actual height-selected ell, nor its j-integrality, full native
initial data, a complete repair or an essential IUT flaw. Original
finite B>=A remains open. Separate critical audit is pending.

## Proof

### Imported results and bounded test

The invocation-start assessment is
`drafts/literature/2026-10-21-normal-closure-all-support-q-orders.md`
(SPECIALIZE), with exactly the target (2). Its inspected primary
coverage and earlier complete readings are reused; no additional
retrieval or authentication is needed for this specialization.

Import S. Mochizuki, *Arithmetic Elliptic Curves in General Position*,
Math. J. Okayama Univ. 52 (2010), 1–28,
[local setup pp.16–17, Definition 3.3 and Remark 3.3.1, p.17](https://www.math.okayama-u.ac.jp/mjou/mjou52/_01_mochizuki.pdf).
With the local valuation surjective onto Z, the split height is the
order of the Tate parameter. For a potentially multiplicative curve,
the height can be computed over a finite split extension and divided
by that extension's ramification index; it is independent of that
choice. This is a curve height, not a point's canonical local height.

Import J. Silverman, *The Arithmetic of Elliptic Curves*, second
edition (2009), [C Theorem 14.1(b,d), p.445](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf),
and K. Kedlaya, *Introduction: the Tate curve*, fall 2004,
[equation (3), p.2 and Theorems 1–2, pp.3–4](https://kskedlaya.org/18.727/tate-curve.pdf).
For a finite Q_p-extension and nonintegral j there is a positive-
valuation geometric Tate parameter. Split multiplicative reduction
gives the pointed Tate isomorphism over the base; nonsplit
multiplicative reduction becomes split over an unramified quadratic
extension. The Tate j-series converges and has integral coefficients:

    j(q)=q^(-1)+744+sum_(m>=1) c_m q^m, c_m in Z.          (3)

These theorems, including convergence and the splitting assertion,
are imported without reproof. The valuation application of (3) to
the present actual local curves is checked below.

Import J. S. Milne, *Algebraic Number Theory*, v3.08 (19 July 2020),
[Theorem 3.34, pp.59–60; Corollary 7.42 and Remark 7.43, p.124](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
and Exercise 4-2, p.83 with solution p.155: in a Galois number-field
extension the global degree is efg; integer valuations restrict with
factor e in finite local extensions, and ramification indices multiply
in towers. No tameness hypothesis is required.

The main gap is original finite B>=A. The intermediate target tests
whether the all-place native q-order predicate introduces anything
beyond rational pole-order avoidance in this proposed field repair.
Continue only with the actual downstairs normalization, prime-to-ell
ramification and both quantified directions. A conflicting case would
refute (2); an unproved premise would leave the attempt incomplete.
L061/L084 concern other fields and are method comparisons only.
L098 classifies reduction but does not compute these heights. The
parked authentication/reapproval route in ATTEMPTS/035 is not reopened.

### Height at an arbitrary actual place, including nonsplit reduction

Fix a survivor and an ordering, then p in S and an arbitrary w|p of
C_o. The actual K=K_w is a finite extension of Q_p, complete and
discretely valued with finite residue field. By L098 the unchanged
E_o/K has multiplicative reduction. Its j-invariant is the image of
the same rational j(E), with negative valuation. These facts verify
the local Tate theorem's hypotheses in every possible residue
characteristic here; no splitness over K is inferred from L098.

Take L=K if the reduction is split, and otherwise take the cited
unramified quadratic splitting extension L/K. There is a pointed
L-isomorphism E_o -> Tate(q) for a parameter q with ord_L(q)>0,
where ord_L is the surjective integer valuation. Its j-invariant
therefore equals the image of j(E_o). In (3), the constant 744 is
integral and ord_L(c_m q^m)>=m ord_L(q) tends to infinity. Thus the
whole convergent remainder after q^(-1) lies in the closed ring O_L.
The leading term has strictly negative order -ord_L(q). The
nonarchimedean valuation rule for summands of unequal orders yields

    ord_L(j(E_o))=-ord_L(q).                              (4)

In particular this step uses the entire convergent remainder, not a
finite numerical truncation or an assertion of dominance without a
tail bound. Apply the cited height convention over this actual split
extension, and restrict integer valuations through L/K and K/Q_p:

    h_w=ord_L(q)/e(L/K)
       =-ord_L(j(E_o))/e(L/K)
       =-ord_w(j(E_o))
       =-e_w v_p(j(E))=e_w n_p.                         (5)

The rational number j(E) is nonzero, so n_p is a positive integer
for p in S; e_w is a positive integer. Hence (5) proves that the
downstairs height is a positive integer. In the nonsplit case the
chosen extension has e(L/K)=1, but formula (5) already keeps the
normalization explicit. Neither a quadratic degree factor nor a
valuation from an ell-division-field completion is inserted. The
height's extension independence ensures that this is the stated
native convention, rather than a choice-dependent split height.

### Prime-to-ell ramification and both quantified implications

C_o is the normal closure over Q of the number field G_o in the
fixed characteristic-zero algebraic closure. Thus C_o/Q is finite
Galois. Audited L092 gives, for every ordering of this same member,

    [C_o:Q]=1105920=2^13*3^3*5.                          (6)

At the actual w over any p, the imported Galois formula gives
[C_o:Q]=e_w f_w g_p, with f_w the residue degree and g_p the number
of places above p. Consequently e_w divides (6). Since ell>=7 is
prime, ell divides none of 2,3,5, so ell does not divide e_w. This
uses Galoisness of C_o/Q, not a degree-divisibility assertion for the
nonnormal literal G_o. It imposes no tameness condition at p.

If ell divides no n_p, then at every p in S and every actual w|p,
(5), primality of ell and ell not dividing e_w give ell not dividing
h_w. This proves the second-to-first implication in (2), with its
full all-place quantifier.

Conversely suppose the first statement of (2). Fix any p in S.
There exists at least one place w of the number field C_o above p,
by the prime decomposition theorem used in the imported degree
formula. If ell divided n_p, (5) would make ell divide h_w, contrary
to the assumption at this actual place. Thus ell does not divide
n_p. As p was arbitrary, the second statement of (2) follows.
In fact a divisible n_p would fail the test at every w|p; existence
of one such place suffices to exclude vacuity in the reverse direction.
The argument was uniform in the survivor and each of its six orderings.

### Qualifications and remaining gap

The bounded mathematical test passes with no changed hypothesis. The
extra ell-integrality assumption is retained from the approved scope:
L098 uses it to exclude ell from S. The local formula and coprimality
argument do not turn it into a conclusion about a height-selected
prime. No choice of ell is made here, and neither avoidance condition
in (2) is asserted for that prime. Rational pole orders at other
members' places are not bounded or replaced by the retained order 30
at three. No prime-seven substitution is used.

The native predicate comparison retains the IUT I May 2020
[reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf),
Definition 3.1(b),(c), pp.61–62, and its all-base-field-place
quantifier. This does not authenticate current author/journal bytes
or establish all initial data for C_o. L092's factor-four relative
degree excess, exact generation/field repairs, full selected/theta
data, April IV authentication and def= boundary, native input/action,
all-image factorization, pilot transport and essentiality remain
unresolved. No complete-solution candidate is proposed.

## Mathlib

Full matching and supporting Tate-curve/native-height/Galois
ramification coverage have not been checked in this step. The earlier
assessment's supporting ramification-tower identity is not a full
matching theorem for (1)–(2). Unknown coverage is not absence. This
is an informal REPRODUCTION using the cited general results and
explicit specialization checks, without formal verification or a
mathematical script.
