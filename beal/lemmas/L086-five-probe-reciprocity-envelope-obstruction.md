# L086 — The five-probe reciprocity envelope does not certify redundancy

## Hypotheses

Use exactly L084's field D=K[theta], supported norm-square space W_S
and subspace T. In particular support comprises every maximal-ring
prime above 2 and 11, and no full-local Kummer condition at the
degree-ten eleven-adic base place is added to T. Retain L069's same
theta, L073's ordered entire eleven-adic algebras and L082's dyadic
algebras C and J. Thus the completions of D above these two primes are

    at 2:  C, J;
    at 11: (Q11,M), (Q11,M), (L,L,L),
    M=Q11(sqrt(-11)), L=Q11[r]/(r^10+55).

Use precisely the following elements of F=Q(t) inside D from L077:

    P={-1, v=-1/t, s=t+1, a=9-7t+5t^2, b=-4-8t-t^2},
    t^3-t^2+t+1=0, theta=8-14t+6t^2.

These are dual probes, not presumed elements of T. For a finite field
completion E of D write (u,c)_E in {+1,-1} for the quadratic Hilbert
symbol. Write 1 for the identity of a square-class group. Put

    epsilon_Q=[(1,-1)], epsilon_L=[(1,-1,-1)],
    I_prim={(1,1),(1,xi)},
    J11={(1,1,1),(epsilon_Q,epsilon_Q,epsilon_L)},

with xi exactly as in L082, and epsilon_Q and epsilon_L ordered as
in L085. No global square-class realization of a prescribed local
tuple is assumed.

## Conclusion

The five reciprocity equations below define a necessary envelope E
containing the combined dyadic and eleven-adic localization of T,
including its possible localized-class-group contributions. Nevertheless

    eta=((1,1); epsilon_Q,epsilon_Q,1) belongs to E,
    pr_11(eta)=(epsilon_Q,epsilon_Q,1) does not belong to J11.

All five equations at eta are certified exactly. Thus this fixed
five-probe sufficient certificate for loc_11(T) subset J11 fails.
This is not a certified class in T, a proof of nonredundancy, or an additional
independent global condition. The actual containment question remains
unresolved, as do the bounds 13+dim ker(n_S) and fourteen, rank and
positive primitive integer emptiness. No complete Beal candidate results.

## Proof

