# C828b — The specified theta-kernel boundary disks do not exist

## Hypotheses

Use the actual kernel
\[
 \Phi(u)=\sum_{n\ge1}
 (4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2})e^{-\pi n^2e^{2u}}
\]
on \(S=\{u:|\Im u|<\pi/4\}\). This is precisely the function
\(P\) in C828a(1), not a truncation or a transformed boundary value.
Set \(r=1/100\). For a finite real \(R\), let
\[
 u_0=R+i\pi/4,\qquad D=\{u:|u-u_0|<r\}.
\]
By extension to this disk we mean a holomorphic function \(f\) on
\(D\) with \(f=\Phi\) on \(D\cap S\). Agreement on any nonempty
open subset of that overlap is equivalent by the identity theorem.

## Conclusion

For every real \(R\), no such \(f\) exists. In particular, the
specified disk continuation cannot hold for every sufficiently large
real \(R\); it fails at every individual \(R\).

This is a **REPRODUCTION/specialization** of the known theta natural
boundary through C828a's existing differential identity. It is an
obstruction to this exact holomorphic crossing prerequisite, not a new
theta boundary theorem or a signed Xi estimate. It gives no conclusion
about interior modular representations, boundary distributions, other
contours, saddle contributions or RH.

## Proof

### Imported identity and exact theta convention

Use only C828a, Proof Section1, equation (5): on \(S\),
\[
 \Theta(t)=\sum_{n\in\mathbb Z}e^{-\pi n^2t},\quad
 H(u)=e^{u/2}\Theta(e^{2u}),\quad H''-H/4=2\Phi.       \tag{1}
\]
That section proves holomorphy and normal convergence on the stated
domains. Its moment estimates, cusp proof and complete Bernstein
exclusion are not used. Thus the factor 2 and the exponential gauge
come from the identical actual kernel, with no rescaling assumption.

