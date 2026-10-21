# L105 — Two-anchor reconstruction of the seven-coordinate equality profile

## Hypotheses

Use L104's F=F_(97^20), F_0=F_97, order-sixteen H subset F_0^*,
code RS[F,H,8], shifted moments, pinned cell 1/4<=delta<5/16,
actual nonzero polynomial D and all nonzero polynomial locators.
Both coefficient syndromes lie in U_S for a seven-set S, and f(T)
is its unique affine lift. Assume |B(a,b)|=16 and that L104's number
t of actual errors equal to f at their parameters is two.
All original parameters and coefficients are allowed in F.

Write the two distinct original finite parameters as gamma_0,gamma_1,
and set P={x in S:f_x(gamma_0)=0},
Q={x in S:f_x(gamma_1)=0}. Then |P|=|Q|=3, they are disjoint,
and S=P disjoint union Q disjoint union {c}. Put J=H minus S.
For a two-set K subset J write

\[
g_K(X)=\prod_{z\in J\setminus K}(X-z).
\]

The construction below uses rational labels only; no symmetry of
arbitrary label assignments is assumed. L103's imported finite-certificate
qualifications remain essential in the equality application. L104 is a
partial reduction whose separate step-292 critical audit found no defect.

## Conclusion

Every two-overlap equality support has the form {x,y} union K with
x in P, y in Q and K a two-subset of J. No overlap pair {x,y} repeats.
There are r=6+n_0 such supports, with 6<=r<=9, where n_0 counts
the non-equal-lift errors disjoint from S. In particular the minimal
profile (t,n_0,n_1,n_2)=(2,0,8,6) is covered.

Two of these supports can be chosen with different P labels and different
Q labels. Their labels alone uniquely reconstruct the projective pencil
on S by the explicit rules below. Its normalized lift has the form

\[
 w(\mu)_z=\begin{cases}
 \mu p_z&z\in P,\\
 q_z&z\in Q,\\
 \mu U-V&z=c,\\
 0&z\notin S,
 \end{cases}                                          \tag{1}
\]

where p,q have nonzero entries in F_0, prescribed entries p_(p_*) and
q_(q_*) equal one, and U,V belong to F_0^*. The point at mu=infinity
has representative w_infty=(p,0,U). The original chart omits precisely
one point mu_*=alpha/beta in F^*, which need not be rational.
The original gamma_i and actual weights need not descend.

For each fixed ordered split (P,Q,c), at most
18*36*35=22,680 seed choices suffice to include every such equality
pencil. Each seed either fails an explicit gate or determines one
rational pencil (1). For a retained pencil, its full two-overlap
recoveries are determined by 324 explicit support tests (4)–(6),
deduplicating mu and deleting mu_* in the prescribed chart.
There are no extension-field weight or recovery-parameter unknowns
left in these tests. Testing whether the retained scalar set has size
at least six is a necessary filter, not a sixteen-event certificate.

No candidate table or maximum is evaluated here. This eliminates
unknown scalars from the minimal-profile test but proves neither its
impossibility nor a six-row survivor, nor the seven-coordinate fifteen
bound. The cases t=0,1 for a specified S and the other equality events
remain unresolved. The separate step-292 critical audit found no defect
in this partial reduction, with the inherited qualifications retained.

## Proof

### Equality restrictions and two usable support seeds

L103 excludes an active lift on at most six coordinates. Thus all
seven coordinates of f are active. L010 gives full weight four at
each bad parameter, distinct supports and degree four at every label.
Each equal-lift event has exactly three zeros in S. Two distinct
finite zeros cannot belong to the same nonzero affine coordinate
polynomial, so P,Q and c have the stated form. The c-coordinate is
nonzero at both selected parameters; its slope may be zero.

Here is the pair restriction needed below, directly from audited L103.
If any two distinct equality errors have supports whose union W has
size at most six, their moment identities at distinct finite parameters
give

\[
 \sigma(b)=\frac{\sigma(e_\eta)-\sigma(e_\gamma)}{\eta-\gamma},
 \qquad \sigma(a)=\sigma(e_\gamma)-\gamma\sigma(b).
\]

