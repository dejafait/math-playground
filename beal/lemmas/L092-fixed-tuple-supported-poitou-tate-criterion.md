# L092 — Complete supported duality criterion for the fixed eleven-adic tuple

## Hypotheses

Use L069's entire fields K and D=K[theta], where

    g(X)=X^3-4X^2-160X-1264,     [D:K]=3.

Use L074's maximal-ring support S_F consisting of ALL primes above
2 and 11 for F=K,D, and its spaces

    H_{F,S}={ [a] in F*/F*^2 : ord_p(a) even for p outside S_F },
    W_S=ker(N_D/K:H_{D,S} -> H_{K,S}).

There is no sign condition in H_{F,S}. All valuations are normalized
maximal-DVR valuations, allowing negative values. Retain L084's exact
subspace T, without a full Kummer condition at the degree-ten base
place above eleven. Use L073/L082's entire ordered completion algebras:

    K tensor Q2 = Q2 x H,       D tensor Q2 = C x J,
    K tensor Q11 = Q11 x Q11 x L,
    D tensor Q11 = (Q11 x M) x (Q11 x M) x (L x L x L),
    H=Q2(pi), pi^11=2, C=Q2[theta], J=H[theta],
    M=Q11(sqrt(-11)), L=Q11[r]/(r^10+55).

At each rational eleven-adic base place the first factor is the simple
root factor and the second is M. Write w_1,w_2 for the two distinct
primes of D giving these ordered M completions. Their residue field
is F11. Fix exactly L086's tuple

    eta=((1,1); epsilon_Q,epsilon_Q,(1,1,1)),
    epsilon_Q=[(1,-1)].

Complete this tuple by the identity at EVERY infinite place of D;
call the completed tuple eta_infty. In particular both real signs
are positive. No global realization or complete dual basis is assumed.

## Conclusion

The following three statements are equivalent:

1. There exists b in T whose entire localization above 2 and 11 is eta.
2. For every [c] in the FULL group H_{D,S},

       product_{w in S_D union S_infty(D)} (eta_infty,w,c)_w = +1.

3. The linear functional on H_{D,S} given by

       lambda([c])=ord_{w_1}(c)+ord_{w_2}(c) mod 2

   is identically zero.

Thus this is an exact criterion for THIS tuple, including supported
nonunit classes and every infinite place. It is not an evaluation of
lambda on the full group. Its five previously tested values vanish
by L086, but their sufficiency is not asserted. Neither realization
nor failure of realization is established. The bounds dim T<=13+k_S
and the supported-unit upper bound fourteen are unchanged, where
k_S=dim ker(n_S) is L084's localized class-norm kernel dimension;
even 13+0 exceeds the threshold eleven. The class kernel, rank and
integer lifting remain unresolved. This is a REPRODUCTION application
of known duality, not
a new general duality theorem or a Beal resolution.

## Proof

