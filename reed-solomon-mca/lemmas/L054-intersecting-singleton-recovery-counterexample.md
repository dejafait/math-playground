# L054 — Three intersecting same-singleton recoveries are realizable

## Hypotheses

Let F=F_(97^20), H={x in F_97^*:x^16=1}, and C=RS[F,H,8],
with the shifted moments sigma_j(e)=sum_(x in H)e_x*x^j for 1<=j<=8.
Use L043's gated local tau=1 setup in the pinned cell
1/4<=delta<5/16. All displayed arithmetic is in F_97 embedded in F.
This is an existence statement for the specified original finite chart,
not a reduction of arbitrary charts or labelings to the prime field.

## Conclusion

There is a gated pencil with three distinct additional full-weight
nonuniversal recoveries at the same singleton y_1. Their outside triples
have pairwise intersection sizes 0,0,1. Thus a proposed extension of
L053 to exclude all three same-singleton recoveries is false.

For this pencil there are exactly three additional nonuniversal candidate
parameters satisfying L043 (4)–(7), all with nonzero recovered weights,
and exactly six finite bad parameters in total. This count holds over F,
not merely over its prime subfield. It does not refute the uniform eleven
bound, improve the global 11/q–16/q interval, or supply a high-count
completion. L053's pairwise-disjoint exclusion is unaffected.
The explicit construction and exhaustive selected-pencil check below
have been independently reproduced within this step; a separate later
critical audit has not been performed.

## Proof

### Gated local pencil

Take

    h=70, d=96, (y_1,y_2)=(75,27), (z_1,z_2)=(1,33),
    (w_1,w_2,w_3)=(18,50,64),
    (gamma_0,gamma_1,gamma_2)=(0,1,2), lambda=1,
    (p,q,r)=(71,16,87).

The subgroup is

    H={1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96}.

The nine labels are distinct. The retained gates hold:
p=71, q=16, 1-p-q=11, r=87 and 1-r=11 modulo 97.
In particular 1-r is 11, and the parameter differences
alpha_0=96, alpha_1=2, alpha_2=96 are nonzero.
Let U be these nine labels and Q(X)=product_(x in H minus U)(X-x).
Its evaluations c_x=Q(x) on U are:

| x | 1 | 18 | 27 | 33 | 50 | 64 | 70 | 75 | 96 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| c_x | 39 | 36 | 44 | 46 | 7 | 1 | 18 | 84 | 18 |

The base errors, zero off their listed supports, are:

| i | Ordered support A_i | Weights in that order |
| --- | --- | --- |
| 0 | (27,70,75,96) | (53,80,13,83) |
| 1 | (1,33,70,96) | (68,23,47,2) |
| 2 | (18,50,64,70) | (61,90,96,93) |

These are exactly L043's local weights c_x*b_(i,x)/alpha_i:
at h the normalized weights are p,q,1-p-q, at d they are r,1-r,
and at each singleton they are one. All twelve listed weights are
nonzero. Set a=e_0 and b=e_1-e_0 as actual words on H. Their syndrome
pencil is s(T)=sigma(a)+T sigma(b), with

    sigma(a)   =(66,27,31,80,52,46,10,60),
    sigma(b)   =(72,86,37, 0,13, 4,15,83),
    sigma(e_2) =(16, 5, 8,80,78,54,40,32)=s(2).

These identities can be checked by the eight finite sums defining sigma.
Equivalently, the local weights give
96e_0+2e_1+96e_2=Q|_H, whose moments vanish by L010's kernel identity.
The prescribed chart therefore satisfies the full L043 setup, including
its local triple and nonpersistence conclusion from L041–L042.

### Three additional recoveries

The following rows give all weights in the displayed K order.
They use rho=2, g=1 and E=rho-(1-rho)mu=2+mu.

| Outside triple S | K | mu | u | E | T | Normalized omega | Actual error e=omega/E |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| (8,50,79) | (8,50,75,79) | 21 | 88 | 23 | 76 | (77,70,23,22) | (16,41,1,60) |
| (12,85,89) | (12,75,85,89) | 55 | 13 | 57 | 63 | (5,63,25,36) | (12,93,60,67) |
| (22,47,89) | (22,47,75,89) | 88 | 18 | 90 | 69 | (95,86,2,49) | (28,57,69,90) |

Each mu is nonzero and different from -1. Each E is nonzero,
T*E=2, and T differs from 0,1,2. The three T values are distinct.
For the three actual errors, direct eight-moment evaluation gives,
respectively,

    ( 9,64,30,80,70,59,83,63)=s(76),
    (43,13,34,80,95, 7,82,51)=s(63),
    (87,44,62,80,76,31,75,64)=s(69).