Both coefficient syndromes therefore lie in U_W. Enlarge W to six
labels if necessary. The same code, field, original chart and actual
nonzero polynomial D and locators meet L103's hypotheses, contradicting
its full-B bound fifteen. Thus every equality pair intersects in at
most one label. This uses only the stated smaller-class bound; L086
and its longer proof chain are not additional inputs.

The equal-lift supports are Q union {c} and P union {c}.
A two-overlap support cannot contain c: its second S label would
give intersection two with one of these supports. It cannot contain
two P labels or two Q labels for the same reason. It therefore has
one label from each triple. Two such supports cannot have the same
overlap pair, again by the pair restriction. There are only nine pairs.
L104 gives r=12-3t+n_0=6+n_0, hence 6<=r<=9 and 0<=n_0<=3.

Fix any one of the r overlap pairs. Of the nine P-by-Q pairs, only
five share its P or Q label (including itself). Since r>=6 and pairs
do not repeat, another pair shares neither. Choose these two support
rows, indexed j=1,2:

\[
 A_j=\{x_j,y_j\}\cup K_j,
 \quad x_1\ne x_2\text{ in }P,\quad y_1\ne y_2\text{ in }Q.
                                                               \tag{2}
\]

Their K_j are distinct, since otherwise their intersection contains
two labels. All are actual full errors at distinct finite parameters
different from gamma_0,gamma_1.

### Reconstruction from the two supports, with no scalar choices

First prescribe p_(p_*)=1 at any fixed p_* in P. Determine the other
p entries from

\[
 \frac{p_z}{p_{z'}}=\frac{g_{K_j}(z)}{g_{K_j}(z')}
 \quad\text{for the two labels }z,z'\in P\setminus\{x_j\},
 \quad j=1,2.                                        \tag{3}
\]

These are two different edges on a three-vertex set. They form a
connected tree, so (3) gives exactly one nonzero vector p with the
prescribed normalization. Every g evaluation is in F_0^*, because
its seven roots lie in J. Thus p belongs to (F_0^*)^P. In exactly the
same way obtain q in (F_0^*)^Q, normalized at q_*, using the two
pairs Q minus {y_j}. There are no cycle-consistency or zero-pivot cases
in either two-edge tree.

For the two seed rows define

\[
 A_j^{\rm rat}=p_z/g_{K_j}(z)\quad(z\in P\setminus\{x_j\}),
 \quad B_j^{\rm rat}=q_z/g_{K_j}(z)\quad(z\in Q\setminus\{y_j\}),
 \quad \mu_j=B_j^{\rm rat}/A_j^{\rm rat},
 \quad C_j=B_j^{\rm rat}g_{K_j}(c).
\]

Each common value is well defined by (3) and nonzero in F_0.
If mu_1=mu_2, reject the seed. Otherwise set, uniquely,

\[
 U=\frac{C_1-C_2}{\mu_1-\mu_2},\qquad V=\mu_1U-C_1.
\]

Reject U=0 or V=0, and reject either seed if either of its two
overlap weights in (6) below is zero. These are finite rational tests.
No rank or generic-nonvanishing assertion replaces these gates.

To prove that actual equality data are reconstructed, put
tau=(T-gamma_0)/(gamma_1-gamma_0). On P and Q the actual lift has
forms d_z*tau and e_z*(tau-1), respectively, with all d_z,e_z nonzero.
At either seed parameter, tau is neither zero nor one. L104's exact
criterion gives f_z=lambda_j*g_(K_j)(z) off its two overlap labels,
with lambda_j nonzero by full outside weights. Dividing two P equations
cancels the same nonzero tau and lambda_j and gives (3) for d.
The corresponding Q equations give (3) for e. Uniqueness of the tree
solutions therefore gives d=alpha*p and e=beta*q, with alpha,beta in F^*.
Write the actual c-coordinate as a+b*tau. Its two endpoint gates say
a!=0 and a+b!=0, permitting b=0.

For tau!=1 define the projective coordinate

\[
 \mu=\frac{\alpha\tau}{\beta(\tau-1)}.
\]