### Imported theorem and why a specialization is needed

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-eleven-poitou-tate-specialization.md`.
Its exact-target discovery, primary proof-case reads and comparison
with ATTEMPTS/038 and /040 are reused. We import J.S. Milne,
[*Arithmetic Duality Theorems*, second edition, 2006](https://www.jmilne.org/math/Books/ADTnot.pdf),
I.4, definitions on printed pp.48-49 and 55-56, Theorem 4.10(b),
pp.56-57, with Lemmas 4.12-4.13 and the finite-module/real-place
proof on pp.58-62. For a number field E, all infinite places in S,
and a finite G_S-module A of order invertible in O_{E,S}, its local
H^1 stage is exact against the full dual global H^1. We use its
local Tate pairings, not a reproof of that theorem. Finite S is
permitted for a finite module; cofinite S is not required.

Here E=D and S=S_D union S_infty(D). L069 proves D is a number
field. Take A=mu_2. It is constant over D and has order two, a unit
in O_D[1/22]. Its dual Hom(mu_2,bar(D)*) is the constant order-two
module, identified with mu_2 by the nontrivial character and -1.
This identifies the local H^1 pairing with the quadratic Hilbert
symbol. For finite S the local restricted product is the ordinary
finite product. At real places H^1 in the theorem is Tate H^1;
in degree one this agrees with ordinary H^1, namely R*/R*^2.
Complex H^1 is zero. Thus real signs are part of the localization
problem, even though their prescribed value here is the identity.

We also reuse J.S. Milne, [*Class Field Theory*, v4.03, 6 August 2020](https://www.jmilne.org/math/CourseNotes/CFTc.pdf),
VII Appendix A.1-A.5, printed pp.226-227, for Kummer classification
and the unramified unit implication; and III Theorem 4.4,
pp.113-114, VIII 5.8-5.10, pp.246-248, for the Hilbert-symbol
identification and odd-residue valuation formula, as applied in
L086. The remaining specialization is to verify support, signs and
the effect of L074's cubic scalar correction on every fixed class.
No extra source discovery or new arithmetic search is used.

### Supported Kummer identification in both directions

Kummer theory identifies H^1(G_D,mu_2) with D*/D*^2: the class of
a corresponds to D(sqrt(a))/D, allowing the trivial extension.
Because mu_2 is constant, inflation identifies H^1(G_{D,S},mu_2)
with the characters whose extensions are unramified at every finite
w outside S_D. We verify that this is precisely H_{D,S}.

If ord_w(a)=2m, write a=varpi^(2m) u in D_w with u a unit.
Dividing by the displayed square reduces the local Kummer extension
to that of u. Since w is not dyadic, 2 is invertible there and the
cited unramified unit theorem applies. Hence the extension is
unramified at w, including the split case. This argument permits
m negative and imposes no principal-ideal or S-unit hypothesis.

Conversely, if ord_w(a) is odd, a square root cannot belong to an
unramified extension of D_w: its normalized valuation there would
have to be ord_w(a)/2, a noninteger, whereas ramification index one
preserves the integer value group. In particular the quadratic
extension cannot be unramified or split. This proves the converse
and the full identification

    H^1(G_{D,S},mu_2)=H_{D,S}.

The same identification applies to the dual constant module. No
restriction to S-unit classes or removal of localized class-group
contributions has occurred.

### Exact localization before imposing the D/K norm

Apply Theorem 4.10(b) with these verified hypotheses. Its exactness
at the local H^1 product says that eta_infty has a supported global
lift [a] in H_{D,S} if and only if it annihilates every class in
the dual H_{D,S}. Local Tate invariants add; their exponentials
are the Hilbert symbols in statement 2, so vanishing is exactly
the displayed product being +1. This uses the full dual group,
not five selected elements. For finite S the image is the actual
image in this finite product, not merely its closure.

Every W_S class has identity at infinity. Indeed L069 gives D
over each real place of K as R x C. If N_D/K(b) is a square, then

    b_R |b_C|^2 > 0,

so b_R>0. There are two such real places and all other factors
are complex. Thus completing eta by positive signs is necessary
for a lift in T, and no unspecified real component was dropped.

### Norm correction preserves support and every prescribed class

Suppose statement 2 holds and choose the supported lift [a] just
obtained, represented by a in D*. Put

    n=N_D/K(a) in K*,       b=a/n in D*.

This is L074's scalar-norm correction on square classes. We verify
it without assuming that n is globally square. For a prime v of
K outside S_K, every prime w above v is outside S_D, whence

    ord_v(n)=sum_{w|v} f(w/v) ord_w(a)

is even. Scalar extension gives ord_w(n)=e(w/v)ord_v(n), also
even. Therefore ord_w(b) is even outside S_D and [b] is supported.
This checks the effect on arbitrary supported nonunit lifts.
Since [D:K]=3,

    N_D/K(b)=n/n^3=n^(-2),

an actual square in K*. Consequently [b] belongs to W_S.

At every prescribed base completion, norm commutes with localization
on the ENTIRE local algebra. The local class of n is the norm of
the corresponding prescribed tuple. Check the base factors separately:

* At the rational dyadic base place the complete factor is C and
  its prescribed class is 1, so its norm to Q2 is square.
* At the degree-eleven dyadic base place the complete factor is J
  and its prescribed class is 1, so its norm to H is square.
* At EACH of the two rational eleven-adic base places the prescribed
  class is (1,-1) in Q11 x M. Its norm class is
  [1*N_M/Q11(-1)]=[(-1)^2]=1.
* At the degree-ten eleven-adic base place the complete algebra is
  L^3 with class (1,1,1), whose product norm is 1.

Thus n is square in each of these five base fields. Its scalar
image is square in EACH field component above them: both dyadic
components, both Q11 factors, both M factors and all three L
factors. Division by n preserves every ordered component of eta.
No identification or ordering has changed.

At either real base place the lift has a_R>0, by eta_infty's
prescribed sign, and its complex component has positive norm.
Hence n_R=a_R|a_C|^2>0, a real square. Division again preserves
the positive real class. All complex classes are trivial. This
checks the prescribed infinite classes independently of the
already proved square global norm of b.

Finally loc_2([b])=(1,1), which belongs to L082's I_prim. Its
rational dyadic projection is the identity full Kummer class.
At both rational eleven-adic places the class epsilon_Q belongs
to the full Kummer image, as certified in L086 using L073.
These are exactly L084's defining local conditions for T; there
is no additional full-local requirement at L. Thus [b] belongs
to T and realizes eta, proving 2 implies 1. Conversely a class
as in 1 is already a supported lift of eta_infty by the sign
argument. The imported exactness proves 1 implies 2.

### Reduction of the full obstruction to the stated functional

For any supported dual [c], all symbols in statement 2 except
the two M symbols are +1 because eta_infty has identity there.
At M the residue cardinality is 11 and -1 is a nonsquare unit.
The odd-residue Hilbert formula cited above therefore gives

    (-1,c)_M=(-1)^ord_M(c).

This holds also for negative valuations: its first argument has
valuation zero, so neither the sign term nor the residue-unit
part of c contributes. Taking the product at w_1,w_2 proves
that statement 2 is exactly statement 3. Multiplying c by a
global square changes each valuation by an even integer; lambda
is a well-defined F2-linear functional on the full supported group.

### Relevance, stopping test and qualifications

The approved intermediate threshold was an exact criterion with
support, signs and all local classes preserved, or a precise failed
hypothesis. The criterion is established. Evaluating lambda on the
complete H_{D,S} is a separate missing arithmetic step; vanishing
on L086's five probes is insufficient. In particular neither weak
approximation nor a local-global square-norm assumption was used.
The correction proves norm-square sufficiency for a hypothetical
supported lift, not the existence of that lift.

If an independently certified full evaluation gives lambda=0,
the criterion would produce a T-class outside L085's J11; a
certified c with lambda(c)=1 would instead rule out this fixed
tuple only. Neither finding is supplied here. Even realization
would not by itself identify the supported-unit contribution,
compute the class kernel, reach dimension eleven or lift to a
primitive integer solution. Evaluation remains parked, and the
stops in ATTEMPTS/034-041 are preserved. No new probes, basis
search, backend availability check or mathematical script is needed
for this theorem application. The separate critical application audit
below confirms the criterion without evaluating it.

### Independent critical application audit — 2026-10-18

The pre-existing SPECIALIZE audit assessment is
`drafts/literature/2026-10-18-fixed-tuple-poitou-tate-audit.md`.
The audit finds no defect in the equivalence. It reuses the canonical
field and local-image inputs, rather than claiming to rerun their
arithmetic certificates. The following checks concern precisely the
specialization and both directions of L092.

**Exactness and support.** Milne ADT I.4, Theorem 4.10(b), printed
pp.56–57, gives image equal to kernel at local H^1. Its definitions
on pp.55–56 and finite-module proof on pp.59–62 were checked directly.
Here the module is finite of order two, every dyadic prime is in S,
and the dual is again the constant order-two module. The finite-module
alternative of Lemma 4.13 applies; its cofinite-S alternative is not
needed. Neither a vanishing Sha group nor class-number information is
a hypothesis of the local-H^1 exactness used here. The finite product
of local square-class groups has no image-versus-closure ambiguity.

For clarity, the unit implication in the support identification can
also be applied exactly in CFT VII A.5's number-field formulation.
At any maximal prime w outside S, choose an element varpi of D with
ord_w(varpi)=1 (an element of the maximal ideal outside its square
suffices). If ord_w(a)=2m, then u=a/varpi^(2m) is in D and is a
unit at w. The Kummer extensions defined by u and a agree; 2u is
a unit at w, so A.5 applies. This works for m<0 as well. Conversely,
an odd valuation would give a half-integral value to a square root
in an unramified extension, which is impossible. Thus the source
identifies the full H_{D,S}, not only its S-unit subgroup, on both
sides of duality. No extra support was introduced by the choice of
varpi: it is used only to identify the same quadratic extension.

**Real places and necessity.** L069 gives two real base places,
with entire algebra R times C at each, and no further real factors.
For b in W_S, write N(b)=q^2 with q nonzero. At either such place,
b_R |b_C|^2=q_R^2>0 forces b_R>0. Consequently every candidate in
T already has the two prescribed identity real classes. Tate H^1
at a real place agrees with ordinary H^1 and retains its sign; the
complex terms are zero. A T-class with the prescribed finite tuple
therefore is a lift of exactly eta_infty, so exactness proves the
necessary annihilation of every supported dual class, regardless of
the signs of that dual class. Real terms vanish because the first
argument is positive, not because the dual classes are assumed positive.

**Sufficiency and component preservation.** Conversely exactness gives
some supported a with the full eta_infty localization. There is no
reason for N(a) to be globally square, and none is used. With n=N(a),
the element b=a/n has norm n^(-2). For every v outside S_K, each
summand f(w/v) ord_w(a) in ord_v(n) is even. Scalar extension
multiplies this even value by e(w/v), so division by n keeps support,
including for negative valuations and nonprincipal ideal-square lifts.

Check the five base completions separately. At Q2 and H the prescribed
cubic classes are identities. At each of the two Q11 places, the
norm of (1,-1) is 1 because M has degree two. At L the product of
the three identity classes is 1. Thus n is square separately in
Q2, H, both Q11 completions and L. Its scalar image is consequently
square in C, J, each of the two simple-root Q11 factors, each of
the two M factors and each of the three ordered L factors. This
checks all nine finite components; multiplication by this scalar
does not permute or identify any factors. At each real place n is
positive because a has its prescribed positive real sign. The
correction therefore also preserves both real classes.

The corrected class lies in W_S and has identity in both dyadic
factors, hence lies in L082's I_prim. The rational dyadic full-image
condition is automatic. At each rational eleven-adic place L073's
exceptional two-torsion image has first entry a square unit and
second entry a nonsquare unit, so its class is precisely (1,-1).
Those are the remaining two full-image conditions in L084. There
is no full-image condition at L in T. Thus sufficiency reaches
exactly T, with no extra local or global premise.

**The entire obstruction functional.** At every component except the
two ordered M factors the first Hilbert-symbol argument is identity.
For M, the residue field is F11 and -1 is a nonsquare unit. CFT
VIII 5.8 therefore gives (-1,c)_M=(-1)^ord_M(c) for every nonzero c,
including units and elements of negative valuation. The exponent is
the maximal-DVR valuation in M; replacing it by v11 would be wrong
because ord_M(11)=2. The two factors multiply to (-1)^lambda(c).
Their primes are distinct and there is no reason to assume their
values equal on an arbitrary element of H_{D,S}. Invariance under
global squares and additivity of valuations prove that this is the
stated linear functional on the entire group.

The audit thus confirms both implications and the exact functional
without correction. It supplies no evaluation beyond L086's probes,
no supported lift, no additional removed direction and no complete
Beal candidate. In particular its confirmed criterion leaves
dim T<=13+k_S and the unit upper bound fourteen unchanged. This is
verification of the existing application of known results, not a new
mathematical result beyond the assessed sources. No new mathematical
script or certificate rerun was needed.

## Mathlib

The full field-specific criterion and supporting Poitou-Tate, Kummer,
Hilbert-symbol, completion-norm and supported-square-class results:
**not checked**. Unknown coverage is not absence. No Lean verification
or independent reproof of the imported duality theorem is claimed.
