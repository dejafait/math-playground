# Lemma 882: a boundary odd fiber forces two fibers in each direction and a label dichotomy

## Hypotheses

Retain exactly L847's actual entire G, positive R,C and full density,
with the original angular orientation dy1 wedge dy2:

\[
 z_j(y)=R e^{u_j(y)+iy_j},\qquad
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
 \qquad Q=F(z_1,z_2)J,\quad J=\det(I-iDu).
\]

Assume L879's hypotheses: u is smooth, real and periodic, J is nowhere
zero, and the first variation of the normalized integral of |Q|
vanishes for every smooth real radial variation compactly supported
in {Q!=0}. Thus L879 gives Q=lambda*s with |lambda|=1 and s real.

Assume a single off-diagonal odd contact in coordinate 1, with label
zeta and angle a. L880 supplies z1(a,t)=zeta for every t. Suppose
zeta lies on its complementary radial curve

\[
 \Gamma_{2|a}=\{z_2(a,t):t\in\mathbb R/2\pi\mathbb Z\}.
\]

This is precisely L881's boundary alternative. L881 implies that
zeta is simple, the bounded interior of Gamma_(2|a) has no G zeros,
and its boundary G zeros are exactly zeta and a second simple label
eta!=zeta. Write b=arg(eta), with all angles taken modulo 2pi.
Starting in coordinate 2 gives the exchanged statement below.

No positivity, symmetry, analyticity of u, simplicity of all G zeros,
finite pullback contact census, collar or graph-existence assumption
is added. All other multiplicities and simultaneous/diagonal contacts
are retained. In particular the hypothesis does not assert RH.

## Conclusion

There is a simple G zero theta!=zeta, with c=arg(theta), such that

\[
 \begin{array}{ll}
 z_1(a,t)=\zeta,&z_1(c,t)=\theta\quad\hbox{for every }t,\\
 z_2(t,a)=\zeta,&z_2(t,b)=\eta\quad\hbox{for every }t.
 \end{array}                                                   \tag{1}
\]

The complementary curve Gamma_(1|a)={z1(t,a)} has no interior G
zeros and has exactly the two simple boundary zeros zeta,theta.
These are exactly the two complete odd-label fibers in each direction:
any single odd-contact seed in coordinate 1 has label zeta or theta,
and any such seed in coordinate 2 has label zeta or eta. This does
not classify all isolated simultaneous odd contacts.

Each of zeta,eta,theta is the G zero of smallest modulus on its own
ray (there is no smaller G zero with that argument). In particular

\[
                     b=c\quad\Longleftrightarrow\quad\eta=\theta.
                                                               \tag{2}
\]

There are two necessary alternatives:

1. If eta=theta, the four fibers in (1) all satisfy L881's boundary
   alternative: each complementary curve has no interior zeros and
   exactly the same two simple boundary labels zeta,eta.
2. If eta!=theta, the three angles a,b,c are distinct. The label theta
   is outside the closed domain bounded by Gamma_(2|c)={z2(c,t)},
   and eta is outside the closed domain bounded by
   Gamma_(1|b)={z1(t,b)}. Each of these curves has its two forced
   simple boundary labels: zeta,eta on Gamma_(2|c), and zeta,theta
   on Gamma_(1|b). Independently for each curve, the only remaining
   possibilities are

   \[
   \begin{array}{c|c|l}
   N_{\rm in}&N_{\rm bd}&\hbox{additional G zeros in the closed domain}\\
   1&2&\hbox{exactly one simple interior zero},\\
   0&4&\hbox{exactly one double boundary zero}.
   \end{array}                                                \tag{3}
   \]

   The additional zero in either row has argument different from
   a,b,c. The two curves need not have the same additional zero
   or the same row of (3).