This is an invertible projectivity, since alpha*beta!=0. It sends
tau=0,1,infinity to 0,infinity,alpha/beta, respectively. Dividing f
by beta*(tau-1) gives (1), with initially F-valued
U=(a+b)/alpha and V=a/beta. At a seed row the Q equations give
the normalized shortening scalar B_j^rat, and the P equations give
mu_j=B_j^rat/A_j^rat. Distinct actual parameter values give distinct
mu_j. The c equation is mu_j*U-V=C_j for j=1,2. Their determinant
mu_1-mu_2 is nonzero, so they give exactly the displayed rational U,V.
The endpoint and full-overlap gates hold for actual data. Thus every
assumed equality pencil is among the retained reconstructed pencils.

This proof does not rationalize the original affine chart or discard
its infinity. It proves uniqueness of the projective lift for the
selected support data, not uniqueness of the original words a,b or
their parameterization. The two coefficient vectors in (1) are independent
because p and q are nonzero on disjoint triples. Injectivity of the
moment map on S preserves that independence.

### Exact remaining row tests and their original-chart meaning

For a reconstructed pencil and any x in P, y in Q, K subset J of
size two, first test that both pairs of values are equal:

\[
 p_z/g_K(z)=A\quad(z\in P\setminus\{x\}),\qquad
 q_z/g_K(z)=B\quad(z\in Q\setminus\{y\}).             \tag{4}
\]

If they are, A,B belong to F_0^*. Put mu=B/A. The remaining equation
on S minus {x,y}, and the full-overlap gates, are precisely

\[
             \mu U-V=B g_K(c),                        \tag{5}
\]
\[
       \mu p_x-Bg_K(x)\ne0,\qquad q_y-Bg_K(y)\ne0.    \tag{6}
\]

The two outside error weights are -B*g_K(k), k in K, automatically
nonzero. At a successful row, subtracting B*g_K evaluated on H from
w(mu) gives exactly these four full error weights, zero elsewhere.
Conversely a full two-overlap recovery of this shape gives (4)–(6)
by L104's one-row criterion. The multiplier is fixed by the Q
equations; no lost scalar or extension-field alternative remains.
For any such row mu belongs to F_0^*, so it is neither base direction.

In a specified original chart retain only mu!=mu_*. At every retained
row the nonzero factor beta*(tau-1) recovers its original error and
all eight original moments. L010 gives same-support badness under
the original nonpersistent-polynomial hypotheses. Count distinct mu,
not witnesses; distinct mu give distinct original finite parameters.
In fact two different successful full support rows cannot give the
same mu: their errors have the same syndrome, so L010's sparse-error
uniqueness makes their full supports identical. Deduplication is still
an explicit safe rule for a future implementation.

There are 3*3*binom(9,2)=324 such support rows. The exact table concerns
the cross-triple two-overlap shapes required at equality. It does not
assert that these are all bad supports of a constructed low-count
pencil; zero/one overlaps and other shapes must still be tested if a
whole bad-set claim is sought.

There are binom(3,2)^2*2=18 unordered pairs of disjoint overlap edges.
Fix a deterministic order on the two edges. Assign K_1 in 36 ways
and K_2 different from K_1 in 35 ways. This yields at most 22,680
seed choices for the fixed ordered split, including seeds subsequently
rejected or giving the same plane. Every equality pencil admits at
least one such seed by (2), proving coverage. This is an upper bound
on cases to test, not an evaluated recovery bound or a field-label
census. No equivalence under subgroup scaling is used.

For completeness, a retained seed does give a local actual pencil,
though generally without six rows. Choose xi in F minus F_0 and take
the affine vector h(T)=T*w_0+(1+xi*T)*w_infty, where
w_0=(0,q,-V). Its direction is mu=xi+1/T, with T=0 representing
infinity; its sole omitted point is xi. All rational successful rows
and both base directions are finite in this chart. The base supports
are Q union {c} and P union {c}; either seed support omits c.
Consequently these three full errors collectively omit every coordinate.
L010's pointwise factorization makes D nonzero at each full event and
ell_z nonzero at a full event omitting z, proving polynomial
nonpersistence before invoking its bad-event conclusion. All are in F,
since F contains elements outside F_0. This checks that no hidden
moment or locator gate survives the local reconstruction. It supplies
at least the two base and two seed events, not six two-overlap rows
and not the remaining events of equality. The prime-field row tests
may still have fewer than six successes for every seed; this has not
been decided.

### Reuse, duplicates and limitations