The external theorem is the theta natural-boundary statement in
[NIST DLMF20.2(ii)](https://dlmf.nist.gov/20.2#ii), version1.2.8,
released15September2026, inspected19November2026: at fixed argument
zero, \(\tau\mapsto\theta_3(0\mid\tau)\) on \(\Im\tau>0\)
cannot be continued holomorphically through any finite real point.
We import this theorem, without reproving it. With the nome convention
of [DLMF20.1](https://dlmf.nist.gov/20.1), its series
[20.2.3](https://dlmf.nist.gov/20.2#E3) gives exactly
\[
 \theta_3(0\mid i e^{2u})=
 1+2\sum_{n\ge1}e^{-\pi n^2e^{2u}}=\Theta(e^{2u})
 \quad(u\in S).                                      \tag{2}
\]
Indeed \(\Im(i e^{2u})=\Re(e^{2u})>0\) there. No continuation
of a modular transformation is being assumed.

### Reconstruction on the whole proposed disk

Suppose \(f\) exists. Since \(r<\pi/2\), the overlap
\(U=D\cap S=D\cap\{\Im u<\pi/4\}\) is a nonempty convex lower
half-disk. Choose \(a=u_0-ir/2\in U\), so \(H(a)\) and \(H'(a)\)
are defined at an interior point. Define on all of \(D\)
\[
 F(u)=H(a)\cosh((u-a)/2)+2H'(a)\sinh((u-a)/2)
       +4\int_a^u\sinh((u-v)/2)f(v)\,dv.              \tag{3}
\]
The integration is within \(D\). To justify holomorphy and path
independence, write the last integral, before its factor 4, as
\[
 \frac12\left(e^{u/2}A(u)-e^{-u/2}B(u)\right),\quad
 A(u)=\int_a^u e^{-v/2}f(v)\,dv,\quad
 B(u)=\int_a^u e^{v/2}f(v)\,dv.
\]
The holomorphic integrands have primitives on the convex disk; take
the primitives vanishing at \(a\). This supplies a solution throughout
the entire disk, rather than just an unspecified small IVP radius.
Differentiation of these primitives yields
\[
 F''-F/4=2f,\qquad F(a)=H(a),\qquad F'(a)=H'(a).       \tag{4}
\]
For example, if \(J\) denotes the integral in (3), then
\(J(a)=J'(a)=0\) and \(J''-J/4=f/2\); the coefficient 4 in
(3) is necessary.

On the connected overlap \(U\), the function \(G=F-H\) satisfies
\(G''-G/4=0\) and \(G(a)=G'(a)=0\), by (1), (4) and \(f=\Phi\).
For completeness, \((e^{u/2}(G'-G/2))'=0\) on \(U\), so this
expression is its zero value at \(a\). Then
\((e^{-u/2}G)'=0\), also with zero value at \(a\). Hence
\(F=H\) on all of \(U\).

This is the elementary constant-coefficient specialization of analytic
IVP existence/uniqueness; compare G. Teschl, *Ordinary Differential
Equations and Dynamical Systems*, AMS GSM140(2012),
[author April2012 preliminary edition](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf),
Section4.1 pp111–114, Theorem4.1/(4.7)–(4.9), and Section4.2 p116.
The explicit formula checks the full-disk and overlap issues not
supplied merely by quoting a local existence radius. No finite boundary
initial data for \(H\) have been assumed.

### Local coordinate and forbidden continuation

Set \(\tau_0=i e^{2u_0}=-e^{2R}\), a nonzero finite real point.
The map \(u\mapsto i e^{2u}\) has derivative \(2\tau_0\ne0\)
at \(u_0\). More explicitly, on a sufficiently small disk
\(E=\{|\tau-\tau_0|<\delta\}\), take
\[
 u(\tau)=u_0+\tfrac12\operatorname{Log}(\tau/\tau_0),  \tag{5}
\]
where the logarithm is the branch near 1 with \(\operatorname{Log}1=0\).
Choose \(0<\delta<|\tau_0|/2\) small enough that \(u(E)\subset D\).
This is possible by continuity, and \(i e^{2u(\tau)}=\tau\).

For \(\tau\in E\) with \(\Im\tau>0\), the quotient
\(\tau/\tau_0\) has positive real part and negative imaginary part.
Its chosen argument is negative, so \(\Im u(\tau)<\pi/4\).
Since \(u(\tau)\in D\) and \(r<\pi/2\), it also has
\(\Im u(\tau)>-\pi/4\). Thus \(u(\tau)\in U\) on the entire
upper half of \(E\), not just on a ray.

The function
\[
 T(\tau)=e^{-u(\tau)/2}F(u(\tau))
\]
is holomorphic on \(E\), since the exponential gauge is holomorphic
and nonvanishing. On its upper half it equals
\(e^{-u(\tau)/2}H(u(\tau))=\theta_3(0\mid\tau)\) by (2) and
the overlap agreement. This contradicts the imported natural-boundary
theorem at \(\tau_0\).

The proof applies to every finite real \(R\). The auxiliary radius
\(\delta\) may depend on \(R\); uniformity of that radius is not
needed to contradict existence on the fixed \(u\)-disk. The claimed
all-large-\(R\) prerequisite is therefore false. No numerical
evidence, saddle approximation or zero-location hypothesis enters.

### Independent audit1669 — 19 November 2026

The approved audit replays the preceding argument without a mathematical
correction. Classification: REPRODUCTION; the external natural-boundary
theorem is reused within assessment1667's approved scope.

First, the normalization in C828a(5) can be checked directly with
\(t=e^{2u}\):
\[
 H'=e^{u/2}(\Theta/2+2t\Theta'),\qquad
 H''=e^{u/2}(\Theta/4+6t\Theta'+4t^2\Theta'').
\]
Since \(\Theta'=-2\pi\sum_{n\ge1}n^2e^{-\pi n^2t}\) and
\(\Theta''=2\pi^2\sum_{n\ge1}n^4e^{-\pi n^2t}\), this gives
exactly \((H''-H/4)/2=\Phi\), with both coefficients in the stated
kernel. The compact normal-convergence argument in C828a Section1
justifies these differentiations; no boundary differentiation occurs.

For the integral \(J\) in (3), primitives give, everywhere on \(D\),
\[
 J'=\tfrac12\int_a^u\cosh((u-v)/2)f(v)\,dv,\qquad
 J''=f(u)/2+J/4.
\]
The endpoint term in the first derivative vanishes because
\(\sinh0=0\); the second has \(\cosh0=1\). Thus the factor 4
and both initial data in (4) are correct. Convexity supplies primitives
on the whole disk, with no boundedness assumption at its boundary.
The two homogeneous integrating-factor identities then prove uniqueness
on the entire connected \(U\), using the interior point \(a\).

Finally, \(\tau_0<0\) for every finite real \(R\).
The choice \(\delta<|\tau_0|/2\) keeps \(\tau/\tau_0\) in the
right half-plane. Its upper-\(\tau\)-half has negative argument,
so (5) puts precisely that half inside the original strip after the
stated shrinking into \(D\). Hence \(T\) agrees with theta3 on
an open upper half-disk, which is the agreement required by the imported
natural-boundary theorem. Neither uniform \(\delta\) in \(R\)
nor boundary initial data are needed. This verifies the negative for
each specified disk, while supplying no signed Mellin or Xi implication.

## Mathlib

Full matching coverage is **not checked**. No formal theorem for this
theta natural-boundary transfer or disk obstruction is claimed.
C828a records supporting normal-convergence and differentiation
references; those are not a matching formal proof of this result.
