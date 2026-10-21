# L090 — Six-label involutions and eight-label cyclic reconstruction

## Hypotheses

Use L089's setting and notation exactly: F=F_(97^20), H the
order-sixteen subgroup of F_97^*, a bijection h:Z/16Z -> H,
unshifted v_i=(1,h(i),...,h(i)^7)^transpose, blocks
B_s={s,s+1,s+4,s+6}, and the full alternating kernel K.
The nonzero circuit coefficients d_(t,i), block coefficients w_(s,i)
and vectors r_s are precisely those defined in L089. Indices are
modulo sixteen. No actual errors, original chart or parameters are
assumed. In the necessary conclusions below assume K!=0.

## Conclusion

For every t put

    a=h(t-1), b=h(t), c=h(t+4),
    d=h(t+6), e=h(t+8), f=h(t+9).

These six labels are distinct. They obey the denominator-free condition

    det [[ab, a+b, 1],
         [cf, c+f, 1],
         [de, d+e, 1]] = 0.                              (1)

Equivalently, there is a unique nonidentity projective involution
phi_t of P^1(F_97) exchanging a with b, d with e, and c with f.
It is already determined by the first two pairs. Explicitly put

    A=a+b-d-e,    B=de-ab,
    C=ab(d+e)-de(a+b).

Then AC-B^2!=0 and

    phi_t(z)=(-Bz-C)/(Az+B).                              (2)

In particular, c determines f uniquely; a pole or an image outside
H, or a repeated label, prevents a bijective solution.

More strongly, the restriction of h to

    J={0,1,4,6,7,8,11,15}

determines the entire labeling whenever K!=0. The eight reconstruction
steps in the proof use only (1), and apply to every labeling satisfying
these sixteen necessary determinant equations. The other two
shared-coordinate gates in each L089 triangle remain unproved for a
reconstructed candidate. No surviving labeling or uniform contradiction
is supplied. Rank R=2 remains possible; the desired uniform threshold
is rank R>=3. There is no actual-error application, arbitrary-family
bound or change to the global interval 11/q–16/q.

## Proof

### Scope, prior comparisons and the circuit-window identities

The direct input is audited L089, including its three necessary
shared-coordinate equations. Its L010/L087/L088 inputs and unshifted
conventions are retained. The ready EXPLORE assessment
`drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`
covers this analytic pass on the unchanged full-kernel target.
No new external result is imported. The elementary involution calculation
also occurs in L036 for a different actual-error branch; that branch's
theorem and hypotheses are not used here. The calculation below is
included to justify the changed six-label specialization and every
possible pole. No general involution or shortening theorem is reproved.

Let T_t={t,...,t+8} as in L089. On T_t intersect T_(t-1), cancellation
of the eight-factor products defining the d coefficients gives

    d_(t-1,i)/d_(t,i)
        =(h(i)-h(t+8))/(h(i)-h(t-1)).                    (3)

On T_t intersect T_(t+1) it similarly gives

    d_(t+1,i)/d_(t,i)
        =(h(i)-h(t))/(h(i)-h(t+9)).                      (4)

Every index used below belongs to the stated intersection. All label
differences and d coefficients divided by are nonzero by bijectivity;
these formulas hold also when the windows wrap modulo sixteen.

### The third shared-coordinate gate involves only six labels

Use L089's third gate, distinguishing its triangle scalars by a script
letter here:

    scriptA w_(t,t+6)+scriptC w_(t+2,t+6)=d_(t,t+6),
    scriptA=d_(t,t),
    scriptC=d_(t,t+3)/w_(t+2,t+3).                       (5)

From the definition of w, the first term divided by d_(t,t+6) is

    [d_(t,t+4)/d_(t,t+6)]
       [d_(t-1,t+6)/d_(t-1,t+4)]
      =(d-e)(c-a)/((d-a)(c-e)),                         (6)

by (3). For the second term, the final ratio in w_(t+2,t+3) gives

    w_(t+2,t+3)/w_(t+2,t+8)
       =d_(t,t+3)/d_(t,t+8).