The unchanged prior assessment is
`drafts/literature/2026-10-17-seven-coordinate-syndrome-bound-review.md`
(EXPLORE). This is a REPRODUCTION application of its distance,
shortening and affine interpolation tools to the approved simultaneous
compatibility test. The exact shortening formula used through L104 is
I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
[accepted manuscript, 2016-02-29, section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2, Lemma 5.3 and the following unnumbered formula,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004).
The seven deleted labels are precisely J minus K, leaving dimension
one and nonzero retained multipliers. No changed shortening hypotheses
or reproof of the general result is needed. The distance input inherited
by L103/L104 is J. I. Hall, *Notes on Coding Theory*,
[GRS chapter, Theorem 5.1.1, pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
with sixteen distinct labels, unit multipliers and dimension eight.

L034 already has a paired-root descent mechanism, and L058 already
descends normalized triangle weights at equality. Neither rationality
alone nor this elementary mechanism is claimed as new. The useful
additional output here is the explicit unique reconstruction from two
support rows and a finite, parameter-free six-row filter for a fixed
two-triple split. L034/L058 are comparisons, not theorem inputs or
justifications for the changed hypotheses. ATTEMPTS/006,007,017,027
do not test these simultaneous moment equations. No claim of novelty
beyond the sources checked, numerical evidence, new source approval,
or complete challenge candidate is made.

### Separate critical audit, 2026-10-17

Step 2026-10-17-mca-292-seven-coordinate-fixed-split-critical-audit
checked the whole reduction and the exact L010/L103/L104 inputs. It
found no mathematical defect or missing direct dependency. Earlier
descent results L034/L058 are comparisons only, not unstated inputs.

For any equality pair with union at most six, subtraction of its two
actual finite moment identities places both coefficient syndromes in
that union's moment image. L103 applies to a containing six-set with
all its field, event and actual polynomial hypotheses unchanged. Thus
pairwise intersections are at most one, without invoking L086. The two
equal-lift supports are Q+c and P+c; this forces every two-overlap
pair to be one P label and one Q label, excludes c, and forbids pair
repetition. At least six among the nine pairs imply two sharing neither
endpoint, because exactly five pairs meet a fixed pair. Their outside
pairs must differ. This proves the seed coverage before enumeration.

For each triple the two omitted labels differ, so its ratio equations
are distinct edges of a three-vertex tree. All g evaluations on S are
nonzero, and fixing its first coordinate to one gives a unique nonzero
rational vector. Actual lift coefficients are alpha*p and beta*q;
neither alpha nor beta is divided out until nonvanishing is established.
For the c-coordinate a+b*tau, division by beta*(tau-1) gives exactly
mu*(a+b)/alpha-a/beta. Both endpoints are nonzero, permitting b=0.
The two actual seed parameters have distinct, finite, nonzero mu,
so their c-equations determine U,V uniquely in F_97. Rejecting equal
mu, zero U/V or canceled overlap weights cannot discard equality data.

The projectivity sends original infinity to alpha/beta in F^*; there
is no inference that this omitted point is rational. For any other row,
its nonzero Q values fix the shortening scalar B and its nonzero P
values then fix mu=B/A in F_97^*. Equations (4)–(6) are therefore
complete over F, not tests of rational samples. Scaling back by
beta*(tau-1) is nonzero at every such retained row. Sparse-error
uniqueness handles duplicate witnesses; deleting the omitted point
cannot increase the count. The two base directions are separate from
these scalars. The 18*36*35 seed count retains every eligible ordered
assignment of outside pairs after fixing the overlap-edge order.

Finally, in the local construction xi outside F_97 omits no rational
successful direction or base direction. The two base supports and one
seed support collectively omit every coordinate. Their full errors and
L010's pointwise factorization establish polynomial nonpersistence
before same-support badness. This construction proves only the selected
events, not a completion. No original chart is rationalized. L103's
inherited finite-certificate qualifications remain essential.

## Mathlib

Full matching two-anchor reconstruction and gated row-table theorem:
**not checked**. Supporting finite-field, projective-coordinate,
affine-interpolation and GRS-shortening coverage: **not checked**.
Unknown coverage is not absence. L103's finite-certificate qualifications
persist; no new finite computation or Lean verification is asserted.