This is a necessary compatibility restriction, not an exclusion or
realization of either alternative. No stationary graph is constructed;
four fixed fibers do not imply a product graph. The independent conceptual
audit of 7 November 2026 below accepts the result without strengthening it.
Its prior EXPLORE assessment did not identify a matching theorem;
POTENTIALLY_NEW records that limited comparison, not certified originality.
The all-degree actual-Xi positivity gap remains open.

## Proof

### Coverage and imported tools

The invocation-start assessment is
`drafts/literature/2026-11-06-odd-contact-boundary-fiber-compatibility.md`,
DECISION EXPLORE, with the exact boundary/two-coordinate target.
L847 supplies the full form and orientation, L879 the global phase
line, L880 its vertex expansions and continuation theorem, and L881
the audited weighted count and its boundary/exterior alternatives.
The argument below justifies the missing second-coordinate seeds;
it never invokes L880 merely because a simultaneous contact exists.

The elementary source input reused for local label isolation is Jiří
Lebl, *Guide to Cultivating Complex Analysis*, v1.10, 5 November 2026,
[Theorem 2.4.7 and its finite-order factorization proof, pp49-50](https://www.jirka.org/ca/ca.pdf#page=49).
G is entire and G(0)>0, so its zeros are isolated and finite-order.
This supplies no identity theorem for smooth u. The real-polynomial
factor comparison has already been specialized in L880; no new
factorization theorem is required here. Likewise L881 already checks
the spatial-cutoff residue hypotheses of Hungerbuehler-Wasem,
*Non-Integer Valued Winding Numbers and a Generalized Residue Theorem*,
Journal of Mathematics 2019, Article 6130464,
[Definition 2, Proposition 3 and Theorem 8, pp2,3,7](https://www.math.ch/norbert.hungerbuehler/publications/Non-Integer_Valued_Winding_Numbers_and_a_Generalized_Residue_Theorem.pdf),
DOI10.1155/2019/6130464. Only L881's accepted specialization is used;
no new contour or residue calculation is introduced.

The positive-contact, product-graph, session43 and retired two-period
stops have different premises or conclusions. No conclusion from them
is used as positivity, graph existence or a missing contact seed.

### Exact bridge to the second coordinate at a simple contact

Consider any complete vertical fiber with simple label rho, angle d.
Suppose at p=(d,e) the second coordinate equals a simple zero sigma.
There is an incoming rho interval on both sides of p. In local lifts
x=y1-d, t=y2-e, the calculations in L880 apply with m=n=1.
If rho!=sigma, isolate the two labels and exclude the diagonal by
continuity. L880's distinct-contact calculation gives

\[
       \overline\lambda Q(x,t)=\kappa x t+o(x^2+t^2),
                         \qquad\kappa\in\mathbb R\setminus\{0\}.
                                                               \tag{4}
\]

If rho=sigma, then d=e modulo 2pi; L880's diagonal calculation,
including the squared diagonal and full J, gives

\[
       \overline\lambda Q(x,t)=\kappa x t(x-t)^2
                                      +o((x^2+t^2)^2),
                         \qquad\kappa\in\mathbb R\setminus\{0\}.
                                                               \tag{5}
\]

The hypotheses for these specific expansions are precisely the
incoming fixed fiber, simple encountered labels, real phase line and
J!=0. In the distinct case the labels may have the same argument:
their different values still exclude the diagonal locally. In the
equal case (5), no diagonal factor is discarded.

In the distinct case all nearby Q zeros are contained in x=0 or
t=0; in the equal case they are contained in x=0, t=0 or x=t.
Indeed each isolated G label requires its fixed angle, equality of
the two coordinates requires equal angles, and J has no zeros.
These containing lines are not yet asserted to be contact sets.

For epsilon=+1 or -1 and sufficiently small delta, consider

\[
 W_+=\{0<\epsilon x<\delta,\ 0<t<|x|/2\},\qquad
 W_-=\{0<\epsilon x<\delta,\ -|x|/2<t<0\}.
\]

They are connected and Q is nonzero on them. Since Q lies in the
fixed line lambda*R, its phase is constant on each wedge. On rays
(x,t)=r(epsilon,h) and r(epsilon,-h), with 0<h<1/2 and r decreasing
to zero, the leading terms in (4), or in (5), are nonzero and have
opposite signs. Thus the two wedge phases are opposite.
For every 0<epsilon*x<delta, (x,0) lies in both wedge closures.
Continuity would make the phases equal if Q(x,0)!=0, so Q(x,0)=0.
At these points x!=0: the isolated first G label cannot be reached,
and the diagonal is absent. Hence the second G factor vanishes and
isolation gives exactly z2(d+x,e)=sigma.

These are single off-diagonal simple contacts, not just formal jets.
One is a valid coordinate-2 seed for L880, which yields the full
horizontal fiber z2(t,e)=sigma. Exchanging both coordinate indices
in this scalar reasoning gives the reverse bridge. F is symmetric
and J remains included; Q is still measured in the original
dy1 wedge dy2 orientation. No reorientation or integral sign occurs.
All further vertices on each new fiber are covered by L880, including
arbitrary other multiplicities and coincidences; they need not be simple.

### Two distinguished fibers in each direction, and no additional odd seeds

Apply the bridge to the original vertical zeta fiber at its two
boundary contacts. At (a,a) the labels agree; at (a,b) they differ.
This proves both horizontal fibers in (1). The angles a,b differ:
the radial curve z2(a,t) takes exactly one value at any given argument,
so it cannot contain two different boundary labels of the same angle.

The horizontal zeta fiber has an established single-contact seed.
Its complementary curve contains zeta at angle a. Therefore L881
applies to it in its boundary alternative and gives exactly one
other simple boundary zero theta and no interior zeros. Its angle
c differs from a for the same radial reason. The reverse bridge at
theta supplies a single vertical seed and then the entire vertical
theta fiber in (1).

Now any single odd seed in coordinate 1 yields a full vertical fiber
by L880. Its label must occur on Gamma_(1|a), whose only G-zero
labels are zeta,theta. The coordinate-2 argument uses Gamma_(2|a)
and forces label zeta or eta. Conversely all four displayed fibers
have single seeds from the bridge or the original hypothesis.
Any complete odd-label fiber has a single seed: its complementary
radial curve meets only finitely many G zeros, and the possible
diagonal point has one angular parameter. Away from this finite set
there is exactly the given odd G contact. Thus there are exactly
two complete odd-label fibers in each direction. This makes no claim
about a simultaneous contact that supplies no single seed.

Both Gamma_(2|a) and Gamma_(1|a) are zero-free in their interiors.
The first has radial boundary values zeta,eta; the second zeta,theta.
Any smaller G zero on one of those rays would lie in the respective
interior. Thus each selected label has minimum modulus among G zeros
on its ray. If b=c and eta!=theta, their positive moduli would have
to satisfy both |eta|<=|theta| and |theta|<=|eta|. Equality of modulus
and argument would then give eta=theta, a contradiction. This proves
(2), without assuming all G zeros have distinct arguments.

### Counts on the two other fibers

If eta=theta, each of the other two fibers has its own label on its
complementary curve, by (1). It has a single seed and L881 again
gives its boundary alternative. The two forced labels already use
the entire boundary count 2. This proves alternative 1.

Suppose instead eta!=theta. Apply L881 to the vertical theta fiber.
Its complementary curve Gamma_(2|c) contains the simple labels zeta
and eta from the two horizontal fibers. L881 excludes theta from
the interior. If theta were on the boundary, the simple-contact
bridge would yield a horizontal theta seed, contrary to the seed
classification above. Thus theta is outside the closed domain.
L881 consequently gives

\[
                 2N_{\rm in}+N_{\rm bd}=4,
                          \qquad N_{\rm bd}\geq2.       \tag{6}
\]

The only integer pairs are (1,2) and (0,4). In the former case the
forced simple boundary labels exhaust the boundary count, and the
interior multiplicity sum 1 means exactly one simple zero. In the
latter case the remaining boundary multiplicity is 2. Two further
simple zeros are impossible: each would, by the bridge, yield a new
horizontal seed. Each already fixed boundary label is encountered
only once on a radial curve. The only remaining possibility is one
additional G zero of multiplicity exactly 2. The horizontal eta
fiber is treated with coordinates exchanged, giving exactly (3)
with boundary labels zeta,theta and its own eta exterior.

Finally, on Gamma_(2|c) the radii at a,b equal |zeta|,|eta|, and the
radius at c is strictly less than |theta| because theta is exterior.
On Gamma_(1|b) the radii at a,c equal |zeta|,|theta|, and the radius
at b is strictly less than |eta|. Each selected label is minimal
on its ray, as just proved. No additional interior or boundary G
zero on either curve can therefore have argument a,b or c. This
also handles potentially coincident arguments of unselected zeros;
none is excluded elsewhere without an argument.

The bounded test has produced the exact bridge and stronger necessary
alternatives. The integer data in alternatives 1 and 2 do not conflict
with L881, but this is only absence of a contradiction from these
counts. Full phase compatibility and smooth graph realization are
unproved. Neither alternative is an actual counterexample; neither
settles mass equality, the sharp L868 threshold, compactness, higher
signs or Xi transfer.

### Independent conceptual audit, 7 November 2026

The unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-06-odd-contact-boundary-fiber-compatibility.md`
covers this audit of the submitted boundary-compatibility argument.
The verdict is acceptance under exactly the hypotheses above, with no
mathematical repair or new conclusion. This is REPRODUCTION: independent
verification of an existing notebook input, not a newly discovered
restriction or certified originality. The full proof and source scopes
remain above; the following checks address its load-bearing steps.

**Exact seeds before propagation.** On an incoming vertical simple
fiber, partial_2 u1=0 at the vertex by smoothness. L880 therefore applies
with its alpha=A+i, beta=d+i, and nonzero full J. At distinct simple
labels its real leading polynomial forces partial_1 u2=0 and gives
exactly (4), with nonzero real coefficient. Distinct labels can have
the same argument: disjoint label discs, rather than different angles,
exclude the diagonal in this case. At an equal-label vertex both G
orders are 1; the three projective factors in L880 have multiplicities
1,1,2. Conjugation fixes the incoming angular factor, cannot interchange
the other two of unequal multiplicities, and yields alpha=beta and
partial_1 u2=0. Its full degree-four polynomial is precisely (5).
The squared diagonal and J are retained; neither is divided out at
the vertex. No assertion of exact contacts follows from this jet alone.

In local lifts of width less than 2pi, an isolated first or second
G label requires x=0 or t=0 respectively. At an equal-label vertex
equality z1=z2 further requires x=t. Thus both displayed wedges are
actual nonzero sets in both vertex cases. They are connected for each
choice of epsilon. Since conjugate(lambda)Q is real and nonzero there,
it has a constant sign on each wedge. On the two fixed rays used in
the proof the factors x,t are nonzero; in (5), x-t is also nonzero.
The signs differ by the sign of t, while the diagonal square is
positive. The little-o remainder suffices along these rays to identify
the exact constant wedge signs; no uniform relative error near an axis
is assumed.

For every fixed 0<epsilon*x<delta, continuity at (x,0) would identify
those opposite signs if Q(x,0) were nonzero. Hence it vanishes. Here
the first isolated label is impossible because x!=0, and the diagonal
is excluded either by disjoint discs or by x!=t. Nonzero J then forces
exactly the second isolated G label. These are single off-diagonal
simple contacts on an interval, so L880's seed hypothesis is met
before its global theorem is used. Exchanging both coordinate indices
conjugates I-iDu by the permutation matrix and preserves its determinant;
F is symmetric. The scalar proof introduces no change to the original
orientation. All subsequent endpoints, with arbitrary other
multiplicities, fall within L880's already audited exhaustive cases.

**Global labels and coincident arguments.** The original L881 boundary
case supplies simple zeta and eta, no interior zeros, and no other
boundary zeros. A radial curve takes just one value at a specified
angle, so a!=b. The two bridges give horizontal zeta and eta fibers.
The horizontal zeta fiber has an actual single seed and contains its
own label on its complementary curve. Thus L881 supplies simple theta,
c!=a, and no other boundary or interior G zeros there. The reverse
bridge gives the vertical theta fiber. Each use of L881 therefore
has both a single seed and the asserted location of its own label.

Any further single odd seed would give a full same-label fiber by
L880. Intersecting it with the horizontal zeta fiber, or with the
vertical zeta fiber in the exchanged case, places that label on one
of the two original complementary curves. Their complete boundary
censuses exclude every new label. Conversely any complete odd-label
fiber has a single seed: the complementary radial curve is compact
and injective in its angle, so it meets only finitely many isolated
ambient G zeros, each at one angle. The possible diagonal adds at
most one angle. An angle outside this finite set gives the required
single contact. This proves the exact census of complete odd fibers,
without classifying isolated simultaneous contacts or assuming a finite
census of all pullback zeros on the torus.

The two zero-free interiors also prove radial minimality separately
for zeta, eta and theta. If b=c, either strict inequality of |eta|
and |theta| would put a G zero inside one of these interiors. Equality
of moduli and arguments gives equality of the labels. This proves (2)
without any assumption about the arguments of other G zeros.

**Remaining counts.** In the matched case, each remaining fiber has
its own label on its complementary curve; L881 gives boundary count
2 and interior count 0. The two forced simple labels exhaust this count.
In the unmatched case, theta cannot be interior to Gamma_(2|c) by
L881. If it were on the boundary, its simplicity and the established
vertical theta fiber would give a horizontal theta seed by the same
bridge, contrary to the preceding census. Thus it is exterior.
The two forced simple labels zeta,eta already give boundary count
at least 2. The nonnegative integer solutions to (6) are then only
(1,2) and (0,4); in particular odd boundary totals are excluded by
the equation, not by an additional parity assumption.

In (1,2) the residual interior multiplicity 1 is one simple zero.
In (0,4) the residual boundary multiplicity 2 can be two distinct
simple zeros or one double zero. Two extra simple boundary zeros
would each give a forbidden horizontal seed by the bridge, so only
one double zero remains. The already forced labels are simple and
occur once on a radial curve; no residual multiplicity can be assigned
to them or to a second traversal. No bridge is asserted at the double
zero. The exchanged argument treats the other complementary curve,
independently; it imposes no equality of the extra labels or cases.

Finally the radii at a,b on Gamma_(2|c) are those of the minimal labels
zeta,eta, and its radius at c is strictly smaller than |theta|.
Minimality excludes any residual zero on these three rays. The
exchanged radii prove the same statement for Gamma_(1|b). This covers
coincident arguments without restricting unselected zeros on other rays.

No missing case or error was found. The direct inputs remain L847 and
L879-L881; the DAG needs no new edge. The audit validates the necessary
dichotomy only. Neither branch is excluded or realized, compatible
counts do not prove phase compatibility, and no product graph, mass
equality, sharp period, compactness, higher sign or Xi transfer follows.
No new source theorem, mathematical script or numerical evidence was
needed for this conceptual audit.

## Mathlib

Full matching coverage and formal coverage of these supporting steps
have not been checked. Unknown coverage is not absence. The exact
seed bridge and coupled-fiber classification above are informal;
the underlying source tools and local lemmas do not constitute a
formalization. The independent informal audit above changes neither
the unchecked Mathlib coverage nor the unresolved graph/RH conclusions.