### Imported theorem and purpose of this specialization

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-17-primitive-eleven-global-comparison.md`.
We reuse its inspected source: J.S. Milne, *Class Field Theory*,
[version 4.03, 6 August 2020](https://www.jmilne.org/math/CourseNotes/CFTc.pdf),
III Theorem 4.4, pp.113–114 (Hilbert-symbol bilinearity and norm
criterion), V Theorem 5.3(a) and Example 5.4, p.179 (global product
formula), VIII 5.8 and its residue calculation, pp.246–247, and
5.10, p.247, with archimedean cases on p.248. All fields here contain
mu_2; the local fields have characteristic zero and D is a number
field. These named theorems are imported, not reproved.

For an odd residue cardinality q, writing u=pi^m u0 and c=pi^n c0
with units u0,c0, the cited residue formula for n=2 gives

    (u,c)=(-1)^(mn(q-1)/2) chi(u0)^n chi(c0)^(-m),

where chi is the quadratic residue character. The letter n in this
display is a valuation exponent, not the degree of the Hilbert symbol.
In particular two units pair to +1, and a unit with nonsquare residue
pairs with c by (-1)^ord(c). Bilinearity gives (1,c)=+1 at every
place, including dyadic ones. No formula for Q2 is applied to J.

The specialized work is checking every omitted place for general W_S,
then testing the exact local tuple against the five equations. L077's
primal rank-two test did not perform this dual comparison. Its prime
generators and the audited local images are reused, not recomputed.

### All omitted places contribute +1

Take any [z] in W_S, represented by z in D*, and c in P. L077
proves c and its inverse integral over Z[1/22]; consequently their
images in D are units at every maximal prime outside S_D. This uses
the actual field embedding and maximal rings, not a polynomial order.
L074 says ord_w(z) is even at each such prime, allowing negative
valuations. Divide z locally by a uniformizer to that even power,
which is a square. The resulting representative and c are units.
Every such place has odd residue characteristic. The residue formula
therefore gives (z,c)_w=+1. This applies to all W_S representatives,
not only S-units, so no ideal-class contribution has been discarded.

At each real place of K, L069 identifies the entire algebra with
R times C, with precisely one real factor. The localized element norm
of z is z_R times |z_C|^2. Since N_D/K(z) is a nonzero square in K,
its value there is positive. Therefore z_R>0 and is a real square.
The real Hilbert symbol is +1 regardless of the sign of c. At complex
places all elements are squares. This extends the sign argument to
all of W_S using its norm condition, not an assertion only about units.

The global product formula now gives, for every c in P,

    product over w above 2 or 11 of (z,c)_w = +1.       (1)

There are exactly the two plus seven factors displayed in the hypotheses;
all other finite and infinite factors have been justified separately.

### The precise necessary envelope

For y=(y_Q,y_M) at a rational eleven-adic base place set

    B_c(y)=(y_Q,c_Q)_Q11 (y_M,c_M)_M.

The two rational base places give the SAME localizations c_Q,c_M
because every probe lies in F, with its fixed t and theta, as L077
proves. For zeta=(z_alpha,z_beta,z_gamma) in (L*/L*^2)^3 put

    B_c^L(zeta)=product over i=alpha,beta,gamma of (z_i,c_i)_L.

For d=(d_C,d_J) define

    B_c^2(d)=(d_C,c_C)_C (d_J,c_J)_J.

All these symbols are well-defined on square classes. Define E to
consist of the tuples (d;y1,y2,zeta) satisfying exactly:

1. d in I_prim;
2. y1,y2 in {1,epsilon_Q};
3. zeta in the ENTIRE norm-square ambient group
   A_L={zeta: z_alpha z_beta z_gamma=1 in L*/L*^2};
4. for each of the five c in P,

       B_c^2(d) B_c(y1) B_c(y2) B_c^L(zeta)=+1.       (2)

By L082 the d choices have square norm in each base factor and
trivial rational dyadic component. L073 identifies each rational
eleven-adic full Kummer image as {1,epsilon_Q}, also of square norm.
For a class in T these are exactly the imposed local conditions of
L084; its norm-square condition implies membership of zeta in A_L.
Equation (1) proves (2). Hence loc_(2,11)(T) is contained in E.
We have not imposed the ramified full Kummer subgroup or presumed
that any independently chosen tuple globalizes.

This defines the full five-equation necessary envelope. To disprove
pr_11(E) subset J11 it suffices to exhibit one tuple and evaluate
every equation at that tuple; a matrix for its other elements is not
needed. In particular no unknown pairing against xi is needed if
the chosen d is identity.

### Exact five-probe witness

Set d=(1,1), y1=y2=epsilon_Q and zeta=(1,1,1).
The identity d is in I_prim. Both rational components are in the
required full images. Their norms are 1*N_M/Q11(-1)=1 because
[M:Q11]=2. The last component lies in A_L, with norm one. Thus
conditions 1–3 hold, retaining both dyadic and all seven eleven-adic
field factors.

At either rational eleven-adic base place,

    B_c(epsilon_Q)=(1,c_Q)_Q11 (-1,c_M)_M.

The first symbol is +1. The residue field of M is F11, where -1
is nonsquare. L077's exact ideals in O_F give
(s)=R above two, (a)=P above eleven, (b)=Q above eleven,
with P corresponding to M and Q to Q11. The elements -1 and v
are ordinary units. Since completion at P uses its maximal-DVR
valuation, the five values of ord_M(c_M) are respectively 0,0,0,1,0.
The residue formula therefore gives the complete table:

| Probe c | -1 | v | s | a | b |
| --- | --- | --- | --- | --- | --- |
| ord_M(c_M) | 0 | 0 | 0 | 1 | 0 |
| B_c(y1) | +1 | +1 | +1 | -1 | +1 |
| B_c(y2) | +1 | +1 | +1 | -1 | +1 |
| B_c^2(d) | +1 | +1 | +1 | +1 | +1 |
| B_c^L(zeta) | +1 | +1 | +1 | +1 | +1 |
| Full product in (2) | +1 | +1 | +1 | +1 | +1 |

The last two factors use identity in every component, so bilinearity
certifies their values in C, J and each of the three copies of L.
There is no uncomputed symbol on this witness. It follows that eta
belongs to E. This is an exact five-equation certificate, not a finite
precision sample or a conjectural dyadic-symbol calculation.

Finally L085 proves epsilon_Q and epsilon_L are nonidentity: -1 is
a nonsquare unit in M and L since both have residue field F11.
Thus (epsilon_Q,epsilon_Q,1) is neither the identity tuple nor
(epsilon_Q,epsilon_Q,epsilon_L). It is outside J11. The required
containment threshold fails even on the identity dyadic slice of E.

### Decision and limits

Stop this fixed five-probe sufficient certificate. This is an
informative NEGATIVE result, classified REPRODUCTION of the assessed
reciprocity method. It is local notebook progress on a mechanism,
not a new general theorem beyond the sources checked. No script is
needed: the exact ideal valuations, symbol formula and five products
give the entire relevant certificate above.

The localization of T could be strictly smaller than E and could
still be contained in J11. Conversely an actual class of T outside
J11 would prove independence, but eta is not such a class. Global
realization, unit/class completeness and integer lifting remain gaps.
Neither a larger probe family nor an affine or class-backend search
was attempted. The earlier stops and the different five-isogeny
survivor remain unchanged. The independent critical review below
confirms this obstruction only.

### Independent critical audit — 2026-10-17

Under the prior SPECIALIZE assessment
`drafts/literature/2026-10-17-five-probe-reciprocity-obstruction-audit.md`,
this audit accepts the stated obstruction without a mathematical
correction. It reuses the precise Milne results cited above and their
previously inspected proof cases. The task is verification of their
field-specific application, not a reproof of reciprocity or a new
global-class construction. No numerical or symbolic script is needed.

**Support and infinite places.** L074 defines W_S using element-square
norm and even normalized valuations at every prime outside the full
support above 2 and 11. Its definition permits negative valuations and
classes coming from localized ideal-class two-torsion. For each probe,
L077 proves both it and its inverse integral over Z[1/22]. Extension
to D therefore gives valuation zero at every such outside prime.
If ord_w(z)=2m, including m<0, replacing z by z/pi_w^(2m) preserves
its square class and leaves a unit. The odd-residue formula pairs
these two units trivially. This proves the outside contribution for
every W_S class, without representing it by an S-unit.

L069's entire algebra at each real base place is R times C. For an
arbitrary representative with N_D/K(z)=q^2, q in K*, evaluation gives
z_R |z_C|^2=q_R^2>0. Thus z_R>0 is a real square. This argument does
not require z to be a unit. All complex components are squares. Hence
every omitted infinite symbol is also +1. The global product theorem
over D consequently leaves exactly the two dyadic and seven
eleven-adic field factors in (1); no real sign or class contribution
is missing.

**Ordering and normalized probe valuations.** L077 proves O_F=Z[t]
and the exact maximal-prime identities

    (2)=R^3, (s)=R, (11)=Q P^2, (a)=P, (b)=Q.

The simple residue t=6 corresponds to Q and the double residue t=3
to P. Under theta=8-14t+6t^2 their residues are respectively 8 and 9.
Thus Q is L073's simple Q11 factor and P is its quadratic M factor,
with the same ordering as L085. Completion at P uses ord_P(a)=1,
not the rationally normalized value 1/2; ord_M(11)=2. The ordinary
units -1,v have valuation zero; (s)=R and (b)=Q are disjoint from P.
This independently checks all five table entries 0,0,0,1,0. Since
the probes lie in F, both rational embeddings of K induce the same
map on this entire cubic algebra, preserving theta and the simple
factor. Their probe valuations and symbols really are identical.

**Envelope inclusion.** By its definition in L084, T imposes the
full local image at both rational eleven-adic places and the primitive
dyadic subgroup at both dyadic places together. L073 gives the former
images as {1,epsilon_Q}: its exceptional point has unit residues
(1,10), so the odd-place square-root criterion identifies its class
with [(1,-1)]. L082 gives precisely I_prim at two. Finally element
norm commutes with localization; at the remaining base place the
entire cubic splits as L^3, so square norm means exactly that the
product of the three component classes is 1. These are conditions
1–3 defining E. Together with (1) they prove loc_(2,11)(T) subset E.
There is no full-local Kummer requirement at that remaining place
in T, and none has been inserted in this inclusion.

**Complete witness verification.** Identity dyadic components satisfy
I_prim and have square norm in both base factors. At either rational
eleven-adic base place, epsilon_Q has norm
1 times N_M/Q11(-1)=(-1)^2=1. The three identity L components also
have product one. Thus all ambient and imposed local memberships
hold for eta before reciprocity is tested.

The nonzero squares of F11 are 1,3,4,5,9, so -1 is nonsquare.
For any probe c, the odd-residue formula with the unit first argument
-1 gives (-1,c_M)_M=(-1)^ord_M(c_M); its other valuation is zero,
so there is no sign or unit-residue term left. The five rational-place
values are consequently +1,+1,+1,-1,+1 at EACH of the two base places.
Their pairwise products are five +1 values. Each of the five dyadic
products is (1,c_C)_C (1,c_J)_J=+1, and each ramified eleven-adic
product is the product of three identity symbols, also +1. This
checks every symbol used at eta. In particular no pairing with xi
or formula for a ramified dyadic field is required by this witness.

The field L has residue F11 by L073, so -1 is nonsquare in L as
well as in M. Hence epsilon_Q and epsilon_L are both nonidentity.
The tuple (epsilon_Q,epsilon_Q,1) differs from the identity in its
first two entries and from J11's other element in its last entry.
This proves pr_11(E) is not contained in J11.

**Logical limit and decision.** Since only loc_(2,11)(T) subset E
has been proved, an element of E outside J11 neither supplies a
global class nor refutes loc_11(T) subset J11. The wording in the
conclusion is clarified to say that eta is not a *certified* T-class;
no impossibility of its globalization is asserted. The audit confirms
the failure of this fixed sufficient certificate and leaves actual
redundancy, independence and both dimension bounds unchanged.
ATTEMPTS/038 remains stopped. The seven direct DAG inputs are exactly
those stated; no additional theorem input or complete Beal candidate
is produced. This is REPRODUCTION of the assessed application, with
no claim of progress beyond the cited general theorems.

## Mathlib

Full matching field-specific envelope obstruction: **not checked**.
Supporting Hilbert symbols, global reciprocity, completion norms and
square-class localization: **not checked**. Unknown coverage is not
evidence of absence; no Lean verification is claimed.