The middle ratio in the same block's definition gives

    w_(t+2,t+8)/w_(t+2,t+6)
       =d_(t+1,t+8)/d_(t+1,t+6).

Consequently scriptC w_(t+2,t+6), divided by d_(t,t+6), is

    [d_(t,t+8)/d_(t,t+6)]
       [d_(t+1,t+6)/d_(t+1,t+8)]
      =(d-b)(e-f)/((d-f)(e-b)),                         (7)

by (4). Thus (5) is equivalent, for any bijective labeling, to

    (d-e)(c-a)/((d-a)(c-e))
      + (d-b)(e-f)/((d-f)(e-b)) = 1.                    (8)

Only the third gate was used. In particular the simplification assumes
neither of the other two gates nor rank two as an additional premise.
K!=0 implies (5) through L089, hence implies (8).

Subtract the first term in (8) from one. Its numerator simplifies to
(a-e)(d-c), with denominator (d-a)(c-e). Multiplying the resulting
equality by its proved nonzero denominators and changing both signs
involving e gives

    (d-a)(d-b)(e-c)(e-f)
      =(e-a)(e-b)(d-c)(d-f).                            (9)

For P(X)=(X-a)(X-b) and Q(X)=(X-c)(X-f), the left side minus
the right side is P(d)Q(e)-P(e)Q(d). Direct expansion is

    P(d)Q(e)-P(e)Q(d)
      =(d-e) det [[ab,a+b,1],[cf,c+f,1],[de,d+e,1]].

Since d!=e, (9) is equivalent to (1). This proves the necessary
determinant condition without introducing a zero-denominator branch.

### The exact involution and its finite-label gates

The two rows (ab,a+b,1) and (de,d+e,1) are independent: proportionality
would, from their last entries, give equality of their sums and products,
so the monic quadratics with root sets {a,b} and {d,e} would coincide.
Those root sets are disjoint. Their cross product is precisely (A,B,C)
in the statement, so this vector is nonzero and is their unique
projective kernel vector over F_97. Condition (1) is equivalent to

    A cf+B(c+f)+C=0.                                    (10)

We must check invertibility before using a fractional linear map.
If AC-B^2=0 and A=0, then B=0; the equation for the pair (a,b)
would force C=0, a contradiction. If A!=0, the pair equation
Axy+B(x+y)+C=0 factors as

    (Ax+B)(Ay+B)=0.

Both disjoint pairs {a,b} and {d,e} would have to contain the same
label -B/A, again impossible. Therefore AC-B^2!=0.

The matrix [[-B,-C],[A,B]] is invertible, has square
(B^2-AC)I, and is not scalar: a scalar matrix would require A=C=0
and -B=B, which forces B=0 in characteristic 97. Thus (2) defines
a nonidentity projective involution. Each pair equation forces
phi_t(x)=y: if Ax+B=0, that equation would also give Bx+C=0,
contradicting AC-B^2!=0. This verifies all paired finite denominators.
The same argument applies to (10). Conversely an involution (2)
exchanging the first two pairs exchanges c,f exactly when (10) holds.