All actual weights are nonzero. To verify specifically the normalized
recovery used in L043, form the word n(mu) on
B={h,d,y_1,y_2,z_1,z_2} with coefficients

    n_y1=n_y2=-mu*c_y, n_z1=c_z1, n_z2=c_z2,
    n_h=c_h(q-mu*p), n_d=c_d[1-(1+mu)r].

For the three rows, its eight moments are

    (13,17,11,94,58,96,66,91),
    (26,62,95, 1,80,11,18,94),
    (70,80,51,22,50,74,57,37),

and equal the moments of the corresponding displayed omega on K.
Thus all eight membership equations hold, not only the first four.
Since K is neither a base support nor K_*={1,27,33,75}, L043's exact
converse verifies its nonuniversal projected case and every (4)–(7)
gate, with the indicated mu fixed also by T=2/(2+mu).
The nonzero omega values verify its final weight gate too.
L010, under L043's nonpersistence conclusion, makes each error unique
and guarantees same-support badness for the actual words a,b.

The first outside triple is disjoint from each of the other two;
the last two meet only at 89. Their union has eight labels, and their
common tag 75 lies outside that union. These are precisely intersecting
same-singleton recoveries, so they refute the proposed stronger exclusion
while satisfying L053's disjoint-triple obstruction.

### Exact count for this pencil, including extension-field parameters

The count six additionally uses the following exhaustive exact finite
certificate; the explicit three-recovery counterexample above does not
depend on the search coverage or this count computation.
For every one of the 1820 four-subsets K of H, invert its four-column
shifted Vandermonde matrix in rows 1..4. Let A_K,B_K be the resulting
four coefficient vectors for sigma(a),sigma(b). Compare moments 5..8
with those of the supplied intercept and slope, obtaining residuals
R_K,S_K in F_97^4. Membership at any T in F is exactly

    R_K+T S_K=0.

The complete certificate verifies S_K!=0 for every K. A nonzero
coordinate therefore forces the unique possible
T=-(R_K)_j/(S_K)_j in F_97. The other three coordinates decide
consistency exactly. Hence this prime-field enumeration exhausts every
extension-field parameter too. It is not a restriction to sampled T.

Exactly six supports are consistent: the three base supports at 0,1,2
and the three displayed additional supports at 76,63,69. All recovered
weights are nonzero and the six parameters are distinct. A weight-less-
than-four representative would lie in some four-support K, so is not
missed; none occurs here. By L010 these are exactly the finite bad
parameters in the pinned cell. The universal support is inconsistent;
also r*q=34 whereas (1-r)*p=5, so L043 (12) fails.
Thus the extra nonuniversal candidate count is three, far below twelve
needed to refute eleven.

Run `python3 scripts/simultaneous-recovery/intersecting_singleton.py`.
The producer stops at this first witness after 447058 scalar/r cases,
37 intersecting common-r triple tests and 121 h tests; this is explicitly
an incomplete all-label search, not an exclusion certificate.
It saves all visited scalar/r cases and the selected witness in
`scripts/simultaneous-recovery/intersecting-singleton-result.json`.

Run `python3 scripts/simultaneous-recovery/verify_intersecting_singleton.py`.
This verifier imports none of the producer's routines. It reconstructs
Q and every base weight, checks every selected gate and all eight moments,
and verifies the five cubic equations by cross multiplication.
It then saves all 1820 Vandermonde solutions, their complete residuals,
tested parameters, and rejected/admitted decisions in
`scripts/simultaneous-recovery/intersecting-singleton-verification.json`.
It checks every admitted error's eight moments and nonzero weights.
The actual/required support coverage is 1820/1820, selected distinct
full-weight recoveries 3/3, total bad parameters six, extra parameters
three and failures zero. Both programs were executed successfully.
The complete selected witness, selected errors, admitted list and
summary were inspected, and the full residual certificate was checked
by this complete verifier execution. This is a reproducible exact
selected-pencil certificate; no negative all-label claim is made.

## Mathlib

Full coverage of this numerical fixed-H construction was not checked;
no absence claim is made. The mathematical supporting inputs are the
already proved moment kernel and sparse uniqueness in L010 and the
separately audited exact recovery criterion and local gates in L043.
No recurrence theorem or other known result is reproved. The ready
literature assessment did not establish coverage of this simultaneous
counterexample; this is local negative evidence, not certified originality.
