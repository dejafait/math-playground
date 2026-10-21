# L020 — Finite-extension global Kummer certificate

## Hypotheses

Retain all hypotheses and notation of L018. In particular, r = rank E(Q),
S_m = Sel(Q,E[p^m]) has the prescribed basis x_1^(m), x_2^(m), and
Sha(E/Q)[p^infinity] is (Q_p/Z_p)^(2-r), with 0 <= r <= 2.
Let F/Q be one finite extension, not necessarily Galois, set
N = [F:Q] and d = v_p(N), and let m >= 2 satisfy m > d.
Assume, for both i = 1,2, that

\[
\operatorname{res}_{F/\mathbf Q}(x_i^{(m)})
\in\operatorname{im}\bigl(E(F)/p^mE(F)
\xrightarrow{\delta_{F,m}}H^1(F,E[p^m])\bigr).
\tag{1}
\]

This is global Kummer realization by points over F, an additional
arithmetic hypothesis. Classical local conditions over F do not imply
(1). No finiteness of Sha over either field is assumed.

## Conclusion

Then r = 2 and Sha(E/Q)[p^infinity] = 0. Consequently the prescribed
classes at every coefficient depth are globally Kummer over Q.

More precisely, if (1) holds at any m >= 2 and r < 2, then necessarily

\[
p^m\mid [F:\mathbf Q],\qquad d\ge m.
\tag{2}
\]

Thus the required degree threshold is strict: the transfer argument
excludes r < 2 only when the achieved depth exceeds the degree's
p-valuation. Under L018, existence of a witness satisfying all the
hypotheses of this lemma is equivalent to r = 2 (the converse uses
F = Q). This is a conditional certificate, not an independent proof
of its arithmetic availability or of analytic rank two.

At the equality boundary m = d, the exact rows, coefficient
compatibility and restriction/corestriction composite tested here
are formally consistent with a nonzero divisible quotient. This is
only a limitation of those algebraic data, not an arithmetic
counterexample to a rank assertion.

## Proof

**Import standard inputs.** For a number field K the finite Kummer
sequence gives

\[
0\longrightarrow E(K)/p^mE(K)
\xrightarrow{\delta_{K,m}}H^1(K,E[p^m])
\xrightarrow{q_{K,m}}H^1(K,E)[p^m]\longrightarrow0.
\tag{3}
\]

