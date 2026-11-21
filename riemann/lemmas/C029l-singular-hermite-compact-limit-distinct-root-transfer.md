# C029l — Singular Hermite forms and distinct nonreal limit zeros

## Hypotheses

Let (p_j) be a sequence of nonconstant polynomials with real coefficients,
of actual degrees d_j >= 1. Assume p_j converges uniformly on every
compact subset of C to an entire function F that is not identically zero.
For each j, list the roots alpha_(j,1),...,alpha_(j,d_j) with their
algebraic multiplicities and put

    s_(j,k) = sum_(h=1)^(d_j) alpha_(j,h)^k,  k >= 0,
    H_j = (s_(j,a+b))_(0 <= a,b < d_j).

In particular s_(j,0)=d_j, including when a root is zero. Let nu_-(H_j)
denote the number of strictly negative eigenvalues, with multiplicity,
of this real symmetric matrix. Assume there is J_0 such that
nu_-(H_j) <= 1 for every j >= J_0. Arbitrary nullity is allowed.

## Conclusion

F has at most two **distinct** zeros in C minus R. No bound on their
algebraic multiplicities is asserted. Neither simplicity, fixed degree,
degree tending to infinity, nor convergence of the matrices is needed.
This is a conditional statement: it does not establish the eventual
index hypothesis for any actual-Xi approximation family or imply RH
without additional arguments.

## Proof

We import Hermite's root-count theorem from Daniel Plaumann,
*Real Algebraic Geometry*, IHP lectures, 14 October 2023,
[Theorem 1.1 and its proof, printed pp. 3–4](https://rtca2023.github.io/pages_Paris/files_m5/rag-ihp.pdf).
For a monic real polynomial of degree d, its Newton-sum Hermite matrix
has rank equal to the number of distinct complex roots and signature
equal to the number of distinct real roots. The signature is positive
index minus negative index. The proof explicitly permits repeated
roots, with their positive integer multiplicity factors, and singular
Hermite matrices. We use this theorem without reproving it.

For each j let a_j be the nonzero leading coefficient of p_j.
The polynomial q_j=p_j/a_j is monic, real, and has actual degree d_j.
It has exactly the same roots with the same multiplicities as p_j;
thus its Hermite matrix is precisely H_j. We apply monic normalization
only for this algebraic theorem. We do not assert q_j converges to F.

Write r_j for the number of distinct real roots of p_j and c_j for its
number of distinct nonreal conjugate pairs. Real coefficients ensure
the latter pairing, including equal multiplicities. Hermite's theorem
gives rank(H_j)=r_j+2c_j and signature(H_j)=r_j. If u_j and v_j are its
positive and negative indices, respectively, these equations read

    u_j+v_j=r_j+2c_j,     u_j-v_j=r_j.

Consequently v_j=c_j, even if H_j has zero eigenvalues. For every
j >= J_0, p_j therefore has 2c_j <= 2 distinct nonreal roots. These
are counts of distinct roots, not sums of their algebraic multiplicities.

We also import the standard Rouché theorem, in the form stated and
proved in Berkeley, *Complex analysis, lecture 2*,
[Lecture 23, 22 April 2026, Rouché theorem and proof](https://math.berkeley.edu/~avizeff/complex_analysis_S26/lecture_23.html):
analytic functions f and h on a neighborhood of the closure of a bounded
domain with piecewise smooth boundary have equal zero counts for f and
f+h, with algebraic multiplicity, if |h|<|f| on the boundary.
No simple-zero hypothesis appears. No reproof is needed here.

Suppose, contrary to the conclusion, that F has three distinct nonreal
zeros z_1,z_2,z_3. Since F is entire and not identically zero, each is
isolated and has a finite positive order m_l. Choose radii rho_l>0
so small that the closed discs

    Dbar_l = {z : |z-z_l| <= rho_l},  l=1,2,3,

are pairwise disjoint, lie in C minus R, and contain no zero of F other
than their centers. Such radii exist: isolation gives the zero-free
punctured neighborhoods, rho_l<|Im(z_l)|/2 avoids R, and shrinking each
radius below one third of every pairwise center distance ensures
disjoint closures. In particular F is nonzero on all three circles.

Let K be the union of these three boundary circles. This is compact,
and continuity gives delta=min_(z in K)|F(z)|>0. Compact convergence
provides one J_1 such that

    sup_(z in K)|p_j(z)-F(z)| < delta/2   for every j >= J_1.

Fix any j >= max(J_0,J_1). On every boundary circle simultaneously,
|p_j-F|<|F|. Both functions are entire, so Rouché applies separately
to each open disc, whose boundary is smooth and has an analytic
neighborhood. It says p_j has exactly m_l zeros there counted with
multiplicity, and in particular at least one root in each disc.
The three discs are disjoint and avoid R, so these include at least
three distinct nonreal roots of this single p_j. This contradicts its
bound of two. Thus F has at most two distinct nonreal zeros.

The finite-disc argument handles any possible infinite set of limit
zeros by selecting three of them first. Its index J_1 depends on those
fixed discs; no uniformity over all limit zeros is claimed or needed.
Root collisions inside a disc do not affect the existence of a root
there, and a root cannot serve two disjoint discs. This is why singular
approximants and multiple limit zeros do not invalidate the argument.

This proof is a standard specialization of the cited theorems, prepared
by assessment2005, not a new root-count theorem or an actual-Xi index
estimate. It addresses only the compact-limit interface. Actual tilted
family convergence, an eventual uniform index bound, and conversion
of the conclusion to RH using Xi-specific properties remain separate.

## Mathlib

Full matching theorem and supporting Hermite/Rouché coverage not checked.
No formalization or absence claim is made. The proof uses the precise
primary citations above and ordinary isolated-zero and compactness facts.