For completeness uniqueness among all nonidentity projective involutions
does not add a hypothesis. An invertible nonscalar matrix N representing
one has N^2=kI. For a two-by-two matrix, direct multiplication gives
N^2-tr(N)N+det(N)I=0. If tr(N)!=0 these identities make N scalar.
Hence tr(N)=0, and N has the form [[-B',-C'],[A',B']]. The first
two pair equations force (A',B',C') proportional to (A,B,C) by the
row independence just proved. This is the claimed uniqueness.

### Eight seeds force all remaining labels

For any two disjoint pairs of finite distinct labels, the preceding
construction gives a unique involution. If a third pair has one label
already known, its other label is its uniquely determined image.
If that image is infinity, outside H, or duplicates an assigned label,
the proposed seed assignment cannot extend to a bijective solution.
This reasoning applies to any of the three pairs, since (1) is unchanged
as a zero condition by permuting its rows.

Starting with J, the following table gives all deductions. The pair
columns list abstract indices, not field values; phi_t acts on their
h labels. At each row both determining pairs and the known member of
the last pair were either seeds or obtained in earlier rows.

| t | Two fully known pairs | Third pair | New index |
|---|---|---|---|
| 0 | (15,0), (6,8) | (4,9) | 9 |
| 7 | (6,7), (11,0) | (13,15) | 13 |
| 9 | (8,9), (15,1) | (13,2) | 2 |
| 2 | (1,2), (6,11) | (8,10) | 10 |
| 1 | (0,1), (7,9) | (5,10) | 5 |
| 5 | (4,5), (11,13) | (9,14) | 14 |
| 6 | (5,6), (10,15) | (12,14) | 12 |
| 3 | (7,12), (9,11) | (2,3) | 3 |

Each row is the triple of pairs
(t-1,t), (t+4,t+9), (t+6,t+8), in a suitable order.
The eight new indices are exactly the complement of J. This proves
that restriction to J is injective on the set of bijective labelings
satisfying all sixteen necessary equations, and therefore on labelings
with K!=0. No existence follows: unused determinant equations and all
other shared-coordinate gates still have to be met.

This is an analytic reconstruction, not a label sweep, positive rank
sample or configuration census. No mathematical program or finite
certificate is needed. It sharpens the residual label restriction but
does not decide the original zero-kernel target. The result is not a
claim of originality beyond the sources in the ready comparison. Its
separate critical review is recorded below.

### Separate critical audit — October 15, 2026, step 240

The exact SPECIALIZE assessment
`drafts/literature/2026-10-15-cyclic-six-label-critical-audit.md`
was available before this audit. The full proof and L089's definitions,
gate derivation and step-226 audit were checked. No mathematical defect
or change to the argument was found. This establishes an audited local
necessary restriction, not a stronger rank bound or a new discovery.

**Input and source scope.** L089 alone is the direct mathematical input.
Its unshifted columns, reciprocal-product circuit normalization and
three necessary gates apply to precisely this fixed field and arbitrary
bijection. Its audited L010/L087/L088 conventions are retained. No
actual error, original chart, or conclusion of L091–L096 is used.
The classical background comparison is Nicholas Phat Nguyen,
[*Projective Line Revisited*](https://www.heldermann-verlag.de/jgg/jgg25/j25h2phat.pdf),
Journal for Geometry and Graphics 25(2) (2021), 187–195,
Section 2, pp. 188–189, including footnote 1 and its affine and inversion
cases, and Proposition 1 with proof, p. 191. Its characteristic-not-two
field convention includes F_97. The explicit matrix calculation here
fixes this specialization's signs, uniqueness and finite-pole gates;
no broader theorem is newly imported. L036 is only a comparison under
different hypotheses, not an input or independent certification.

**Circuit ratios and the actual third gate.** Adjacent windows have
eight common indices. Replacing t-1 by t+8 in the product for d gives
exactly (3); replacing t by t+9 gives (4). Modulo sixteen these are
still nine distinct indices and the two omitted endpoints are distinct.
The indices c,d used in (3) are t+4,t+6 in its overlap; d,e used in
(4) are t+6,t+8 in that overlap. All reciprocals are therefore defined.
L089's normalization gives scriptA=d_(t,t), so the first summand in
(5), after division by d_(t,t+6), is the quotient of the window ratios
at d and c, namely (6). In block s=t+2 its last ratio gives
w_(s,t+3)/w_(s,t+8)=d_(t,t+3)/d_(t,t+8), and its middle ratio gives
w_(s,t+8)/w_(s,t+6)=d_(t+1,t+8)/d_(t+1,t+6).
Substituting both in scriptC cancels d_(t,t+3) and yields (7),
the quotient of the next-window ratios at d and e. Every cancelled
quantity is a nonzero circuit or block coefficient. Thus the gate is
equivalent to (8), without assuming either remaining shared gate.

**Clearing denominators and the determinant sign.** The denominator
factors in (8) are d-a, c-e, d-f, e-b. All are nonzero because the
offsets -1,0,4,6,8,9 are distinct modulo sixteen and h is bijective.
The numerator of one minus the first fraction is
(d-a)(c-e)-(d-e)(c-a)=(a-e)(d-c). Equating this with the second
fraction and reversing the two signs c-e and a-e gives exactly (9).
To check the expansion fully, put p=ab, s=a+b, q=cf, u=c+f.
Both the displayed determinant and
[P(d)Q(e)-P(e)Q(d)]/(d-e) equal

    (s-u)de+(q-p)(d+e)+pu-sq.

Since d-e is nonzero, (8), (9) and (1) are equivalent for every
bijection, not merely for a hypothetical surviving kernel. K!=0 is
used only to obtain the gate from L089.

**Invertibility, affine maps and poles.** Equality of the first two
determining pair rows would give the same monic quadratic with disjoint
root pairs, which is impossible. Their cross product is exactly
(A,B,C) as stated, so it spans their common kernel over F_97.
If AC-B^2=0 and A=0, then B=0 and the pair equation forces C=0.
If A!=0, multiplying the pair equation by A gives
(Ax+B)(Ay+B)=0; each disjoint pair would contain -B/A. Both cases
are impossible. Thus the matrix is invertible and its square is the
nonzero scalar (B^2-AC)I. It cannot be scalar in characteristic 97.

For A=0, invertibility gives B!=0 and the map is the affine involution
z -> -z-C/B, fixing infinity and with no finite pole. For A!=0 the
unique pole is -B/A, exchanged with infinity. A finite paired label x
cannot be this pole: its pair equation would also give Bx+C=0,
which, together with Ax+B=0, would force AC-B^2=0. Thus both finite
directions of each prescribed exchange are valid. Equation (10) is
equivalent to the third exchange with the same nonzero denominator.
Conversely any projective involution has a representative N with
N^2 a nonzero scalar matrix. Cayley–Hamilton makes a nonscalar N
trace zero, since nonzero trace would express N as a scalar matrix.
Writing such N in the stated coefficient form recovers the two pair
equations, and row independence proves uniqueness. These checks cover
all projective involutions, including the affine case, over F_97.

**All eight deductions and injectivity.** At each row two complete
pairs consist of four distinct already known labels; the known label
in the third pair is a fifth distinct label. The row equation therefore
forces exactly its involution image, regardless of which pair is last.
Checked in order, the table gives

    t=0:  new 9,  using known indices 15,0,6,8,4;
    t=7:  new 13, using known indices 6,7,11,0,15;
    t=9:  new 2,  using known indices 8,9,15,1,13;
    t=2:  new 10, using known indices 1,2,6,11,8;
    t=1:  new 5,  using known indices 0,1,7,9,10;
    t=5:  new 14, using known indices 4,5,11,13,9;
    t=6:  new 12, using known indices 5,6,10,15,14;
    t=3:  new 3,  using known indices 7,12,9,11,2.

Each triple of pairs equals (t-1,t), (t+4,t+9), (t+6,t+8)
modulo sixteen, up to row order and reversing an unordered pair.
Every listed known index lies in J or an earlier row's output.
The outputs {9,13,2,10,5,14,12,3} are distinct and are exactly
the complement of J. Induction on these eight rows therefore proves
the asserted injectivity on full bijective solutions. Infinity, an
image outside H, or a collision with any assigned label rejects the
seed assignment at that row. If a later collision would occur, that
later row rejects it. None of these rejection gates can discard an
actual full bijective solution.

Passing the eight rows is not sufficient: the other eight determinant
equations and the other two shared gates per triangle remain necessary,
and no rank conclusion is inferred from passing them. No labeling is
constructed, no uniform contradiction is proved, and no mathematical
script or numerical certificate is required by this analytic audit.
The direct input remains L089, so the DAG is unchanged. The argument
is unchanged, so PROOF.md is unchanged. ATTEMPTS/020,032–034 remain
in force for their respective stopped mechanisms. Uniform rank,
arbitrary-family coverage and challenge qualifications remain open;
the fixed-code interval stays 11/q–16/q.

## Mathlib

Full matching coverage for this cyclic six-label condition and its
eight-seed reconstruction has not been checked. No absence or formal
verification claim is made. All moment and circuit inputs are the
audited calculations of L089; the determinant and two-by-two matrix
specializations needed here are proved explicitly.