Use Milne, *Elliptic Curves*, second edition (2021), Chapter IV
Section 2, equations (28)--(29),
[printed pp. 112--113](https://www.jmilne.org/math/Books/EC2.pdf#page=117),
including its number-field formulation. Restriction is natural for
this exact sequence, since the multiplication sequence of Galois
modules defining it is the same over Q and F. In particular,
q_(F,m) res(x) = res(q_(Q,m)(x)).

For the discrete Galois module E(Qbar), restriction and corestriction
in H^1 satisfy

\[
\operatorname{cor}_{F/\mathbf Q}\operatorname{res}_{F/\mathbf Q}
=N\operatorname{id}_{H^1(\mathbf Q,E)}.
\tag{4}
\]

Import Milne, *Class Field Theory*, v4.03 (2020-08-06), Chapter II
Example 1.29 and Proposition 1.30,
[printed p. 70](https://www.jmilne.org/math/CourseNotes/CFT.pdf#page=79),
with continuous discrete cohomology as in Proposition II.4.2,
[printed p. 87](https://www.jmilne.org/math/CourseNotes/CFT.pdf#page=96).
The subgroup G_F of G_Q has finite index N; it need not be normal.
These are supporting transfer and Kummer inputs, imported without
reproof; neither cited theorem states the whole L018-specific criterion.

**Audit the continuous, non-normal application.** Write G = G_Q,
H = G_F and M = E(Qbar), with M discrete. Choose the embedding of F
in Qbar once. Then H is open and [G:H] = N, whether or not F/Q is
Galois. For a continuous cocycle c:G -> M, compactness of G makes
its image finite. Choose an open normal subgroup U of G contained
in H, in c^(-1)(0), and in the stabilizers of all values of c.
Such a U exists by taking the normal core of a sufficiently small
open subgroup. Thus c takes values in M^U and factors through G/U.
Its restriction factors through H/U. Milne II.1.30 applies to the
finite group G/U and its subgroup H/U, whose index is still N;
normality of H/U is not required. The coset representatives defining
finite transfer also represent G/H, so inflation commutes with these
restriction and corestriction maps. Inflating the finite-group
identity proves (4) on the class of c. This checks the application
of the imported theorem, rather than reproving transfer. No passage
to a Galois closure changes N, and no assertion about the reverse
composite res cor on H^1(F,E) is needed.

**Audit finite Kummer naturality and coefficients.** In (3), q_(K,m)
is induced by coefficient inclusion E[p^m] -> E(Qbar). Restriction
commutes with that inclusion and with the connecting map delta, so
the restriction diagram has point map E(Q)/p^m -> E(F)/p^m and
quotient map H^1(Q,E)[p^m] -> H^1(F,E)[p^m]. In particular, a
globally Kummer restricted class has zero image in H^1(F,E), not
merely zero localizations. This is precisely the implication needed
below. It does not identify the kernel of restriction with a group
of rational points.

For the downward transition from depth n+1 to n, map the short exact
multiplication sequence for [p^(n+1)] to that for [p^n] using [p]
on E[p^(n+1)], [p] on the middle E(Qbar), and identity on the last
E(Qbar). The equality [p^n][p] = [p^(n+1)] makes this a diagram of
exact sequences. It induces reduction on E(K)/p^(n+1), multiplication
by p on H^1(K,E)[p^(n+1)], and the coefficient map rho_n between
the finite-coefficient groups. Thus q_(K,n) rho_n = p q_(K,n+1).
For the upward coefficient inclusion, the corresponding maps on the
two copies of E(Qbar) are identity and [p]; it induces multiplication
by p on the point quotients and inclusion on H^1(K,E) torsion.
These are the two different directions in Milne's
[Chapter IV diagram, printed p. 129](https://www.jmilne.org/math/Books/EC2.pdf#page=134).
Restricting the Q rows to the Selmer subgroups gives L018's finite
rows. No finiteness of Sha and no local coefficient injectivity enter
this audit.

**Track the basis into Sha, rather than confusing local and global
conditions.** Put b_i = q_(Q,m)(x_i^(m)). The finite Selmer sequence
in L018 is exact:

\[
0\longrightarrow E(\mathbf Q)/p^mE(\mathbf Q)
\longrightarrow S_m\xrightarrow{q_{\mathbf Q,m}}
\Sha(E/\mathbf Q)[p^m]\longrightarrow0.
\tag{5}
\]

Consequently b_1,b_2 generate Sha(E/Q)[p^m] over Z/p^mZ. By (1),
(3), and naturality, res(b_i) = 0 in H^1(F,E). Apply (4) to obtain
N b_i = 0. Hence N annihilates the entire group Sha(E/Q)[p^m].
No assertion about finiteness of Sha(F) or injectivity of restriction
has been used. In particular we do not cancel N on integral cohomology
when p divides it.

**Compare actual annihilation with the required exponent.** If r < 2,
L018 identifies

\[
\Sha(E/\mathbf Q)[p^m]\simeq
(\mathbf Z/p^m\mathbf Z)^{2-r},
\tag{6}
\]

which has an element of exact order p^m. An integer N annihilates
such an element only if p^m divides N. This proves (2). Since m > d
in the stated certificate, r < 2 is impossible. L018 already gives
r <= 2, so r = 2 and the full p-primary Sha group is zero.
Then (5), at every depth, gives global rational Kummer realization
of every Selmer class. Conversely r = 2 makes (1) true with F = Q,
N = 1, d = 0 and any m >= 2, proving the asserted equivalence.

**Equality-boundary test with the complete tested formal maps.** The
annihilator observation alone does not check whether natural exact
rows and coefficient compatibility add an obstruction at m = d.
Here is an explicit formal test of those additional data. It is not
a construction of Galois cohomology, an elliptic curve or a field.

Fix r in {0,1}, put k = 2-r, choose a >= 2, and formally set N = p^a.
Let D = Q_p/Z_p, R_n = Z/p^n Z and
iota_n:R_n^k -> D^k[p^n] send v to p^(-n)v modulo Z_p^k.
At every depth n >= 1 take the exact rows

\[
0\to A_{Q,n}=R_n^r\to C_{Q,n}=R_n^r\oplus R_n^k
\xrightarrow{q_{Q,n}}B_Q[p^n]=D^k[p^n]\to0,
\qquad q_{Q,n}(u,v)=\iota_n(v),
\tag{7}
\]
\[
0\to A_{F,n}=R_n^2\to C_{F,n}=R_n^2\oplus R_n^k
\xrightarrow{q_{F,n}}B_F[p^n]=D^k[p^n]\to0,
\qquad q_{F,n}(z,w)=\iota_n(w).
\tag{8}
\]

Here B_Q = B_F = D^k; injections into the middle terms are inclusion
of the first summands. These rows model the shapes of the Q Selmer
row and an F global Kummer row. Define formal restriction and
corestriction on B by [p^a] and identity, respectively. On the finite
middle terms define

\[
\mathrm{Res}_n(u,v)=((u,v),p^a v),\qquad
\mathrm{Cor}_n((z_u,z_v),w)=(p^a z_u,w),
\tag{9}
\]

where z_u has r coordinates and z_v has k coordinates. The point
maps are u -> (u,0) and (z_u,z_v) -> p^a z_u. They respect the
inclusions in (7)--(8). The quotient maps commute because

\[
q_{F,n}\mathrm{Res}_n(u,v)=\iota_n(p^a v)=p^a q_{Q,n}(u,v),
\qquad
q_{Q,n}\mathrm{Cor}_n(z,w)=\iota_n(w)=q_{F,n}(z,w).
\tag{10}
\]

On C_(Q,n), the composite Cor_n Res_n sends (u,v) to
(p^a u,p^a v), namely multiplication by N. On A_(Q,n) and B_Q
the same composite is multiplication by N. Downward coefficient
maps are reduction on all finite coordinates and multiplication by
p on B[p^(n+1)]; iota_n(v mod p^n) = p iota_(n+1)(v).
All maps in (9) commute with reduction, since their coefficients
are integral and independent of n. Upward maps multiply finite
coordinates by p, and correspond under iota to inclusion on B
torsion; (9) commutes with them as well. Thus these are compatible
rows at every depth, not just separate group orders. The Q tower
has exactly L018's formal structure D^2 with point submodule D^r
and quotient D^k.

At n = a, p^a v = 0 in R_a^k. Therefore the restrictions of
every element of C_(Q,a), and in particular both columns of any
prescribed R_a-basis, lie in A_(F,a). Yet B_Q[p^a] is nonzero and
has exponent p^a. At n > a a standard quotient column has image
iota_n(p^a e_j) of exact order p^(n-a), so at least that column
is outside the formal point kernel after restriction. Indeed at
any n > a a basis cannot have both restrictions in the point
kernel, because its quotient images generate R_n^k and [p^a]
is nonzero on that group.

This supplies a negative boundary test: the exact rows, naturality,
coefficient compatibility and tested composite identity do not
replace m > d by m >= d. It checks a stronger formal package than
annihilation alone. It asserts neither that these maps arise from a
finite-index Galois subgroup nor that actual torsors have such a
splitting field; untested arithmetic constraints remain outside the
model. The mathematical audit found no error in the conditional
certificate.

**Limits of the step.** At d >= m, multiplication by N is zero on
(6) even when 2-r is positive. The transfer annihilator comparison
alone then gives no rank lower bound. This does not assert the
existence of a realizing F in that regime, or an elliptic curve
realizing r < 2 under L018's arithmetic assumptions. Separately
splitting two torsors requires taking a common field and checking
its degree; the degrees of separate fields cannot be substituted.
Nor can fields of increasing degree be treated as a fixed witness
unless at one depth the strict inequality m > d holds.

The discriminating test succeeds exactly as proposed: the global
realization premise plus m > d supplies the missing conditional
lower bound r >= 2. Constructing those points and matching their
Kummer classes remains open. Production of L018's two-prime premise
from analytic order two, uniform prime hypotheses, analytic comparison
and higher ranks are also unresolved. This result is a REPRODUCTION
by specialization of the assessed standard descent inputs, with no
claim of mathematical progress beyond the checked literature or a
complete BSD candidate.

## Mathlib

Full coverage of this L018-specific certificate: **not checked**.
Supporting restriction/corestriction, continuous Galois cohomology
and the finite Kummer sequence: **not checked**. The cited Milne
Proposition II.1.30 supports (4), and equations IV.(28)--(29) support
(3); neither is a full-statement library match. No absence or
originality claim follows. Coverage of the explicit equality-boundary
formal rows and maps (7)--(10): **not checked**; these are a direct
algebraic audit of the imported identities, not an arithmetic theorem.
